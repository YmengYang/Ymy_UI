#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: category_locators.py
# @Author: PGQ
# @E-mail: panguoqing.pgq@sunyur.com
# @Time: 3月 10, 2021
# ---
from selenium.webdriver.common.by import By


class CreateFieldLocators:

    # 字段loc
    single_text_loc = '//li[contains(text(),"单行文本")]'

    # 字段通用配置
    field_name_loc = '//label[contains(text(),"字段名称")]/following-sibling::div//input'
    field_api_name_loc = '//label/span[contains(text(),"API Name")]/../following-sibling::div//input'
    min_loc = '//label[contains(text(),"最小长度")]/following-sibling::div//input'
    max_loc = '//label[contains(text(),"最大长度")]/following-sibling::div//input'
    input_text_loc = '//label[contains(text(),"输入框提示")]/following-sibling::div//input'
    point_text_loc = '//label[contains(text(),"叹号提示")]/following-sibling::div//input'


    multi_text_loc = '//li[contains(text(),"多行文本")]'
    auto_number_loc = '//li[contains(text(),"自增编号")]'
    auto_value_locs = '//label[text()="字段名称"]/following::div//input[@class="el-input__inner"]'
    single_value_loc = '//li[contains(text(),"单选")]'
    multi_value_loc = '//li[contains(text(),"多选")]'
    boolean_value_loc = '//li[contains(text(),"布尔值")]'
    number_loc = '//li[contains(text(),"数字")]'
    amount_loc = '//li[contains(text(),"金额")]'
    percent_loc = '//li[contains(text(),"百分数")]'
    date_loc = '//li[contains(text(),"日期")]'
    date_time_loc = '//li[contains(text(),"日期时间")]'
    start_ending_loc = '//li[contains(text(),"起止时间")]'
    address_loc = '//li[contains(text(),"地址字段")]'
    org_loc = '//li[contains(text(),"组织")]'
    preson_loc = '//li[contains(text(),"人员")]'
    area_loc = '//li[contains(text(),"行政区域")]'
    picture_loc = '//li[contains(text(),"图片")]'
    file_loc = '//li[contains(text(),"文件")]'

    # 创建对象时第一个组最后一个字段，默认是主属性字段
    # base_field_loc = 'div.el-col.el-col-12:nth-child(5) div.field-box div.el-form-item div.el-form-item__content > div.design-default-component'

    base_field_loc = '//div[@class="detail-content"]//div[@class="pass-group-content syue-clr"]/span/div[5]'
