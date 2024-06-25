#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: logger.py
# @Author: PGQ
# @E-mail: panguoqing.pgq@sunyur.com
# @Time: 2月 26, 2021
# ---
import os
import logging
from concurrent_log_handler import ConcurrentRotatingFileHandler


class Logger(object):
    '''
封装后的logging
    '''

    def __init__(self, logger=None):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        log_file = os.path.join(os.path.dirname(__file__), '..', 'logs', 'test_log.log')
        # fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        # fh.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] %(message)s')

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(ch)

        # 定义handler的输出格式
        # formatter = logging.Formatter(
        #    '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')


        # 设置回滚文件
        # log_file_name_= "{}{}.log".format(log_file_name, "")
        rotating_file = ConcurrentRotatingFileHandler(log_file, "a", 512 * 1024, 10, encoding="utf8")
        rotating_file.setFormatter(formatter)
        self.logger.addHandler(rotating_file)

        #  添加下面一句，在记录日志之后移除句柄
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件
        rotating_file.close()
        # ch.close()

    def getlog(self):
        return self.logger
