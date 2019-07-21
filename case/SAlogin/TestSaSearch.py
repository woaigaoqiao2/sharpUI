
"""
SA登録模块搜索
author:cjp
"""

import time
import unittest
from selenium import webdriver
from business.SAlogin.SaSearch import SaSearch
from business.Login import Login
from selenium.common.exceptions import TimeoutException

class TestSaSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(30)
        self.driver.maximize_window()
        self.url = "https://sharpsit.jusdaglobal.com"
        try:
            self.driver.get(self.url)
        except TimeoutException as e:
            self.driver.quit()
            self.driver.get(self.url)
        time.sleep(2)
        self.login = Login()
        self.login.test_click_login_btn(self.driver)
        time.sleep(5)
        self.driver.implicitly_wait(30)


    def test001ETATimeSearch(self):
        self._testMethodDoc = "根据ETA 时间段搜索数据"
        p = SaSearch(self.driver)
        actualresult=p.ETATimeSearch()
        self.assertNotEqual(actualresult,'No data available')


    def test002ETDTimeSearch(self):
        self._testMethodDoc = "根据ETD 结束日期搜索数据"
        p = SaSearch(self.driver)
        actualresult=p.ETDTimeEndSearch()
        self.assertNotEqual(actualresult,'No data available')


    def test003ETDStartSearch(self):
        self._testMethodDoc = "根据ETD开始日期搜索数据"
        p = SaSearch(self.driver)
        actualresult=p.ETDTimeStartSearch()
        self.assertNotEqual(actualresult,'No data available')



    def test004ETDStartEndSearch(self):
        self._testMethodDoc = "根据ETD开始结束日期搜索数据"
        p = SaSearch(self.driver)
        actualresult=p.ETDTimeStartEndSearch()
        self.assertNotEqual(actualresult,'No data available')


    def test005InvoiceNoSearch(self):
        self._testMethodDoc = "根据invoiceNo搜索数据"
        p = SaSearch(self.driver)
        actualresult=p.InvoiceNoSearch()
        self.assertNotEqual(actualresult,'No data available')


    def test006VolNO(self):
        self._testMethodDoc = "根据Vol NO搜索数据"
        p = SaSearch(self.driver)
        actualresult=p.VolNOSearch()
        self.assertNotEqual(actualresult,'No data available')


    def test007BenShipping(self):
        self._testMethodDoc = "根据本船名搜索数据"
        p = SaSearch(self.driver)
        actualresult = p.BenShipping()
        self.assertNotEqual(actualresult, 'No data available')


    def test008ShippingShe(self):
        self._testMethodDoc = "根据船社・航空会社搜索数据"
        p = SaSearch(self.driver)
        actualresult = p.ShippingSheSearch()
        self.assertNotEqual(actualresult, 'No data available')


    def test009HaiWaiQu(self):
        self._testMethodDoc = "根据海外取引先搜索数据"
        p = SaSearch(self.driver)
        actualresult = p.HaiWaiQu()
        self.assertNotEqual(actualresult, 'No data available')


    def test010ZheChu(self):
        self._testMethodDoc = "根据積出港搜索数据"
        p = SaSearch(self.driver)
        actualresult = p.ZheChu()
        self.assertNotEqual(actualresult, 'No data available')


    def test011LuYang(self):
        self._testMethodDoc = "根据陸揚港搜索数据"
        p = SaSearch(self.driver)
        actualresult = p.LuYang()
        self.assertNotEqual(actualresult, 'No data available')


    def test012XingTai(self):
        self._testMethodDoc = "根据輸送形態搜索数据"
        p = SaSearch(self.driver)
        actualresult = p.XingTai()
        self.assertNotEqual(actualresult, 'No data available')


    def test013YaiStartTime(self):
        self._testMethodDoc = "根据依賴开始日期搜索数据"
        p = SaSearch(self.driver)
        actualresult = p.YiLaiStart()
        self.assertNotEqual(actualresult, 'No data available')


    def test014YaiEndTime(self):
        self._testMethodDoc = "根据依賴结束搜索数据"
        p = SaSearch(self.driver)
        actualresult = p.YiLaiEnd()
        self.assertNotEqual(actualresult, 'No data available')


    def test015YaiStartEndTime(self):
        self._testMethodDoc = "根据依賴开始结束搜索数据"
        p = SaSearch(self.driver)
        actualresult = p.YiLaiStartEnd()
        self.assertNotEqual(actualresult, 'No data available')

    def tearDown(self):
        self.driver.quit()