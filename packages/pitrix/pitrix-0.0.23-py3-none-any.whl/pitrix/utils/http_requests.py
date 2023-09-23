#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from pitrix.utils.log import logger
from requests.exceptions import ReadTimeout, HTTPError, RequestException
try:
    from requests.packages import urllib3
    urllib3.disable_warnings()
except Exception:
    import logging
    logging.captureWarnings(True)
from tenacity import retry, stop_after_delay, stop_after_attempt


class HttpRequests:
    HTTP_RETRY = 3
    HTTP_MAX_RETRY_TIME = 5

    @staticmethod
    @retry(stop=(stop_after_attempt(HTTP_RETRY) | stop_after_delay(HTTP_MAX_RETRY_TIME)))
    def http_requests(method=None,url=None,params=None,data=None,json=None,headers=None,files=None,cookies=None,verify=False,cert=None,proxies=None,timeout=30,auth=None):
        """
       :param method:请求的方式，get、post等等
       :param url: 请求的地址 http://xxxx:post
       :param data:传递的参数
       :param headers:传递的请求头
       :param files:上传的文件,例如files={'file':open('favicon.ico','rb')},传二进制文件
       :param cookie:请求时传递的cookie值
       :param verify:是否忽略SSLError,False为忽略，True为显示
       :param cert:指定证书文件，需要有crt和key文件，并且指定他们的路径,例如cert=('/path/server.crt','/path/key')
       :param proxies:设置代理,例如proies = {"http":"http://10.10.1.10:3128","https":"http://10.10.1.10:1080"}
       :param timeout:设置请求的超时时间,连接和读取的总时长,例如timeout=1
       :param auth:用户认证，auth=HTTPBasicAuth('username','password')
       :return:
        """
        try:
            if method.strip().lower() == 'get' or method is None:
                res = requests.get(url=url,params=params,headers=headers,cookies=cookies,verify=verify,cert=cert,proxies=proxies,timeout=timeout,auth=auth)
            elif method.strip().lower() == 'post':
                res = requests.post(url=url,data=data,json=json,headers=headers,cookies=cookies,files=files,verify=verify,cert=cert,proxies=proxies,timeout=timeout,auth=auth)
            else:
                raise ValueError("暂不支持除GET、POST以外的请求方法")
        except ReadTimeout as e:
            logger.critical("HTTP请求ReadTimeout,原因:{0}".format(e))
            raise e
        except HTTPError as e:
            logger.critical("HTTP请求HTTPError,原因:{0}".format(e))
            raise e
        except RequestException as e:
            logger.critical("HTTP请求RequestException,原因:{0}".format(e))
            raise e
        except Exception as e:
            logger.critical("HTTP请求Exception,原因:{0}".format(e))
            raise e
        else:
            return res


if __name__ == '__main__':
    url = "http://www.baidu.com"
    res = HttpRequests.http_requests('get', url,timeout=0.01) # 测试下重试装饰器
    if res:
        print(res.text)
