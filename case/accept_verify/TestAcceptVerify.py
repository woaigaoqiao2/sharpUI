#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 13:13
# @Author  : 二部测试-陈兴川
# @File    : TestAcceptVerify.py
#@email    :chenxingchuan@chinasoftinc.com

import unittest,os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from business.accept_verify.Accept_verify import AcceptVerify
from business.indexpage.Login import Login
from business.indexpage.index_page import IndexPage
from common.basepage import Basepage
import time
from ddt import ddt,data
from data.acceptverify_data import AcceptVerify_datas
from common.pl.CreateInvoice import CreateInvoice
from common.shippingAdvice.ShippingAdvice import ShippingAdvice
from common.companies.Companies import Companies
from common.deliveryDirector.DeliveryDirector import DeliveryDirector
from common.loggen import Logger

logger=Logger('TestAcceptVerify.py').getlog()
@ddt
class Test_AcceptVerify(unittest.TestCase,AcceptVerify):
    def setUp(self):
        # options=Options()
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        # options.add_argument('window-size=1920x3000')
        # options.add_argument("--disable-gpu")
        # options.add_argument("--disable-dev-shm-usage")
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url="https://sharpsit.jusdaglobal.com"
        self.driver.get(self.url)
        Basepage(self.driver)
        Login().test_click_login_btn(self.driver)
        logger.info("进行登录")
        self.wait_box()
        IndexPage(self.driver).click_accpet_verify()
        logger.info("点击受入确认")


    @data(*AcceptVerify_datas.containerno_data)
    def test1containerno(self,item):
         self._testMethodDoc = item['test_name']
         r=CreateInvoice().practical()
         if r.get("code")==200:
            b=r.get("invoiceNo")
         else:
            logger.error("创建测试数据失败：code={}".format(r.get("code")))
            return r
         r=ShippingAdvice().practical(b)
         if r.get("code")!=200:
            logger.error("绑定BL和NL失败：code={}".format(r.get("code")))
            return r
         r=DeliveryDirector().practical(blNo=b)
         if r.get("code")!=200:
            logger.error("送信失败：code={}".format(r.get("code")))
            return r
         r=Companies().practical(blNo=b)
         if r.get("code")!=200:
            logger.error("纳入指示失败：code={}".format(r.get("code")))
            return r
         else:
              item["no"]=b
              item["check"]=b
         logger.info("现在开始测试：{}".format(item['test_name']))
         self.input_container_no(item['no'])
         logger.info("输入集装箱号码:{}".format(item["no"]))
         self.click_search_buttom()
         logger.info("点击検索按钮")
         time.sleep(1)
         result=self.get_result()
         logger.info("获取查询到的结果{}".format(result))
         for i in result:
             if i[3]==item['check']:
                 b=True
             else:
                 b=False
                 break
         try:
             self.assertTrue(b)
             logger.info("测试用例：{}  测试通过".format(item['test_name']))
         except:
             logger.error("测试用例：{}  测试结果与预期结果不一致".format(item['test_name']))
             raise
    @data(*AcceptVerify_datas.sta)
    def test2eta(self,item):
        self._testMethodDoc = item['test_name']
        logger.info("现在开始测试：{}".format(item['test_name']))
        self.selectETA(item["etastart"],item["etaend"])
        logger.info("输入ETA起始时间：{}和ETA结束时间：{}".format(item["etastart"],item["etaend"]))
        self.click_search_buttom()
        time.sleep(1)
        result = self.get_result()
        logger.info("查询结果：{}".format(result))
        for i in result:
            d = time.strptime(i[8], "%Y-%m-%d")
            if item['etastart']!="null":
                etastarttime = time.strptime(item['etastart'], "%Y-%m-%d")
                if d >=etastarttime:
                    b = True
                else:
                    b = False
                    break
            else:
                b=True
            if item['etaend']!="null":
                etaendtime = time.strptime(item['etaend'], "%Y-%m-%d")
                if d <= etaendtime:
                    c = True
                else:
                    c = False
                    break
            else:
                c=True
            if b==True and c==True:
                b=True
        try:
            self.assertTrue(b)
            logger.info("测试用例：{}  测试通过".format(item['test_name']))
        except:
            logger.error("测试用例：{}  测试结果与预期结果不一致".format(item['test_name']))
            raise
    @data(*AcceptVerify_datas.etd)
    def test3etd(self, item):
        self._testMethodDoc = item['test_name']
        logger.info("现在开始测试：{}".format(item['test_name']))
        self.selectETD(item['etdstart'],item['etdend'])
        logger.info("输入ETD起始时间：{}和ETD结束时间：{}".format(item['etdstart'],item['etdend']))
        self.click_search_buttom()
        time.sleep(1)
        result = self.get_result()
        logger.info("查询结果：{}".format(result))
        for i in result:
            d = time.strptime(i[9], "%Y-%m-%d")
            if item["etdstart"]!="null":
                etdstarttime = time.strptime(item['etdstart'], "%Y-%m-%d")
                if d >= etdstarttime:
                    b = True
                else:
                    b = False
                    break
            else:
                b=True
            if item['etdend'] != "null":
                etaendtime = time.strptime(item['etdend'], "%Y-%m-%d")
                if d <= etaendtime:
                    c = True
                else:
                    c = False
                    break
            else:
                c = True
            if b == True and c == True:
                b = True
        try:
            self.assertTrue(b)
            logger.info("测试用例：{}  测试通过".format(item['test_name']))
        except:
            logger.error("测试用例：{}  测试结果与预期结果不一致".format(item['test_name']))
            raise

    def tearDown(self):
        self.driver.quit()






