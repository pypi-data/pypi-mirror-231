#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: ewkoll ideath@operatorworld.com
Date: 2023-09-17 23:48:20
LastEditors: ewkoll
LastEditTime: 2023-09-17 23:49:49
Description: 
Copyright (c) 2023 by ewkoll email: ideath@operatorworld.com, All Rights Reserved.
"""
from uuid import uuid4
import time


def generate_uuid():
    """
    主键UUID
    """
    return str(uuid4())


def today():
    """
    @description: 当天日期
    @return:
    """
    return time.strftime("%Y-%m-%d", time.localtime())


from .user import *
