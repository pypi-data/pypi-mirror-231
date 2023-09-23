#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from urllib.parse import urlparse
from sqlalchemy import create_engine
from mitmproxy import http, ctx, flowfilter
from sqlalchemy.orm import sessionmaker

from pitrix.fixture import project
from pitrix.utils.log import logger
from pitrix.utils.yaml_tool import load_yaml
from pitrix.database.pitrix_table import Api


class Record:

    def __init__(self, pitrix_db=None, whitelist_host=None):
        if pitrix_db is None:
            self.db = project.db_path
        else:
            self.db = pitrix_db

        self.api_data = {}
        self.count = 1

        engine = create_engine(f"sqlite:///{self.db}")
        session = sessionmaker(bind=engine)
        self.session = session()

        self.filtration_suffix = (".jpg", ".png", ".gz", ".js", ".gif",
                                  ".svg", ".css", ".html", ".png", ".woff",
                                  ".jpg", ".mp3", ".mp4", ".ttf", ".ico")

        if whitelist_host is None:
            self.whitelist_host = []
            self.whitelist_host.append(self.get_config())
        logger.info(f"搜集的域名列表为:{self.whitelist_host}")

    @classmethod
    def get_config(cls):
        """
        获取测试环境配置
        @return:
        """
        config = load_yaml(project.conf_yaml)
        env = config.get('env')
        current_env_config = config.get(env)
        host = current_env_config.get('host')
        hostname = cls.extract_domain(host)
        return hostname

    @classmethod
    def extract_domain(cls, url):
        try:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            return domain
        except Exception as e:
            print(f"Error: {e}")
            return None

    def save_api_to_db(self):
        """
        保存API信息到DB
        @param table:
        @return:
        """
        try:
            new_api = Api(start_time=f"{self.api_data.get('start_time')}",
                          host=f"{self.api_data.get('host')}",
                          url=f"{self.api_data.get('url')}",
                          method=f"{self.api_data.get('method')}",
                          headers=f"{self.api_data.get('headers')}",
                          body=f"{self.api_data.get('body')}",
                          response=f"{self.api_data.get('response')}",
                          duration=f"{self.api_data.get('duration')}",
                          status_code=f"{self.api_data.get('status_code')}"
                          )
            self.session.add(new_api)
            self.session.commit()
        except Exception as e:
            logger.error(f"api table 插入失败,原因:{e}")
            self.session.rollback()

    def request(self, flow: http.HTTPFlow):
        """
        获取请求信息
        @param flow:
        @return:
        """
        request = flow.request
        for _host in self.whitelist_host:
            if _host in request.url:
                self.api_data['host'] = str(request.host)
                self.api_data['url'] = str(request.url)
                self.api_data['method'] = str(request.method.lower())

                headers_dict = {}
                headers = request.headers
                for key, value in headers.items():
                    headers_dict[key] = value
                self.api_data['headers'] = str(headers_dict)
                if request.method == 'POST':
                    self.api_data['body'] = flow.request.get_text()

    def response(self, flow: http.HTTPFlow):
        """
        获取响应信息
        @param flow:
        @return:
        """
        request = flow.request
        response = flow.response
        for _host in self.whitelist_host:
            if _host in request.url:
                self.api_data['response'] = flow.response.text
                req_start_time = flow.request.timestamp_start
                start_time = datetime.fromtimestamp(req_start_time).strftime('%Y-%m-%d %H:%M:%S')
                self.api_data['start_time'] = start_time
                res_end_time = flow.response.timestamp_end
                self.api_data['duration'] = float(res_end_time) - float(req_start_time)
                self.api_data['status_code'] = float(flow.response.status_code)
                self.save_api_to_db()
                self.count = self.count + 1

    def fittler(self, flow=None):
        """
        过滤
        :param flow:
        :return: 满足过滤条件返回True 不满足返回False
        """
        if self.filtration_suffix and flow.request.url.endswith(self.filtration_suffix):
            return True
        return False

    def whitelist(self, flow=None):
        """
        白名单域名
        :param flow:
        :return: 在白名单中的域名返回True 没有在白名单中的域名返回False
        """
        if not self.whitelist_host:
            return True
        request_url = flow.request.url
        sizer_url_list = self.whitelist_host
        for sizer_url in sizer_url_list:
            if sizer_url in request_url:
                return True


addons = [Record()]
