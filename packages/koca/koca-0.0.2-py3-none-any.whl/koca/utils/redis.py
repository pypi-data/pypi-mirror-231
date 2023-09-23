#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Description: Redis包装。
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-24 09:46:56
@LastEditTime: 2022-09-15 15:35:48
"""
from flask import current_app
import json


class Redis(object):
    """
    包装Redis函数。
    """

    @staticmethod
    def redis():
        """
        Redis连接池实例
        """
        return current_app.koca.config.REDIS

    @staticmethod
    def token_expire():
        """
        令牌过期时间
        """
        return current_app.koca.config.TOKEN_EXPIRE_TIME

    @staticmethod
    def token_key(key):
        """
        用户Token的Redis存储Key
        """
        return "token_" + key

    @classmethod
    def set_user_info_by_token(cls, key, value, expire=None):
        """
        存储Token对应的用户信息。
        """
        cls.redis().hset(cls.token_key(key), "user_info", value)
        cls.redis().pexpire(cls.token_key(key), expire or cls.token_expire())

    @classmethod
    def get_user_info_by_token(cls, key):
        """
        根据Token获取用户信息。
        """
        str_user_info = cls.redis().hget(cls.token_key(key), "user_info")
        if str_user_info is not None:
            return json.loads(str_user_info)

    @classmethod
    def pexpire_token(cls, key, time=None):
        """
        设置Token的过期时间。
        """
        cls.redis().pexpire(cls.token_key(key), time or cls.token_expire())

    @classmethod
    def remove_token(cls, key):
        """
        移除用户Token
        """
        cls.redis().pexpire(cls.token_key(key), 0)

    @classmethod
    def set(cls, key, val, expire=None):
        """
        SET
        """
        cls.redis().set(key, val, ex=expire)

    @classmethod
    def get(cls, key):
        """
        GET
        """
        return cls.redis().get(key)
