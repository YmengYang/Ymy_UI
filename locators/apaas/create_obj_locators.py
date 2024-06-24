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


class CreateObjLocators:
    apaas_loc = '//div[contains(text(),"aPaas")]'
    search_text_loc = '//input[@placeholder="请输入，支持模糊搜索"]'
    text_span_loc = '//span[text()="apaas测试租户"]'
    search_loc = '//span[contains(text(),"查询")]'
    sys_config_loc = '//table/tbody/tr[1]//a[contains(text(),"系统配置")]'
    new_object_loc = '//span[contains(text(),"新建-租户")]'
    obj_name_loc = '//label[contains(text(),"对象名称")]/following-sibling::div//input'
    obj_describe_loc = '//textarea[@placeholder="请输入对象描述，300字以内"]'
    obj_icon_loc = '//label[contains(text(),"对象icon:")]/following-sibling::div//span[1]'
    next_loc = '//span[contains(text(),"下一步")]'
    main_field_name_loc = '//span[contains(text(),"字段名称")]/../following-sibling::div//input'
    main_field_apiName_loc = '//label[contains(text(),"字段API Name")]/following-sibling::div//input'
    min_loc = '//label[contains(text(),"限制字数")]/../../following-sibling::div//input'
    max_loc = '//label[contains(text(),"限制字数")]/../../following-sibling::div[3]//input'
    input_text_loc = '//label[contains(text(),"输入框提示")]/following-sibling::div//input'
    point_text_loc = '//label[contains(text(),"叹号提示")]/following-sibling::div//input'

    # 字段类型loc
    single_text_loc = '//li[contains(text(),"单行文本")]'
    group_loc = '//li[contains(text(),"分组")]'

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

    # 字段通用配置
    field_name_loc = '//label[contains(text(),"字段名称")]/following-sibling::div//input'
    field_api_name_loc = '//label/span[contains(text(),"API Name")]/../following-sibling::div//input'
    field_min_loc = '//label[contains(text(),"最小长度")]/following-sibling::div//input'
    field_max_loc = '//label[contains(text(),"最大长度")]/following-sibling::div//input'
    # input_text_loc = '//label[contains(text(),"输入框提示")]/following-sibling::div//input'
    # point_text_loc = '//label[contains(text(),"叹号提示")]/following-sibling::div//input'

    # 系统预置字段
    system_locs = '//div[@class="detail-content"]//div[@class="pass-group-content syue-clr"]/span//div[@class="field-name"]'
    main_field_loc = '//div[@data-name="单行文本"]//div[@class="design-default-component"]'
    # system_group_loc = '//div[@class="group-item"]//span[contains(text(), "系统信息")]/parent::h3//parent::div/following-sibling::div'
    # 分组
    group_edit_loc = '//div[@class="group-item"]//span[contains(text(),"分组")]/../following-sibling::div//span[@class="group-edit"]/i'
    group_name_loc = '//label[contains(text(),"分组名称")]/following-sibling::div//input'
    group_api_name_loc = '//label[@for="apiName"]/following-sibling::div//input'
    group_div_loc = '//div[@class="group-item"]//span[contains(text(), "分组")]/parent::h3//parent::div/following-sibling::div'
    # 辅助类按钮
    roll_loc = '.sy-group-table .el-scrollbar__wrap'
    save_loc = '//span[contains(text(),"保存")]'
    comfirm_loc = '//span[contains(text(),"确 定")]'
    return_loc = '//span[contains(text(),"返回列表页")]'
    enable_loc = '//h1[@class="basic-title syue-clr"]//span[contains(text(),"启用")]'

    # 对象列表
    search_obj_loc = '//input[@placeholder="请输入对象名称"]'
    total_loc = '//span[@class="el-pagination__total"]'

    a_loc='(//div[@data-name="单行文本"])[2]'
    b_loc='//div[@class="group-item"]//span[contains(text(), "分组")]/parent::h3//parent::div/following-sibling::div'