#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import click
from emoji import emojize
from typing import List, Text
from mitmproxy.tools.main import mitmdump
from click_help_colors import HelpColorsGroup, version_option

from pitrix.fixture import project
from pitrix.extension.models import PitrixYaml
from pitrix.constants.constants import PitrixConf
from pitrix import __version__, __project__, __image__
from pitrix.utils.yaml_tool import load_yaml,dump_yaml
from pitrix.runner import run as runner_run, threads_run, processes_run
from pitrix.scaffold import create_scaffold, delete_folder, create_virtual_environment


def _handle_login(is_login: bool):
    if is_login is False:
        return
    sys.path.append(os.getcwd())
    exec('from login import Login')
    login_obj = locals()['Login']()
    return login_obj


@click.group(cls=HelpColorsGroup,
             invoke_without_command=True,
             help_headers_color='magenta',
             help_options_color='green',
             context_settings={"max_content_width": 120, })
@version_option(version=__version__, prog_name=__project__, message_color="cyan")
@click.pass_context
def main(ctx):
    sys.path.append(str(project.root_dir))
    click.echo(__image__)
    ctx.ensure_object(dict)
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@main.command()
@click.argument("project_name")
@click.option('--venv', '-v', is_flag=True)
@click.pass_context
def startproject(ctx, project_name, venv):
    """创建一个新项目,例如:pitrix startproject demo,指定 -v 或者 --venv 来配置创建虚拟环境"""
    folder_path = os.path.join(os.getcwd(), project_name)
    ctx.obj['project_path'] = folder_path
    create_scaffold(project_name)
    click.echo(emojize(":beer_mug: 项目脚手架创建完成！"))

    if venv:
        # create_virtual_environment(ctx.obj['project_path'])
        create_virtual_environment(project_name)


@main.command()
@click.argument("project_name")
@click.pass_context
def deleteproject(ctx, project_name):
    """删除一个项目,例如:pitrix deleteproject demo"""
    folder_path = os.path.join(os.getcwd(), project_name)
    click.echo(f"项目路径:{folder_path}")
    delete_folder(project_name)


@main.command(help="运行测试用例", context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
@click.option("-e", "--env", help="切换测试环境")
@click.option("--mp", "--multi-process", help="多进程执行测试用例", is_flag=True)
@click.option("--mt", "--multi-thread", help="多线程执行测试用例", is_flag=True)
@click.option("--no_login", help="是否执行登录", is_flag=True, flag_value=False, default=True)
@click.option("--no_gen", help="是否生成测试报告.", is_flag=True, flag_value=False, default=True)
@click.option("--dist-suite", "d_suite",
              help="Distribute each test package under the test suite to a different worker.")
@click.option("--dist-file", "d_file", help="Distribute each test file under the test package to a different worker.")
@click.option("--dist-mark", "d_mark", help="Distribute each test mark to a different worker.")
@click.pass_context
def run(ctx, env, no_login, mp, mt, no_gen, d_mark, d_file, d_suite):
    pytest_args = ctx.args
    if env:
        set_conf_file(env)
    login_obj = _handle_login(no_login)
    if mp:
        click.echo(f"🚀<{__project__.title()}> 多进程模式准备启动...")
        processes_run(_handle_dist_mode(d_mark, d_file, d_suite),
                      login=login_obj,
                      extra_args=pytest_args,
                      is_gen_allure=no_gen)
        ctx.exit()
    elif mt:
        click.echo(f"🚀<{__project__.title()}> 多线程模式准备启动...")
        threads_run(_handle_dist_mode(d_mark, d_file, d_suite),
                    login=login_obj,
                    extra_args=pytest_args,
                    is_gen_allure=no_gen)
        ctx.exit()
    else:
        click.echo(f"🚀<{__project__.title()}> 单进程模式准备启动...")
        click.echo(f"🚀<测试环境> {env}")
        runner_run(pytest_args, login=login_obj, is_gen_allure=no_login)
        ctx.exit()


@main.command(help="流量录制, 默认 8082 端口")
@click.option("-e", "--env", help="切换录制环境")
@click.option("-p", "--port", type=int, default=8082, help='指定代理服务端口,默认端口:8082.')
def record(env,port):
    if env:
        set_conf_file(env)
    click.echo(f"<{__project__.title()}> 开始进行流量录制,端口:{port}")
    mitmdump([f'-p {port}', f'-s {PitrixConf.RECORD_FILE}'])


def _handle_dist_mode(d_mark, d_file, d_suite):
    if d_mark:
        params = [f"-m {mark}" for mark in d_mark]
        mode_msg = "dist-mark"
        click.echo(f"🚀<{__project__.title()}> 分配模式: {mode_msg}")
        return params

    if d_file:
        params = {"path": d_file}
        mode_msg = "dist-file"
        click.echo(f"🚀<{__project__.title()}> 分配模式: {mode_msg}")
        return params

    if d_suite:
        params = d_suite
        mode_msg = "dist-suite"
        click.echo(f"🚀<{__project__.title()}> 分配模式: {mode_msg}")
        return params

    params = _handle_aomaker_yaml()
    mode_msg = f"dist-mark({__project__.lower()}.yaml策略)"
    click.echo(f"🚀<{__project__.title()}> 分配模式: {mode_msg}")
    return params


def _handle_aomaker_yaml() -> List[Text]:
    if not os.path.exists(project.pitrix_yaml):
        click.echo(emojize(f':confounded_face: {__project__.title()} 策略文件{project.pitrix_yaml}不存在！'))
        sys.exit(1)
    yaml_data = load_yaml(project.pitrix_yaml)
    content = PitrixYaml(**yaml_data)
    targets = content.target
    marks = content.marks
    d_mark = []
    for target in targets:
        if "." in target:
            target, strategy = target.split(".", 1)
            marks_li = marks[target][strategy]
        else:
            marks_li = marks[target]
        d_mark.extend([f"-m {mark}" for mark in marks_li])
    return d_mark


def set_conf_file(env):
    """
    读取并设置配置文件
    @param env:
    @return:
    """
    conf_path = str(project.conf_yaml)
    if os.path.exists(conf_path):
        doc = load_yaml(conf_path)
        doc['env'] = env
        if not doc.get(env):
            click.echo(emojize(f':confounded_face: 测试环境-{env}还未在配置文件中配置！'))
            sys.exit(1)
        dump_yaml(conf_path,doc)
        click.echo(emojize(f':rocket:<{__project__.title()}> 当前测试环境: {env}'))
    else:
        click.echo(emojize(f':confounded_face: 配置文件{conf_path}不存在'))
        sys.exit(1)


if __name__ == '__main__':
    main()
