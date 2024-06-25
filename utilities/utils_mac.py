#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site:
# @File: test_003_protocol_create.py
# @Author: PGQ
# @E-mail: panguoqing.pgq@sunyur.com
# @Time: 1月 30, 2021
# ---

import configparser
import datetime
import os, time
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import pyperclip


# 模拟键盘找到要上传的文件，进行上传
def uploadfile(fileName, dir=""):
    k = PyKeyboard()
    m = PyMouse()
    filePathheard = '/'
    # 模拟快捷键Command+Shift+G
    k.press_keys(['Command', 'Shift', 'G'])
    #
    # k.press_keys(['Command', 'Space'])
    # time.sleep(1)
    # 输入文件路径
    x_dim, y_dim = m.screen_size()
    m.click(x_dim // 2, y_dim // 2, 1)

    # 复制斜杠
    pyperclip.copy(filePathheard)
    time.sleep(1)
    # 粘贴斜杠
    k.press_keys(['Command', 'V'])
    time.sleep(1)
    # 拼接完整路径
    filePath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', dir, fileName)

    # 输入文件全路径
    k.type_string(str(filePath))
    time.sleep(2)
    # 前往文件
    k.press_keys(['Return'])
    time.sleep(2)
    # 点击确定进行上传
    k.press_keys(['Return'])
    time.sleep(3)


def get_timestamp():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')


# 获取前/后1天或N天的日期，offsetDay=-1：前1天；offsetDay=1：后1天
def get_offsetdate(offsetDay=-1):
    today = datetime.datetime.now()
    # 计算偏移量
    offset = datetime.timedelta(days=+offsetDay)
    # 获取想要的日期的时间
    offset_date = (today + offset).strftime('%Y-%m-%d')
    return offset_date


def read_config_data_key(section, key):
    cfg_filename = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
    # cur_path = os.path.abspath(os.path.dirname(__file__))
    # root_path = cur_path[:cur_path.find("sunyur_pytest_allure\\") + len("sunyur_pytest_allure\\")]
    # cfg_filename = os.path.join(root_path, "%s" % "config.ini")
    cp = configparser.RawConfigParser()
    cp.read(cfg_filename, encoding="utf-8")
    return cp.get(section, key)


def read_config_data_given_keys(section, *keys, all_value=True):
    cfg_filename = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
    # cur_path = os.path.abspath(os.path.dirname(__file__))
    # root_path = cur_path[:cur_path.find("sunyur_pytest_allure\\") + len("sunyur_pytest_allure\\")]
    # cfg_filename = os.path.join(root_path, "%s" % "config.ini")
    cp = configparser.RawConfigParser()
    cp.read(cfg_filename, encoding="utf-8")
    data = dict.fromkeys(keys, None)
    for k, v in cp.items(section):
        if k in keys:
            data[k] = v
        if all_value:
            if all(data.values()):
                break

    return data

