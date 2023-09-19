#!/Users/christmas/opt/anaconda3/bin/python3
# -*- coding: utf-8 -*-
#  日期 : 2023/4/11 13:35
#  作者 : Christmas
#  邮箱 : 273519355@qq.com
#  项目 : Project
#  版本 : python 3
#  摘要 :
"""

"""
import os


def osprint(_str):
    """
    打印信息
    :param _str: 打印信息
    :return:
    """
    os.system(f'echo `date "+%Y-%m-%d %T"` "---> {_str}"')


def osprints(_status, _str):
    """
    打印信息
    :param _status: 状态
    :param _str: 打印信息
    :return:
    """
    os.system(f'echo `date "+%Y-%m-%d %T"` "---> [{_status}] {_str}"')


def cprintf(_status=None, _str=None, _voice=True, _log_level='INFO'):
    """
    以颜色打印信息
    :param _status: 状态
    :param _str: 打印信息
    :param _voice: 是否语音提示
    :return:
    """
    if not _status:
        os.system(f'echo `date "+%Y-%m-%d %T"` "---> {_str}"')
    elif _status == 'SUCCESS':  # 绿色
        os.system(f'echo -e `date "+%Y-%m-%d %T"` "---> \033[1;32m[{_status}]\033[0m\033[32m {_str}\033[0m"')
    elif _status == 'INFO':  # 蓝色
        os.system(f'echo -e `date "+%Y-%m-%d %T"` "---> \033[1;34m[{_status}]\033[0m\033[34m {_str}\033[0m"')
    elif _status == 'WARNING':  # 橙色
        os.system(f'echo -e `date "+%Y-%m-%d %T"` "---> \033[1;33m[{_status}]\033[0m\033[33m {_str}\033[0m"')
    elif _status == 'ERROR':  # 红色
        if _voice:
            os.system(f'echo -e `date "+%Y-%m-%d %T"` "---> \033[1;31m[{_status}]\033[0m\033[31m {_str}\033[0m\a"')
        else:
            os.system(f'echo -e `date "+%Y-%m-%d %T"` "---> \033[1;31m[{_status}]\033[0m\033[31m {_str}\033[0m"')
