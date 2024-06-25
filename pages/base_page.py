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

from utilities.utils import uploadfile,get_timestamp
from utilities.json_path import JsonPath
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time, os
import pytest
import json
import pyautogui

from utilities.logger import Logger
log = Logger(__name__).getlog()

import allure
from allure_commons.types import AttachmentType


class BasePage:
    timeout = 20  # 最大超时时间10s
    frequency = 0.5  # 检查频率0.5s

    def __init__(self, driver, name, url):
        self.name = name
        self.url = url
        self.driver = driver
        self.dict_cookies = ""

    def load(self, cookies=""):
        self.driver.get(self.url)
        if cookies != "":
            self.driver.add_cookie(cookies)
            self.driver.get(self.url)
        self.driver.maximize_window()
        cookies_dict = {}
        for item in self.driver.get_cookies():
            cookies_dict[item["name"]] = item["value"]
            # cookies_dict["value"] =
        self.dict_cookies = cookies_dict

    def is_page_loaded(self):
        # Utils.log("INFO", f"Verifying {self.name}, loaded")
        result = False
        try:
            result = WebDriverWait(self.driver, self.timeout, self.frequency).until(EC.url_contains(self.url))
        except Exception as e:
            # Utils.log("ERROR", f"{self.name}, is not getting displayed; {e.__cause__}")
            pytest.fail("该用例执行失败，因为 %s 页面加载失败" % self)
            # pass
        return result

    def get_dict_cookies(self):
        return self.dict_cookies




    # 定义定位方法
    def sy_find_element(self, loc, bol=True):
        # try:
        # WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(loc))
        # element = self.driver.find_element(*loc)
        # piont = element.location['y']
        # if piont > 500:
        #     heigh = piont - 200
        #     self.driver.execute_script("window.scrollTo(0, %s)"%heigh)
        # # self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", self.driver.find_element(*loc))
        # WebDriverWait(self.driver, self.timeout,1).until(EC.visibility_of_element_located(*loc))
        # WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_element(*loc).is_displayed())

        if self.sy_is_visibility(loc) and self.sy_is_presences(loc) and self.sy_is_clickable(loc):
            if bol:
                loc1 = By.XPATH, "%s" % loc
                self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*loc1))
            return self.sy_is_visibility(loc)
        else:
            pytest.fail("该用例执行失败，因为 %s 页面中未能找到 %s 元素" % (self, loc))


    def sy_find_elements(self, loc):
        # return self.driver.find_elements(*loc)
        if self.sy_is_presences(loc):
            return self.sy_is_presences(loc)
        else:
            pytest.fail("该用例执行失败，因为 %s 页面中未能找到 %s 元素" % (self, loc))

    def sy_get_element_text(self, loc):
        return str.strip(self.sy_find_element(loc).text)

    def get_element_value(self, loc, value):
        return self.sy_find_element(loc).get_attribute(value)

    # 重写switch_frame方法
    def sy_switch_frame(self, loc):
        loc = By.XPATH, "%s" % loc
        return self.driver.switch_to_frame(loc)

    # 切换新窗口
    def sy_switch_page(self, index=0):
        # current_handle = self.driver.current_window_handle
        # handles  = self.driver.window_handles
        # for window in handles:
        #     if window != current_handle:
        #         self.driver.switch_to.window(window)
        time.sleep(1)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    # def sy_scrollLeft(self,loc1,loc,x_pixel):
    #     self.sy_move_element(loc1)
    #     js='document.getElementsByXpath("%s").scrollLeft=%s;' % (loc,x_pixel)
    #     self.sy_script(js)

    def sy_scrollLeft(self, css_loc, x_pixel):
        js = 'document.querySelector("%s").scrollLeft=%s;' % (css_loc, x_pixel)
        self.sy_script(js)

    # 定义script方法，用于执行js脚本，范围执行结果
    def sy_script(self, src):
        self.driver.execute_script(src)

    # 等待元素可见
    def sy_is_visibility(self, loc):
        '''
        元素可见，返回本身，不可见返回 False
        '''

        try:
            loc = By.XPATH, "%s" % loc
            result = WebDriverWait(self.driver, self.timeout, self.frequency).until(
                EC.visibility_of_element_located(loc))
            return result
        except:
            return False

    # 等待所有元素存在
    def sy_is_presences(self, loc):
        '''
        所有元素均加载完成，返回本身，未加载 返回 False
        '''

        try:
            loc = By.XPATH, "%s" % loc
            result = WebDriverWait(self.driver, self.timeout, self.frequency).until(
                EC.presence_of_all_elements_located(loc))
            return result
        except:
            return False

    # 等待元素可点击
    def sy_is_clickable(self, loc):
        '''
        所有元素均加载完成，返回本身，未加载 返回 False
        '''

        try:
            loc = By.XPATH, "%s" % loc
            result = WebDriverWait(self.driver, self.timeout, self.frequency).until(EC.element_to_be_clickable(loc))
            return result
        except:
            return False

    # 重写click方法
    def sy_click(self, loc: object, bol: object = True):
        """
        动作：1.点击loc
        """
        self.sy_find_element(loc, bol).click()

    # 根据索引去点击元素的方法
    def sy_clicks(self, loc, index):
        """
        动作：1.点击loc 索引以1开始
        """
        try:
            self.sy_find_elements(loc)[index - 1].click()
        except AttributeError:
            pytest.fail("该用例执行失败，因为 %s 页面中未能找到 %s 元素" % (self, loc))

    def sy_clears(self, loc, index):
        """
        动作：1.点击loc 索引以1开始
        """
        try:
            self.sy_find_elements(loc)[index - 1].clear()
        except AttributeError:
            pytest.fail("该用例执行失败，因为 %s 页面中未能找到 %s 元素" % (self, loc))

    # 重写定义send_keys方法
    def sy_inputs(self, loc, value, index=1, clear_first=True, click_first=True):
        """
        动作：1.点击loc；2.清空loc；3.输入内容value
        """
        try:
            # loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.sy_clicks(loc, index)
            if clear_first:
                self.sy_clears(loc, index)
            # self.find_element(loc).send_key(value)
            self.sy_find_elements(loc)[index - 1].send_keys(value)
        except AttributeError:
            time_str = time.strftime("%Y%m%d-%H%M%S")
            allure.attach(self.driver.get_screenshot_as_png(), name=f"fail_step_{time_str}",
                          attachment_type=AttachmentType.PNG)
            pytest.fail("该用例执行失败，因为 %s 页面中未能找到 %s 元素" % (self, loc))

    # 重写定义send_keys方法
    def sy_input1(self, loc, value,):
        """
        默认动作：1.点击loc；2.清空loc；3.输入内容value
        """
        try:

            self.sy_click(loc)
            self.sy_find_element(loc).send_keys(value)
            log.info("输入：%s " % value)
        except AttributeError:
            time_str = time.strftime("%Y%m%d-%H%M%S")
            allure.attach(self.driver.get_screenshot_as_png(), name=f"fail_step_{time_str}",
                          attachment_type=AttachmentType.PNG)
            pytest.fail("该用例执行失败，因为 %s 页面中未能找到 %s 元素" % (self, loc))


    def sy_input(self, loc, value, clear_first=True, click_first=True):
        """
        默认动作：1.点击loc；2.清空loc；3.输入内容value
        """
        try:

            # loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.sy_click(loc)
            if clear_first:
                self.sy_find_element(loc).clear()
            self.sy_find_element(loc).send_keys(value)
            log.info("输入：%s " % value)
        except AttributeError:
            time_str = time.strftime("%Y%m%d-%H%M%S")
            allure.attach(self.driver.get_screenshot_as_png(), name=f"fail_step_{time_str}",
                          attachment_type=AttachmentType.PNG)
            pytest.fail("该用例执行失败，因为 %s 页面中未能找到 %s 元素" % (self, loc))


    # 重写定义send_keys方法
    def sy_input_selects(self, loc, value, index, stime=1.5):
        """
        默认动作：1.点击loc；2.清空loc；3.输入内容value，4自动查询结果列表中含有【value】的span 索引  5.点击
        """
        self.sy_input(loc, value)
        time.sleep(stime)
        # loc = (By.XPATH, "(//span[contains(text(),'%s')])" % value)
        # static_loc = (By.XPATH, "(//span[contains(text(),'%s')])[%s]" % (value, index))
        # self.sy_clicks(loc, index)
        self.sy_click_spans(value, index)

    # 根据查询结果选择
    def sy_input_select(self, loc, value):
        """
        默认动作：1.输入内容后，自动查询结果列表中选中含有【value】的span
        """
        # self.sy_click(loc)
        self.sy_input(loc, value)
        time.sleep(1)
        self.sy_click_span(value)

    def sy_click_span(self, itemname, tag="span"):
        """
        默认动作：1.点击loc 索引
        """
        loc = "//%s[contains(text(),'%s')]" % (tag, itemname)
        self.sy_find_element(loc).click()

    def sy_click_title_span(self, itemname):
        """
        示例：选择一级二级三级商品类目
        """
        loc = "//span[@title='%s' and contains(text(),'%s')]" % (itemname, itemname)
        self.sy_find_element(loc).click()

        # 根据索引去点击元素的方法

    def sy_click_spans(self, itemname, index=1):
        """
        默认动作：1.点击loc 索引
        """
        loc = "//span[contains(text(),'%s')]" % itemname
        self.sy_clicks(loc, index)

    # 根据点击列表选择
    def sy_click_selects(self, loc, itemname, index=1):
        """
        默认动作：1.点击loc,选中含有【itemname】的span 索引
        """
        self.sy_click(loc)
        time.sleep(1)
        # loc = (By.XPATH, "//span[contains(text(),'%s')]" % itemname)
        self.sy_click_spans(itemname, index)

    # 根据点击列表选择
    def sy_click_select(self, loc, itemname, tag="span"):
        """
        默认动作：1.点击loc,选中含有【itemname】的span
        """
        self.sy_click(loc)
        time.sleep(0.5)
        self.sy_click_span(itemname, tag)

    # 根据点击列表选择
    def sy_click_select_date(self, loc, itemname, tag="span"):
        """
        默认动作：1.点击loc,选中含有【itemname】的span
        """
        self.sy_click(loc)
        time.sleep(0.5)
        self.sy_click_span(itemname, tag)

    # 根据单选按钮标签选择
    def sy_radio_select(self, itemname):
        """
        默认动作：1.选中 【itemname】标签前面的单选按钮
        """
        loc = "//span[contains(text(),'%s')]/preceding-sibling::span[1]" % itemname
        self.sy_click(loc)

    # 选择省份
    def sy_area_select(self, loc, itemname='全国'):
        self.sy_click(loc)
        time.sleep(0.5)
        loc = "//span[@title='%s']/preceding-sibling::span[1]" % itemname
        self.sy_click(loc)

    # 选择省份
    def sy_area_selects(self, loc, itemname='全国', index=1):
        self.sy_click(loc)
        time.sleep(0.5)
        loc = "//span[@title='%s']/preceding-sibling::span[1]" % itemname
        self.sy_clicks(loc, index)

    # # 根据查询结果选择
    # def search_txt(self, loc, itemname):
    #     """
    #     默认动作：返回
    #     dir 默认为空
    #     """
    #     static_loc = (By.XPATH, "//%s[contains(text(),'%s')]" % (loc, itemname))
    #     return self.is_element_present(static_loc)

    # 鼠标悬停

    def sy_double_click(self,loc):
        """
        鼠标双击操作
        """
        element = self.sy_find_element(loc)
        # 第一步：创建一个鼠标操作的对象
        action = ActionChains(self.driver)
        # 第二步：进行点击动作（事实上不会进行操作，只是添加一个点击的动作）
        action.double_click(element)
        # 第三步：执行动作
        action.perform()

    def sy_context_click(self,loc):
        """
        鼠标右击操作
        """
        element = self.sy_find_element(loc)
        # 第一步：创建一个鼠标操作的对象
        action = ActionChains(self.driver)
        # 第二步：进行点击动作（事实上不会进行操作，只是添加一个点击的动作）
        action.context_click(element)
        # 第三步：执行动作
        action.perform()

    def sy_move_element(self, loc):
        """
        默认动作：1.鼠标移动到loc
        """

        element = self.sy_find_element(loc)
        # 鼠标移到悬停元素上
        ActionChains(self.driver).move_to_element(element).perform()

    # def sy_drag_element2(self,source_loc,target_loc,type="By.XPATH"):
    #     """
    #     鼠标在一个元素loc1上拖动到另一个元素loc2上
    #     """
    #     time.sleep(1)
    #     if type=="By.XPATH":
    #         loc1 = By.XPATH, "%s" % source_loc
    #         loc2 = By.XPATH, "%s" % target_loc
    #     else:
    #         loc1 = By.CSS_SELECTOR, "%s" % source_loc
    #         loc2 = By.CSS_SELECTOR, "%s" % target_loc
    #     source = self.driver.find_element(*loc1)
    #     target = self.driver.find_element(*loc2)
    #     #获取屏幕缩放比率
    #     dpr = self.driver.execute_script('return window.devicePixelRatio')
    #     source_width = source.size.get('width')*dpr/2
    #     source_height = source.size.get('height')*dpr/2
    #
    #     target_width = target.size.get('width')*dpr/2
    #     target_height = target.size.get('height')*dpr/2
    #
    #     action = ActionChains(self.driver)
    #     action.drag_and_drop(source, target).perform()
        # source_position = self.sy_find_element(loc1)
        # target_position = self.sy_find_element(loc2)
        # action = ActionChains(self.driver)
        # self.sy_move_element(loc1)
        # source_position = WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located(loc1))
        # target_position = WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located(loc2))
        # ------------鼠标滑动操作------------
        # action.drag_and_drop(element,button).perform()
        # pyautogui.moveTo(source.location['x'] + 50, source.location['y'] + 18)
        # pyautogui.dragTo(target.location['x'] + 70, target.location['y'] + 15, duration=1)

    # def sy_drag_element3(self, s_x_pos,s_y_pos,t_x_pos,t_y_pos):
    #     """
    #     鼠标滑动操作,将元素移动到另一个元素中心位置，推荐使用 By.CSS_SELECTOR
    #     By.XPATH OR By.CSS_SELECTOR
    #     """
    #
    #     pyautogui.moveTo(s_x_pos, s_y_pos,tween=pyautogui.easeInOutQuad)
    #     # 开始拖动元素
    #     pyautogui.dragTo(t_x_pos, t_y_pos,tween=pyautogui.easeInOutQuad, duration=0.5, button='left')


    def sy_drag_element(self, source_loc,target_loc,y_pos,type="By.XPATH"):
        """
        鼠标滑动操作,将元素移动到另一个元素中心位置，推荐使用 By.CSS_SELECTOR
        type:By.XPATH OR By.CSS_SELECTOR
        y_pos：往下滚动量
        """
        #初始化浏览器位置
        self.driver.execute_script("var q=document.documentElement.scrollTop=0")
        time.sleep(0.5)
        if type=="By.XPATH":
            loc1 = By.XPATH, "%s" % source_loc
            loc2 = By.XPATH, "%s" % target_loc
        else:
            loc1 = By.CSS_SELECTOR, "%s" % source_loc
            loc2 = By.CSS_SELECTOR, "%s" % target_loc
        source = self.driver.find_element(*loc1)
        target = self.driver.find_element(*loc2)
        #滚动到合适的位置，方便元素拖拽

        time.sleep(0.5)
        # 获取屏幕缩放比率
        dpr = self.driver.execute_script('return window.devicePixelRatio')
        y_real_pos = y_pos / dpr
        self.driver.execute_script("var q=document.documentElement.scrollTop=%s" % y_real_pos)

        source_width  = source.size.get('width')/2
        source_height = source.size.get('height')/2

        target_width  = target.size.get('width')/2
        target_height = target.size.get('height')/2
        #获取浏览器导航头高度
        browser_nav_height = self.driver.execute_script('return window.outerHeight - window.innerHeight;')

        # 光标快速移动到元素位置
        pyautogui.moveTo((source.location['x']+source_width)*dpr, (source.location['y']+source_height+browser_nav_height)*dpr-y_pos, tween=pyautogui.easeInOutQuad)
        # pyautogui.moveTo((target.location['x']+target_width)*dpr, (target.location['y']+target_height+browser_nav_height)*dpr-y_pos, tween=pyautogui.easeInOutQuad)
        # 开始拖动元素
        pyautogui.dragTo((target.location['x']+target_width)*dpr, (target.location['y']+target_height+browser_nav_height)*dpr-y_pos,tween=pyautogui.easeInOutQuad, duration=0.5, button='left')






    # 点击后上传附件
    def sy_upload_file(self, loc, filename, dir=""):
        """
        默认动作：1.点击loc；2.上传dir下的文件filename
        dir 默认为空
        """
        self.sy_click(loc)
        time.sleep(1.5)
        uploadfile(filename, dir)
        time.sleep(2)

    def sy_get_col(self, loc, value):
        elements = self.sy_find_element(loc)
        for i in len(elements):
            loc2 = loc + "th[%s]" % i
            if value in self.sy_get_element_text(loc2):
                res = i
                break
        return res

    def sy_get_table_loc(self, loc1='//div[@class="source-item__list"]//form//table//thead[1]/tr[1]/th', value="品牌",
                         loc2='//div[@class="source-item__list"]//form//table//tbody[1]/tr[1]/td[%s]//input'):
        elements = self.driver.find_elements_by_xpath(loc1)

        for i in range(1, len(elements) + 1):
            loc = loc1 + "[%s]" % i
            if value in self.sy_get_element_text(loc):
                res = i
                break
        loc = loc2 % res
        return loc

    def get_path_from_json(self, menuitem="商品上下架2", user_type="cgs"):
        md = JsonPath()
        if user_type == "cgs":
            json_path = os.path.join(os.path.dirname(__file__), '..', 'environment', "cgs_menu.json")
        else:
            json_path = os.path.join(os.path.dirname(__file__), '..', 'environment', "gys_menu.json")
        with open(json_path, 'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            md.find_path_by_value(load_dict, menuitem)  #
        return md.list_path

    def sence_locators(self, sence):
        scene_loc = '//div[@id="header"]//a/div[@class="item" and contains(text(),"%s")]' % sence
        return scene_loc

    def cgs_menu_locators(self, menu):
        menu_loc = '//div[@class="memu-wrap"]//li/div[@class="el-submenu__title"]/span[@slot="title" and text()="%s"]' % menu
        return menu_loc

    def gys_menu_locators(self, menu):
        menu_loc = '//div[@class="sidebar-list"]//li/div[contains(text(),"%s")]' % menu
        return menu_loc

    def cgs_menuitem_locators(self, menuitem):
        menuitem_loc = '//ul[@class="el-menu el-menu--inline"]//li/a[text()="%s"]' % menuitem
        return menuitem_loc

    def gys_menuitem_locators(self, menuitem):
        menuitem_loc = '//ul[@class="el-menu el-menu--inline"]//li/span[text()="%s"]' % menuitem
        return menuitem_loc

    def sy_click_scene_menu(self, menuitem, user_type="cgs", is_expansion=True):
        """
        menuitem:菜单子项名称
        is_expansion：菜单项是否已经展开
        user_type:cgs-采购协同平台菜单，gys-供应协同平台菜单
        特别说明：只针对三级，场景，菜单，菜单子项目
        """
        res_list = self.get_path_from_json(menuitem, user_type)
        if len(res_list) == 1:
            menu = res_list[0].split(",")
            self.sy_click(self.sence_locators(menu[0]))
            time.sleep(2)
            if is_expansion != True:  # 如果没有展开，就点击菜单项目展开
                if user_type == "cgs":
                    self.sy_click(self.cgs_menu_locators(menu[1]))
                else:
                    self.sy_click(self.gys_menu_locators(menu[1]))
                time.sleep(2)
            if user_type == "cgs":
                self.sy_click(self.cgs_menuitem_locators(menu[2]))
            else:
                self.sy_click(self.gys_menuitem_locators(menu[2]))
            time.sleep(2)
        else:
            print("检索的菜单项存在重名情况！")

    def sy_screenshot(self):
        """
        Page页面截图函数
        特殊说明：只针对Page页面
        """
        time_str = get_timestamp()
        allure.attach(self.driver.get_screenshot_as_png(), name=f"screenshot_{time_str}",
                      attachment_type=AttachmentType.PNG)


    def sy_click_all_elements(self, loc):
        """
        连续点击loc 对应的元素
        :param elements_loc: 能够获取elements_list的loc
        :return:
        """
        elements = self.driver.find_elements_by_xpath(loc)
        for element in elements:
            element.click()



    def sy_click_in_all_elements(self, loc1,item_name,loc2):
        """
        从loc1对应的所有元素中匹配到 item_name ,点击对应的loc2
        """
        elements = self.sy_find_elements(loc1)
        for i in range(len(elements)):
            if elements[i].text == item_name:
                j=i+1
                target_loc= loc2 % j
                self.sy_click(target_loc)







