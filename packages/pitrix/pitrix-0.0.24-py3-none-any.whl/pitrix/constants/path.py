#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading
from pathlib import Path
from pitrix import __project__
from pitrix.constants.constants import DataBase


class Project:
    instance = None
    lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if cls.instance:
                return cls.instance
            cls.instance = object.__new__(cls)
            return cls.instance

    def __init__(self):
        self.root_dir = Path.cwd()
        Path(self.root_dir).cwd()
        self.conf_dir = self.root_dir.joinpath("config")
        self.apis_dis = self.root_dir.joinpath("apis")
        self.data_dir = self.root_dir.joinpath("datas")
        self.log_dir = self.root_dir.joinpath("logs")
        self.report_dir = self.root_dir.joinpath("reports")
        self.case_dir = self.root_dir.joinpath("testcases")
        self.pytest_ini = self.root_dir.joinpath("pytest.ini")
        self.db_path = self.root_dir.joinpath("database", DataBase.DB_NAME)
        self.conf_yaml = self.root_dir.joinpath("config", "config.yaml")
        self.log_file = self.root_dir.joinpath(self.log_dir, f"{__project__.lower()}.log")
        self.allure_results = self.root_dir.joinpath("reports", "json")
        self.allure_report = self.root_dir.joinpath("reports", "html")
        self.allure_summary_file = self.root_dir.joinpath(self.allure_results, "widgets", "summary.json")
        self.allure_env_file = self.root_dir.joinpath(self.allure_results, 'environment.properties')
        self.allure_type_file = self.root_dir.joinpath(self.allure_results, 'categories.json')
        self.notification_yaml = self.root_dir.joinpath(self.conf_dir, 'notification.yaml.temp')
        self.pitrix_yaml = self.root_dir.joinpath(self.conf_dir,f'{__project__.lower()}.yaml')


project = Project()
