#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import json
import time
import shutil
from collections import namedtuple

from pitrix.utils.log import logger
from pitrix.fixture import project, db_config
from pitrix.extension.template import categories_json


def mk_trend():
    """
    将上次测试报告中的测试历史数据拷贝到最新的生成的历史数据中
    @param config: 项目配置类
    @return:
    """
    allure_report_history_path = os.path.join(project.allure_report, 'history')
    allure_results_history_path = os.path.join(project.allure_results, 'history')
    if os.path.exists(allure_results_history_path):
        shutil.rmtree(allure_results_history_path)
    shutil.copytree(allure_report_history_path, allure_results_history_path)


def mk_allure_report():
    """
    生成allure测试报告
    @param config: 项目配置类
    @return:
    """
    try:
        allure_env_prop()
        gen_allure()
        mk_trend()
        categories()
        logger.success("Allure Report Successfully")
        return True
    except Exception as e:
        logger.critical(f"Allure Report Failed: {str(e)}")
        return False


def gen_allure(is_clear=False):
    """
    生成allure测试报告
    @param is_clear:
    @return:
    """
    cmd = f'allure generate ' \
          f'-c {project.allure_results} ' \
          f'-o {project.allure_report}'
    if is_clear:
        cmd = cmd + '--clean'
    os.system(cmd)
    time.sleep(3)


def allure_env_prop():
    """
    写入配置信息到allure测试报告中
    @return:
    """
    conf: dict = db_config.get_all()
    if conf:
        content = ""
        for k, v in conf.items():
            content += f"{k}={v}\n"
        if not project.allure_report.exists():
            project.allure_report.mkdir(parents=True,exist_ok=True)
        with open(project.allure_env_file, mode='w', encoding='utf-8') as f:
            f.write(content)


def categories():
    """
    写类型信息到allure测试报告
    @param config:
    @return:
    """
    with open(project.allure_type_file, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(categories_json, indent=2, ensure_ascii=False))


class AllureGetData:

    @staticmethod
    def get_summary(allure_summary_json):
        """
        获取所有 allure 报告中执行用例的情况
        @param allure_summary_json: 文件地址,位于allure report/widgets/summary.json
        @return:
        """
        Summary = namedtuple('Summary', ['total', 'passed', 'broken', 'failed', 'skipped',
                                         'passed_rate', 'failed_rate', 'run_time', 'unknown'])

        if os.path.exists(allure_summary_json):
            with open(allure_summary_json, "r", encoding='utf-8') as f:
                data = json.load(f)
            total = data['statistic']['total'] if data['statistic']['total'] is not None else 0
            passed = data['statistic']['passed'] if data['statistic']['passed'] is not None else 0
            broken = data['statistic']['broken'] if data['statistic']['broken'] is not None else 0
            failed = data['statistic']['failed'] if data['statistic']['failed'] is not None else 0
            skipped = data['statistic']['skipped'] if data['statistic']['skipped'] is not None else 0
            unknown = data['statistic']['unknown'] if data['statistic']['unknown'] is not None else 0
            passed_rate = round(passed / (total - skipped))
            failed_rate = round(failed / (total - skipped))
            run_time = round(data['time']['duration'] / 1000, 2)

            summary = Summary(total=total, passed=passed, failed=failed,
                              broken=broken, unknown=unknown, skipped=skipped,
                              passed_rate=passed_rate, failed_rate=failed_rate, run_time=run_time
                              )
            return summary
