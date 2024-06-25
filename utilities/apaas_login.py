#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: img_rec.py.py
# @Author: PGQ
# @E-mail: panguoqing.pgq@sunyur.com
# @Time: 5月 25, 2021
# ---


import requests
import os
import time
import urllib.request
from io import StringIO
import io
import http.cookiejar

class ApaasLogin(object):

    def __init__(self):
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Host': 'uat.eai.sunyur.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        }

    # 获取taken
    def get_cookies(self):
        result = requests.Session()
        r = result.get(
            'http://uat.eai.sunyur.com/eai/login?jobNumber=MDAxMDU=',
            headers=self.headers)
        cookies = requests.utils.dict_from_cookiejar(result.cookies)
        dict_cookies={}
        for x, y in cookies.items():
            dict_cookies['name'] = str(x)
            dict_cookies['value'] = str(y)
        print(dict_cookies)
        return dict_cookies


if __name__ == '__main__':

    # file = os.path.join(os.path.dirname(__file__), '..', 'resources', 'verification_code', '1.jpg')
    man = ApaasLogin()

    if man.get_cookies():
        # 获取成功,taken获取一次就可以了，taken 生成后如果不用参数"isref=1"刷新，就一直不会变。如果写死在您的软件中，就要慎用"isref=1"，否则您之前写死的软件都要改taken。

        # 开始识别
        # 获取文件二进制流
        url="https://abc.sunyur.com/supplier/getImageVerifyCode?source=register&t=1621995292564"

        print('识别结果：' + url )


