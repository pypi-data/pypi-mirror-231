#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: ewkoll ideath@operatorworld.com
Date: 2023-09-17 21:48:55
LastEditors: ewkoll
LastEditTime: 2023-09-18 00:08:58
Description: JSON的编码器
Copyright (c) 2023 by ewkoll email: ideath@operatorworld.com, All Rights Reserved.
"""
from __future__ import print_function
import decimal
import base64
import json
import datetime


class JSONEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        """
        创建JSON编码器，用于转换某些类型的数据。
        """
        self._iterator_limit = 1000
        self.decode_byte = False
        self.decode_byte_tobase64 = False
        super(JSONEncoder, self).__init__(*args, **kwargs)

    def set_iterator_limit(self, iterator_limit):
        if iterator_limit is not None:
            self._iterator_limit = iterator_limit

    def set_decode_byte_tobase64(self, decode_byte_tobase64):
        self.decode_byte_tobase64 = decode_byte_tobase64

    def set_decode_byte(self, decode_byte):
        self.decode_byte = decode_byte

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        if isinstance(obj, bytes):
            if self.decode_byte == True:
                if self.decode_byte_tobase64 == True:
                    return base64.b64encode(obj).decode()
                else:
                    return str(obj, encoding="utf-8")
            return None
        if hasattr(obj, "as_dict") and callable(getattr(obj, "as_dict")):
            return obj.as_dict()
        else:
            count = self._iterator_limit
            array = None
            try:
                iterator = iter(obj)
                array = []
                for i, obj in enumerate(iterator):
                    array.append(obj)
                    if i >= count:
                        break
            except TypeError as e:
                pass

            if array is not None:
                return array
            else:
                return json.JSONEncoder.default(self, obj)


class DateEncoder(json.JSONEncoder):
    """
    Object of type 'datetime' is not JSON serializable
    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


class CommonJsonEncoder(json.JSONEncoder):
    """
    通用的JSON序列化。
    """

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        if isinstance(obj, bytes):
            return base64.b64encode(obj).decode()
        else:
            return json.JSONEncoder.default(self, obj)
