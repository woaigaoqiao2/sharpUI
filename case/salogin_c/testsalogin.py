#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 13:35
# @Author  : 二部测试-陈兴川
# @File    : testsalogin.py
#@email    :chenxingchuan@chinasoftinc.com

import unittest,os
from time import sleep
from selenium import webdriver
from business.Login import Login
from common.Browser import Browser
from business.test_customs.HomePage import HomePage
from pageElement.SAlogin.HomePage import HomePageElement
from business.test_customs.ReferenceNewBuilding import ReferenceNewBuilding
from business.test_customs.NewlyBuild import NewlyBuild



class TestReferenceNewlyBuilt_c(unittest.TestCase):


    def setUp(self):
        # option = Options()
        # option.add_argument('----headless')
        # option.add_argument('--no-sandbox')
        # option.add_argument('window-size=1920x1080')
        # self.driver = webdriver.Chrome(chrome_options=option)
        self.driver = webdriver.Chrome()
        self.url = "https://sharpsit.jusdaglobal.com"
        # self.driver.implicitly_wait(15)
        # self.driver.set_page_load_timeout(15)
        # self.driver.set_script_timeout(15)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()


    def test_reference_newly_built01(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]用以前的海关数据，创建一条新的海关数据，且積出港与陸揚港不同"
        sleep(1.5)
        Login().test_click_login_btn(driver)
        sleep(5)
        bussiness = ReferenceNewBuilding()
        BL_No = bussiness.reference_newly_built01(driver)
        sleep(1.5)
        homepage = HomePage()
        homepage.BL_No_search(driver, BL_No)
        sleep(1.5)
        locate = HomePageElement()
        status_element = locate.locate_status(BL_No)
        sleep(1.5)
        actual_status = Browser(driver,10).get_text(status_element)
        self.assertEqual("SA一時保存",actual_status)

class TestShippingAdvice_c(unittest.TestCase):
    def setUp(self):
        # option = Options()
        # option.add_argument('----headless')
        # option.add_argument('--no-sandbox')
        # option.add_argument('window-size=1920x1080')
        # self.driver = webdriver.Chrome(chrome_options=option)
        self.driver = webdriver.Chrome()
        self.url = "https://sharpsit.jusdaglobal.com"
        # self.url = "https://sharpuat.jusdaglobal.com"
        # self.driver.implicitly_wait(15)
        # self.driver.set_page_load_timeout(15)
        # self.driver.set_script_timeout(15)
        # self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()


    def test_newly_built8(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]海关新建海运，填写必填项，送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = NewlyBuild()
        BL_No,tips = bussiness.newlyBuilt08(driver)
        sleep(1.5)
        homepage = HomePage()
        homepage.BL_No_search(driver, BL_No)
        sleep(1.5)
        locate = HomePageElement()
        status_element = locate.locate_status(BL_No)
        actual_status = Browser(driver,10).get_text(status_element)
        if "有償INVが無いと、SAを作成できません。" in tips:
            self.assertEqual("SA一時保存",actual_status)
        else:
            self.assertEqual("SA登録済",actual_status)


    def test_newly_built9(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]海关新建空运，填写必填项，送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = NewlyBuild()
        BL_No,tips = bussiness.newlyBuilt09(driver)
        sleep(1.5)
        homepage = HomePage()
        homepage.BL_No_search(driver, BL_No)
        sleep(1.5)
        locate = HomePageElement()
        status_element = locate.locate_status(BL_No)
        sleep(1.5)
        actual_status = Browser(driver,10).get_text(status_element)
        if "有償INVが無いと、SAを作成できません。" in tips:
            self.assertEqual("SA一時保存",actual_status)
        else:
            self.assertEqual("SA登録済",actual_status)


    def test_newly_built10(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]海关新建海运，送信时取消，查看状态是否变化"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = NewlyBuild()
        BL_No = bussiness.newlyBuilt10(driver)
        sleep(1.5)
        homepage = HomePage()
        homepage.BL_No_search(driver, BL_No)
        sleep(1.5)
        locate = HomePageElement()
        status_element = locate.locate_status(BL_No)
        sleep(1.5)
        actual_status = Browser(driver,10).get_text(status_element)
        self.assertEqual("SA一時保存",actual_status)


    def test_newly_built11(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]海关新建空运，送信时取消，查看状态是否变化"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = NewlyBuild()
        BL_No = bussiness.newlyBuilt11(driver)
        sleep(1.5)
        homepage = HomePage()
        homepage.BL_No_search(driver, BL_No)
        sleep(1.5)
        locate = HomePageElement()
        status_element = locate.locate_status(BL_No)
        sleep(1.5)
        actual_status = Browser(driver,10).get_text(status_element)
        self.assertEqual("SA一時保存",actual_status)
