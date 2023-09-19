# Copyright © 2023 Pathway


from __future__ import annotations

import itertools
from functools import lru_cache
from typing import TYPE_CHECKING, Any, Dict, Iterator, Optional, Tuple, cast

from pathway.internals.trace import trace_user_frame

if TYPE_CHECKING:
    from pathway.internals.groupby import GroupedJoinResult
    from pathway.internals.table import Table

from abc import abstractmethod

import pathway.internals.column as clmn
import pathway.internals.expression as expr
from pathway.internals import thisclass
from pathway.internals.arg_handlers import (
    arg_handler,
    join_kwargs_handler,
    reduce_args_handler,
    select_args_handler,
)
from pathway.internals.decorators import contextualized_operator
from pathway.internals.desugaring import (
    DesugaringContext,
    SubstitutionDesugaring,
    TableSelectDesugaring,
    combine_args_kwargs,
    desugar,
)
from pathway.internals.helpers import StableSet
from pathway.internals.join_mode import JoinMode
from pathway.internals.operator_input import OperatorInput
from pathway.internals.shadows import operator as op
from pathway.internals.table_like import TableLike
from pathway.internals.type_interpreter import eval_type
from pathway.internals.universe import Universe


class Joinable(TableLike, DesugaringContext):
    @abstractmethod
    def _subtables(self) -> StableSet[Table]:
        ...

    @abstractmethod
    def _subjoinables(self) -> StableSet[Joinable]:
        ...

    @abstractmethod
    def keys(self):
        ...

    @abstractmethod
    def select(self, *args: expr.ColumnReference, **kwargs: Any) -> Table:
        ...

    @abstractmethod
    def filter(self, filter_expression: expr.ColumnExpression) -> Joinable:
        ...

    @abstractmethod
    def __getitem__(self, args: str | expr.ColumnReference) -> expr.ColumnReference:
        ...

    def __iter__(self) -> Iterator[expr.ColumnReference]:
        return (self[name] for name in self.keys())

    @abstractmethod
    def _get_colref_by_name(self, name, exception_type) -> expr.ColumnReference:
        ...

    @abstractmethod
    def _operator_dependencies(self) -> StableSet[Table]:
        ...

    @trace_user_frame
    def __getattr__(self, name) -> expr.ColumnReference:
        """Get columns by name.

        Warning:
            - Fails if it tries to access nonexistent column.

        Returns:
            Column expression.

        Example:

        >>> import pathway as pw
        >>> t1 = pw.debug.parse_to_table('''
        ... age | owner | pet
        ... 10  | Alice | dog
        ... 9   | Bob   | dog
        ... 8   | Alice | cat
        ... 7   | Bob   | dog
        ... ''')
        >>> t2 = t1.select(t1.age)
        >>> pw.debug.compute_and_print(t2, include_id=False)
        age
        7
        8
        9
        10
        """
        try:
            return super().__getattr__(name)
        except AttributeError:
            pass
        return self._get_colref_by_name(name, AttributeError)

    @trace_user_frame
    @desugar(substitution={thisclass.left: "self", thisclass.right: "other"})
    @arg_handler(handler=join_kwargs_handler(allow_how=True, allow_id=True))
    def join(
        self,
        other: Joinable,
        *on: expr.ColumnExpression,
        id: Optional[expr.ColumnReference] = None,
        how: JoinMode = JoinMode.INNER,
    ) -> JoinResult:
        """Join self with other using the given join expression.

        Args:
            other:  the right side of the join.
            on:  a list of column expressions. Each must have == as the top level operation
                and be of the form LHS: ColumnReference == RHS: ColumnReference.
            id: optional argument for id of result, can be only self.id or other.id
            how: by default, inner join is performed. Possible values are JoinMode.{INNER,LEFT,RIGHT,OUTER}
              correspond to inner, left, right and outer join respectively.

        Returns:
            JoinResult: an object on which `.select()` may be called to extract relevant
            columns from the result of the join.

        Example:

        >>> import pathway as pw
        >>> t1 = pw.debug.parse_to_table('''
        ... age  | owner  | pet
        ...  10  | Alice  | 1
        ...   9  | Bob    | 1
        ...   8  | Alice  | 2
        ... ''')
        >>> t2 = pw.debug.parse_to_table('''
        ... age  | owner  | pet | size
        ...  10  | Alice  | 3   | M
        ...  9   | Bob    | 1   | L
        ...  8   | Tom    | 1   | XL
        ... ''')
        >>> t3 = t1.join(
        ...     t2, t1.pet == t2.pet, t1.owner == t2.owner, how=pw.JoinMode.INNER
        ... ).select(age=t1.age, owner_name=t2.owner, size=t2.size)
        >>> pw.debug.compute_and_print(t3, include_id = False)
        age | owner_name | size
        9   | Bob        | L
        """
        from pathway.internals import join

        return join.JoinResult._table_join(self, other, *on, mode=how, id=id)

    @trace_user_frame
    @desugar(substitution={thisclass.left: "self", thisclass.right: "other"})
    @arg_handler(handler=join_kwargs_handler(allow_how=False, allow_id=True))
    def join_inner(
        self,
        other: Joinable,
        *on: expr.ColumnExpression,
        id: Optional[expr.ColumnReference] = None,
    ) -> JoinResult:
        """Inner-joins two tables or join results.

        Args:
            other:  the right side of the join.
            on:  a list of column expressions. Each must have == as the top level operation
                and be of the form LHS: ColumnReference == RHS: ColumnReference.
            id: optional argument for id of result, can be only self.id or other.id

        Returns:
            JoinResult: an object on which `.select()` may be called to extract relevant
            columns from the result of the join.

        Example:

        >>> import pathway as pw
        >>> t1 = pw.debug.parse_to_table('''
        ... age  | owner  | pet
        ...  10  | Alice  | 1
        ...   9  | Bob    | 1
        ...   8  | Alice  | 2
        ... ''')
        >>> t2 = pw.debug.parse_to_table('''
        ... age  | owner  | pet | size
        ...  10  | Alice  | 3   | M
        ...  9   | Bob    | 1   | L
        ...  8   | Tom    | 1   | XL
        ... ''')
        >>> t3 = t1.join(t2, t1.pet == t2.pet, t1.owner == t2.owner, how=pw.JoinMode.INNER).select(age=t1.age, owner_name=t2.owner, size=t2.size)  # noqa: E501
        >>> pw.debug.compute_and_print(t3, include_id = False)
        age | owner_name | size
        9   | Bob        | L
        """
        from pathway.internals import join

        return join.JoinResult._table_join(self, other, *on, mode=JoinMode.INNER, id=id)

    @trace_user_frame
    @desugar(substitution={thisclass.left: "self", thisclass.right: "other"})
    @arg_handler(handler=join_kwargs_handler(allow_how=False, allow_id=True))
    def join_left(
        self,
        other: Joinable,
        *on: expr.ColumnExpression,
        id: Optional[expr.ColumnReference] = None,
    ) -> JoinResult:
        """
        Left-joins two tables or join results.

        Args:
            other: Table or join result.
            *on: Columns to join, syntax `self.col1 == other.col2`
            id: optional id column of the result

        Remarks:
        args cannot contain id column from either of tables, \
        as the result table has id column with auto-generated ids; \
        it can be selected by assigning it to a column with defined \
        name (passed in kwargs)

        Behavior:
        - for rows from the left side that were not matched with the right side,
        missing values on the right are replaced with `None`
        - rows from the right side that were not matched with the left side are skipped
        - for rows that were matched the behavior is the same as that of an inner join.

        Returns:
            JoinResult: an object on which `.select()` may be called to extract relevant
            columns from the result of the join.

        Example:

        >>> import pathway as pw
        >>> t1 = pw.debug.table_from_markdown(
        ...     '''
        ...         | A  | B
        ...       1 | 11 | 111
        ...       2 | 12 | 112
        ...       3 | 13 | 113
        ...       4 | 13 | 114
        ...     '''
        ... )
        >>> t2 = pw.debug.table_from_markdown(
        ...     '''
        ...         | C  | D
        ...       1 | 11 | 211
        ...       2 | 12 | 212
        ...       3 | 14 | 213
        ...       4 | 14 | 214
        ...     '''
        ... )
        >>> pw.debug.compute_and_print(t1.join_left(t2, t1.A == t2.C
        ... ).select(t1.A, t2_C=t2.C, S=pw.require(t1.B + t2.D,t2.id)),
        ... include_id=False)
        A  | t2_C | S
        11 | 11   | 322
        12 | 12   | 324
        13 |      |
        13 |      |
        """
        from pathway.internals import join

        return join.JoinResult._table_join(self, other, *on, mode=JoinMode.LEFT, id=id)

    @trace_user_frame
    @desugar(substitution={thisclass.left: "self", thisclass.right: "other"})
    @arg_handler(handler=join_kwargs_handler(allow_how=False, allow_id=True))
    def join_right(
        self,
        other: Joinable,
        *on: expr.ColumnExpression,
        id: Optional[expr.ColumnReference] = None,
    ) -> JoinResult:
        """
        Outer-joins two tables or join results.

        Args:
            other: Table or join result.
            *on: Columns to join, syntax `self.col1 == other.col2`
            id: optional id column of the result

        Remarks: args cannot contain id column from either of tables, \
        as the result table has id column with auto-generated ids; \
        it can be selected by assigning it to a column with defined \
        name (passed in kwargs)

        Behavior:
        - rows from the left side that were not matched with the right side are skipped
        - for rows from the right side that were not matched with the left side,
        missing values on the left are replaced with `None`
        - for rows that were matched the behavior is the same as that of an inner join.

        Returns:
            JoinResult: an object on which `.select()` may be called to extract relevant
            columns from the result of the join.

        Example:

        >>> import pathway as pw
        >>> t1 = pw.debug.table_from_markdown(
        ...     '''
        ...         | A  | B
        ...       1 | 11 | 111
        ...       2 | 12 | 112
        ...       3 | 13 | 113
        ...       4 | 13 | 114
        ...     '''
        ... )
        >>> t2 = pw.debug.table_from_markdown(
        ...     '''
        ...         | C  | D
        ...       1 | 11 | 211
        ...       2 | 12 | 212
        ...       3 | 14 | 213
        ...       4 | 14 | 214
        ...     '''
        ... )
        >>> pw.debug.compute_and_print(t1.join_right(t2, t1.A == t2.C
        ... ).select(t1.A, t2_C=t2.C, S=pw.require(pw.coalesce(t1.B,0) + t2.D,t1.id)),
        ... include_id=False)
        A  | t2_C | S
           | 14   |
           | 14   |
        11 | 11   | 322
        12 | 12   | 324

        Returns:
            OuterJoinResult object

        """
        from pathway.internals import join

        return join.JoinResult._table_join(self, other, *on, mode=JoinMode.RIGHT, id=id)

    @trace_user_frame
    @desugar(substitution={thisclass.left: "self", thisclass.right: "other"})
    @arg_handler(handler=join_kwargs_handler(allow_how=False, allow_id=True))
    def join_outer(
        self,
        other: Joinable,
        *on: expr.ColumnExpression,
        id: Optional[expr.ColumnReference] = None,
    ) -> JoinResult:
        """Outer-joins two tables or join results.

        Args:
            other: Table or join result.
            *on: Columns to join, syntax `self.col1 == other.col2`
            id: optional id column of the result

        Remarks: args cannot contain id column from either of tables, \
            as the result table has id column with auto-generated ids; \
            it can be selected by assigning it to a column with defined \
            name (passed in kwargs)

        Behavior:
        - for rows from the left side that were not matched with the right side,
        missing values on the right are replaced with `None`
        - for rows from the right side that were not matched with the left side,
        missing values on the left are replaced with `None`
        - for rows that were matched the behavior is the same as that of an inner join.

        Returns:
            JoinResult: an object on which `.select()` may be called to extract relevant
            columns from the result of the join.

        Example:

        >>> import pathway as pw
        >>> t1 = pw.debug.table_from_markdown(
        ...     '''
        ...         | A  | B
        ...       1 | 11 | 111
        ...       2 | 12 | 112
        ...       3 | 13 | 113
        ...       4 | 13 | 114
        ...     '''
        ... )
        >>> t2 = pw.debug.table_from_markdown(
        ...     '''
        ...         | C  | D
        ...       1 | 11 | 211
        ...       2 | 12 | 212
        ...       3 | 14 | 213
        ...       4 | 14 | 214
        ...     '''
        ... )
        >>> pw.debug.compute_and_print(t1.join_outer(t2, t1.A == t2.C
        ... ).select(t1.A, t2_C=t2.C, S=pw.require(t1.B + t2.D,t1.id,t2.id)),
        ... include_id=False)
        A  | t2_C | S
           | 14   |
           | 14   |
        11 | 11   | 322
        12 | 12   | 324
        13 |      |
        13 |      |
        """
        from pathway.internals import join

        return join.JoinResult._table_join(self, other, *on, mode=JoinMode.OUTER, id=id)

    @property
    def _desugaring(self) -> TableSelectDesugaring:
        return TableSelectDesugaring(self)

    @abstractmethod
    def _substitutions(
        self, cnt: Iterator
    ) -> Tuple[Table, Dict[expr.InternalColRef, expr.ColumnExpression]]:
        ...


class JoinResult(Joinable, OperatorInput):
    """Result of a join between tables.

    Example:

    >>> import pathway as pw
    >>> t1 = pw.debug.parse_to_table('''
    ...    age  owner  pet
    ... 1   10  Alice    1
    ... 2    9    Bob    1
    ... 3    8  Alice    2
    ... ''')
    >>> t2 = pw.debug.parse_to_table('''
    ...     age  owner  pet size
    ... 11   10  Alice    3    M
    ... 12    9    Bob    1    L
    ... 13    8    Tom    1   XL
    ... ''')
    >>> joinresult= t1.join(t2, t1.pet == t2.pet, t1.owner == t2.owner)   # noqa: E501
    >>> isinstance(joinresult, pw.JoinResult)
    True
    >>> pw.debug.compute_and_print(joinresult.select(t1.age, t2.size), include_id=False)
    age | size
    9   | L
    """

    _context: clmn.JoinContext
    _left_table: Table
    _right_table: Table
    _original_left: Joinable
    _original_right: Joinable
    _substitution: Dict[thisclass.ThisMetaclass, Joinable]
    _chained_join_desugaring: SubstitutionDesugaring
    _joined_on_names: StableSet[str]
    _all_colnames: StableSet[str]
    _id_colref_table: Table
    _join_mode: JoinMode

    def __init__(
        self,
        _universe: Universe,
        _context: clmn.JoinContext,
        _left_table: Table,
        _right_table: Table,
        _original_left: Joinable,
        _original_right: Joinable,
        _substitution: Dict[thisclass.ThisMetaclass, Joinable],
        _chained_join_desugaring: SubstitutionDesugaring,
        _joined_on_names: StableSet[str],
        _join_mode: JoinMode,
    ):
        super().__init__(_universe)
        self._context = _context
        self._left_table = _left_table
        self._right_table = _right_table
        self._substitution = {**_substitution, thisclass.this: self}
        self._chained_join_desugaring = _chained_join_desugaring
        self._joined_on_names = _joined_on_names
        self._join_mode = _join_mode
        self._original_left = _original_left
        self._original_right = _original_right
        assert _original_left._subtables().isdisjoint(_original_right._subtables())
        self._all_colnames = StableSet.union(
            _original_left.keys(), _original_right.keys()
        )
        from pathway.internals.common import coalesce

        self._id_colref_table = self.select(
            **{
                name: coalesce(thisclass.left[name], thisclass.right[name])
                for name in self._joined_on_names
                if name != "id"
            }
        )

    @staticmethod
    def _compute_universe(
        left_table: Table,
        right_table: Table,
        id: Optional[clmn.Column],
        mode: JoinMode,
    ) -> Universe:
        if id is left_table._id_column:
            if mode == JoinMode.LEFT:
                return left_table._universe
            elif mode == JoinMode.INNER:
                return left_table._universe.subset()
            else:
                raise KeyError("Cannot assign id's for this join type.")
        elif id is right_table._id_column:
            if mode == JoinMode.RIGHT:
                return right_table._universe
            elif mode == JoinMode.INNER:
                return right_table._universe.subset()
            else:
                raise KeyError("Cannot assign id's for this join type.")
        else:
            assert id is None
            return Universe()

    def _eval(self, expression: expr.ColumnExpression) -> clmn.ColumnWithExpression:
        expression = self._chained_join_desugaring.eval_expression(expression)
        return expression._column_with_expression_cls(
            context=self._context,
            universe=self._universe,
            expression=expression,
        )

    def _subtables(self) -> StableSet[Table]:
        return self._original_left._subtables() | self._original_right._subtables()

    def _subjoinables(self) -> StableSet[Joinable]:
        return (
            self._original_left._subjoinables()
            | self._original_right._subjoinables()
            | StableSet([self])
        )

    def keys(self):
        common_colnames = self._original_left.keys() & self._original_right.keys()
        return self._all_colnames - (common_colnames - self._joined_on_names)

    def _get_colref_by_name(
        self,
        name: str,
        exception_type,
    ) -> expr.ColumnReference:
        if name == "id":
            return self._id_colref_table.id
        elif name in self._joined_on_names:
            if self._join_mode is JoinMode.INNER:
                return self._original_left[name]
            else:
                return self._id_colref_table[name]
        elif name in self._original_left.keys() and name in self._original_right.keys():
            raise exception_type(
                f"Column {name} appears on both left and right inputs of join."
            )
        elif name in self._original_left.keys():
            return self._original_left[name]
        elif name in self._original_right.keys():
            return self._original_right[name]
        else:
            raise exception_type(f"No column with name {name}.")

    def __getitem__(self, args: str | expr.ColumnReference) -> expr.ColumnReference:
        if isinstance(args, expr.ColumnReference):
            assert args.table is self or args.table is thisclass.this
            return self._get_colref_by_name(args.name, KeyError)
        else:
            return self._get_colref_by_name(args, KeyError)

    @trace_user_frame
    @desugar
    @arg_handler(handler=select_args_handler)
    @contextualized_operator
    def select(self, *args: expr.ColumnReference, **kwargs: Any) -> Table:
        """Computes result of a join.

        Args:
            args: Column references.
            kwargs: Column expressions with their new assigned names.


        Returns:
            Table: Created table.

        Example:

        >>> import pathway as pw
        >>> t1 = pw.debug.parse_to_table('''
        ... age  | owner  | pet
        ...  10  | Alice  | 1
        ...   9  | Bob    | 1
        ...   8  | Alice  | 2
        ... ''')
        >>> t2 = pw.debug.parse_to_table('''
        ... age  | owner  | pet | size
        ...  10  | Alice  | 3   | M
        ...  9   | Bob    | 1   | L
        ...  8   | Tom    | 1   | XL
        ... ''')
        >>> t3 = t1.join(t2, t1.pet == t2.pet, t1.owner == t2.owner).select(age=t1.age, owner_name=t2.owner, size=t2.size)   # noqa: E501
        >>> pw.debug.compute_and_print(t3, include_id=False)
        age | owner_name | size
        9   | Bob        | L
        """
        columns: Dict[str, clmn.Column] = {}

        all_args = combine_args_kwargs(args, kwargs)

        for new_name, expression in all_args.items():
            columns[new_name] = self._eval(expression)
        from pathway.internals.table import Table

        return Table(
            columns=columns,
            universe=self._context.universe,
            id_column=clmn.IdColumn(self._context),
        )

    @lru_cache
    def _operator_dependencies(self) -> StableSet[Table]:
        return (
            self._left_table._operator_dependencies()
            | self._right_table._operator_dependencies()
        )

    @desugar
    @trace_user_frame
    def filter(self, filter_expression: expr.ColumnExpression) -> FilteredJoinResult:
        """Filters rows, keeping the ones satisfying the predicate.

        Example:

        >>> import pathway as pw
        >>> t1 = pw.debug.parse_to_table('''
        ...    age  owner  pet
        ... 1   10  Alice    1
        ... 2    9    Bob    1
        ... 3    8  Alice    2
        ... ''')
        >>> t2 = pw.debug.parse_to_table('''
        ...     age  owner  pet size
        ... 11   10  Alice    3    M
        ... 12    9    Bob    1    L
        ... 13    8    Tom    1   XL
        ... ''')
        >>> result = t1.join(t2).filter(t1.owner == t2.owner).select(t1.age, t2.size)   # noqa: E501
        >>> pw.debug.compute_and_print(result, include_id=False)
        age | size
        8   | M
        9   | L
        10  | M
        """
        filtered_table = self.select(tmp_filter=filter_expression).filter(
            thisclass.this.tmp_filter
        )
        return FilteredJoinResult(self, filtered_table)

    @trace_user_frame
    @desugar
    def groupby(
        self,
        *args: expr.ColumnReference,
        id: Optional[expr.ColumnReference] = None,
    ) -> GroupedJoinResult:
        """Groups join result by columns from args.

        Note:
            Usually followed by `.reduce()` that aggregates the result and returns a table.

        Args:
            args: columns to group by.
            id: if provided, is the column used to set id's of the rows of the result

        Returns:
            GroupedJoinResult: Groupby object.

        Example:

        >>> import pathway as pw
        >>> t1 = pw.debug.parse_to_table('''
        ...    cost  owner  pet
        ... 1   100  Alice    1
        ... 2    90    Bob    1
        ... 3    80  Alice    2
        ... ''')
        >>> t2 = pw.debug.parse_to_table('''
        ...     cost  owner  pet size
        ... 11   100  Alice    3    M
        ... 12    90    Bob    1    L
        ... 13    80    Tom    1   XL
        ... ''')
        >>> result = (t1.join(t2, t1.owner==t2.owner).groupby(pw.this.owner)
        ...     .reduce(pw.this.owner, pairs = pw.reducers.count()))
        >>> pw.debug.compute_and_print(result, include_id=False)
        owner | pairs
        Alice | 2
        Bob   | 1
        """
        for arg in args:
            if not isinstance(arg, expr.ColumnReference):
                if isinstance(arg, str):
                    raise ValueError(
                        f"Expected a ColumnReference, found a string. Did you mean this.{arg} instead of {repr(arg)}?"
                    )
                else:
                    raise ValueError(
                        "In JoinResult.groupby() all arguments have to be a ColumnReference."
                    )
        from pathway.internals.groupby import GroupedJoinResult

        return GroupedJoinResult(
            join_result=self,
            args=args,
            id=id,
        )

    @trace_user_frame
    @desugar
    @arg_handler(handler=reduce_args_handler)
    def reduce(
        self, *args: expr.ColumnReference, **kwargs: expr.ColumnExpression
    ) -> Table:
        """Reduce a join result to a single row.

        Equivalent to `self.groupby().reduce(*args, **kwargs)`.

        Args:
            args: reducer to reduce the table with
            kwargs: reducer to reduce the table with. Its key is the new name of a column.

        Returns:
            Table: Reduced table.

        Example:

        >>> import pathway as pw
        >>> t1 = pw.debug.parse_to_table('''
        ...    cost  owner  pet
        ... 1   100  Alice    1
        ... 2    90    Bob    1
        ... 3    80  Alice    2
        ... ''')
        >>> t2 = pw.debug.parse_to_table('''
        ...     cost  owner  pet size
        ... 11   100  Alice    3    M
        ... 12    90    Bob    1    L
        ... 13    80    Tom    1   XL
        ... ''')
        >>> result = t1.join(t2, t1.owner==t2.owner).reduce(total_pairs = pw.reducers.count())
        >>> pw.debug.compute_and_print(result, include_id=False)
        total_pairs
        3
        """
        for arg in args:
            if not isinstance(arg, expr.ColumnReference):
                if isinstance(arg, str):
                    raise ValueError(
                        f"Expected a ColumnReference, found a string. Did you mean this.{arg} instead of {repr(arg)}?"
                    )
                else:
                    raise ValueError(
                        "In JoinResult.reduce() all positional arguments have to be a ColumnReference."
                    )
        return self.groupby().reduce(*args, **kwargs)

    def _substitutions(
        self, cnt: Iterator
    ) -> Tuple[Table, Dict[expr.InternalColRef, expr.ColumnExpression]]:
        subs: Dict[expr.InternalColRef, str] = {}  # old to new
        for subjoinable in self._subjoinables():
            for expression in subjoinable:
                subs[expression._to_internal()] = f"c{next(cnt)}"
            subs[subjoinable.id._to_internal()] = f"c{next(cnt)}"
        tab = self.select(
            **{
                new_name: expression.to_colref()
                for expression, new_name in subs.items()
            },
        )
        subs_full: Dict[expr.InternalColRef, expr.ColumnExpression] = {
            expression: tab[new_name] for expression, new_name in subs.items()
        }
        subs_full[self.id._to_internal()] = tab.id
        return tab, subs_full

    @staticmethod
    def _table_join(
        left: Joinable,
        right: Joinable,
        *on: expr.ColumnExpression,
        mode: JoinMode,
        id: Optional[expr.ColumnReference] = None,
    ) -> JoinResult:
        if left == right:
            raise ValueError(
                "Cannot join table with itself. Use <table>.copy() as one of the arguments of the join."
            )

        cnt: Iterator = itertools.count(0)

        left_table, left_substitutions = left._substitutions(cnt)
        right_table, right_substitutions = right._substitutions(cnt)

        chained_join_desugaring = SubstitutionDesugaring(
            {**left_substitutions, **right_substitutions}
        )

        if id is not None:
            id = cast(expr.ColumnReference, chained_join_desugaring.eval_expression(id))
            id_column = id._column
        else:
            id_column = None

        common_column_names: StableSet[str] = StableSet()

        on_ = tuple(validate_shape(cond) for cond in on)

        for cond in on_:
            cond_left = cast(expr.ColumnReference, cond._left)
            cond_right = cast(expr.ColumnReference, cond._right)
            if cond_left.name == cond_right.name:
                common_column_names.add(cond_left.name)

        on_ = tuple(
            cast(
                expr.ColumnBinaryOpExpression,
                chained_join_desugaring.eval_expression(cond),
            )
            for cond in on_
        )

        for cond in on_:
            validate_join_condition(cond, left_table, right_table)

        on_left = tuple(
            left_table._eval(cond._left, left_table._table_restricted_context)
            for cond in on_
        )
        on_right = tuple(
            right_table._eval(cond._right, right_table._table_restricted_context)
            for cond in on_
        )

        swp = id_column is not None and id_column is right_table._id_column
        assert (
            id_column is None
            or (id_column is left_table._id_column)
            or (id_column is right_table._id_column)
        )

        left_context_table = clmn.ContextTable(universe=left._universe, columns=on_left)
        right_context_table = clmn.ContextTable(
            universe=right._universe, columns=on_right
        )
        substitution: Dict[thisclass.ThisMetaclass, Joinable] = {
            thisclass.left: left,
            thisclass.right: right,
        }
        universe = JoinResult._compute_universe(
            left_table, right_table, id_column, mode
        )
        if swp:
            context = clmn.JoinContext(
                universe,
                right_table,
                left_table,
                right_context_table,
                left_context_table,
                id_column is not None,
                mode in [JoinMode.RIGHT, JoinMode.OUTER],
                mode in [JoinMode.LEFT, JoinMode.OUTER],
            )
        else:
            context = clmn.JoinContext(
                universe,
                left_table,
                right_table,
                left_context_table,
                right_context_table,
                id_column is not None,
                mode in [JoinMode.LEFT, JoinMode.OUTER],
                mode in [JoinMode.RIGHT, JoinMode.OUTER],
            )
        return JoinResult(
            universe,
            context,
            left_table,
            right_table,
            left,
            right,
            substitution,
            chained_join_desugaring,
            common_column_names,
            mode,
        )


class FilteredJoinResult(JoinResult):
    _context: clmn.JoinFilterContext
    _join_result: JoinResult

    def __init__(
        self,
        join_result: JoinResult,
        filtering: Table,
    ):
        universe = filtering._universe
        self._filtering = filtering
        self._join_result = join_result
        new_context = clmn.JoinFilterContext(
            **{  # type: ignore
                **vars(
                    join_result._context,
                ),
                "universe": universe,
                "filtering_column": filtering._id_column,
            }
        )
        super().__init__(
            universe,
            new_context,
            join_result._left_table,
            join_result._right_table,
            join_result._original_left,
            join_result._original_right,
            join_result._substitution,
            join_result._chained_join_desugaring,
            join_result._joined_on_names,
            join_result._join_mode,
        )

    @lru_cache
    def _operator_dependencies(self) -> StableSet[Table]:
        return self._join_result._operator_dependencies() | [self._filtering]


def validate_shape(cond: expr.ColumnExpression) -> expr.ColumnBinaryOpExpression:
    if (
        not isinstance(cond, expr.ColumnBinaryOpExpression)
        or cond._operator != op.eq
        or not isinstance(cond._left, expr.ColumnReference)
        or not isinstance(cond._right, expr.ColumnReference)
    ):
        raise ValueError(
            "join condition should be of form <left_table>.<column> == <right_table>.<column>"
        )
    return cond


def validate_join_condition(
    cond: expr.ColumnExpression, left: Table, right: Table
) -> Tuple[expr.ColumnReference, expr.ColumnReference, expr.ColumnBinaryOpExpression]:
    eval_type(cond)
    cond = validate_shape(cond)
    cond_left = cast(expr.ColumnReference, cond._left)
    cond_right = cast(expr.ColumnReference, cond._right)
    if cond_left.table == right and cond_right.table == left:
        raise ValueError(
            "The boolean condition is not properly ordered.\n"
            + "The left part should refer to left joinable and the right one should refer to the right joinable,"
            + " e.g. t1.join(t2, t1.bar==t2.foo)."
        )
    if cond_left.table != left:
        raise ValueError(
            "Left part of a join condition has to be a reference to a table "
            + "on the left side of a join"
        )
    if cond_right.table != right:
        raise ValueError(
            "Right part of a join condition has to be a reference to a table "
            + "on the right side of a join"
        )
    return cond_left, cond_right, cond
