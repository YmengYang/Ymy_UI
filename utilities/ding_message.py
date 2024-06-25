#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: dingding_msg.py
# @Author: PGQ
# @E-mail: panguoqing.pgq@sunyur.com
# @Time: 5月 27, 2021
# ---
import requests, json
import os



class DingMessage:
    def __init__(self):
        d = {}
        # proDir = os.path.abspath(os.path.dirname((__file__)))
        # prometheus_data_file = "D:\\gitlab\\workspace\\abc_UI自动化\\target\\allure-report\\export\\prometheusData.txt"
        prometheus_data_file = "D:\\prometheusData.txt"
        report_url = "http://deploy.sunyur.com/view/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/job/abc_UI%E8%87%AA%E5%8A%A8%E5%8C%96/allure/"
        f = open(prometheus_data_file, 'r')
        for lines in f:
            for c in lines:
                launch_name = lines.strip('\n').split(' ')[0]
                num = lines.strip('\n').split(' ')[1]
                d.update({launch_name: num})
        f.close()
        retries_run = d.get('launch_retries_run')  # 运行总数
        status_passed = d.get('launch_status_passed')  # 通过数量
        status_failed = d.get('launch_status_failed')  # 不通过数量
        status_broken = d.get('launch_status_broken')  # 中断数量
        '''
        钉钉推送
        '''
        self.content = "# UI自动化脚本执行完成！\n---\n> 运行用例总数：%s    通过用例数量：%s  \n> 失败用例数量：%s    中断用例数量：%s\n---\n#### [>>>报告地址<<<](%s)" % (retries_run, status_passed, status_failed, status_broken, report_url)
        # self.content = "## UI自动化脚本执行完成！\n|用例总数|通过|失败|中断|\n|:---------:|:------:|:------:|:------:|\n|   %s   |  %s  |  %s  |  %s  |\n### [>>>报告地址<<<](%s)" % (
        # retries_run, status_passed, status_failed, status_broken, report_url)

    def sendsRtx(self):
        notice_mobile = ["15010141090", "17812182928"]
        # dingding_url = 'https://oapi.dingtalk.com/robot/send?access_token=5383292a3ba2dcbcfc74f2fd61ad5d83b5b82170d8e70fcdec68f4939f9c8f5f'
        dingding_url = 'https://oapi.dingtalk.com/robot/send?access_token=aab413ffc11a0c2f8ec482cf2e52811788cd315b393c2b4099fe97d7c6fdcdaa'
        data_headers = {
            'Content-Type': 'application/json',
            'Data_Type': 'msg'
        }
        data_json = {
            "msgtype": "markdown",
            "markdown": {
                "title": "UI自动化报告",
                "text": self.content
            },
            "at": {
                "atMobiles": notice_mobile
                ,
                "atDingtalkIds": [
                    ""
                ],
                "isAtAll": "false"
            }
        }

        res = requests.post(dingding_url, data=json.dumps(data_json), headers=data_headers)
        print(res.text)


if __name__ == '__main__':
    m = DingMessage()
    m.sendsRtx()
