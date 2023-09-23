#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 常规的装饰器函数。
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-21 11:29:55
LastEditTime: 2023-09-17 23:29:32
'''
from decorator import decorator
from flask import current_app, g, request, session
from koca.errors import NotAuthenticated, Forbidden
import logging
import inspect
from urllib.parse import urlparse


@decorator
def print_flask_handle(func, name=None, config=None, *args, **kw):
    '''
    @description: 装饰器，用于分析调用流程。
    @return:
    '''
    if config and config.LOG_FUNC_INVOKE:
        try:
            func_name = inspect.stack()[1][3] or func.__name__
            print("{0} {1}".format(name, func_name))
        except:
            pass
    result = func(*args, **kw)
    return result


@decorator
def required_auth(func, roles=None, *args, **kw):
    '''
    @description: 鉴权检查装饰器。
    @return:
    '''
    authenticator = current_app.koca.authenticator
    if authenticator:
        try:
            identity = authenticator.authenticate(request, roles)
        except NotAuthenticated:
            raise Forbidden(exception=NotAuthenticated())
    else:
        identity = None

    # 存储鉴权结果描述信息。
    g.identity = identity
    result = func(*args, **kw)
    return result


"""
def log_request(attrib_field='attributes'):
    '''
    @description: 请求日志记录器，用于记录特定的API请求。
    @return:
    '''
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            other = {
                "method": request.method,
                "url": request.path,
                "ip": session.get('ip'),
                "identity": g.get('identity'),
                "page": g.get('get'),
                "format": g.get('format'),
                "page_size": g.get('page_size'),
                "headers": request.headers,
                "attributes": request.args.get(attrib_field)
            }
            rlogger = current_app.koca.request_log
            with rlogger.log_time(**other):
                retval = f(*args, **kwargs)
            return retval
        return wrapper
    return decorator
"""


@decorator
def log_request(func, attr_args="params", *args, **kwargs):
    '''
    @description: 请求日志记录器，用于记录特定的API请求，全局日志等级在INFO级别以下才输出数据。
    @return:
    '''
    config = current_app.koca.config
    if config.LOGGER_LEVEL <= logging.INFO:
        other = {
            "method": request.method,
            "url": request.path,
            "ip": session.get('ip'),
            "identity": g.get('identity'),
            "page": g.get('get'),
            "format": g.get('format'),
            "page_size": g.get('page_size'),
            "headers": str(request.headers),
            "params": request.args.get(attr_args)
        }
        rlogger = current_app.koca.request_log
        with rlogger.log_time(**other):
            retval = func(*args, **kwargs)
        return retval
    else:
        return func(*args, **kwargs)