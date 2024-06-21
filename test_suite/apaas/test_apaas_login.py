import pytest
import allure
import time
import pytest
from pages.apaas.apaas_page import ApaasPage
from environment.data import Data
from datetime import datetime

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
        # 记录日志信息
        log.info("进入 apaas 页面~")


