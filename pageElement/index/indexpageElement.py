#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 12:57
# @Author  : 二部测试-陈兴川
# @File    : indexpageElement.py
#@email    :chenxingchuan@chinasoftinc.com
from selenium.webdriver.common.by import By
#登录后首页元素
class Index:
    #受入確認按钮
    acceptverify_button=(By.XPATH,'//div/div[text()="受入確認"]')