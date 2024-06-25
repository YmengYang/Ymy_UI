#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: json_path.py
# @Author: PGQ
# @E-mail: panguoqing.pgq@sunyur.com
# @Time: 5月 31, 2021
# ---
import os, json


class JsonPath(object):
    def __init__(self):
        self.path_list = ""
        self.list_path = []

    def find_path_by_value(self, target, value):
        if isinstance(target, dict):
            for k, v in target.items():
                if str(value) in str(v):
                    if self.path_list == '':
                        self.path_list = k
                    else:
                        self.path_list = self.path_list + ',' + k
                    self.find_path_by_value(v, value)

        elif isinstance(target, (list, tuple)):  # 判断了它是列表
            for i in target:
                if str(value) in str(i):
                    self.find_path_by_value(i, value)

        elif isinstance(target, (str, int)):
            if str(value) == str(target):  # 必须完全相同
                path_list = self.path_list + ',' + str(value)
                self.list_path.append(path_list)
            else:
                index = self.path_list.rfind(",")
                self.path_list = self.path_list[0:index]


if __name__ == '__main__':
    md = JsonPath()

    json_path = os.path.join(os.path.dirname(__file__), '..', 'environment', "cgs_menu.json")
    menu_name = "预算编制结果"
    with open(json_path, 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
        md.find_path_by_value(load_dict, menu_name)  # 执行递归函数
        print(md.list_path)
