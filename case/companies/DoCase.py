"""
Created on 2019年6月24日

case操作类
@author: chinasoft.l.yu

"""

import unittest
from selenium import webdriver
from business.Companies.DoBussinsess import DoBussinsess

doBussinsess = DoBussinsess()
class DoCase(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.driver.set_script_timeout(20)
        self.url = "https://sharpsit.jusdaglobal.com"
        driver = self.driver
        driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    #   未选中数据时，点击纳入指示变更
    def testPracticala(self):
        self._testMethodDoc = "纳入指示变更_检索_未选中数据时，点击纳入指示变更"
        p = {}
        p['click'] = False
        p['end'] = True
        r = doBussinsess.practical(self.driver,self._testMethodDoc,**p)
        assert r == False

    #   选中多条数据时，点击纳入指示变更
    def testPracticalb(self):
        self._testMethodDoc = "纳入指示变更_检索_选中多条数据时，点击纳入指示变更"
        p = {}
        p['query'] = True
        p['checkData'] = "many"
        p['click'] = False
        p['end'] = True
        r = doBussinsess.practical(self.driver,self._testMethodDoc,**p)
        assert r == False

    #   指示Mail送信济时，点击纳入指示变更
    def testPracticalc(self):
        self._testMethodDoc = "纳入指示变更_检索_状态为指示Mail送信济时，点击纳入指示变更"
        p = {}
        p['query'] = True
        p['checkData'] = "many"
        p['click'] = False
        p['end'] = True
        p['status'] = "指示Mail送信済"
        r = doBussinsess.practical(self.driver,self._testMethodDoc,**p)
        assert r == False

    #   纳入指示剂时，点击纳入指示变更
    def testPracticald(self):
        self._testMethodDoc = "纳入指示变更_检索_状态为纳入指示剂时，点击纳入指示变更"
        p = {}
        p['doNo'] = "19S0000185"
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['end'] = True
        p['status'] = "納入指示済"
        r = doBussinsess.practical(self.driver,self._testMethodDoc,**p)
        assert r == "success"

    #   纳入指示剂时，纳入场所、纳入予顶日、受入定时间为空时，点击变更
    def testPracticale(self):
        self._testMethodDoc = "纳入指示变更_变更_状态为纳入指示剂时，纳入场所、纳入予顶日、受入定时间为空时，点击变更"
        p = {}
        p['doNo'] = "19S0000185"
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['status'] = "納入指示済"
        p['save'] = True
        r = doBussinsess.practical(self.driver,self._testMethodDoc,**p)
        assert r == "success"

    #   纳入指示剂时，纳入场所、纳入予定日不为空、时间值为空时，点击变更
    def testPracticalf(self):
        self._testMethodDoc = "纳入指示变更_变更_状态为纳入指示剂时，纳入场所、纳入予定日不为空、时间值为空时，点击变更"
        p = {}
        p['doNo'] = "19S0000185"
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['status'] = "納入指示済"
        p['input'] = True
        p['time'] = True
        p['save'] = True
        r = doBussinsess.practical(self.driver,self._testMethodDoc,**p)
        assert r == "success"

    #   纳入指示剂时，纳入场所、纳入予定时间不为空、时间输入值大于2359时，点击变更
    def testPracticalg(self):
        self._testMethodDoc = "纳入指示变更_变更_状态为纳入指示剂时，纳入场所、纳入予定时间不为空、时间输入值大于2359时，点击变更"
        p = {}
        p['doNo'] = "19S0000185"
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['status'] = "納入指示済"
        p['input'] = True
        p['time'] = True
        p['date'] = "2360"
        p['save'] = False
        r = doBussinsess.practical(self.driver,self._testMethodDoc,**p)
        assert r == False


    #   纳入指示剂时，纳入场所、纳入予定时间不为空、时间输入特殊符号时，点击变更
    def testPracticalh(self):
        self._testMethodDoc = "纳入指示变更_变更_状态为纳入指示剂时，纳入场所、纳入予定时间不为空、时间输入特殊符号时，点击变更"
        p = {}
        p['doNo'] = "19S0000185"
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['status'] = "納入指示済"
        p['input'] = True
        p['time'] = True
        p['date'] = "#$$%@"
        p['save'] = False
        r = doBussinsess.practical(self.driver,self._testMethodDoc,**p)
        assert r == False


    #   纳入指示剂时，纳入场所、纳入予定时间不为空、时间输入中文字符时，点击变更
    def testPracticalj(self):
        self._testMethodDoc = "纳入指示变更_变更_状态为纳入指示剂时，纳入场所、纳入予定时间不为空、时间输入中文字符时，点击变更"
        p = {}
        p['doNo'] = "19S0000185"
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['status'] = "納入指示済"
        p['input'] = True
        p['time'] = True
        p['date'] = "测试"
        p['save'] = False
        r = doBussinsess.practical(self.driver,self._testMethodDoc,**p)
        assert r == False

    #   纳入指示剂时，纳入场所、纳入予定时间不为空、时间输入字符长度大于4时，点击变更
    def testPracticalk(self):
        self._testMethodDoc = "纳入指示变更_变更_状态为纳入指示剂时，纳入场所、纳入予定时间不为空、时间输入字符长度大于4时，点击变更"
        p = {}
        p['doNo'] = "19S0000185"
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['status'] = "納入指示済"
        p['input'] = True
        p['time'] = True
        p['date'] = "测试2434"
        p['save'] = False
        r = doBussinsess.practical(self.driver,self._testMethodDoc,**p)
        assert r == False


    #   纳入指示剂时，纳入场所、纳入予定时间不为空、时间输入字符长度小于4时，点击变更
    def testPracticali(self):
        self._testMethodDoc = "纳入指示变更_变更_状态为纳入指示剂时，纳入场所、纳入予定时间不为空、时间输入字符长度小于4时，点击变更"
        p = {}
        p['doNo'] = "19S0000185"
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['status'] = "納入指示済"
        p['input'] = True
        p['time'] = True
        p['date'] = "测试4"
        p['save'] = False
        r = doBussinsess.practical(self.driver,self._testMethodDoc,**p)
        assert r == False


    #   纳入指示剂时，纳入场所、纳入予定时间、时间不为空时，点击变更
    def testPracticall(self):
        self._testMethodDoc = "纳入指示变更_变更_状态为纳入指示剂时，纳入指示剂时，纳入场所、纳入予定时间、时间不为空时，点击变更"
        p = {}
        p['doNo'] = "19S0000185"
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['status'] = "納入指示済"
        p['input'] = True
        p['time'] = True
        p['date'] = "1000"
        p['save'] = True
        r = doBussinsess.practical(self.driver,self._testMethodDoc,**p)
        assert r == "success"