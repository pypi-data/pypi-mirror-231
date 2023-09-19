# Copyright © 2023 Pathway

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Callable, Dict, Type, TypeVar, cast

from pathway.internals import expression as expr


class ExpressionVisitor(ABC):
    def eval_expression(self, expression, **kwargs):
        impl: Dict[Type, Callable] = {
            expr.ColumnReference: self.eval_column_val,
            expr.ColumnUnaryOpExpression: self.eval_unary_op,
            expr.ColumnBinaryOpExpression: self.eval_binary_op,
            expr.ReducerExpression: self.eval_reducer,
            expr.ReducerIxExpression: self.eval_reducer_ix,
            expr.CountExpression: self.eval_count,
            expr.ApplyExpression: self.eval_apply,
            expr.ColumnConstExpression: self.eval_const,
            expr.ColumnIxExpression: self.eval_ix,
            expr.ColumnCallExpression: self.eval_call,
            expr.PointerExpression: self.eval_pointer,
            expr.CastExpression: self.eval_cast,
            expr.DeclareTypeExpression: self.eval_declare,
            expr.CoalesceExpression: self.eval_coalesce,
            expr.RequireExpression: self.eval_require,
            expr.IfElseExpression: self.eval_ifelse,
            expr.NumbaApplyExpression: self.eval_numbaapply,
            expr.AsyncApplyExpression: self.eval_async_apply,
            expr.MakeTupleExpression: self.eval_make_tuple,
            expr.SequenceGetExpression: self.eval_sequence_get,
            expr.MethodCallExpression: self.eval_method_call,
            expr.IsNotNoneExpression: self.eval_not_none,
            expr.IsNoneExpression: self.eval_none,
            expr.UnwrapExpression: self.eval_unwrap,
        }
        if not isinstance(expression, expr.ColumnExpression):
            return self.eval_any(expression, **kwargs)
        return impl[type(expression)](expression, **kwargs)

    @abstractmethod
    def eval_column_val(self, expression: expr.ColumnReference):
        ...

    @abstractmethod
    def eval_unary_op(self, expression: expr.ColumnUnaryOpExpression):
        ...

    @abstractmethod
    def eval_binary_op(self, expression: expr.ColumnBinaryOpExpression):
        ...

    @abstractmethod
    def eval_const(self, expression: expr.ColumnConstExpression):
        ...

    @abstractmethod
    def eval_reducer(self, expression: expr.ReducerExpression):
        ...

    @abstractmethod
    def eval_reducer_ix(self, expression: expr.ReducerIxExpression):
        ...

    @abstractmethod
    def eval_count(self, expression: expr.CountExpression):
        ...

    @abstractmethod
    def eval_apply(self, expression: expr.ApplyExpression):
        ...

    @abstractmethod
    def eval_numbaapply(self, expression: expr.NumbaApplyExpression):
        ...

    @abstractmethod
    def eval_async_apply(self, expression: expr.AsyncApplyExpression):
        ...

    @abstractmethod
    def eval_pointer(self, expression: expr.PointerExpression):
        ...

    @abstractmethod
    def eval_ix(self, expression: expr.ColumnIxExpression):
        ...

    @abstractmethod
    def eval_call(self, expression: expr.ColumnCallExpression):
        ...

    @abstractmethod
    def eval_cast(self, expression: expr.CastExpression):
        ...

    @abstractmethod
    def eval_declare(self, expression: expr.DeclareTypeExpression):
        ...

    @abstractmethod
    def eval_coalesce(self, expression: expr.CoalesceExpression):
        ...

    @abstractmethod
    def eval_require(self, expression: expr.RequireExpression):
        ...

    @abstractmethod
    def eval_ifelse(self, expression: expr.IfElseExpression):
        ...

    @abstractmethod
    def eval_not_none(self, expression: expr.IsNotNoneExpression):
        ...

    @abstractmethod
    def eval_none(self, expression: expr.IsNoneExpression):
        ...

    @abstractmethod
    def eval_make_tuple(self, expression: expr.MakeTupleExpression):
        ...

    @abstractmethod
    def eval_sequence_get(self, expression: expr.SequenceGetExpression):
        ...

    @abstractmethod
    def eval_method_call(self, expression: expr.MethodCallExpression):
        ...

    @abstractmethod
    def eval_unwrap(self, expression: expr.UnwrapExpression):
        ...

    def eval_any(self, expression, **kwargs):
        expression = expr.ColumnConstExpression(expression)
        return self.eval_const(expression, **kwargs)


ColExprT = TypeVar("ColExprT", bound=expr.ColumnExpression)


class IdentityTransform(ExpressionVisitor):
    def eval_expression(self, expression: ColExprT, **kwargs) -> ColExprT:
        return super().eval_expression(expression, **kwargs)

    def eval_column_val(
        self, expression: expr.ColumnReference, **kwargs
    ) -> expr.ColumnReference:
        return expr.ColumnReference(
            column=expression._column, table=expression._table, name=expression._name
        )

    def eval_unary_op(
        self, expression: expr.ColumnUnaryOpExpression, **kwargs
    ) -> expr.ColumnUnaryOpExpression:
        result = self.eval_expression(expression._expr, **kwargs)
        return expr.ColumnUnaryOpExpression(expr=result, operator=expression._operator)

    def eval_binary_op(
        self, expression: expr.ColumnBinaryOpExpression, **kwargs
    ) -> expr.ColumnBinaryOpExpression:
        left = self.eval_expression(expression._left, **kwargs)
        right = self.eval_expression(expression._right, **kwargs)
        return expr.ColumnBinaryOpExpression(
            left=left, right=right, operator=expression._operator
        )

    def eval_const(
        self, expression: expr.ColumnConstExpression, **kwargs
    ) -> expr.ColumnConstExpression:
        return expr.ColumnConstExpression(expression._val)

    def eval_reducer(
        self, expression: expr.ReducerExpression, **kwargs
    ) -> expr.ReducerExpression:
        args = [self.eval_expression(arg, **kwargs) for arg in expression._args]
        return expr.ReducerExpression(expression._reducer, *args)

    def eval_reducer_ix(
        self, expression: expr.ReducerIxExpression, **kwargs
    ) -> expr.ReducerIxExpression:
        [arg] = [self.eval_expression(arg, **kwargs) for arg in expression._args]
        return expr.ReducerIxExpression(
            expression._reducer, cast(expr.ColumnIxExpression, arg)
        )

    def eval_count(
        self, expression: expr.CountExpression, **kwargs
    ) -> expr.CountExpression:
        return expr.CountExpression()

    def eval_apply(
        self, expression: expr.ApplyExpression, **kwargs
    ) -> expr.ApplyExpression:
        expr_args = [self.eval_expression(arg, **kwargs) for arg in expression._args]
        expr_kwargs = {
            name: self.eval_expression(arg, **kwargs)
            for name, arg in expression._kwargs.items()
        }
        return expr.ApplyExpression(
            expression._fun, expression._return_type, *expr_args, **expr_kwargs
        )

    def eval_numbaapply(
        self, expression: expr.NumbaApplyExpression, **kwargs
    ) -> expr.NumbaApplyExpression:
        expr_args = [self.eval_expression(arg, **kwargs) for arg in expression._args]
        expr_kwargs = {
            name: self.eval_expression(arg, **kwargs)
            for name, arg in expression._kwargs.items()
        }
        return expr.NumbaApplyExpression(
            expression._fun, expression._return_type, *expr_args, **expr_kwargs
        )

    def eval_async_apply(
        self, expression: expr.AsyncApplyExpression, **kwargs
    ) -> expr.AsyncApplyExpression:
        expr_args = [self.eval_expression(arg, **kwargs) for arg in expression._args]
        expr_kwargs = {
            name: self.eval_expression(arg, **kwargs)
            for name, arg in expression._kwargs.items()
        }
        return expr.AsyncApplyExpression(
            expression._fun, expression._return_type, *expr_args, **expr_kwargs
        )

    def eval_pointer(
        self, expression: expr.PointerExpression, **kwargs
    ) -> expr.PointerExpression:
        expr_args = [self.eval_expression(arg, **kwargs) for arg in expression._args]
        optional = expression._optional
        return expr.PointerExpression(expression._table, *expr_args, optional=optional)

    def eval_ix(
        self, expression: expr.ColumnIxExpression, **kwargs
    ) -> expr.ColumnIxExpression:
        column_expression = self.eval_expression(
            expression._column_expression, **kwargs
        )
        keys_expression = self.eval_expression(expression._keys_expression, **kwargs)
        return expr.ColumnIxExpression(
            column_expression=column_expression,
            keys_expression=keys_expression,
            optional=expression._optional,
        )

    def eval_call(
        self, expression: expr.ColumnCallExpression, **kwargs
    ) -> expr.ColumnCallExpression:
        expr_args = [self.eval_expression(arg, **kwargs) for arg in expression._args]
        col_expr = self.eval_expression(expression._col_expr, **kwargs)
        assert isinstance(col_expr, expr.ColumnRefOrIxExpression)
        return expr.ColumnCallExpression(col_expr=col_expr, args=expr_args)

    def eval_cast(
        self, expression: expr.CastExpression, **kwargs
    ) -> expr.CastExpression:
        result = self.eval_expression(expression._expr, **kwargs)
        return expr.CastExpression(return_type=expression._return_type, expr=result)

    def eval_declare(
        self, expression: expr.DeclareTypeExpression, **kwargs
    ) -> expr.DeclareTypeExpression:
        result = self.eval_expression(expression._expr, **kwargs)
        return expr.DeclareTypeExpression(
            return_type=expression._return_type, expr=result
        )

    def eval_coalesce(
        self, expression: expr.CoalesceExpression, **kwargs
    ) -> expr.CoalesceExpression:
        expr_args = [self.eval_expression(arg, **kwargs) for arg in expression._args]
        return expr.CoalesceExpression(*expr_args)

    def eval_require(
        self, expression: expr.RequireExpression, **kwargs
    ) -> expr.RequireExpression:
        val = self.eval_expression(expression._val, **kwargs)
        expr_args = [self.eval_expression(arg, **kwargs) for arg in expression._args]
        return expr.RequireExpression(val, *expr_args)

    def eval_ifelse(
        self, expression: expr.IfElseExpression, **kwargs
    ) -> expr.IfElseExpression:
        return expr.IfElseExpression(
            self.eval_expression(expression._if, **kwargs),
            self.eval_expression(expression._then, **kwargs),
            self.eval_expression(expression._else, **kwargs),
        )

    def eval_not_none(
        self, expression: expr.IsNotNoneExpression, **kwargs
    ) -> expr.IsNotNoneExpression:
        return expr.IsNotNoneExpression(
            self.eval_expression(expression._expr, **kwargs)
        )

    def eval_none(
        self, expression: expr.IsNoneExpression, **kwargs
    ) -> expr.IsNoneExpression:
        return expr.IsNoneExpression(self.eval_expression(expression._expr, **kwargs))

    def eval_make_tuple(
        self, expression: expr.MakeTupleExpression, **kwargs
    ) -> expr.MakeTupleExpression:
        expr_args = [self.eval_expression(arg, **kwargs) for arg in expression._args]
        return expr.MakeTupleExpression(*expr_args)

    def eval_sequence_get(
        self, expression: expr.SequenceGetExpression, **kwargs
    ) -> expr.SequenceGetExpression:
        return expr.SequenceGetExpression(
            self.eval_expression(expression._object, **kwargs),
            self.eval_expression(expression._index, **kwargs),
            self.eval_expression(expression._default, **kwargs),
            check_if_exists=expression._check_if_exists,
        )

    def eval_method_call(
        self, expression: expr.MethodCallExpression, **kwargs
    ) -> expr.MethodCallExpression:
        expr_args = [self.eval_expression(arg, **kwargs) for arg in expression._args]
        return expr.MethodCallExpression(
            expression._fun_mapping,
            expression._name,
            *expr_args,
        )

    def eval_unwrap(
        self, expression: expr.UnwrapExpression, **kwargs
    ) -> expr.UnwrapExpression:
        result = self.eval_expression(expression._expr, **kwargs)
        return expr.UnwrapExpression(expr=result)
