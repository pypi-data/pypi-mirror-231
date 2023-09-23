#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: Token创建和验证
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-25 15:31:35
LastEditTime: 2023-09-17 23:59:58
'''

from flask import current_app
import jwt
from datetime import datetime, timedelta

def create_token(username, **kwargs):
    '''
    用户登录的时候，为相应的用户创建令牌。
    '''
    key = current_app.config["SECRET_KEY"]
    expires_time = current_app.config["TOKEN_EXPIRE_TIME"]
    exp = datetime.utcnow() + timedelta(microseconds = expires_time)
    data = {"username": username, "exp": exp, "expires_time": expires_time}
    data.update(**kwargs)
    token = jwt.encode(data, key)
    return str(token, 'UTF_8')


def verify_token(token):
    '''
    验证Token的有效性。
    返回用户名。
    '''
    key = current_app.config["SECRET_KEY"]
    try:
        data = jwt.decode(token, key)
        if data is None:
            return None
        
        exp = data[exp]
        if datetime.utcnow() > exp:
            return None
    except Exception:
        return None
    return data["username"]
