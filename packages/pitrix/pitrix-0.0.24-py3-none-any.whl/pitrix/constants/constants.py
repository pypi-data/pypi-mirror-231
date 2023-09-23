#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from pitrix import __project__


class DataBase:
    DB_NAME = f"{__project__.lower()}.db"
    CONFIG_TABLE = 'config'
    CACHE_TABLE = 'cache'
    SCHEMA_TABLE = 'schema'
    API_TABLE = 'api'


class PitrixConf:
    PITRIX_BASE = os.path.dirname(os.path.dirname(__file__))
    PITRIX_TEMPLATE_SUFFIX = '.temp'
    PITRIX_TEMPLATE_DIR = os.path.join(PITRIX_BASE, "templates")
    RECORD_FILE = os.path.join(PITRIX_BASE,'extension','record.py')


class MysqlConfig:
    MYSQL_CONF = {
        "user": "root",
        "password": "12345678",
        "host": "localhost",
        "port": 3306,
    }


class LogConfig:
    """
    +----------------------+------------------------+------------------------+
    | Level name           | Severity value         | Logger method          |
    +======================+========================+========================+
    | ``TRACE``            | 5                      | |logger.trace|         |
    +----------------------+------------------------+------------------------+
    | ``DEBUG``            | 10                     | |logger.debug|         |
    +----------------------+------------------------+------------------------+
    | ``INFO``             | 20                     | |logger.info|          |
    +----------------------+------------------------+------------------------+
    | ``SUCCESS``          | 25                     | |logger.success|       |
    +----------------------+------------------------+------------------------+
    | ``WARNING``          | 30                     | |logger.warning|       |
    +----------------------+------------------------+------------------------+
    | ``ERROR``            | 40                     | |logger.error|         |
    +----------------------+------------------------+------------------------+
    | ``CRITICAL``         | 50                     | |logger.critical|      |
    +----------------------+------------------------+------------------------+
    """
    TRACE = 'TRACE'
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    SUCCESS = 'SUCCESS'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICA = 'CRITICAL'

    RETENTION = "10 days"
    ROTATION = "10MB"
    COMPRESSION = 'zip'
    BACKTRACE = False
    ENQUEUE = True  # 具有使日志记录调用非阻塞的优点(适用于多线程)

    FILE_HANDLER_DEFAULT_LEVEL = INFO
    CONSOLE_HANDLER_DEFAULT_LEVEL = DEBUG

    FILE_FORMAT = "{time:YYYY-MM-DD HH:mm:ss} | {process.name} | {thread.name} | {module}.{function}:{line} | {level}:{message}"  # 时间|进程名|线程名|模块|方法|行号|日志等级|日志信息
    CONSOLE_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | " \
                     "{process.name} | " \
                     "{thread.name} | " \
                     "<cyan>{module}</cyan>.<cyan>{function}</cyan>" \
                     ":<cyan>{line}</cyan> | " \
                     "<level>{level}</level>: " \
                     "<level>{message}</level>"
