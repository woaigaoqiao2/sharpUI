

"""

纳入场所指定

"""
import unittest

from selenium import webdriver
from business.Companies.API1234 import Jiekou
from business.Companies.SjlWarehouseBussinses import SjlWarehouseBussinses

sjlWarehouseBussinses = SjlWarehouseBussinses()
class SjlWarehouseCase(unittest.TestCase):


    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.url = "https://sharpsit.jusdaglobal.com"
        driver = self.driver
        driver.get(self.url)

    def tearDown(self):
        self.driver.quit()


    #   未选择数据时，点击纳入场所指定
    def testOpenWindowa(self):
        self._testMethodDoc = "纳入指示_纳入场所指定_未选择数据时，点击纳入场所指定"
        p = {}
        p['click'] = False
        p['end'] = True
        r = sjlWarehouseBussinses.openWindow(self.driver,self._testMethodDoc,**p)
        assert r == False

    #   选择多条数据时，点击纳入场所指定
    def testOpenWindowb(self):
        self._testMethodDoc = "纳入指示_纳入场所指定_选择多条数据时，点击纳入场所指定"
        p = {}
        p['query'] = True
        p['checkData'] = "many"
        p['click'] = False
        p['end'] = True
        r = sjlWarehouseBussinses.openWindow(self.driver,self._testMethodDoc,**p)
        assert r == False

    #   納入指示済时，点击纳入场所指定
    def testOpenWindowc(self):
        self._testMethodDoc = "纳入指示_纳入场所指定_納入指示Status为納入指示済时，点击纳入场所指定"
        p = {}
        p['status'] = "納入指示済"
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['end'] = True
        r = sjlWarehouseBussinses.openWindow(self.driver,self._testMethodDoc,**p)
        assert r == "success"

    #   指示Mail送信済时，点击纳入场所指定
    def testOpenWindowd(self):
        self._testMethodDoc = "纳入指示_纳入场所指定_納入指示Status为指示Mail送信済时，点击纳入场所指定"
        p = {}
        p['status'] = "指示Mail送信済"
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['end'] = True
        r = sjlWarehouseBussinses.openWindow(self.driver,self._testMethodDoc,**p)
        assert r == "success"

    #   指示Mail送信済时，SJL納入場所、最终纳入场所、纳入予定日、时间为空时，点击保存
    def testOpenWindowe(self):
        self._testMethodDoc = "纳入指示_纳入场所指定_納入指示Status为指示Mail送信済，" \
                              "SJL納入場所、最终纳入场所、纳入予定日、时间为空时，点击保存"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        dn=doNum.get("result")
        p = {}
        p['doNo'] = dn
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['save'] = False
        r = sjlWarehouseBussinses.openWindow(self.driver,self._testMethodDoc,**p)
        assert r == False

    #   指示Mail送信済时，SJL納入場所、最终纳入场所、纳入予定日不为空、时间为空时，点击保存
    def testOpenWindowf(self):
        self._testMethodDoc = "纳入指示_纳入场所指定_指示Mail送信済，SJL納入場所、最终纳入场所、纳入予定日不为空、时间为空时，点击保存"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        dn = doNum.get("result")
        p = {}
        p['doNo'] = dn
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['input'] = True
        p['date'] = True
        p['save'] = False
        r = sjlWarehouseBussinses.openWindow(self.driver,self._testMethodDoc,**p)
        assert r == False


    #   指示Mail送信済时，SJL納入場所、最终纳入场所、纳入予定日不为空、时间输入值大于2359时，点击保存
    def testOpenWindowg(self):
        self._testMethodDoc = "纳入指示_纳入场所指定_指示Mail送信済，SJL納入場所、最终纳入场所、纳入予定日不为空、时间输入值大于2359时，点击保存"
        doNum=Jiekou().getDONO()
        if(doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        dn = doNum.get("result")
        p = {}
        p['doNo'] = dn
        p['query'] = True
        p['checkData'] = "one"
        p['click'] = True
        p['input'] = True
        p['date'] = True
        p['time'] = "2400"
        p['save'] = False
        r = sjlWarehouseBussinses.openWindow(self.driver,self._testMethodDoc,**p)
        assert r == False