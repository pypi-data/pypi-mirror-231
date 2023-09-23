#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import click
from genson import SchemaBuilder
from pitrix.constants.constants import PitrixConf


def add_template_suffix(dir='./', target_suffix=PitrixConf.PITRIX_TEMPLATE_SUFFIX):
    """
    将执行目录下的文件后缀名改为.temp
    @param dir:
    @param target_suffix:
    @return:
    """
    for root, dir, files in os.walk(dir):
        if files:
            for file in files:
                source_file = os.path.join(root, file)
                file_name, file_extension = os.path.splitext(source_file)
                if file_extension != target_suffix:
                    target_file = source_file + target_suffix
                    click.echo(f"源文件:{source_file},目标文件:{target_file}")
                    os.rename(source_file, target_file)


def genson(data):
    """
    生成jsonschema
    :param data: json格式数据
    :return: jsonschema
    """
    builder = SchemaBuilder()
    builder.add_object(data)
    to_schema = builder.to_schema()
    return to_schema


if __name__ == '__main__':
    add_template_suffix(dir=PitrixConf.PITRIX_TEMPLATE_DIR)
