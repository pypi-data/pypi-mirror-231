#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 
@Author: ideath@operatorworld.com
@Date: 2019-09-27 13:57:03
@LastEditors: ideath
@LastEditTime: 2019-09-27 14:06:08
'''
from flask import current_app
from werkzeug.local import LocalProxy

# Application Context
# ===================
#
# Readability proxies


def _get_logger():
    return current_app.koca.logger


logger = LocalProxy(_get_logger)
