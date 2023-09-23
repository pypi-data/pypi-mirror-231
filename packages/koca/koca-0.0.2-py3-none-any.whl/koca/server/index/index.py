#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 主页路由蓝图
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-25 14:19:08
LastEditTime: 2023-09-18 16:12:15
'''
from flask import Blueprint, send_from_directory, current_app
from koca.utils import response_success
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    '''
    主页渲染。
    '''
    appName = current_app.koca.config.get('APP_NAME')
    appVersion = current_app.koca.config.get('APP_VERSION')
    appEmail = current_app.koca.config.get('APP_EMAIL')
    return response_success("Flask App!", {'name': appName, 'version': appVersion, 'email': appEmail})


@main.route('/static/<filename>')
def static(filename):
    uploadFolder = current_app.koca.config.get('UPLOAD_FOLDER')
    if uploadFolder is None:
        uploadFolder = '{}/server/static/'.format(os.getcwd())
    return send_from_directory(uploadFolder, filename, as_attachment=True)
