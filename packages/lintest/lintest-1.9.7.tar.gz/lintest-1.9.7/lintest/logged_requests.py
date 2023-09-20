import os
import json as json_func
import requests
import settings

import curlify


def generate_curl(request):
    """
    根据 response.request 内容生产对应的 cURL
    @author: Wang Lin
    """
    command = "curl --compressed -X {method} -H {headers} -d '{data}' '{uri}'"

    method = request.method

    headers = ['"{0}: {1}"'.format(k, v) for k, v in request.headers.items()]
    headers = " -H ".join(headers)

    data = request.body
    uri = request.url

    return command.format(method=method, headers=headers, data=data, uri=uri)


def log_curl(func):
    """
    log curl 装饰器
    @author: Wang Lin
    """

    def wrapper(*args, **kw):
        self = None
        from .base_testcase import BaseTestCase

        #
        for item in args:
            try:
                if isinstance(item.this, BaseTestCase):
                    self = item.this
                    break
            except BaseException:
                pass

        res = func(*args, **kw)

        if not hasattr(settings, "always_generate_curl") or settings.always_generate_curl is False:
            if res.status_code == 200:
                return res

        # 只有failed的时候 或 显示设置 always_generate_curl=True  才自动生成 cURL
        if self:
            self.logger.info(
                os.linesep + os.linesep + "================================ cURL Start ==========================")
            self.logger.info(os.linesep + curlify.to_curl(res.request))
            self.logger.info(
                os.linesep + "================================ cURL End ============================" + os.linesep)
        else:
            # 原生requests调用。 此处直接把cURL输出到控制台
            print("================================ cURL Start ==========================" + os.linesep)
            print(curlify.to_curl(res.request))
            print("================================ cURL End ============================" + os.linesep)
        return res

    return wrapper


class LoggedRequests:
    def __init__(self, executing_case):
        self.this = executing_case
    """
    封装 requests module 的常用方法，自动log 每次 request 的参数 & response 内容
    @author: Wang Lin
    """

    @log_curl
    def get(self, url, params=None, **kwargs):
        self = self.this

        # 增加此判断逻辑，解释参见 post 方法
        if hasattr(settings, "auto_log_request") and settings.auto_log_request is False:
            # 直接调用 开源 requests
            return requests.get(url, params, **kwargs)

        self.logger.info(
            os.linesep + os.linesep + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GET Start:")
        self.logger.info(os.linesep + "---------------- URL: " + url)

        if params is not None:
            self.logger.info(os.linesep + "-------------- params:")
            self.logger.info(os.linesep + self.pformat(params))

        if len(kwargs.keys()) > 0:
            self.logger.info(os.linesep + "-------------- kwargs:")
            self.logger.info(os.linesep + json_func.dumps(kwargs, indent=2))

        # call requests.get()
        response = requests.get(url, params, **kwargs)

        self.logger.info(
            os.linesep + os.linesep + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< GET Response:")
        self.logger.info(response)

        # todo
        if response.status_code == 200:
            try:
                # self.logger.info(self.pformat(response.json()))
                self.logger.info(os.linesep + json_func.dumps(response.json(), ensure_ascii=False, indent=2))
            except BaseException:
                return response

        self.logger.info(
            os.linesep + "========================= GET DONE =========================" + os.linesep + os.linesep)

        return response

    @log_curl
    def post(self, url, data=None, json=None, **kwargs):
        self = self.this

        #  为了 不重复记录 log,则 增加如下判断， 如果 settings.auto_log_request = False, 则不需要框架自动记录log!
        if hasattr(settings, "auto_log_request") and settings.auto_log_request is False:
            # 直接调用 开源 requests
            return requests.post(url, data, json, **kwargs)

        self.logger.info(
            os.linesep + os.linesep + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> POST Start:")
        self.logger.info(os.linesep + "------------ URL: " + url)

        if data is not None:
            self.logger.info(os.linesep + os.linesep + "------------ post data:")

            # # todo: headers type
            # if kwargs['headers']['Content-Type'] == 'application/x-www-form-urlencoded':
            #     self.logger.info(os.linesep + self.pformat(data))
            # else:
            #     self.logger.info(os.linesep + self.pformat(json_func.loads(data)))

            try:
                # 此处省去各种判断逻辑, 如果 json.loads()报错，则直接 记录原始data
                # self.logger.info(os.linesep + self.pformat(json_func.loads(data)))
                self.logger.info(os.linesep + json_func.dumps(json_func.loads(data), ensure_ascii=False, indent=2))
            except BaseException:
                self.logger.info(os.linesep + self.pformat(data))

            # self.logger.info(os.linesep + "------------ data end -------" + os.linesep)

        if json is not None:
            self.logger.info(os.linesep + os.linesep + "------------ json:")
            self.logger.info(os.linesep + json_func.dumps(json, ensure_ascii=False, indent=2))

        if len(kwargs.keys()) > 0:
            self.logger.info(os.linesep + os.linesep + "------------ kwargs:")
            self.logger.info(os.linesep + json_func.dumps(kwargs, ensure_ascii=False, indent=2))

        # call requests.post()
        response = requests.post(url, data, json, **kwargs)

        self.logger.info(
            os.linesep + os.linesep + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< POST Response:")
        self.logger.info(response)

        # todo
        if response.status_code == 200:
            try:
                # dumps()方法中的 indent参数 如果 不为空 则会自动format输出结果
                self.logger.info(os.linesep + json_func.dumps(response.json(), ensure_ascii=False, indent=2))
            except BaseException:
                self.logger.info(response.__dict__)
                return response

        self.logger.info(
            os.linesep + "========================= POST DONE =========================" + os.linesep + os.linesep)

        return response

    @log_curl
    def put(self, url, data=None, **kwargs):
        self = self.this

        # 增加此判断逻辑，解释参见 post 方法
        if hasattr(settings, "auto_log_request") and settings.auto_log_request is False:
            # 直接调用 开源 requests
            return requests.put(url, data, **kwargs)

        self.logger.info(
            os.linesep + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PUT Start:")
        self.logger.info(os.linesep + "-------------- URL: " + url)

        if data is not None:
            self.logger.info(os.linesep + "------------ data:")
            try:
                self.logger.info(os.linesep + self.pformat(json_func.loads(data)))
            except BaseException:
                self.logger.info(os.linesep + self.pformat(data))

        if len(kwargs.keys()) > 0:
            self.logger.info(os.linesep + "------------ kwargs:")
            self.logger.info(os.linesep + json_func.dumps(kwargs, ensure_ascii=False, indent=2))

        # call requests.put()
        response = requests.put(url, data, **kwargs)

        self.logger.info(
            os.linesep + os.linesep + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PUT Response:")
        self.logger.info(response)

        # todo
        if response.status_code == 200:
            try:
                self.logger.info(os.linesep + json_func.dumps(response.json(), ensure_ascii=False, indent=2))
            except BaseException:
                return response

        self.logger.info(
            os.linesep + "========================= PUT DONE =========================" + os.linesep + os.linesep)

        return response

    @log_curl
    def delete(self, url, **kwargs):
        self = self.this
        
        # 增加此判断逻辑，解释参见 post 方法
        if hasattr(settings, "auto_log_request") and settings.auto_log_request is False:
            # 直接调用 开源 requests
            return requests.delete(url, **kwargs)

        self.logger.info(
            os.linesep + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> DELETE Start:")
        self.logger.info(os.linesep + "--------------- URL: " + url)

        if len(kwargs.keys()) > 0:
            self.logger.info(os.linesep + "------------ kwargs:")
            self.logger.info(os.linesep + json_func.dumps(kwargs, ensure_ascii=False, indent=2))

        # call requests.delete()
        response = requests.delete(url, **kwargs)

        self.logger.info(
            os.linesep + os.linesep + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< DELETE Response:")
        self.logger.info(response)

        # todo
        if response.status_code == 200:
            try:
                self.logger.info(os.linesep + json_func.dumps(response.json(), ensure_ascii=False, indent=2))
            except BaseException:
                return response

        self.logger.info(
            os.linesep + "========================= DELETE DONE =========================" + os.linesep + os.linesep)

        return response
