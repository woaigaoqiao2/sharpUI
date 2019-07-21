#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 13:04
# @Author  : 二部测试-陈兴川
# @File    : index_page.py
#@email    :chenxingchuan@chinasoftinc.com

from pageElement.index.indexpageElement import Index
from common.basepage import Basepage

class IndexPage(Index,Basepage):

    def click_accpet_verify(self):
        self.click_element(self.acceptverify_button,'点击受入確認')