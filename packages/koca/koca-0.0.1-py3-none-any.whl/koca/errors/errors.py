#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 程序内部异常，非预期的结果。
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-21 11:30:19
LastEditTime: 2021-08-09 14:58:03
'''
from collections import OrderedDict


class UserError(Exception):
    """
    内部程序异常。
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        if len(args) > 0:
            self.message = args[0]

    def __str__(self) -> str:
        return "Internal program exception: {}".format(self.message)


class ArgumentError(UserError):
    '''
    抛出参数异常。
    '''

    def __str__(self) -> str:
        return "Parameter is abnormal."


class InternalError(UserError):
    '''
    程序内部非预期异常。
    '''

    def __str__(self) -> str:
        return "Unexpected exception inside the program."


class NotAuthenticated(Exception):
    '''
    鉴权失败异常。
    '''

    def __str__(self) -> str:
        return "User rights verification failed"
