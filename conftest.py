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

import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import configparser
from environment.data import Data
from utilities.utils import get_timestamp
import platform
import random
import allure
import time
from allure_commons.types import AttachmentType


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        time_str = time.strftime("%Y%m%d-%H%M%S")
        allure.attach(item.cls.driver.get_screenshot_as_png(), name=f"fail_step_{time_str}",
                      attachment_type=AttachmentType.PNG)


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     '''
#     获取每个用例状态的钩子函数
#     :param item:
#     :param call:
#     :return:
#     '''
#     # 获取钩子方法的调用结果
#     outcome = yield
#     rep = outcome.get_result()
#     # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             # let's also access a fixture for the fun of it
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         # 添加allure报告截图
#         if hasattr(_driver, "get_screenshot_as_png"):
#             with allure.step('添加失败截图...'):
#                 allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


def pytest_addoption(parser):
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    # 查看系统类型
    platform_ = platform.system()
    if platform_ == "Windows":
        driver_path = os.path.join(os.path.dirname(__file__), 'drivers', 'windows', 'chromedriver')
    else:
        driver_path = os.path.join(os.path.dirname(__file__), 'drivers', 'mac', 'chromedriver')

    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')
    environment = config.get("ENV", "environment")
    parser.addoption("--environment", action="store", default=environment)
    browser = config.get("DRIVERS", "browser")
    parser.addoption("--browser", action="store", default=browser)
    mode = config.get("DRIVERS", "mode")
    parser.addoption("--mode", action="store", default=mode)
    parser.addoption("--driver_path", action="store", default=driver_path)

    # 初始化环境参数文件
    if environment == "abc":
        basedata_file = "basedata_abc.ini"
    elif environment == "emp":
        basedata_file = "basedata_emp.ini"
    elif environment == "jxg":
        basedata_file = "basedata_jxg.ini"
    else:
        basedata_file = "basedata_abc.ini"
    basedata_path = os.path.join(os.path.dirname(__file__), '..', 'environment', basedata_file)
    config.read(basedata_path, encoding='utf-8')
    dict_res = config._defaults
    for k, v in dict_res.items():
        setattr(Data, k, v)


def pytest_collection_modifyitems(items):
    """
    解决用例执行，TestResults中参数中文是 unicode 编码 问题
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        # print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope="session",autouse=True)
def driver_init(request, pytestconfig):
    browser = pytestconfig.getoption('browser')
    mode = pytestconfig.getoption('mode')
    driver_path = pytestconfig.getoption('driver_path')
    # 设置chrome默认选项
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-infobars')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')
    options.add_argument('’–log-level=3')
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    # options.add_argument('--enable-devtools-experiments')

    if browser == "chrome":
        # 本地驱动：local
        if mode == "local":
            driver = webdriver.Chrome(executable_path=driver_path, options=options)
        else:
            driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=30).install(), options=options)
    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        driver = webdriver.Chrome(
            ChromeDriverManager(log_level=0, print_first_line=False, cache_valid_range=30).install())

    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
        # setattr(cls.obj, "logger", logger)

    yield
    driver.close()
    if driver is not None:
        driver.quit()


@pytest.fixture(scope="function", autouse=True)
def data_init():
    old_houzhui = Data.v_houzhui
    old_rand = Data.v_rand
    new_rand = str(random.randint(15000000000, 15099999999))
    new_houzhui = get_timestamp()

    param_tmp = {x: y for x, y in vars(Data).items() if '__' not in x}
    for name, value in param_tmp.items():
        if old_houzhui in value:
            value = value.replace(old_houzhui, new_houzhui)
            setattr(Data, name, value)
        if old_rand in value:
            value = value.replace(old_rand, new_rand)
            setattr(Data, name, value)
