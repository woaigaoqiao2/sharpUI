'''
Created on 2019年5月22日

纳入场所一括登录

@author: chinasoft.l.yu
'''
import unittest
from selenium import webdriver

from business.Companies.DeliveryOrdersBussinses import DeliveryOrdersBussinses
from business.Companies.API1234 import Jiekou
deliveryOrdersBussinses = DeliveryOrdersBussinses()

class TestOrdersCase(unittest.TestCase):


    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.url = "https://sharpsit.jusdaglobal.com"
        driver = self.driver
        driver.get(self.url)

    def tearDown(self):
        self.driver.quit()
    #   不选择数据时，点击纳入场所一括登录
    def testOpenWindowa(self):
        self._testMethodDoc = "纳入指示_    纳入场所一括登录_不输入数据时点击纳入场所一括登录"
        r = deliveryOrdersBussinses.openWindow(self.driver)
        assert r == False

    #   納入指示済时，点击纳入场所一括登录
    def testOpenWindowb(self):
        self._testMethodDoc = "纳入指示_纳入场所一括登录_纳入指示status为纳入指示剂时选择多条点击纳入场所一括登录"
        r = deliveryOrdersBussinses.openWindowb(self.driver)
        assert r == False

    def testOpenWindowe(self):
        self._testMethodDoc = "纳入指示_纳入场所一括登录_纳入指示status为纳入指示剂时选择一条点击纳入场所一括登录"
        r = deliveryOrdersBussinses.openWindowe(self.driver)
        assert r == False

    #   指示Mail送信済时，点击納入場所一括登録
    def testOpenWindowc(self):
        self._testMethodDoc = "纳入指示_纳入场所一括登录_纳入指示status为指示Mail送信済时选择多条点击纳入场所一括登录"
        r = deliveryOrdersBussinses.openWindowc(self.driver)
        assert r == "success"

    def testOpenWindowd(self):
        self._testMethodDoc = "纳入指示_纳入场所一括登录_纳入指示status为指示Mail送信済时选择一条点击纳入场所一括登录"
        r = deliveryOrdersBussinses.openWindowd(self.driver)
        assert r == "success"

    #   指示Mail送信済时，纳入场所、纳入予定时间、时间为空时，点击追加  #需要符合条件的D/O NO参数
    def testOpenWindowDoa(self):
        self._testMethodDoc = "纳入指示_追加_纳入指示status指示Mail送信済时，纳入场所、纳入予定时间、时间为空时，点击追加"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        r = deliveryOrdersBussinses.openWindowDo(self.driver,doNum.get("result"))
        assert r == False

    #   指示Mail送信済时，纳入场所、纳入予定时间不为空时、时间为空，点击追加 #需要符合条件的D/O NO参数
    def testOpenWindowDob(self):
        self._testMethodDoc = "纳入指示_追加_纳入指示status指示Mail送信済时，纳入场所、纳入予定时间不为空时、时间为空时，点击追加"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        r = deliveryOrdersBussinses.openWindowDob(self.driver,doNum.get("result"))
        assert r == False

    #   指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间输入值大于2359时，点击追加#需要符合条件的D/O NO参数
    def testOpenWindowDoc(self):
        self._testMethodDoc = "纳入指示_追加_指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间输入值大于2359时，点击追加"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:"+doNum.get("result"))
            assert doNum.get("result") == False
        time = 2360
        r = deliveryOrdersBussinses.openWindowDoc(self.driver,doNum.get("result"),time,self._testMethodDoc)
        assert r == False

    #   指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间输入值特殊字符时，点击追加#需要符合条件的D/O NO参数
    def testOpenWindowDod(self):
        self._testMethodDoc = "纳入指示_追加_指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间输入值特殊字符时，点击追加"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        #doNum = "19S0000198"    #19S0000198
        time = "#$#%$5"
        r = deliveryOrdersBussinses.openWindowDoc(self.driver,doNum.get("result"),time,self._testMethodDoc)
        assert r == False

    #   指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间输入值中文字符时，点击追加#需要符合条件的D/O NO参数
    def testOpenWindowDoe(self):
        self._testMethodDoc = "纳入指示_追加_指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间输入值中文字符时，点击追加"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        #doNum = "19S0000198"    #19S0000198
        time = "啊啊啊啊啊"
        r = deliveryOrdersBussinses.openWindowDoc(self.driver,doNum.get("result"),time,self._testMethodDoc)
        assert r == False

    #   指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间输入值长度小于4时，点击追加#需要符合条件的D/O NO参数
    def testOpenWindowDof(self):
        self._testMethodDoc = "纳入指示_追加_指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间输入值长度小于4时，点击追加"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        #doNum = "19S0000198"    #19S0000198
        time = "123"
        r = deliveryOrdersBussinses.openWindowDoc(self.driver,doNum.get("result"),time,self._testMethodDoc)
        assert r == False

    #   指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间输入值长度大于4时，点击追加#需要符合条件的D/O NO参数
    def testOpenWindowDog(self):
        self._testMethodDoc = "纳入指示_追加_指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间输入值长度大于4时，点击追加"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        #doNum = "19S0000198"    #19S0000198
        time = "12334"
        r = deliveryOrdersBussinses.openWindowDoc(self.driver,doNum.get("result"),time,self._testMethodDoc)
        assert r == False

    #   指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间不为空时，点击追加#需要符合条件的D/O NO参数
    def testOpenWindowDoh(self):
        self._testMethodDoc = "纳入指示_追加_指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间不为空时，点击追加"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        #doNum = "19S0000198"    #19S0000198
        time = "1233"
        r = deliveryOrdersBussinses.openWindowDod(self.driver,doNum.get("result"),time,self._testMethodDoc)
        assert r == True

    #   指示Mail送信済时，纳入场所、纳入予定时间、时间不为空时，注释为数字时，点击追加#需要符合条件的D/O NO参数，
    def testOpenWindowDoi(self):
        self._testMethodDoc = "纳入指示_追加_指示Mail送信済时，纳入场所、纳入予定时间已填写值、时间不为空时，点击追加"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        #doNum = "19S0000198"  # 19S0000198
        time = "1233"
        desc='2568744478'
        r = deliveryOrdersBussinses.openWindowDoe(self.driver, doNum.get("result"), time, desc,self._testMethodDoc)
        assert r == True

    #   指示Mail送信済时，纳入场所、纳入予定时间、时间不为空时，注释为特殊字符时，点击追加#需要符合条件的D/O NO参数，
    def testOpenWindowDoj(self):
        self._testMethodDoc = "纳入指示_追加_指示Mail送信済时，注释为特殊字符时,纳入场所、纳入予定时间已填写值、时间不为空时，点击追加"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == True
        #doNum = "19S0000198"  # 19S0000198
        time = "1233"
        desc = '#￥%%*&'
        r = deliveryOrdersBussinses.openWindowDoe(self.driver, doNum.get("result"), time, desc,self._testMethodDoc)
        assert r == True
#   指示Mail送信済时，纳入场所、纳入予定时间、时间不为空时，注释为中文字符时，点击追加#需要符合条件的D/O NO参数，
    def testOpenWindowDok(self):
        self._testMethodDoc = "纳入指示_追加_指示Mail送信済时，注释为中文字符时，纳入场所、纳入予定时间已填写值、时间不为空时，点击追加"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        #doNum = "19S0000198"  # 19S0000198
        time = "1233"
        desc = '注释中文字符测试'
        r = deliveryOrdersBussinses.openWindowDoe(self.driver, doNum.get("result"), time,desc, self._testMethodDoc)
        assert r == True