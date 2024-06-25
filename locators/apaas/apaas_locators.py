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


class ApaasLocators:

    apaas_login_user_loc = '//input[@placeholder="请输入账号"]'
    apaas_login_password_loc = '//input[@placeholder="请输入密码"]'
    apaas_button_loc = '//button/span[contains(text(),"登录")]'
    apaas_loc = '//div[contains(text(),"aPaas")]'
    apaas_creat = '//div/a[@href="#/paas/tenantlevel/object-create"]'

    #配置端页签元素
    field_loc = '//div[@id="tab-field"]'
    page_loc = '//div[@id="tab-page"]'
    list_loc = '//div[@id="tab-list"]'
    button_loc = '//div[@id="button"]'
    print_loc = '//div[@id="print"]'
    export_loc = '//div[@id="tab-import-export"]'
    language_loc = '//div[@id="tab-language"]'
    #创建对象
    object_name = '//input[@placeholder="请输入（10字以内）"]'
    next_loc = '//div[contains(text(),"下一步")]'
    main_field = '//input[@placeholder="请输入（20字以内）"]'
    main_field_type = '//input[@value="paas-autoNumber"]/.."]'
    single_text = '//span[contains(text(),"单行文本")]'
    save ='//div[contains(text(),"保存")]'
    select_object_name ='//input[@placeholder="请输入对象名称"]'
    list_object_name ='//tbody[@class="sy-table-tbody"]/tr[1]/td[1] //span'

    #创建字段
    multiline = '//div[@role="dialog"][@aria-label="新建字段"]//span[contains(text(),"多行文本")]'
    all_required = '//div[@role="dialog"][@aria-label="新建字段"]//span[contains(text(),"所有页面必填")]'
    #单选
    single_choice = '//div[@role="dialog"][@aria-label="新建字段"]//span[@class="fields-name"][contains(text(),"单选")]'
    value_type = '//div[@role="dialog"][@aria-label="新建字段"]//div[@class="value-type"]/div/div/div'     #数值类型设置

    #多选
    multiple_choice = '//div[@role="dialog"][@aria-label="新建字段"]//span[@class="fields-name"][contains(text(),"多选")]'

    #布尔值
    oolean = '//div[@role="dialog"][@aria-label="新建字段"]//span[@class="fields-name"][contains(text(),"布尔值")]'

    #数字
    num = '//div[@role="dialog"][@aria-label="新建字段"]//span[@class="fields-name"][contains(text(),"数字")]'
    red_mark = '//div[@role="dialog"][@aria-label="新建字段"]//form[1]/div[2]/div[1]/div[13]/div[2]/label[1]/span[1]/span[1]'

    #查找关联
    find_association = '//div[@role="dialog"][@aria-label="新建字段"]//span[@class="fields-name"][contains(text(),"查找关联")]'
    find_document = '//span[contains(text(),"请选择")]'
    b = '//div[@class="el-select__selected-item el-select__placeholder is-transparent"]//preceding-sibling::div/span'
    find = '//body/div[2]/div[6]//span[contains(text(),"对象104408")]'

    field_name = '//div[@role="dialog"]//input[@placeholder="请输入字段名称"]'
    create_field = '//div[@class="transition-wrap"]//div[@class="button-gallery-item"]/button'
    set_formula = '//div[@role="dialog"]//div[@class="sy-paas-config-button paas-config-button-normal el-tooltip__trigger el-tooltip__trigger"]'
    #公式中设置变量
    formula_name = '//div[@role="dialog"][@aria-label="公式设置"]//span[contains(text(),"名称")]'
    save_formula = '//div[@role="dialog"][@aria-label="公式设置"]//footer/button[@class="el-button el-button--primary el-button--mini"]'
    set_page_display = '//div[@role="dialog"][@aria-label="新建字段"]//thead/tr[1]/th[2]/div[1]/label[1]/span[1]/span[1]'
    save_field = '//div[@role="dialog"][@aria-label="新建字段"]//div[@class="right-footer"]//button[3]'

    #新建页面
    page_create = '//button[@class="el-button el-button--primary el-button--small"]'
    page_name_loc = '//div[@aria-label="新建页面"]//input[@placeholder="请输入页面名称，20个字符以内，示例：如销售订单详情页"]'
    select_app = '//div[@class="el-select__selected-item el-select__placeholder"]//span[contains(text(),"采购用户工作台")]'
    pc_terminal = '//div[@role="dialog"]//input[@value="PC"]/..'
    h5_terminal = '//div[@role="dialog"]//input[@value="PC"]/..'
    page_next = '//div[@role="dialog"]//button[@class="el-button el-button--primary"]'
    page_use = '//div[@role="dialog"]//span[contains(text(),"选择应用")]/../following-sibling::div'
    pur = '//body/div[2]/div[8]//span[contains(text(),"采购用户工作台")]'
    sup = '//body/div[2]/div[8]//span[contains(text(),"供应商工作台")]'
    mall = '//body/div[2]/div[8]//span[contains(text(),"需求用户工作台")]'

    page_type = '//div[@role="dialog"]//span[contains(text(),"页面分类")]/../following-sibling::div'
    edit_page = '//body/div[2]/div[9]//span[contains(text(),"编辑页")]'
    detail_page = '//body/div[2]/div[9]//span[contains(text(),"详情页")]'
    new_page = '//body/div[2]/div[9]//span[contains(text(),"新建页")]'

    #创建列表页面
    list_create = '//button[@class="el-button el-button--primary el-button--mini"]'
    list_name_loc = '//div[@aria-label="新建列表页"]//input[@placeholder="请输入列表名称"]'
    list_text= '//div[@aria-label="新建列表页"]//textarea[@class="el-textarea__inner"]'






