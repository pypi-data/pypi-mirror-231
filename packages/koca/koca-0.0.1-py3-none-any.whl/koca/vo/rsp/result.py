#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: ewkoll ideath@operatorwrold.com
Date: 2023-09-18 11:09:29
LastEditors: ewkoll
LastEditTime: 2023-09-18 11:14:51
Description: 
Copyright (c) 2023 by ewkoll email: ideath@operatorwrold.com, All Rights Reserved.
'''
from koca.utils import response_json

class Result:
    def __init__(self) -> None:
        self.head = {}
        self.detail = None
        self.body= None
        self.code = "0"
        self.msg = "请求处理成功"
        
    def success(self, msg, body=None):
        self.msg = msg
        self.body = body
        resp_data = {
            'msg': self.msg,
            'code': self.code,
            'body': self.body,            
        }
        return response_json(resp_data)
        
    def failed(self, msg, body=None):
        self.code = '-500'
        self.msg = msg
        self.body = body    
        resp_data = {
            'msg': self.msg,
            'code': self.code,
            'body': self.body,            
        }
        return response_json(resp_data)
        
        