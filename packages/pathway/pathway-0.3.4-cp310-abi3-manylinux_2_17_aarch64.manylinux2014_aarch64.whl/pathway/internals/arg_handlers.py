# Copyright © 2023 Pathway

from __future__ import annotations

from functools import wraps

import pathway.internals.expression as expr
from pathway.internals.join_mode import JoinMode
from pathway.internals.trace import trace_user_frame


def arg_handler(*, handler):
    handler = trace_user_frame(handler)

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            args, kwargs = handler(*args, **kwargs)
            return func(*args, **kwargs)

        return inner

    return wrapper


def groupby_handler(self, *args, id=None, **kwargs):
    if kwargs:
        raise ValueError(
            "Table.groupby() received extra kwargs.\n"
            + "You probably want to use Table.groupby(...).reduce(**kwargs) to compute output columns."
        )
    return (self, *args), {"id": id}


def windowby_handler(self, time_expr, *args, window, shard=None, **kwargs):
    if args:
        raise ValueError(
            "Table.windowby() received extra args.\n"
            + "It handles grouping only by a single column."
        )
    if kwargs:
        raise ValueError(
            "Table.windowby() received extra kwargs.\n"
            + "You probably want to use Table.windowby(...).reduce(**kwargs) to compute output columns."
        )
    return (self, time_expr), {"window": window, "shard": shard}


def join_kwargs_handler(*, allow_how: bool, allow_id: bool):
    def handler(self, other, *on, **kwargs):
        processed_kwargs = {}
        if "how" in kwargs:
            how = kwargs.pop("how")
            processed_kwargs["how"] = how
            if not allow_how:
                raise ValueError(
                    "Received `how` argument but was not expecting any.\n"
                    + "Consider using a generic join method that handles `how` "
                    + "to decide on a type of a join to be used."
                )
            elif isinstance(how, JoinMode):
                pass
            elif isinstance(how, str):
                raise ValueError(
                    "Received `how` argument of join that is a string.\n"
                    + "You probably want to use one of "
                    + "JoinMode.INNER, JoinMode.LEFT, JoinMode.RIGHT or JoinMode.OUTER values."
                )
            else:
                raise ValueError(
                    "How argument of join should be one of "
                    + "JoinMode.INNER, JoinMode.LEFT, JoinMode.RIGHT or JoinMode.OUTER values."
                )

        if "id" in kwargs:
            id = kwargs.pop("id")
            processed_kwargs["id"] = id
            if not allow_id:
                raise ValueError(
                    "Received `id` argument but was not expecting any.\n"
                    + "Not every join type supports `id` argument."
                )
            elif id is None:
                pass
            elif isinstance(id, str):
                raise ValueError(
                    "Received `id` argument of join that is a string.\n"
                    + f"Did you mean <table>.{id}"
                    + f" instead of {repr(id)}?"
                )
            elif not isinstance(id, expr.ColumnReference):
                raise ValueError(
                    "The id argument of a join has to be a ColumnReference."
                )

        if "defaults" in kwargs:
            processed_kwargs["defaults"] = kwargs.pop("defaults")

        if "direction" in kwargs:
            direction = processed_kwargs["direction"] = kwargs.pop("direction")
            from pathway.stdlib.temporal import Direction

            if isinstance(direction, str):
                raise ValueError(
                    "Received `direction` argument of join that is a string.\n"
                    + "You probably want to use one of "
                    + "Direction.BACKWARD, Direction.FORWARD or Direction.NEAREST values."
                )
            if not isinstance(direction, Direction):
                raise ValueError(
                    "direction argument of join should be of type asof_join.Direction."
                )

        if kwargs:
            raise ValueError(
                "Join received extra kwargs.\n"
                + "You probably want to use TableLike.join(...).select(**kwargs) to compute output columns."
            )
        return (self, other, *on), processed_kwargs

    return handler


def reduce_args_handler(self, *args, **kwargs):
    for arg in args:
        if expr.smart_name(arg) is None:
            if isinstance(arg, str):
                raise ValueError(
                    f"Expected a ColumnReference, found a string. Did you mean this.{arg} instead of {repr(arg)}?"
                )
            else:
                raise ValueError(
                    "In reduce() all positional arguments have to be a ColumnReference."
                )
    return (self, *args), kwargs


def select_args_handler(self, *args, **kwargs):
    for arg in args:
        if not isinstance(arg, expr.ColumnRefOrIxExpression):
            if isinstance(arg, str):
                raise ValueError(
                    f"Expected a ColumnReference, found a string. Did you mean this.{arg} instead of {repr(arg)}?"
                )
            else:
                raise ValueError(
                    "In select() all positional arguments have to be a ColumnReference."
                )
    return (self, *args), kwargs
