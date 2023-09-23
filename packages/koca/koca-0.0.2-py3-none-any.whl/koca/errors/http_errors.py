#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Description: HTTP异常代码。
@Author: Ewkoll
@Email: ideath@operatorworld.com
@License: Apache-2.0
@Date: 2020-08-21 11:30:19
@LastEditTime: 2020-08-25 16:58:53
"""
from flask import g
from werkzeug.exceptions import HTTPException
from werkzeug.utils import escape
from werkzeug.urls import iri_to_uri


class HttpCode(HTTPException):
    def __init__(self, message=None, exception=None, **details):
        """
        @description: 状态返回信息。
        @param {str} message 提示文字。
        @param {obj}} exception 异常信息。
        @param {obj}} context 上下文，存储请求耗时。请求API名称等信息。
        @param {obj}} details 结果集。
        @return:
        """
        super(HttpCode, self).__init__()
        self.message = message or self.description
        self.details = details
        self.context = g.get("context")
        self.exception = exception

    def get_body(self, environ=None, scope=None):
        """
        @description: 获取HTTP返回体信息。
        @return:
        """
        result = {
            "code": str(self.code),
            "type": self.name,
            "message": self.message,
        }

        if self.context:
            result.update(self.context)

        if self.details:
            result.update(self.details)

        if self.exception:
            result["reason"] = str(self.exception)

        import json

        return json.dumps(result)

    def get_headers(self, environ=None, scope=None):
        """
        @description: 响应头。
        @return:
        """
        return [("Content-Type", "application/json")]


class CommonSuccess(HttpCode):
    """
    获取数据成功，Get
    """

    code = 200
    description = "Success"


class CommonCreated(HttpCode):
    """
    资源创建成功，Post
    """

    code = 201
    description = "Created"


class CommonUpdated(HttpCode):
    """
    资源修改成功，Put
    """

    code = 201
    description = "Updated"


class CommonAccepted(HttpCode):
    """
    请求已经被接受，异步任务。
    """

    code = 202
    description = "Accepted"


class CommonNoContent(HttpCode):
    """
    删除成功，没有返回体
    """

    code = 204
    description = "No Content"


class CommonResetContent(HttpCode):
    """
    刷新页面。
    """

    code = 205
    description = "Reset Content"


class CommonFailed(HttpCode):
    """
    返回业务请求失败，在200范围内，异常和失败的差异只是存在一个字段描述异常信息，因此业务失败必须要有异常类传递。
    """

    code = 200
    description = "Failed"


class MovedHttpCode(HttpCode):
    def __init__(self, location):
        """
        返回重定向请求。
        """
        display_location = escape(location)
        location = iri_to_uri(location, safe_conversion=True)
        super(MovedHttpCode, self).__init__(
            details={"location": location, "display_location": display_location}
        )


class MovedPermanently(MovedHttpCode):
    """
    *301* `Moved Permanently`
    用于Get或者Head请求的永久重定向。
    当返回301请求的时候，如果原来的请求是POST发起的，后续重定向会变成Get请求。
    """

    code = 301
    description = "the resource requested has been definitively moved to the URL given by the Location headers"


class Found(MovedHttpCode):
    """
    *302* `Found`
    用于Get或者Head请求的临时重定向。
    当返回302请求的时候，如果原来的请求是POST发起的，后续重定向会变成Get请求。
    """

    code = 302
    description = "the resource requested has been temporarily moved to the URL given by the Location header."


class SeeOther(HttpCode):
    """
    *303* `See Other`
    当Put或者Delete请求之后，请求已经执行，告诉文件上传成功或者删除成功，返回重定向Location，并且浏览器使用GET发起请求。
    """

    code = 303
    description = "The method used to display this redirected page is always GET."

    def __init__(self, message, location):
        display_location = escape(location)
        location = iri_to_uri(location, safe_conversion=True)
        super(SeeOther, self).__init__(
            message=message,
            details={"location": location, "display_location": display_location},
        )


class NotModified(MovedHttpCode):
    """
    *304* `Not Modified`
    资源没有改变。
    """

    code = 304
    description = "there is no need to retransmit the requested resources."


class TemporaryRedirect(MovedHttpCode):
    """
    *307* `Temporary Redirect`
    临时重定向，请求的方法和包体不发生变化
    Put、Post请求的时候，请求体还没有处理，重定向请求也需要用Put、Post的模式发起，并且附带上次请求的请求体内容。
    """

    code = 307
    description = (
        "307 Temporary Redirect, The request method and the body will not be altered."
    )


class PermanentRedirect(MovedHttpCode):
    """
    *308* `Permanent Redirect`
    永久重定向，请求的方法和包体不发生变化
    Put、Post请求的时候，请求体还没有处理，重定向请求也需要用Put、Post的模式发起，并且附带上次请求的请求体内容。
    """

    code = 308
    description = (
        "308 Permanent Redirect, The request method and the body will not be altered."
    )


class BadRequest(HttpCode):
    """
    *400* `Bad Request`
    当浏览器发送不能出来的请求的时候返回。
    """

    code = 400
    description = (
        "The browser (or proxy) sent a request that this server could not understand."
    )


class SecurityError(BadRequest):
    """
    *400* `Bad Request`
    请求安全检查失败。
    """

    code = 400
    description = "The browser (or proxy) sent a request that security check failed."


class UnAuthorized(HttpCode):
    """
    *401* `UnAuthorized`
    未授权的请求。
    """

    code = 401
    description = "The server could not verify that you are authorized to access the URL requested."

    def __init__(self, www_authenticate="Basic realm=Input username and password!"):
        super(UnAuthorized, self).__init__()
        if isinstance(www_authenticate, (tuple, list)):
            self.www_authenticate = www_authenticate
        else:
            self.www_authenticate = [www_authenticate]

    def get_headers(self, environ=None):
        headers = super(UnAuthorized, self).get_headers(environ)
        if self.www_authenticate:
            headers.append(
                ("WWW-Authenticate", ", ".join([str(x) for x in self.www_authenticate]))
            )
        return headers


class Forbidden(HttpCode):
    """
    *403* `Forbidden`
    禁止访问URL。
    """

    code = 403
    description = "You don't have the permission to access the requested resource."


class NotFound(HttpCode):
    """
    *404* `Not Found`
    资源未找到。
    """

    code = 404
    description = (
        "The requested URL was not found on the server. If you entered"
        " the URL manually please check your spelling and try again."
    )


class MethodNotAllowed(HttpCode):
    """
    *405* `Method Not Allowed`
    请求方法不允许。
    """

    code = 405
    description = "The method is not allowed for the requested URL."

    def __init__(self, allow_methods=None):
        super(MethodNotAllowed, self).__init__()
        self.allow_methods = allow_methods

    def get_headers(self, environ=None):
        headers = super(MethodNotAllowed, self).get_headers(environ)
        if self.allow_methods:
            headers.append(("Allow Method", ", ".join(self.allow_methods)))
        return headers


class NotAcceptable(HttpCode):
    """
    *406* `Not Acceptable`
    不可接受的响应，后端返回的格式，前端请求的时候Accept类型中不存在。
    """

    code = 406
    description = (
        "The resource identified by the request is only capable of"
        " generating response entities which have content"
        " characteristics not acceptable according to the accept"
        " headers sent in the request."
    )


class RequestTimeout(HttpCode):
    """
    *408* `Request Timeout`
    请求超时的时候返回.
    """

    code = 408
    description = (
        "The server closed the network connection because the browser"
        " didn't finish the request within the specified time."
    )


class Conflict(HttpCode):
    """
    *409* `Conflict`
    资源冲突，Rest中Post相同的资源。
    """

    code = 409
    description = (
        "A conflict happened while processing the request. The"
        " resource might have been modified while the request was being"
        " processed."
    )


class Gone(HttpCode):
    """
    *410* `Gone`
    当资源以前存在，但是现在已经重定向到新的位置的时候，连接失效。
    """

    code = 410
    description = "The requested URL is no longer available on this server and there is no forwarding address"


class LengthRequired(HttpCode):
    """
    *411* `Length Required`
    当请求的``Content-Length``不存在或者长度为0的时候。
    """

    code = 411
    description = "A request with this method requires a valid Content-Length header."


class PreconditionFailed(HttpCode):
    """
    *412* `Precondition Failed`
    先决条件失败``If-Match``, ``If-None-Match``, or ``If-Unmodified-Since``.
    """

    code = 412
    description = (
        # 请求URL的前提条件是评估失败。
        "The precondition on the request for the URL failed positive evaluation."
    )


class RequestEntityTooLarge(HttpCode):
    """
    *413* `Request Entity Too Large`
    请求的数据过大的时候。
    """

    code = 413
    description = "The data value transmitted exceeds the capacity limit."


class RequestURITooLarge(HttpCode):
    """
    *414* `Request URI Too Large`
    请求的URL太长。
    """

    code = 414
    description = (
        "The length of the requested URL exceeds the capacity limit for"
        " this server. The request cannot be processed."
    )


class UnsupportedMediaType(HttpCode):
    """
    *415* `Unsupported Media Type`
    不支持的媒体类型。
    """

    code = 415
    description = (
        "The server does not support the media type transmitted in the request."
    )


class RequestedRangeNotSatisfiable(HttpCode):
    """
    *416* `Requested Range Not Satisfiable`
    服务器无法处理所请求的数据区间。
    文件下载的时候，请求数据范围超过下载文件的长度范围，返回此错误代码。
    """

    code = 416
    description = "The server cannot provide the requested range."

    def __init__(self, length=None, units="bytes"):
        super(RequestedRangeNotSatisfiable, self).__init__()
        self.units = units
        self.length = length

    def get_headers(self, environ=None):
        headers = super(RequestedRangeNotSatisfiable, self).get_headers(environ)
        if self.length is not None:
            headers.append(("Content-Range", "%s */%d" % (self.units, self.length)))
        return headers


class ExpectationFailed(HttpCode):
    """
    *417* `Expectation Failed`
    服务器无法满足 Expect 请求消息头中的期望条件。
    浏览器不会使用此头信息。
    PUT /somewhere/fun HTTP/1.1
    Host: origin.example.com
    Content-Type: video/h264
    Content-Length: 1234567890987
    Expect: 100-continue
    当发送以上请求到服务器，服务器判断Content-Length头信息不能满足，返回417状态码。
    """

    code = 417
    description = "The server could not meet the requirements of the Expect header"


class ImATeapot(HttpCode):
    """
    *418* `I'm a teapot`
    The server should return this if it is a teapot and someone attempted
    to brew coffee with it.
    """

    code = 418
    description = "This server is a teapot, not a coffee machine"


class UnprocessableEntity(HttpCode):
    """
    *422* `Unprocessable Entity`
    表示服务器理解请求实体的Content-Type，并且请求实体的语法是正确的，但是服务器不能处理所包含的指示.
    """

    code = 422
    description = (
        "The request was well-formed but was unable to be followed due"
        " to semantic errors."
    )


class Locked(HttpCode):
    """
    *423* `Locked`
    请求的资源被锁定.
    """

    code = 423
    description = "The resource that is being accessed is locked."


class FailedDependency(HttpCode):
    """
    *424* `Failed Dependency`
    依赖其他操作失败。
    """

    code = 424
    description = (
        "The method could not be performed on the resource because the"
        " requested action depended on another action and that action"
        " failed."
    )


class PreconditionRequired(HttpCode):
    """
    *428* `Precondition Required`
    请求的前置条件缺失，http://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/If-Match
    多客户端操作同个资源问题。
    解决更新丢失问题：
    1. 比如上传文件之前，检查此文件是否在编辑中。
    2. 获取文件前，检查文件在某个时间之前还未改变。
    """

    code = 428
    description = (
        "This request is required to be conditional; try using"
        ' "If-Match" or "If-Unmodified-Since".'
    )


class TooManyRequests(HttpCode):
    """
    *429* `Too Many Requests`
    限流返回状态码
    """

    code = 429
    description = "This user has exceeded an allotted request count. Try again later."


class RequestHeaderFieldsTooLarge(HttpCode):
    """
    *431* `Request Header Fields Too Large`
    请求中的首部字段的值过大，服务器拒绝接受客户端的请求。客户端可以在缩减首部字段的体积后再次发送请求。
    """

    code = 431
    description = "One or more header fields exceeds the maximum size."


class UnavailableForLegalReasons(HttpCode):
    """
    *451* `Unavailable For Legal Reasons`
    是一种HTTP协议的错误状态代码，表示服务器由于法律原因，无法提供客户端请求的资源。
    """

    code = 451
    description = "Unavailable for legal reasons."


class InternalServerError(HttpCode):
    """
    *500* `Internal Server Error`
    服务器内部错误。
    """

    code = 500
    description = "The server encountered an internal error and was unable to complete your request."


class NotImplemented(HttpCode):
    """
    *501* `Not Implemented`
    请求的方法不被服务器支持。
    """

    code = 501
    description = "The server does not support the action requested by the browser."


class BadGateway(HttpCode):
    """
    *502* `Bad Gateway`
    后端服务器调用发生错误。
    """

    code = 502
    description = (
        "The proxy server received an invalid response from an upstream server."
    )


class ServiceUnavailable(HttpCode):
    """
    *503* `Service Unavailable`
    服务暂时不可用。
    """

    code = 503
    description = (
        "The server is temporarily unable to service your request due"
        " to maintenance downtime or capacity problems. Please try"
        " again later."
    )


class GatewayTimeout(HttpCode):
    """
    *504* `Gateway Timeout`
    连接后端服务器超时。
    """

    code = 504
    description = "The connection to an upstream server timed out."


class HTTPVersionNotSupported(HttpCode):
    """
    *505* `HTTP Version Not Supported`
    服务器不支持客户端请求的HTTP协议版本。
    """

    code = 505
    description = (
        "The server does not support the HTTP protocol version used in the request."
    )
