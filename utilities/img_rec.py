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

class ImgRec(object):

    def __init__(self):
        self.username = ''

        self.Token = ''

        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }
        self.img_id=''

    # 获取taken
    def get_taken(self, username="xiaopan", passord="sy@123"):
        brtn = False
        r = requests.get(
            'http://api.95man.com:8888/api/Http/UserTaken?user=' + username + '&pwd=' + passord + '&isref=0',
            headers=self.headers)
        arrstr = r.text.split('|')
        if (arrstr[0] == '1'):
            self.username = username
            self.Token = arrstr[1]
            brtn = True
        return brtn

    # 识别图片
    def post_img_rec(self, imgbyte, codetype=1):
        """
        imbyte: 图片字节
        imgtype: 类型 1为通用类型 更多精准类型请参考 http://fast.net885.com/auth/main.html
        """
        strRtn = ''
        # imbyte = open(filepath, 'rb').read()
        # filename = os.path.basename(filepath)
        filename="test.jpg"

        files = {'imgfile': (filename, imgbyte)}
        r = requests.post(
            'http://api.95man.com:8888/api/Http/Recog?Taken=' + self.Token + '&imgtype=' + str(codetype) + '&len=0',
            files=files, headers=self.headers)
        arrstr = r.text.split('|')
        # 返回格式：识别ID|识别结果|用户余额
        if (int(arrstr[0]) > 0):
            self.img_id=arrstr[0]
            strRtn = arrstr[1]

        return strRtn

    # 识别报错
    def report_error(self):
        """
        imageid:报错题目的图片ID
        """
        r = requests.get('http://api.95man.com:8888/api/Http/ReportErr?Taken=' + self.Token + '&ImgID=' + str(self.img_id),
                         headers=self.headers)
        arrstr = r.text.split('|')
        if (arrstr[0] == '1'):
            print('识别成功！')
        else:
            print('识别失败，错误信息：%s' % arrstr[1])


    def get_img_code_from_url(self,url,cookie_dict=""):
        #将dict形式的cookies转化为cookiesjar
        cookiejar = requests.utils.cookiejar_from_dict(cookie_dict)
        handler = urllib.request.HTTPCookieProcessor(cookiejar)
        opener = urllib.request.build_opener(handler)
        code=""
        while len(code) != 4:
            imgbyte = io.BytesIO(opener.open(url).read())
            code = self.post_img_rec(imgbyte)
        return code

if __name__ == '__main__':

    # file = os.path.join(os.path.dirname(__file__), '..', 'resources', 'verification_code', '1.jpg')
    Ks95man = ImgRec()

    if Ks95man.get_taken():
        # 获取成功,taken获取一次就可以了，taken 生成后如果不用参数"isref=1"刷新，就一直不会变。如果写死在您的软件中，就要慎用"isref=1"，否则您之前写死的软件都要改taken。

        # 开始识别
        # 获取文件二进制流
        url="https://abc.sunyur.com/supplier/getImageVerifyCode?source=register&t=1621995292564"
        code=Ks95man.get_img_code_from_url(url)
        print('识别结果：' + code )

        # 识别报错
        Ks95man.report_error()


