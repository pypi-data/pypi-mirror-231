#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: ewkoll ideath@operatorwrold.com
Date: 2023-09-18 10:16:56
LastEditors: ewkoll
LastEditTime: 2023-09-20 15:32:28
Description: 
Copyright (c) 2023 by ewkoll email: ideath@operatorwrold.com, All Rights Reserved.
'''
from koca.utils import response_success, response_failed
from flask import Blueprint, request
from flask import current_app

api_bp = Blueprint('api', __name__)


@api_bp.route('/api/<apiname>', methods=['POST'])
def api(apiname):
    '''
    包装所有的API入口
    '''
    bex = current_app.koca.bex
    callable = bex.endpoint(apiname)
    if callable is None:
        return response_failed("bex接口未定义")
    
    request_json = request.get_json()
    return callable(request_json)