#!/usr/bin/python
# encoding=utf-8

from abc import ABCMeta, abstractmethod

from pitrix import __project__
from pitrix.utils.log import logger
from pitrix.constants.path import project
from pitrix.utils.yaml_tool import load_yaml
from pitrix.database.cache import Config, Cache, Schema

db_cache = Cache(project.db_path)
db_config = Config(project.db_path)
db_schema = Schema(project.db_path)


class BaseLogin(metaclass=ABCMeta):

    def __init__(self):
        self.config = load_yaml(project.conf_yaml)
        self.current_env = self.config.get('env')
        self.current_env_conf = self.config.get(self.current_env)
        self.host = self.config.get(self.current_env).get('host')
        self.account = self.config.get(self.current_env).get('account')
        logger.info(f"测试环境:{self.current_env}")
        logger.info(f"测试host:{self.host}")
        logger.info(f"测试账号:{self.account}")

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def make_headers(self, resp_login: dict):
        pass


class SetUpSession:

    def __init__(self, login):
        logger.info(f"<{__project__.title()} 正在进行初始化.>")
        self.login_obj = login
        self.set_session_vars()
        logger.info(f"<{__project__.title()} 初始化执行完成,开始进入测试环节.>")

    def set_session_vars(self):
        config = load_yaml(project.conf_yaml)
        env = config.get('env')
        db_config.set("current_env", env)
        conf_dict = config.get(env)
        for k, v in conf_dict.items():
            db_config.set(k, v)

        if self.login_obj:
            resp = self.login_obj.login()
            logger.info(f"登录结果:{resp}")
            headers = self.login_obj.make_headers(resp)
            if headers:
                db_cache.set('headers', headers)


class TearDownSession:

    def __init__(self):
        logger.info(f"<{__project__.title()} 正在执行清理数据库操作.>")
        self.clear_env()
        logger.info(f"<{__project__.title()} 数据库缓存清理完成.>")

    def clear_env(self):
        db_cache.clear()
        db_cache.close()
        db_config.close()
