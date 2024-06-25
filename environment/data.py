#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: data.py
# @Author: PGQ
# @E-mail: panguoqing.pgq@sunyur.com
# @Time: 3月 10, 2021
# ---
from utilities.utils import get_timestamp, get_offsetdate
import time
import random


#######存放不同环境取值相同的变量，或者变量变量取值不会影响流程的变量#######

class Data:
    v_houzhui = get_timestamp()
    v_rand = str(random.randint(15000000000, 15099999999))

    # 协议数据：
    protocol_no_ = "XYBH%s" % v_houzhui
    protocol_name_ = "协议名称%s" % v_houzhui
    start_date_ = get_offsetdate(-5)
    end_date_ = get_offsetdate(100)

    remark_ = "备注信息备注信息备注信息备注信息备注信息备注信息%s" % v_houzhui

    # 物料部分：
    product_code_ = "SKU%s" % v_houzhui  # 商品编码
    untax = "2.45"  # 未税价
    upperlimit1 = "5"  # 阶梯价 上限1
    untax1 = "2.54"  # 阶梯价 未税1
    upperlimit2 = "10"  # 阶梯价 上限2
    untax2 = "2.13"  # 阶梯价 未税2
    product_exp_ = "协议商品说明协议商品说明%s" % v_houzhui  # 协议商品说明

    # 运费规则
    free_shipping_price = "6.34"  # 包邮价
    shipping_price = "5.32"  # 未包邮价

    # 合同帽数据：
    limit_quota = "120000"  # 合同金额限制
    deadline_start_data = "2021-01-01"  # 合同有效期-开始
    deadline_end_data = "2021-12-12"  # 合同有效期-结束
    quota_limit = "11000"  # 限量
    quant_limit = "10000"  # 限额
    stock = "10000"  # 库存数量

    # 合同台账数据：
    contract_account_import_filename = "合同台账导入模板.xlsx"

    product_name_ = "GKL商品名称%s" % v_houzhui

    bar_code_ = v_houzhui
    category_code_ = "LMGKL%s" % v_houzhui
    category_name_ = "类目%s" % v_rand

    # 物料数据：
    material_code_ = "WLGKL%s" % v_houzhui
    material_name_ = "物料名称gkl%s" % v_houzhui
    material_desc_ = "物料描述%s" % v_houzhui

    tag_name_ = "自动化场景标签%s" % v_houzhui

    # 导入数据所在目录：
    import_dir = "import\\tmp"

    img_name = "jiating.jpg"
    file_name = "word.zip"
    scene_file_name = "changjing.png"

    cgs_url = "http://abc.sunyur.com/purchaser"
    gys_url = "http://abc.sunyur.com/supplier"
    mall_url = "http://abc.sunyur.com/mall"
    apaas_url ="http://eai.newdev.sunyur.com/#/member/login?url=%2F&isHashJump=true"

    apaas_user = "gaokailin.gkl@sunyur.com"
    apaas_password = "1234!qwer"
    cgs_user = "panguoqing"
    cgs_password = "12345abc"
    gys_user = "gyspgqtest001"
    gys_password = "pgqabd863"
    demand_user='wangyue'
    demand_password='wangyue#wy'

    cgscode = "GSBMpgqtest0912001"
    gyscode = "GSBMpgqtest0912001"
    cgycode = "G08001"

    # 协议数据：
    cgs = "自动化公司全称【勿动】"
    gys = "自动化供应商名称【勿动】"
    # 商务员
    cgy = "潘国庆"
    # 采购组织
    cgz = "自动化采购组名称【勿动】"
    cgzz = "自动化采购组织名称【勿动】"
    pay_way = "银行转账"
    # 标准固定价格协议 ，浮动折扣价格协议
    pricing_method = "标准固定价格协议"
    # 物资类型： 普通物资， 领用物资
    material_type = "普通物资"
    # 运费类型： 供应商承担运费（包邮)， 自定义运费
    freight_type = "供应商承担运费（包邮)"

    mater_name = "自动化测试物料【勿动】"  # 物料名称
    mater_code = "wlbhpgqtest0912001"  # 物料编号
    mater_spec = "12x12"  # 物料规格
    mater_spec_ = "12X12_%s" % v_houzhui  # 物料规格2
    unit = "个"  # 物料单位
    tax = "13%"  # 税率
    moq = "1"  # 起订量
    # 运费规则
    freight_tax = "3%"  # 运费税率
    freight_area = "北京"  # 城市名称

    brand = "自动化测试品牌【勿动】"  # 品牌

    address = "自动化地点【勿动】"

    inventory_organization = "自动化库存组织【勿动】"

    # 物料数据：
    mater_one_catagary = "自动化一级物料分类【勿动】"
    mater_two_catagary = "自动化二级物料分类【勿动】"
    mater_three_catagary = "自动化三级物料分类【勿动】"

    # 商城类目
    # 物料类型：商城内部自用、外部系统对接
    mater_type = "商城内部自用"

    # 货到付款,#先款后货
    transaction_way = "货到付款"
    pay_type = "收货后"
    pay_day = "30天"

    protocol_total = "10000000"  # 协议总额
    # 发票类型：增值税专票，增值税普票
    invoice_type = "增值税专票"
    # 协议文本



    # 采购额上限
    amount = "1000"

    delivery = "25"  # 交货周期 25天

    sure_date = "一个月"  # 质保期

    ref_price = "1.23"  # 参考价
    market_price = "2.23"  # 市场价
    area = "全国"  # 送货区域

    contract_name = "自动化测试合同名称【勿动】"

    # 商城类目
    mall_one_catagary = "办公用品"
    mall_two_catagary = "办公设备"
    mall_three_catagary = "投影仪"

    # *************************************************************************************寻源
    gys_ = "供应商名称%s" % v_houzhui
    gys_code_ = "GYSZSUP%s" % v_rand  # 供应商社会信用代码
    phone_ = "%s" % v_rand
    RFQ_name_ = "询价单名称%s" % v_houzhui
    IFB_name_ = "招标单名称%s" % v_houzhui
    # phone_ ="15010141092"

    scene_name_ = "GKL场景%s" % v_houzhui

    # product_name = "测试商品名称210407053526"
    # product_code = "210407053526"

    ########商品比价用：
    strategy_name_ = "采购策略单名称%s" % v_houzhui

    ##领用商城用：
    company_name = '测试'
    business_unit_name = "自动化业务单元名称【勿动】"
    quote_template_name = "自动化测试报价模板【勿动】"

    # 申请单数据
    application_title_ = "申请单标题%s" % v_houzhui
    application_instructions_ = "采购申请说明%s" % v_houzhui
    user_department = "自动化子测试组织【勿动】"

    address_detail = "自动化测试收货地址【勿动】"
    distributor_apportionment_ratio = "10"
    material_property_fixed = "固定资产"
    material_property_stock = "存货"
    material_property_cost = "费用"
    cost_center = "自动化成本中心名称【勿动】"
    target_group = "自动化受益对象【勿动】"
    expense_type = "自动化费用类型【勿动】"
    expense_sub_type = "自动化子费用类型名称【勿动】"
    # budget_type = "部门预算"
    # accounting_subject = "存货"
    accounting_subject = "自动化核算科目名称【勿动】"
    expect_delivery_date = "2021/12/12"
    asset_code_ = "ZCBM%s" % v_houzhui
    purchase_description_ = "购买说明%s" % v_houzhui
    remarks_to_suppliers_ = "对供应商备注%s" % v_houzhui
    # 需求池
    dispatch_reason_ = "UI自动化分派原因说明%s" % v_houzhui
    close_reason_ = "UI自动化关闭原因说明%s" % v_houzhui

    # 预算编制结果数据
    budget_org_name = "部门预算"
    budget_pro_name = "项目预算"
    budget_per_name = "员工预算"
    budget_number_ = "YSH%s" % v_houzhui
    budget_name_ = "预算名称%s" % v_houzhui
    budget_period_start_ = get_offsetdate(365)
    budget_period_end_ = get_offsetdate(365)
    budget_line_code_ = "预算行号%s" % v_houzhui
    # budget_amount = "1000"
    budget_account = "UI预算科目名称【勿动】"
    budget_xunit_name = "UI_XM预算单元名称【勿动】"
    budget_zunit_name = "UI_ZZ预算单元名称【勿动】"

    # budget_number_search = "预算号20210413145020"
    # 预算单元数据
    budget_unit_code_ = "YSDYBM%s" % v_houzhui
    budget_unit_name_ = "预算单元名称%s" % v_houzhui
    budget_unit_remark_ = "预算单元备注%s" % v_houzhui

    # 报表
    report_name_ = "UI自动化报表%s" % v_rand
    role_name = "采购员"

    #-----公司主体
    company_full_name_ = "scm公司全称%s" % v_houzhui
    company_short_name_ = "scm公司简称%s" % v_houzhui
    company_code_ = "scm%s" % v_houzhui
    #税务登记号：18位数字
    tax_registration_code_ = v_houzhui
    tax_payer_type = "一般纳税人"
    #开户行
    bank_deposit = "建设银行"
    account_ = "scm账号%s" % v_houzhui

    ##公告数据
    notice_title = "UI自动化公告标题%s" % v_rand



    # apaas
    obj_name = "对象名称%s" % v_houzhui





