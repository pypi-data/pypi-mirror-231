#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 验证码图片和声音生成。
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-23 15:13:22
@LastEditTime: 2020-08-23 15:18:30
'''
from io import BytesIO
import base64
from . import random_font
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha


def generate_verifiy_code(code, width=100, height=42, encode=True):
    '''
    @description: 生成字符串验证码数据。
    @param {str} code 验证码字符串。
    @return: base64编码后的png图片数据。
    '''
    image = ImageCaptcha(width=width,
                         height=height,
                         fonts=[random_font()])
    data = image.generate(code)
    if not encode:
        return data.getvalue()
    else:
        return base64.b64encode(data.getvalue())


def generate_verifiy_audio(code, encode=True):
    '''
    @description: 生成字符串音频数据，默认的音频数据是英文的。{{language}}-{{character}}-{{username}}.wav
    @param {str} code 验证码字符串。
    @return: base64编码后的wav音频数据。
    '''
    audio = AudioCaptcha()
    data = audio.generate(code)
    if not encode:
        return data
    else:
        return base64.b64encode(data)
