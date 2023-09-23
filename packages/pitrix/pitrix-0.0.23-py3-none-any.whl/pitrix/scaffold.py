#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import click
import platform

from pitrix import __project__
from pitrix.constants.constants import DataBase
from pitrix.constants.constants import PitrixConf
from pitrix.database.pitrix_table import create_tables


def create_folder(path):
    """
    创建目录
    @param path:
    @return:
    """
    if not os.path.exists(path):
        os.makedirs(path)
        click.echo(f"创建文件夹: {path}")


def create_file(path, file_content=""):
    """
    创建文件
    @param path:
    @param file_content:
    @return:
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(file_content)
    click.echo(f"创建文件: {path}")


def delete_folder(path):
    """
    删除目录
    @param path:
    @return:
    """
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)
        click.echo(f"删除目录:{path} 成功")
    else:
        click.echo(f"{path} 未找到,请手动删除项目")


def create_scaffold(project_name):
    """
    创建脚手架
    @param project_name:
    @return:
    """
    if os.path.isdir(project_name):
        click.echo(f"项目文件夹 {project_name} 已存在，请指定新的项目名称.")
        sys.exit(1)
    elif os.path.isfile(project_name):
        click.echo(f"工程名称 {project_name} 与已存在的文件冲突，请指定一个新的文件.")
        sys.exit(1)

    click.echo("🏗🏗🏗 开始创建脚手架 🏗🏗🏗 ")
    click.echo(f"创建新项目:【{project_name}】")
    click.echo(f"项目根目录: {os.path.join(os.getcwd(), project_name)}")

    create_folder(project_name)

    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

    click.echo(f"模版路径:{template_path}")

    for root, dirs, files in os.walk(template_path):
        relative_path = root.replace(template_path, "").lstrip("\\").lstrip("/")
        print("relative_path: {}".format(relative_path))
        if dirs:
            for dir_ in dirs:
                create_folder(os.path.join(project_name, relative_path, dir_))
        if files:
            for file in files:
                with open(os.path.join(root, file), encoding="utf-8") as f:
                    create_file(
                        os.path.join(project_name, relative_path, file.rstrip(PitrixConf.PITRIX_TEMPLATE_SUFFIX)),
                        f.read())

    db_dir_path = os.path.join(project_name, "database")
    db_file_path = os.path.join(db_dir_path, DataBase.DB_NAME)

    create_folder(db_dir_path)

    create_tables(db_file_path)

    click.echo("😄😄😄 脚手架创建完成 😄😄😄 ")

    return True


def create_virtual_environment(project_name):
    """
    创建虚拟环境
    @param project_name:
    @return:
    """
    os.chdir(project_name)
    click.echo("🛠🛠🛠  开始创建虚拟环境 🛠🛠🛠 ")
    os.system("python3 -m venv .venv")
    click.echo("创建虚拟环境: .venv")
    click.echo("😄😄😄  虚拟环境创建完成 😄😄😄 ")

    click.echo(f"⏳ ⏳ ⏳  开始安装 {__project__.title()} 测试框架 ⏳ ⏳ ⏳ ")
    if platform.system().lower() == 'windows':
        os.chdir(".venv")
        os.chdir("Scripts")
        os.system(f"pip3 install {__project__.title()}")
    elif platform.system().lower() in ['linux', 'darwin']:
        os.chdir(".venv")
        os.chdir("bin")
        os.system(f"pip3 install {__project__.title()}")
    else:
        raise ValueError("暂不支持此平台")
    click.echo(f"😄😄😄  {__project__.title()} 安装完成 😄😄😄 ")
