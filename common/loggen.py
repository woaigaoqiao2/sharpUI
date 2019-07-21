#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 9:51
# @Author  : 二部测试-陈兴川
# @File    : acceptverify.py
#@email    :chenxingchuan@chinasoftinc.com



import logging
import os,time

class Logger:
    def __init__(self,logger):
        self.logger=logging.getLogger(logger) #创建一个日志收集器
        self.logger.setLevel(logging.DEBUG)
        ch=logging.StreamHandler() #创建1个handler输出到控制台
        ch.setLevel(logging.INFO)
        log_path = os.path.abspath(__file__)
        log_path = os.path.split(log_path)[0]
        log_path=os.path.split(log_path)[0]+"\\logs\\"
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_name = log_path + rq + '.log' #创建日志文件
        fh=logging.FileHandler(log_name) #创建1个handler输出到输入日志文件
        fh.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

