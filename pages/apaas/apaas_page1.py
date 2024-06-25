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

from locators.apaas.apaas_locators import ApaasLocators as loc
from environment.data import Data
from pages.base_page import BasePage
from utilities.utils import *
from selenium import webdriver



from utilities.logger import Logger
log = Logger(__name__).getlog()


class ApaasPage(BasePage):

    url = Data.apaas_url
    # 创建 WebDriver 对象
    driver = webdriver.Chrome()


    def __init__(self, driver, name="ApaasPage", url=url):
        self.driver = driver
        self.name = name
        self.url = url


    def apaas_login(self,username,password):
        self.sy_input(loc.apaas_login_user_loc,username)
        self.sy_input(loc.apaas_login_password_loc,password)
        time.sleep(2)
        self.sy_click(loc.apaas_button_loc)

    def open_apaas(self):
        self.sy_click(loc.apaas_loc)
        
        time.sleep(3)

    def mv_ele(self):
        print(loc.search_text_loc)

        self.sy_click(loc.search_loc)