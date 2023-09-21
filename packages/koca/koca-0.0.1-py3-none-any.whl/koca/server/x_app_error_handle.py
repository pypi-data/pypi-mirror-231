#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 拦截错误响应码
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-21 14:50:02
@LastEditTime: 2020-08-25 18:32:28
'''
from flask import make_response, jsonify
from koca.errors import *
from koca.utils import response_json


def init_app_error_handle(app, config):
    '''
    @description: 初始化拦截函数。
    @return:
    '''
    @app.errorhandler(400)
    def handle_400(e):
        r = BadRequest()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(403)
    def handle_403(e):
        r = Forbidden()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(404)
    def handle_404(e):
        r = NotFound()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(405)
    def handle_405(e):
        r = MethodNotAllowed()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(406)
    def handle_406(e):
        r = NotAcceptable()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(408)
    def handle_408(e):
        r = RequestTimeout()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(409)
    def handle_409(e):
        r = Conflict()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(410)
    def handle_410(e):
        r = Gone()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(411)
    def handle_411(e):
        r = LengthRequired()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(412)
    def handle_412(e):
        r = PreconditionFailed()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(413)
    def handle_413(e):
        r = RequestEntityTooLarge()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(414)
    def handle_414(e):
        r = RequestURITooLarge()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(415)
    def handle_415(e):
        r = UnsupportedMediaType()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(416)
    def handle_416(e):
        r = RequestedRangeNotSatisfiable()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(417)
    def handle_417(e):
        r = ExpectationFailed()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(418)
    def handle_418(e):
        r = ImATeapot()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(422)
    def handle_422(e):
        r = UnprocessableEntity()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(423)
    def handle_423(e):
        r = Locked()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(424)
    def handle_424(e):
        r = FailedDependency()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(428)
    def handle_428(e):
        r = PreconditionRequired()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(429)
    def handle_429(e):
        r = TooManyRequests()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(431)
    def handle_431(e):
        r = RequestHeaderFieldsTooLarge()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(451)
    def handle_451(e):
        r = UnavailableForLegalReasons()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(500)
    def handle_500(e):
        r = InternalServerError()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(501)
    def handle_501(e):
        r = NotImplemented()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(502)
    def handle_502(e):
        r = BadGateway()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(503)
    def handle_503(e):
        r = ServiceUnavailable()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(504)
    def handle_504(e):
        r = GatewayTimeout()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code

    @app.errorhandler(505)
    def handle_505(e):
        r = HTTPVersionNotSupported()
        return response_json({'code': str(r.code), 'type': r.name, 'message': r.description}), r.code
