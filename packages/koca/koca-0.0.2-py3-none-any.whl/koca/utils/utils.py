#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 通用函数
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-21 11:29:55
LastEditTime: 2023-09-22 14:17:02
'''
from flask import Response, request, g, make_response
from zlib import crc32
from types import FunctionType
from koca.utils.formatters import JSONEncoder
from koca.errors import ArgumentError
from urllib.parse import urlparse, urljoin
from pathlib import Path

import datetime
import os
import re
import random
import json
import time
import shutil
import base64
import hashlib
import tempfile


def md5(data):
    '''
    @description: md5字符串。
    @return:
    '''
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()


def md5_timestamp():
    '''
    @description: MD5时间戳
    @return:
    '''
    return md5(str(time.time()))


def unicode_escape(data):
    '''
    @description: 处理unicode中文
    @return:
    '''
    if type(data) == bytes:
        return data.decode('unicode_escape')
    return bytes(data, encoding='utf-8').decode('unicode_escape')


def today():
    '''
    @description: 当天日期
    @return:
    '''
    return time.strftime("%Y-%m-%d", time.localtime())


def now():
    '''
    @description: 当前时间
    @return:
    '''
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def make_path(path):
    '''
    @description: 确保目录存在。
    @return:
    '''
    dataPath = Path(path)
    if not dataPath.exists():
        os.makedirs(path)


def get_work_path():
    '''
    @description: 获取工作目录。
    @return:
    '''
    return os.getcwd()


def set_work_path(path):
    '''
    @description: 设置工作目录。
    @return:
    '''
    os.chdir(path)
    return os.getcwd()


def dir_path(path, callback):
    '''
    @description: 目录遍历
    @return:
    '''
    ls = os.listdir(path)
    if isinstance(callback, FunctionType):
        for file in ls:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                callback(path, file)
            elif os.path.isdir(file_path):
                dir_path(file_path, callback)


def load_path_pyfile(path, file):
    '''
    @description: 加载指定目录文件
    @return:
    '''
    if file != '__init__.py' and file.endswith(".py"):
        pos = file.rfind('.')
        if pos != -1:
            file = file[0:len(file) - pos]
            path = path.replace('\\', '.')
            path = path.replace('/', '.')
            __import__(path + '.' + file)
    

def load_path(path):
    '''
    @description: 加载指定目录文件
    @return:
    '''
    dir_path(path, callback=load_path_pyfile)


def move_file(srcfile, dstfile):
    '''
    @description: 移动文件。
    @return: 
    '''
    if not os.path.isfile(srcfile):
        return False
    else:
        try:
            fpath, _ = os.path.split(dstfile)
            if not os.path.exists(fpath):
                os.makedirs(fpath)
            shutil.move(srcfile, dstfile)
            return True
        except:
            return False


def copy_file(srcfile, dstfile):
    '''
    @description: 拷贝文件。
    @return: 
    '''
    if not os.path.isfile(srcfile):
        return False
    else:
        try:
            fpath, _ = os.path.split(dstfile)
            if not os.path.exists(fpath):
                os.makedirs(fpath)
            shutil.copyfile(srcfile, dstfile)
            return True
        except:
            return False


def move_folder(src_folder, dst_folder):
    '''
    @description: 移动文件夹。
    @return: 
    '''
    if not os.path.exists(src_folder):
        return
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    shutil.move(src_folder, dst_folder)


def copy_folder(src_folder, dst_folder):
    '''
    @description: 拷贝文件夹。
    @return: 
    '''
    if not os.path.exists(src_folder):
        return
    if os.path.exists(dst_folder):
        # 删除非空目录。
        shutil.rmtree(dst_folder)
    shutil.copytree(src_folder, dst_folder)


def read_raw_file(filePath):
    '''
    读取原始文件。
    '''
    with open(filePath, 'rb') as f:
        return f.read()


def write_raw_file(filePath, fileData):
    '''
    写入原始文件。
    '''
    if fileData:
        with open(filePath, 'wb') as f:
            return f.write(fileData)


def generate_secretkey(len=48):
    '''
    @description: 生成随机Base64密钥
    @return:
    '''
    return base64.b64encode(os.urandom(len)).decode()


def random_email():
    '''
    @description: 生成随机邮箱
    @return:
    '''
    result = ''
    for num in range(1, 12):
        result += random.choice('abcdefghijklmnopqrstuvwxyz')
    return result + '@operatorworld.com'

def str_to_bool(string):
    '''
    @description: 转换字符串变量到BOOL变量。
    @return: True ["true", "yes", "1", "on"] False ["false", "no", "0", "off"] None [Other]
    '''
    if string is not None:
        if string.lower() in ["true", "yes", "1", "on"]:
            return True
        elif string.lower() in ["false", "no", "0", "off"]:
            return False
    return None


def bytes_to_str(data):
    """
    二进制转字符串。
    """
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    data = data.strip()
    return data


def response_json(obj, decode_byte=False):
    '''
    @description: 返回`application/json`类型响应。
    @return:
    '''
    if g.pretty_print:
        indent = 4
    else:
        indent = None

    encoder = JSONEncoder(indent=indent)
    encoder.set_iterator_limit(g.json_record_limit)
    encoder.set_decode_byte(decode_byte)
    data = encoder.iterencode(obj)
    return Response(data, mimetype='application/json')


def db2json(data):
    '''
    @description: 转换成字符串。
    @return:
    '''
    return json.dumps(data, cls=JSONEncoder)


def obj2json(data):
    '''
    @description: 转换成字符串。
    @return:
    '''
    return json.dumps(data)


def json2obj(data):
    '''
    @description: 字符串转换成对象。
    @return:
    '''
    return json.loads(data)


def response_success(message, data=None, code=None):
    '''
    @description: 返回成功消息
    @return:
    '''
    resp_data = {
        'code': code or '200',
        'data': data,
        'message': message
    }
    return response_json(resp_data)


def response_success_withbytes(message, data=None, code=None):
    '''
    @description: 返回成功消息，并且返回二进制数据
    @return:
    '''
    resp_data = {
        'code': code or '200',
        'data': data,
        'message': message
    }
    return response_json(resp_data, True)


def response_failed(message, data=None, code=None):
    '''
    @description: 返回失败消息
    @return:
    '''
    resp_data = {
        'code': code or '0',
        'data': data,
        'message': message
    }
    return response_json(resp_data)


def convert2json(obj):
    '''
    @description: 转换成json对象。
    @return:
    '''
    if g.pretty_print:
        indent = 4
    else:
        indent = None

    encoder = JSONEncoder(indent=indent)
    encoder.set_iterator_limit(g.json_record_limit)
    return encoder.iterencode(obj)


def filter_none_dict(record):
    '''
    @description: 过滤掉空值字典。
    @return:
    '''
    for k in list(record):
        if not record[k]:
            record.pop(k)


class CustomDict(dict):

    def __init__(self, *args, **kwargs):
        """
        自定义字典。
        """
        super(dict, self).__init__(*args, **kwargs)

    def __getattr__(self, attr):
        try:
            return super(CustomDict, self).__getitem__(attr)
        except KeyError:
            try:
                return super(CustomDict, self).__getattribute__(attr)
            except:
                return None

    def __setattr__(self, attr, value): self.__setitem__(attr, value)


def builtin_load_module(module_path):
    '''
    @description: 模块载入。
    @return:
    '''
    mod = __import__(module_path)
    path = module_path.split(".")[1:]
    for token in path:
        mod = getattr(mod, token)
    return mod


def coalesce_option_value(value, value_type, label=None):
    '''
    转换到对象的指定类型。
    '''
    value_type = value_type.lower()
    try:
        if value_type == 'str':
            return_value = str(value)
        elif value_type == 'list':
            if isinstance(value, str):
                return_value = value.split(",")
            else:
                return_value = list(value)
        elif value_type == "float":
            return_value = float(value)
        elif value_type in ["integer", "int"]:
            return_value = int(value)
        elif value_type in ["bool", "boolean"]:
            if not value:
                return_value = False
            elif isinstance(value, str):
                return_value = str_to_bool(value)
            else:
                return_value = bool(value)
        else:
            raise ArgumentError("unknown option value type %s" % value_type)
    except ValueError:
        if label:
            label = "parameter %s " % label
        else:
            label = ""

        raise ArgumentError("unable to convert %svalue '%s' into type %s" % (label, value, value_type))
    return return_value


def coalesce_options(options, types):
    """
    根据类型合并数据。
    """
    out = {}

    for key, value in options.items():
        if key in types:
            out[key] = coalesce_option_value(value, types[key], key)
        else:
            out[key] = value

    return out


def is_ipadress(str):
    '''
    判断是否是IP
    '''
    p = re.compile(
        '^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(str):
        return True
    else:
        return False


def is_https(str):
    '''
    判断是否是HTTPS开头。
    '''
    return str.strip().lower().startswith("https")


def is_secure_cookie(str):
    '''
    判断是否是HTTPS的COOKIE。
    '''
    if is_https(str):
        return True
    return False


def get_real_ip():
    '''
    获取真实用户IP地址，获取Nginx传递的真实IP地址，通过特定的头并base64后传递。
    '''
    ip = request.headers.get("NGINX-X-Real-IP")
    if ip:
        ip = base64.b64decode(ip)
        if not is_ipadress(ip):
            ip = None
    if ip is None:
        proxy_ip_length = len(request.access_route)
        if (proxy_ip_length > 0):
            ip = request.access_route[proxy_ip_length - 1]
        else:
            ip = request.remote_addr or '127.0.0.1'
    return ip


def is_not_empty(s):
    '''
    空字符串
    '''
    return bool(s and s.strip())


def get_file_crc32(filename):
    '''
    计算文件crc32
    '''
    with open(filename, 'rb') as f:
        return crc32(f.read())


def response_text(data):
    '''
    @description: 返回`text/plain`类型响应。
    @return:
    '''
    response = make_response(data)
    response.headers['Content-Type'] = 'text/plain'
    return response

def response_image_callback(data, callback=None):
    '''
    @description: 返回`image/png`类型响应。
    @return:
    '''
    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    if callback != None:
        callback(response)
    return response

def is_safe_url(target):
    '''
    @description: 检查URL
    @return: 
    '''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

def compare_upper(input, compare):
    '''
    @description: 不区分大小写对比
    @return: 
    '''
    return input.upper() == compare.upper()


def split_list(data_list):
    '''
    @description: 数组拆分
    @return: 
    '''
    half = len(data_list)//2
    return data_list[:half], data_list[half:]


def mkdtemp(suffix=None, prefix=None):
    '''
    @description: 创建临时目录
    @return: 
    '''
    return tempfile.mkdtemp(suffix, prefix)


def rmtree(dirpath):
    '''
    @description: 删除目录
    @return: 
    '''
    return shutil.rmtree(dirpath)


def mkstemp(suffix=None, prefix=None, dir=None, text=False):
    '''
    @description: 生成临时文件 os.close(fd) os.unlink(filename)
    @return: 
    '''
    return tempfile.mkstemp(suffix, prefix, dir, text)


def is_empty(str):
    '''
    @description: 判断是否为空
    @return: 
    '''
    return str == None or str.strip() == ''


def format_utc_time(utc_time):
    '''
    @description: 标准时间转本地时间。
    @return: 
    '''
    utc_date = datetime.datetime.strptime(utc_time, '%Y-%m-%dT%H:%M:%S.%fZ')
    local_dt = utc_date + datetime.timedelta(hours=8)
    return local_dt.strftime('%Y-%m-%d %H:%M:%S')