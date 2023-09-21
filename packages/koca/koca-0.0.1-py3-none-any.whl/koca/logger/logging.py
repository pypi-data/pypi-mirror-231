#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 日志输出模块，输出行记录模式或者JSON格式模式日志。
@Author: ideath@operatorworld.com
@Date: 2019-09-27 15:46:53
LastEditors: ewkoll
LastEditTime: 2023-09-17 23:11:12
'''
from contextlib import contextmanager
from queue import Queue
from threading import Thread
from koca.utils import get_logger, filter_none_dict, is_not_empty, DateEncoder

import datetime
import io
import json
import koca.extend as extend

REQUEST_LOG_ITEMS = [
    "timestamp",        # 请求时间戳
    "ip",               # 请求IP地址
    "method",           # 请求方法
    "url",              # 请求URL
    "identity",         # 身份标识
    "elapsed_time",     # 请求消耗时间
    "page",             # 请求分页
    "page_size",        # 请求页面大小
    "format",           # 请求的格式类型
    "headers"           # 请求头数据
]


def configured_request_log_handlers(config, logger):
    '''
    @description: 配置请求日志记录的处理Hadnler，通过Extend模块载入并初始化。
    @return:
    '''
    handlers = []
    options = config.load_config_section('request_log')
    if not options is None:
        log_type = options.pop('type')
        if not log_type is None:
            if is_not_empty(log_type):
                try:
                    handler = extend.request_log_handlers(log_type, **options)
                    handlers.append(handler)
                except Exception as e:
                    logger.error(e)
    return handlers


class RequestLogger(object):

    def __init__(self, handlers=None):
        '''
        请求日志记录类
        '''
        if handlers:
            self.handlers = list(handlers)
        else:
            self.handlers = []

        self.logger = get_logger()

    @contextmanager
    def log_time(self, **other):
        import time
        timestamp = datetime.datetime.now()
        start = time.time()
        yield
        elapsed = time.time() - start
        self.log(timestamp, elapsed, **other)

    def log(self, timestamp, elapsed, **other):
        record = {
            "timestamp": timestamp,
            "elapsed_time": elapsed
        }
        record.update(other)
        filter_none_dict(record)
        for handler in self.handlers:
            try:
                handler.write_record(record)
            except Exception as e:
                self.logger.error("Server log handler error (%s): %s"
                                  % (type(handler).__name__, str(e)))


class AsyncRequestLogger(RequestLogger):

    def __init__(self, handlers=None):
        '''
        异步输出日志。
        '''
        super(AsyncRequestLogger, self).__init__(handlers)
        self.queue = Queue()
        self.thread = Thread(target=self.log_consumer, name="async_logging")
        self.thread.daemon = True
        self.thread.start()

    def log(self, *args, **kwargs):
        self.queue.put((args, kwargs))

    def log_consumer(self):
        while True:
            (args, kwargs) = self.queue.get()
            super(AsyncRequestLogger, self).log(*args, **kwargs)


class CommonRequestLogHandler(object):

    def __init__(self, path=None, **options):
        '''
        使用默认的日志输出。
        '''
        self.path = path

    def write_record(self, record):
        if self.path is None:
            return

        with io.open(self.path, 'ab') as f:
            f.write(bytes(str(record), encoding="utf8"))
            f.write(bytes('\n', encoding="utf8"))


class JsonRequestLogHandler(object):

    def __init__(self, path=None, **options):
        '''
        Json文件输出路径。
        '''
        self.path = path

    def write_record(self, record):
        if self.path is None:
            return

        json_record = json.dumps(record, cls=DateEncoder)
        with io.open(self.path, 'ab') as f:
            f.write(bytes(json_record, encoding="utf8"))
            f.write(bytes('\n', encoding="utf8"))
