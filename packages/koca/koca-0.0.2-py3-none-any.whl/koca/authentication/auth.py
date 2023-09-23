#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: ewkoll ideath@operatorworld.com
Date: 2023-09-17 23:00:07
LastEditors: ewkoll
LastEditTime: 2023-09-17 23:33:13
Description: 
Copyright (c) 2023 by ewkoll email: ideath@operatorworld.com, All Rights Reserved.
"""
from koca.utils.token import verify_token
from koca.utils import Redis
from flask import current_app
import koca.extend as extend
from koca.errors import NotAuthenticated


def configured_authenticator(config, logger):
    """
    @description: 默认载入基于Token的模式。
    @return
    """
    auth_mode = "token"
    return extend.authenticators(auth_mode, logger=logger)


class TokenAuthHandler(object):
    def __init__(self, **options):
        """
        基于Token的认证模式
        """
        self.logger = options["logger"]
        self.logger.debug("Token auth mode init")

    def authenticate(self, request, roles):
        """
        鉴权检查
        """
        token = request.headers.get("Token") or request.headers.get("x-access-token")
        if token:
            user_name = verify_token(token)
            if user_name:
                user_info = Redis.get_user_info_by_token(token)
                if user_info:
                    current_app.koca.user_info = user_info
                    user_data = user_info.get("user")
                    if user_data and user_name == user_data.get("username"):
                        role = user_info.get("role")
                        if "role_name" in role:
                            role_name = role["role_name"].strip()
                            if role_name in roles:
                                Redis.pexpire_token(token)
                                return user_info
        raise NotAuthenticated()
