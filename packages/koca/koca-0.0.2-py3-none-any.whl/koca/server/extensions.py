#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: ewkoll ideath@operatorworld.com
Date: 2023-09-17 21:45:07
LastEditors: ewkoll
LastEditTime: 2023-09-17 23:39:22
Description: 注册Flask扩展功能
Copyright (c) 2023 by ewkoll email: ideath@operatorworld.com, All Rights Reserved.
"""
from koca.utils import CustomDict, get_logger, str_to_bool, get_real_ip
from koca.authentication import configured_authenticator
from flask_restful import Api
from koca.errors import ConfigError
from koca.logger import configured_request_log_handlers
from koca.logger import AsyncRequestLogger, RequestLogger
from flask import g, current_app, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

import socket
import os
import nacos

def store_option(config, option, default):
    """
    @description: 存储可选设置，当config类没有配置的情况。
    @return:
    """
    value = config.get(option.upper())
    if value is None:
        value = default
    setattr(current_app.koca, option, value)


def initialize_app(app, config):
    """
    @description: 注册全局的一些信息。
    @return:
    """
    with app.app_context():
        import logging

        logging.basicConfig()
        logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
        logging.getLogger("sqlalchemy.pool").setLevel(logging.INFO)
        current_app.koca = CustomDict()
        current_app.koca.config = config
        logger = get_logger(
            config.LOGGER_NAME, config.LOGGER_PATH, config.LOGGER_FORMAT
        )
        current_app.koca.logger = logger
        logger.setLevel(config.LOGGER_LEVEL)

        # 设置JSON格式化，数据序列化最大值范围，跨域标志，以及接口鉴权模式配置。
        store_option(config, "pretty_print", False)
        store_option(config, "page_index", 1)
        store_option(config, "page_size", 10)
        store_option(config, "lang", "zh-CN")
        store_option(config, "json_record_limit", 1000)

        # 初始化鉴权模块。
        authenticator = configured_authenticator(config, logger)
        current_app.koca.authenticator = authenticator

        # 初始化异步日志。
        handlers = configured_request_log_handlers(config, logger)
        current_app.koca.handlers = handlers


def load_global_attribute(app, config):
    """
    @description: 设置请求上下文全局信息。
    @return:
    """
    g.json_record_limit = current_app.koca.json_record_limit

    if "lang" in request.args:
        g.lang = str_to_bool(request.args.get("lang"))
    else:
        g.lang = current_app.koca.lang

    if "pretty_print" in request.args:
        g.pretty_print = str_to_bool(request.args.get("pretty_print"))
    else:
        g.pretty_print = current_app.koca.pretty_print

    if "page_index" in request.args:
        g.page_index = int(request.args.get("page_index"))
    else:
        g.page_index = current_app.koca.page_index

    if "page_size" in request.args:
        g.page_size = int(request.args.get("page_size"))
    else:
        g.page_size = current_app.koca.page_size

    if "page" in request.args:
        g.page_index = int(request.args.get("page"))
    elif "page" in request.headers:
        g.page_index = int(request.headers.get("page"))
    else:
        g.page_index = current_app.koca.page_index

    if "pageSize" in request.args:
        g.page_size = int(request.args.get("pageSize"))
    elif "pageSize" in request.headers:
        g.page_size = int(request.headers.get("pageSize"))
    else:
        g.page_size = current_app.koca.page_size


def register_global_handle(app, config):
    """
    @description: 注册一些全局的流程处理入口函数。
    @return:
    """
    from koca.utils import print_flask_handle

    @app.before_request
    @print_flask_handle(name=app.name, config=config)
    def before_request():
        """
        @description: 注册一个函数，在每次请求前运行。
        @return:
        """
        # 载入请求会话中的默认信息。
        load_global_attribute(app, config)

    @app.after_request
    @print_flask_handle(name=app.name, config=config)
    def after_request(rsp):
        """
        @description: 注册一个函数，响应处理完成，没有发生异常的时候调用。
        @return:
        """
        rsp.headers["Server"] = "Ewkoll"
        return rsp

    @app.teardown_request
    @print_flask_handle(name=app.name, config=config)
    def teardown_request(exception):
        """
        @description: 注册一个函数，响应处理完成后调用，如果发生异常传递异常信息。
        @return:
        """
        if exception:
            logger = current_app.koca.logger
            other = {
                "path": request.path,
                "exception": exception,
                "ip": get_real_ip(),
                "args": request.args,
                "headers": request.headers,
                "referrer": request.referrer,
            }
            logger.warn(str(other))


def register_logger(app, config):
    """
    @description: 注册日志处理相关的模块。
    @return:
    """
    with app.app_context():
        handlers = current_app.koca.handlers
        if handlers:
            if not config.ASYNC_LOGGING:
                current_app.koca.request_log = RequestLogger(handlers)
            else:
                current_app.koca.request_log = AsyncRequestLogger(handlers)


def register_commands(app, config):
    """
    @description: 注册命令支持。
    @return:
    """
    from koca.server.commands import init_commands

    init_commands(app, config)


def register_extensions(app, config):
    """
    @description: 初始化所有的扩展信息。
    @return:
    """
    db.init_app(app)
    app.koca.db = db

    def error_router(self, original_handler, e):
        """This function decides whether the error occured in a flask-restful
        endpoint or not. If it happened in a flask-restful endpoint, our
        handler will be dispatched. If it happened in an unrelated view, the
        app's original error handler will be dispatched.
        In the event that the error occurred in a flask-restful endpoint but
        the local handler can't resolve the situation, the router will fall
        back onto the original_handler as last resort.

        :param original_handler: the original Flask error handler for the app
        :type original_handler: function
        :param e: the exception raised while handling the request
        :type e: Exception

        """
        """
        if self._has_fr_route():
            try:
                return self.handle_error(e)
            except Exception:
                pass  # Fall through to original handler
        """
        return original_handler(e)

    Api.error_router = error_router
    api = Api(app)
    app.koca.api = api
    
    # 注册接口请求。
    from .api import api_bp

    url_prefix = config.URL_PREFIX
    app.register_blueprint(api_bp, url_prefix=url_prefix, config=config)


def register_blueprint(app, config):
    """
    @description: 注册蓝图
    @return:
    """
    from .index import main

    app.register_blueprint(main)


def get_interface_ip(family: socket.AddressFamily) -> str:
    host = "fd31:f903:5ab5:1::1" if family == socket.AF_INET6 else "10.253.155.219"
    with socket.socket(family, socket.SOCK_DGRAM) as s:
        try:
            s.connect((host, 58162))
        except OSError:
            return "::1" if family == socket.AF_INET6 else "127.0.0.1"
        return s.getsockname()[0]

def register_nacos(app, config):
    """
    @description: 注册Nacos
    @return:
    """
    if config.NACOS is None:
        return

    address = config.NACOS.SERVER_ADDRESSES
    namespace = config.NACOS.NAMESPACE or "public"
    appname = config.NACOS.REGISTER_NACOS_NAME or app.name()
    port = os.getenv('FLASK_RUN_PORT')
    if address is None or port is None:
        raise ConfigError("Nacos")
    
    
    client = nacos.NacosClient(address, namespace=namespace)
    display_hostname = get_interface_ip(socket.AF_INET)
    client.add_naming_instance(appname, display_hostname, port)
    app.koca.nacos_client = client
    