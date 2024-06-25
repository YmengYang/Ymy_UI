# import pytest
# import allure
import time
import pytest
from pages.apaas.apaas_page import ApaasPage
from environment.data import Data
from datetime import datetime
from locators.apaas.apaas_locators import ApaasLocators as loc
from utilities.logger import Logger
log = Logger(__name__).getlog()


def timestamp():
    return datetime.now().strftime("%H%M%S")
# 定义测试类，包含 Apaas 登录相关的测试用例
class TestApaasLogin:
    # 定义 Apaas 页面的 URL
    apaas_url = Data.apaas_url

    @pytest.fixture(autouse=True)
    def load_url(self, driver_init, ):
        """
        该夹具在每个测试用例执行前执行

        1. 清除浏览器的所有 cookie
        2. 创建 ApaasPage 对象，并加载 Apaas 页面
        3. 进行 Apaas 登录操作
        4. 打开 Apaas 页面
        5. 记录日志信息

        :param driver_init: 一个 fixture，用于初始化浏览器驱动
        :return: 无
        """
        # 清除浏览器的所有 cookie
        self.driver.delete_all_cookies()
        # 创建 ApaasPage 对象
        self.ApaasPage = ApaasPage(self.driver, name="LoginPage")
        # 加载 Apaas 页面
        self.ApaasPage.load()
        # 进行 Apaas 登录操作
    def test_apaas_create(self):
        self.ApaasPage.apaas_login(Data.apaas_user, Data.apaas_password)
        # 打开 Apaas 页面
        object_name = "对象"+timestamp()
        self.ApaasPage.open_apaas(object_name)

        self.ApaasPage.page_create("采购商_编辑页"+timestamp(), loc.pur,loc.edit_page)
        self.ApaasPage.page_create("采购商_新建页"+timestamp(), loc.pur, loc.new_page)
        self.ApaasPage.page_create("采购商_详情页"+timestamp(), loc.pur, loc.detail_page)
        self.ApaasPage.page_create("供应商_编辑页"+timestamp(), loc.sup, loc.edit_page)
        self.ApaasPage.page_create("供应商_新建页"+timestamp(), loc.sup, loc.new_page)
        self.ApaasPage.page_create("供应商_详情页"+timestamp(), loc.sup, loc.detail_page)
        self.ApaasPage.page_create("需求端_新建页"+timestamp(), loc.mall, loc.new_page)
        self.ApaasPage.page_create("需求端_编辑页"+timestamp(), loc.mall, loc.edit_page)
        self.ApaasPage.page_create("需求端_详情页"+timestamp(), loc.mall, loc.detail_page)
        time.sleep(3)
        self.ApaasPage.create_single_field("单行文本"+timestamp())
        self.ApaasPage.single_choice("单选" + timestamp())
        self.ApaasPage.multiple_choice("多选"+timestamp())
        self.ApaasPage.oolean("布尔值" + timestamp())
        self.ApaasPage.num("数字" + timestamp())
        self.ApaasPage.find_association("查找关联" + timestamp())
        self.ApaasPage.list_create("自动化列表" + timestamp())
        self.ApaasPage.driver.quit()
        # 记录日志信息
        log.info("进入 apaas 页面~")


