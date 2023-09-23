#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import yaml


def load_yaml(yaml_file, mode='r'):
    """
    加载 yaml 文件并检查文件内容格式
    @param yaml_file:
    @param mode:
    @return:
    """
    with open(yaml_file, mode=mode) as stream:
        try:
            yaml_content = yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as ex:
            err_msg = f"YAMLError:\n file: {yaml_file}\n error: {ex}"
            raise err_msg
        return yaml_content


def dump_yaml(file, content):
    """
    python对象转化yaml文档
    :return:
    """
    with open(file, "w", encoding="utf-8") as f:
        yaml.dump(content, f, allow_unicode=True)


def check_yaml(dir):
    """
    检查指定的路径下的yaml文件语法是否正确
    :param dir: yaml文件路径
    :return:
    """
    yaml_file = []
    filelist = os.listdir(dir)
    for i in filelist:
        current_path = os.path.join(dir, i)
        if os.path.isfile(current_path):
            if current_path.endswith('.yaml'):
                yaml_file.append(os.path.join(os.path.abspath(dir), i))
        if os.path.isdir(current_path):
            check_yaml(current_path)
    for ym in yaml_file:
        try:
            with open(ym, 'r', encoding='utf-8') as f:
                cont = f.read()
            yaml.warnings({'YAMLLoadWarning': False})
            yaml.load(cont, Loader=yaml.FullLoader)
        except Exception as e:
            print(f"{ym} 文件读取错误:{str(e)}")
            sys.exit(1)
