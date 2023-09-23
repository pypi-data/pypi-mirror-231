#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pytest
import threading
from multiprocessing import Pool
from configparser import ConfigParser
from configparser import NoOptionError
from functools import singledispatchmethod
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

from pitrix import __project__
from pitrix.utils.log import logger
from pitrix.extension.allure_report import mk_allure_report
from pitrix.fixture import BaseLogin, SetUpSession, TearDownSession, project, db_config

RUN_MODE = {
    "Runner": "main",
    "ProcessesRunner": "mp",
    "ThreadsRunner": "mt"
}


class HandleIni(ConfigParser):
    def __init__(self, filenames):
        super().__init__()
        self.read(filenames=filenames, encoding='utf-8')


def _init(func, login):
    method_of_class_name = func.__qualname__.split('.')[0]
    db_config.set("run_mode", RUN_MODE[method_of_class_name])
    SetUpSession(login)


def fixture_session(func):
    """全局夹具装饰器"""

    def wrapper(*args, **kwargs):
        login = kwargs.get('login')
        _init(func, login)
        r = func(*args, **kwargs)
        TearDownSession()
        return r

    return wrapper


class Runner:
    def __init__(self, is_processes=False):
        self.pytest_args = ["-s",
                            f"--alluredir={project.allure_results}",
                            "--show-capture=no",
                            "--log-format=%(asctime)s %(message)s",
                            "--log-date-format=%Y-%m-%d %H:%M:%S"
                            ]

    @fixture_session
    def run(self, args: list, login: BaseLogin = None, is_gen_allure=True, **kwargs):
        """
        单进程运行测试用例
        @param args:
        @param login:
        @param is_gen_allure:
        @param kwargs:
        @return:
        """
        args.extend(self.pytest_args)
        pytest_opts = _get_pytest_ini()
        logger.info(f"<{__project__.title()}> 单进程启动")
        logger.info(f"<{__project__.title()}> pytest的执行参数：{args}")
        if pytest_opts:
            logger.info(f"<{__project__.title()}> pytest.ini配置参数：{pytest_opts}")
        pytest.main(args)
        if is_gen_allure:
            mk_allure_report()

    @staticmethod
    def make_testsuite_path(path: str) -> list:
        """
        构建测试套件路径列表
        :param path: 测试套件所在目录
        :return: 测试套件路径列表
        """
        path_list = [path for path in os.listdir(path) if "__" not in path]
        testsuite = []
        for p in path_list:
            testsuite_path = os.path.join(path, p)
            if os.path.isdir(testsuite_path):
                testsuite.append(testsuite_path)

        return testsuite

    @staticmethod
    def make_testfile_path(path: str) -> list:
        """
        构建测试文件路径列表
        :param path: 测试文件所在目录
        :return: 测试文件路径列表
        """
        path_list = [path for path in os.listdir(path) if "__" not in path]
        testfile_path_list = []
        for p in path_list:
            testfile_path = os.path.join(path, p)
            if os.path.isfile(testfile_path):
                testfile_path_list.append(testfile_path)
        return testfile_path_list

    @singledispatchmethod
    def make_task_args(self, arg):
        raise TypeError("arg type must be List or Path")

    @make_task_args.register(list)
    def _(self, arg: list) -> list:
        """dist_mode:mark"""
        return arg

    @make_task_args.register(str)
    def _(self, arg: str) -> list:
        """dist_mode:suite"""
        path_list = self.make_testsuite_path(arg)
        return path_list

    @make_task_args.register(dict)
    def _(self, arg: dict) -> list:
        """dist_mode:file"""
        path_list = self.make_testfile_path(arg["path"])
        return path_list


class ProcessesRunner(Runner):

    @fixture_session
    def run(self, task_args, login: BaseLogin = None, extra_args=None, is_gen_allure=True, **kwargs):
        """
        多进程启动pytest任务
        :param task_args:
                list：mark标记列表
                str：测试套件或测试文件所在目录路径
        :param login: Login登录对象
        :param extra_args: pytest其它参数列表
        :param is_gen_allure: 是否自动收集allure报告，默认收集
        :return:
        """
        if extra_args is None:
            extra_args = []
        extra_args.extend(self.pytest_args)
        task_args = self.make_task_args(task_args)
        process_count = len(task_args)
        with Pool(process_count) as p:
            logger.info(f"<{__project__.title()}> 多进程任务启动，进程数：{process_count}")
            for arg in make_args_group(task_args, extra_args):
                p.apply_async(main_task, args=(arg,))
            p.close()
            p.join()
        if is_gen_allure:
            mk_allure_report()


class ThreadsRunner(Runner):

    @fixture_session
    def run(self, task_args: list or str, login: BaseLogin = None, extra_args=None, is_gen_allure=True, **kwargs):
        """
        多线程启动pytest任务
        :param task_args:
                list：mark标记列表
                str：测试套件或测试文件所在目录路径
        :param login: Login登录对象
        :param extra_args: pytest其它参数列表
        :param is_gen_allure: 是否自动收集allure报告，默认收集
        :return:
        """
        if extra_args is None:
            extra_args = []
        extra_args.extend(self.pytest_args)
        task_args = self.make_task_args(task_args)
        thread_count = len(task_args)
        thread_name = f"{__project__.title()}_Thread"
        with ThreadPoolExecutor(max_workers=thread_count, thread_name_prefix=thread_name) as p:
            logger.info(f"<{__project__.title()}> 多线程任务启动，线程数：{thread_count}")
            futures = [p.submit(main_task, arg) for arg in make_args_group(task_args, extra_args)]
            wait(futures, return_when=ALL_COMPLETED)
            p.shutdown()
        if is_gen_allure:
            mk_allure_report()


def _get_pytest_ini() -> list:
    conf = HandleIni(project.pytest_ini)
    try:
        pytest_opts = conf.get('pytest', 'addopts')
    except NoOptionError:
        pytest_opts = []
    if pytest_opts:
        pytest_opts = pytest_opts.split()
    return pytest_opts


def main_task(args: list):
    """pytest启动"""
    current_thread = threading.current_thread()
    logger.info(f"{current_thread.ident} - {current_thread.getName()} 开始启动")
    pytest_opts = _get_pytest_ini()
    logger.info(f"<{__project__.title()}> pytest的执行参数：{args}")
    if pytest_opts:
        logger.info(f"<{__project__.title()}> pytest.ini配置参数：{pytest_opts}")
    pytest.main(args)


def make_args_group(args: list, extra_args: list):
    """构造pytest参数列表
    pytest_args_group： [['-s','-m demo'],['-s','-m demo2'],...]
    :return pytest_args_group[-1] --> ['-s','-m demo2']
    """
    pytest_args_group = []
    for arg in args:
        pytest_args = []
        pytest_args.append(arg)
        pytest_args.extend(extra_args)
        pytest_args_group.append(pytest_args)
        yield pytest_args_group[-1]


run = Runner().run
threads_run = ThreadsRunner().run
processes_run = ProcessesRunner(is_processes=True).run
