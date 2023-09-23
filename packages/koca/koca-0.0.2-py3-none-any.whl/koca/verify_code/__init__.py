#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Description: 验证码集合
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-23 15:13:22
@LastEditTime: 2020-08-23 15:17:11
"""
import random

def random_string():
    """
    @description: 生成随机字符串。
    @return: 随机字符串。
    """
    length = random.randint(4, 6)
    result = ""
    for i in range(length):
        value = random.randint(0, 2) % 3
        if value == 0:
            result += str(random.randint(0, 9))
        elif value == 1:
            result += chr(random.randint(97, 122))
        else:
            result += chr(random.randint(65, 90))
    return result


def random_font():
    """
    @description: 返回一个随机字体。
    @return: 字体路径。
    """
    array_fonts = [
        "./font/micross.ttf",
        "./font/bellb.ttf",
        "./font/angsaz.ttf",
        "./font/angsai.ttf",
        "./font/angsab.ttf",
        "./font/angsa.ttf",
        "./font/ahronbd.ttf",
    ]
    return array_fonts[random.randint(0, len(array_fonts) - 1)]


"""
@description: 模块载入。
@return: 
"""
try:
    from koca.verify_code.captcha import *
except:
    print("verification code module load failed...")


def get_verification_code(width=100, height=42, level=0, encode=True):
    """
    @description: 获取验证码。
    @param {int}  level >=3 之后使用简单验证码图片。
    @return: 验证码，Base64图片验证码
    """
    from .captcha import generate_verifiy_code
    code = random_string()
    if level < 3:
        return code, generate_verifiy_code(code, width, height, encode)
    return None
