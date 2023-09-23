#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from typing import List, Dict
from pitrix.fixture import project
from pitrix.exceptions import FileNotFound, YamlKeyError
from pitrix.utils.yaml_tool import load_yaml


def data_maker(file_path: str, class_name: str, method_name: str) -> List[Dict]:
    """
    从测试数据文件中读取文件，构造数据驱动的列表参数
    :param file_path: 测试数据文件（相对路径，相对项目根目录）
    :param class_name: 类名
    :param method_name: 方法名
    :return:
            eg:
            [{"name":"zz"},{"name":"yy"},...]
    """
    yaml_path = os.path.join(project.root_dir, file_path)
    if not os.path.exists(yaml_path):
        raise FileNotFound(yaml_path)
    class_data = load_yaml(yaml_path).get(class_name)
    if class_data is None:
        raise YamlKeyError(file_path, class_name)
    method_data = class_data.get(method_name)
    if method_data is None:
        raise YamlKeyError(file_path, method_name)
    return method_data
