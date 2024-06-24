import time
import pytest
from locators.apaas.apaas_locators import ApaasLocators as loc
from environment.data import Data
from pages.base_page import BasePage
from utilities.utils import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from utilities.logger import Logger
log = Logger(__name__).getlog()


class ApaasPage(BasePage):

    url = Data.apaas_url

    def __init__(self, driver, name="ApaasPage", url=url):
        self.driver = driver
        self.name = name
        self.url = url


    def apaas_login(self,username,password):
        self.sy_input(loc.apaas_login_user_loc,username)
        self.sy_input(loc.apaas_login_password_loc,password)
        time.sleep(2)
        self.sy_click(loc.apaas_button_loc)

    def open_apaas(self,object_name="对象02"):
        self.sy_click(loc.apaas_loc)
        self.driver.get("http://eai.newdev.sunyur.com/apaas_design/?id=1270&updateMenu=true#/paas/tenantlevel/custom-object/list")
        time.sleep(3)
        self.sy_click(loc.apaas_creat)
        self.sy_input(loc.object_name,object_name)
        self.sy_click(loc.next_loc)
        self.sy_input(loc.main_field,"名称")
        self.sy_click(loc.next_loc)
        self.sy_click(loc.save)
        time.sleep(2)
        self.sy_input(loc.select_object_name,object_name)
        self.sy_click(loc.list_object_name)
        time.sleep(3)

    def create_single_field(self, field_name="商品名称"):
        self.sy_click(loc.create_field)
        self.sy_input(loc.field_name, field_name)
        self.sy_click(loc.set_formula)
        self.sy_click(loc.formula_name)
        self.sy_click(loc.save_formula)
        time.sleep(3)
        self.sy_click(loc.set_page_display)
        time.sleep(3)
        self.sy_click(loc.save_field)
        time.sleep(3)

    def single_choice(self, field_name="商品名称"):
        self.sy_click(loc.create_field)
        self.sy_click(loc.single_choice)
        self.sy_input(loc.field_name, field_name)
        time.sleep(3)
        self.sy_click(loc.set_page_display)
        time.sleep(3)
        self.sy_click(loc.save_field)
        time.sleep(3)

    def multiple_choice(self, field_name="商品名称"):
        self.sy_click(loc.create_field)
        self.sy_click(loc.multiple_choice)
        self.sy_input(loc.field_name, field_name)
        time.sleep(3)
        self.sy_click(loc.set_page_display)
        time.sleep(3)
        self.sy_click(loc.save_field)
        time.sleep(3)

    def oolean(self, field_name="商品名称"):
        self.sy_click(loc.create_field)
        self.sy_click(loc.oolean)
        self.sy_input(loc.field_name, field_name)
        time.sleep(3)
        self.sy_click(loc.set_page_display)
        time.sleep(3)
        self.sy_click(loc.save_field)
        time.sleep(3)

    def num(self, field_name="数字"):
        self.sy_click(loc.create_field)
        self.sy_click(loc.num)
        self.sy_input(loc.field_name, field_name)
        self.sy_click(loc.red_mark)
        time.sleep(3)
        self.sy_click(loc.set_page_display)
        time.sleep(3)
        self.sy_click(loc.save_field)
        time.sleep(3)

    def find_association(self, field_name="查找关联"):
        self.sy_click(loc.create_field)
        self.sy_click(loc.find_association)
        self.sy_input(loc.field_name, field_name)
        self.sy_click(loc.find_document)
        time.sleep(3)
        input_element = self.driver.find_element(By.XPATH, loc.find_document)
        # time.sleep(3)
        input_element.send_keys("公司主体OU标准下拉")
        time.sleep(3)
        try:
            # 使用XPath或其他定位策略找到包含特定文本的下拉项
            dropdown_item = self.driver.find_element(By.XPATH,"//span[contains(text(),'公司主体OU标准下拉')]")
            dropdown_item.click()  # 点击选中该项
        except NoSuchElementException:
            # 处理元素未找到异常，可能意味着下拉项不存在或者筛选没有正确工作
            pytest.fail("Dropdown item with the search text was not found.")
        time.sleep(3)
        self.sy_click(loc.set_page_display)
        time.sleep(3)
        self.sy_click(loc.save_field)
        time.sleep(3)

    def page_create(self, page_name="页面管理"):
        self.sy_click(loc.page_loc)
        self.sy_click(loc.page_create)
        self.sy_input(loc.page_name_loc, page_name)
        self.sy_click(loc.pc_terminal)
        self.sy_click(loc.page_next)
        self.sy_click(loc.save)

    def list_create(self, list_name="自动化列表"):
        self.sy_click(loc.list_loc)
        self.sy_click(loc.list_create)
        self.sy_input(loc.list_name_loc, list_name)
        self.sy_click(loc.pc_terminal)
        self.sy_input(loc.list_text, "gfdsgfdgfsdgkfdgdsgs")
        time.sleep(3)
        self.sy_click(loc.page_next)
        self.sy_click(loc.save)
        time.sleep(3)