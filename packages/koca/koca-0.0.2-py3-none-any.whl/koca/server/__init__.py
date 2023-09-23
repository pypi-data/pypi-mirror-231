#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: ewkoll ideath@operatorworld.com
Date: 2023-09-17 21:45:07
LastEditors: ewkoll
LastEditTime: 2023-09-17 21:45:07
Description: 
Copyright (c) 2023 by ewkoll email: ideath@operatorworld.com, All Rights Reserved.
"""
from flask import Flask
from koca.loader import initialize_bex
from koca.utils import builtin_load_module, load_path
from koca.server.x_app_error_handle import init_app_error_handle
from koca.server.extensions import db, initialize_app, register_nacos
from koca.server.extensions import register_blueprint, register_global_handle
from koca.server.extensions import register_extensions, register_logger, register_commands


app = Flask(__name__.split(".")[0])


def create_app(config):
    """
    @description: 创建Flask应用
    @return:
    """
    if config is None:
        return
    
    app.config.from_mapping(config)
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    initialize_app(app, config)
    initialize_bex(app, config)
    init_app_error_handle(app, config)

    register_global_handle(app, config)
    register_extensions(app, config)
    register_logger(app, config)
    register_commands(app, config)
    register_blueprint(app, config)
    register_nacos(app, config)
    load_api_package(app, config)
    return app


def load_api_package(app, config):
    if config.API_PACKAGE_NAME is None:
        load_path(config.API_PATH_NAME or "business")
    else:
        builtin_load_module(config.API_PACKAGE_NAME)
