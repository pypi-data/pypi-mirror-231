# Copyright © 2023 Pathway

from __future__ import annotations

import asyncio
import functools
import json
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Awaitable, Callable, ClassVar, Dict, Optional, Type

import pathway.internals as pw
import pathway.io as io
from pathway.internals import asynchronous, operator, parse_graph
from pathway.internals.api import BasePointer
from pathway.internals.helpers import StableSet
from pathway.internals.operator import Operator


class _AsyncStatus(Enum):
    PENDING = "-PENDING-"
    FAILURE = "-FAILURE-"
    SUCCESS = "-SUCCESS-"


_ASYNC_STATUS_COLUMN = "_async_status"


class _AsyncConnector(io.python.ConnectorSubject):
    _requests: asyncio.Queue
    _apply: Callable
    _loop: asyncio.AbstractEventLoop
    _transformer: AsyncTransformer
    _state: Dict[BasePointer, Any]
    _tasks: Dict[BasePointer, asyncio.Task]
    _invoke: Callable[..., Awaitable[Dict[str, Any]]]

    def __init__(self, transformer: AsyncTransformer) -> None:
        super().__init__()
        self._transformer = transformer
        self._event_loop = asyncio.new_event_loop()
        self.set_options()

    def set_options(
        self,
        capacity: Optional[int] = None,
        retry_strategy: Optional[asynchronous.AsyncRetryStrategy] = None,
        cache_strategy: Optional[asynchronous.CacheStrategy] = None,
    ):
        self._invoke = asynchronous.async_options(
            capacity=capacity,
            retry_strategy=retry_strategy,
            cache_strategy=cache_strategy,
        )(self._transformer.invoke)

    def run(self) -> None:
        self._tasks = {}
        self._state = {}
        self._transformer.open()

        async def loop_forever(event_loop: asyncio.AbstractEventLoop):
            self._maybe_create_queue()

            while True:
                request = await self._requests.get()
                if request == "*FINISH*":
                    break

                (key, values, addition) = request
                previous_task = self._tasks.get(key, None)

                if previous_task is None:
                    self._set_status(key, _AsyncStatus.PENDING)

                async def task(
                    key: BasePointer,
                    values: Dict[str, Any],
                    addition: bool,
                    previous_task: Optional[asyncio.Task],
                ):
                    if addition is False:
                        # Remove last values if this is not addition
                        if previous_task is not None:
                            await previous_task
                        self._remove_by_key(key)
                    else:
                        try:
                            result = await self._invoke(**values)
                            self._assert_result_against_schema(result)
                            # If there is a task pending for this key,
                            # let's wait for it and discard result to preserve order
                            if previous_task is not None:
                                await previous_task
                            self._upsert(key, result)
                        except Exception:
                            self._set_status(key, _AsyncStatus.FAILURE)

                current_task = event_loop.create_task(
                    task(key, values, addition, previous_task)
                )
                self._tasks[key] = current_task

            await asyncio.gather(*self._tasks.values())

        self._event_loop.run_until_complete(loop_forever(self._event_loop))

    def _set_status(self, key: BasePointer, status: _AsyncStatus) -> None:
        data = self._state.get(
            key,
            {
                col: status.value
                for col in self._transformer.output_schema.column_names()
            },
        )
        self._upsert(key, data, status)

    def _upsert(
        self, key: BasePointer, data: Dict, status=_AsyncStatus.SUCCESS
    ) -> None:
        data = {**data, _ASYNC_STATUS_COLUMN: status.value}
        payload = json.dumps(data).encode()
        self._remove_by_key(key)
        self._add(key, payload)
        self._state[key] = data

    def _remove_by_key(self, key) -> None:
        if key in self._state:
            payload = json.dumps(self._state[key]).encode()
            self._remove(key, payload)

    def _assert_result_against_schema(self, result: Dict) -> None:
        if result.keys() != self._transformer.output_schema.keys():
            raise ValueError("result of async function does not match output schema")

    def on_stop(self) -> None:
        self._transformer.close()

    def on_subscribe_change(
        self, key: BasePointer, row: Dict[str, Any], time: int, is_addition: bool
    ) -> Any:
        self._put_request((key, row, is_addition))

    def on_subscribe_end(self) -> None:
        self._put_request("*FINISH*")

    def _put_request(self, message) -> None:
        def put_message(message):
            self._maybe_create_queue()
            self._requests.put_nowait(message)

        self._event_loop.call_soon_threadsafe(put_message, message)

    def _maybe_create_queue(self) -> None:
        if not hasattr(self, "_requests"):
            self._requests = asyncio.Queue()

    def _is_internal(self) -> bool:
        return True


class AsyncTransformer(ABC):
    """
    Allows to perform async transformations on a table.

    :py:meth:`invoke` will be called asynchronously for each row of an input_table.

    Output table can be acccesed via :py:attr:`result`.

    Example:

    >>> import pathway as pw
    >>> import asyncio
    >>> class OutputSchema(pw.Schema):
    ...    ret: int
    ...
    >>> class AsyncIncrementTransformer(pw.AsyncTransformer, output_schema=OutputSchema):
    ...     async def invoke(self, value) -> Dict[str, Any]:
    ...         await asyncio.sleep(0.1)
    ...         return {"ret": value + 1 }
    ...
    >>> input = pw.debug.parse_to_table('''
    ...   | value
    ... 1 | 42
    ... 2 | 44
    ... ''')
    >>> result = AsyncIncrementTransformer(input_table=input).result
    >>> pw.debug.compute_and_print(result, include_id=False)
    ret
    43
    45
    """

    output_schema: ClassVar[Type[pw.Schema]]
    _connector: _AsyncConnector
    _input_table: pw.Table

    def __init__(self, input_table: pw.Table) -> None:
        assert self.output_schema is not None
        self._connector = _AsyncConnector(self)
        self._input_table = input_table

    def __init_subclass__(cls, /, output_schema: Type[pw.Schema], **kwargs):
        super().__init_subclass__(**kwargs)
        cls.output_schema = output_schema

    def open(self) -> None:
        """
        Called before actual work. Suitable for one time setup.
        """
        pass

    def close(self) -> None:
        """
        Called once at the end. Proper place for cleanup.
        """
        pass

    @abstractmethod
    async def invoke(self, *args, **kwargs) -> Dict[str, Any]:
        """
        Called for every row of input_table. The arguments will correspond to the
        columns in the input table.

        Should return dict of values matching :py:attr:`output_schema`.
        """
        ...

    def with_options(
        self,
        capacity: Optional[int] = None,
        retry_strategy: Optional[asynchronous.AsyncRetryStrategy] = None,
        cache_strategy: Optional[asynchronous.CacheStrategy] = None,
    ) -> AsyncTransformer:
        """
        Sets async options.

        Args:
            capacity: maximum number of concurrent operations.
            retry_strategy: defines how failures will be handled.
        Returns:
            self
        """
        self._connector.set_options(capacity, retry_strategy, cache_strategy)
        return self

    @functools.cached_property
    def result(self) -> pw.Table:
        """
        Resulting table.
        """
        return (
            self._output_table.update_types(**{_ASYNC_STATUS_COLUMN: str})
            .filter(pw.this[_ASYNC_STATUS_COLUMN] == _AsyncStatus.SUCCESS.value)
            .without(pw.this[_ASYNC_STATUS_COLUMN])
            .update_types(**self.output_schema)
        )

    @functools.cached_property
    def _output_table(self) -> pw.Table:
        io.subscribe(
            self._input_table,
            self._connector.on_subscribe_change,
            self._connector.on_subscribe_end,
        )
        output_node = list(parse_graph.G.global_scope.nodes)[-1]

        table: pw.Table = io.python.read(
            self._connector,
            value_columns=[*self.output_schema.column_names(), _ASYNC_STATUS_COLUMN],
            autocommit_duration_ms=1000,
        )
        input_node = table._source.operator

        class AsyncInputHandle(operator.InputHandle):
            @property
            def dependencies(self) -> StableSet[Operator]:
                return StableSet([output_node])

        input_node._inputs = {
            "async_input": AsyncInputHandle(
                operator=input_node,
                name="async_input",
                value=self._input_table,
            )
        }

        return table.promise_universe_is_subset_of(self._input_table)
