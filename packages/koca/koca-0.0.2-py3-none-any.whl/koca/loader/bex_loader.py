#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: ewkoll ideath@operatorwrold.com
Date: 2023-09-18 11:22:01
LastEditors: ewkoll
LastEditTime: 2023-09-18 15:13:47
Description: 
Copyright (c) 2023 by ewkoll email: ideath@operatorwrold.com, All Rights Reserved.
"""
from __future__ import annotations
import typing as t
from functools import update_wrapper

F = t.TypeVar("F", bound=t.Callable[..., t.Any])


def setupmethod(f: F) -> F:
    def wrapper_func(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
        return f(self, *args, **kwargs)

    return t.cast(F, update_wrapper(wrapper_func, f))


class BexLoader:
    def __init__(self) -> None:
        self.bex_functions: dict[str, t.Callable] = {}

    def endpoint(self, endpoint: str) -> t.Callable[[F], F]:
        return self.bex_functions.get(endpoint, None)

    @setupmethod
    def add_url_rule(
        self,
        endpoint: str | None = None,
        view_func: t.Callable | None = None,
        **options: t.Any,
    ) -> None:
        if view_func and hasattr(view_func, "__name__") and "." in view_func.__name__:
            raise ValueError("'view_func' name may not contain a dot '.' character.")

        if endpoint and "." in endpoint:
            raise ValueError("'endpoint' may not contain a dot '.' character.")

        if endpoint is None:
            endpoint = view_func.__name__

        self.bex_functions[endpoint] = view_func

    @setupmethod
    def route(self, **options: t.Any):
        def decorator(f):
            bex_name = options.pop("bex_name", None)
            self.add_url_rule(bex_name, f)
            return f

        return decorator
