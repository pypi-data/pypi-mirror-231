#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 扩展模块。
@Author: ideath@operatorworld.com
@Date: 2019-09-27 15:57:42
LastEditors: ewkoll
LastEditTime: 2023-09-18 16:10:16
'''
from koca.utils import builtin_load_module, coalesce_options
from koca.errors import *
from textwrap import dedent
from collections import OrderedDict

__all__ = [
    "authenticators",
    "request_log_handlers"
]

'''
内部扩展，当前模块实现支持部分。
'''
BUILTIN_EXTENSIONS = {
    "authenticators": {
        "token": "koca.authentication:TokenAuthHandler"
    },
    "request_log_handlers": {
        "json": "koca.logger:JsonRequestLogHandler",
        "common": "koca.logger:CommonRequestLogHandler",
    }
}


class Extension(object):

    def __init__(self, _type, _name, _factory):
        """
        扩展对象。
        """
        if _factory is None:
            raise ArgumentError("Can't set none extension factory "
                                "(in extension '{}')".format(_name))

        self._type = _type
        self._name = _name
        self.set_factory(_factory)

    def set_factory(self, _factory):
        self.factory = _factory

    @property
    def type(self):
        return self._type

    @property
    def name(self):
        return self._name

    @property
    def options(self):
        return self._options

    @property
    def options_type(self):
        return self._options_types

    @property
    def factory(self):
        if self._factory is not None:
            return self._factory
        else:
            raise InternalError("No factory set for extension '{}'"
                                .format(self.name))

    @factory.setter
    def factory(self, _factory):
        if _factory is None:
            raise InternalError("Can't set extension factory to None")

        self._factory = _factory
        options = []
        if hasattr(_factory, "__options__"):
            options = _factory.__options__ or []

        self._options = OrderedDict()
        self._options_types = {}
        for option in options:
            name = option["name"]
            self._options[name] = option
            self._options_types[name] = option.get("type", "string")

    @property
    def label(self):
        label = self._factory.__name__
        if hasattr(self._factory, "__label__"):
            label = self._factory.__label__ or label
        return label

    @property
    def description(self):
        description = ""
        if hasattr(self._factory, "__description__"):
            description = self._factory.__description__ or description
        return dedent(description)

    def create(self, *args, **kwargs):
        kwargs = coalesce_options(dict(kwargs), self.options_type)
        return self.factory(*args, **kwargs)


class ExtensionFinder(object):

    def __init__(self, _type):
        self._type = _type
        self.extensions = {}
        self.builtins = BUILTIN_EXTENSIONS.get(self._type, {})

    def builtin(self, name):
        '''
        @description: 创建内建扩展。
        @return: 
        '''
        try:
            ext_mod = self.builtins[name]
        except KeyError:
            return None

        (modname, attr) = ext_mod.split(":")
        module = builtin_load_module(modname)
        factory = getattr(module, attr)
        ext = Extension(self._type, name, factory)
        self.extensions[name] = ext
        return ext

    def names(self):
        '''
        @description: 获取支持的扩展名称。
        @return: 
        '''
        names = list(self.builtins.keys())
        return sorted(names)

    def get(self, name):
        '''
        @description: 根据名称获取扩展对象。
        @return: 
        '''
        ext = self.extensions.get(name)

        if not ext:
            ext = self.builtin(name)
            if not ext:
                raise InternalError(
                    "Get '{}' extension '{}' Failed.".format(self._type, name))

        return ext

    def __call__(self, ext_name, *args, **kwargs):
        '''
        @description: 创建扩展对象。
        @return: 
        '''
        return self.create(ext_name, *args, **kwargs)

    def factory(self, name):
        '''
        @description: 获取扩展对象工厂。
        @return: 
        '''
        ext = self.get(name)

        if not ext.factory:
            raise InternalError(
                "Get factory for extension '{}' Failed.".format(name))

        return ext.factory

    def create(self, ext_name, *args, **kwargs):
        '''
        @description: 通过给定参数扩展名称创建扩展对象，通过Options配置默认的参数变量。
        @return: 
        '''
        ext = self.get(ext_name)
        return ext.create(*args, **kwargs)

    def register(self, ext_name, factory):
        '''
        @description: 直接注册创建扩展名对象。
        @return: 
        '''
        ext = Extension(self._type, ext_name, factory)
        self.extensions[ext_name] = ext
        return ext


builtin_extend = {}
for k, v in BUILTIN_EXTENSIONS.items():
    builtin_extend[k] = ExtensionFinder(k)

request_log_handlers = builtin_extend['request_log_handlers']
authenticators = builtin_extend['authenticators']
