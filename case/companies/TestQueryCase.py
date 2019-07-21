'''
Created on 2019年5月22日

@author: chinasoft.l.yu
'''
import json
from time import sleep
import unittest
from selenium import webdriver
from business.Companies.QueryBussinses import QueryBussinses
from business.Companies.CompaniesRequest import CompaniesRequest
from business.Companies.API1234 import Jiekou

queryBussinses = QueryBussinses()
class TestQueryCase(unittest.TestCase):
    
    
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.url = "https://sharpsit.jusdaglobal.com"
        driver = self.driver
        driver.get(self.url)
        sleep(2)
        
    ##    根据条件查询不到数据
    def testcompaniesQueryNoData(self):
        self._testMethodDoc = "纳入指示-检索-对不存在的数据检索"
        no = "嗡嗡嗡呃"
        result = queryBussinses.companiesQueryNoData(self.driver,no)
        print("------------纳入指示-无数据查询--------------返回结果："+result)
        expectValue = "No data available"
        print("------------纳入指示-无数据查询--------------预期结果："+expectValue)
        assert result == expectValue

    ##    默认检索
    def testCompaniesQueryNoParams(self):
        self._testMethodDoc = "纳入指示-检索-默认检索"
        rParams = {}
        data = CompaniesRequest.queryDeliveryOrders(self, **rParams)
        r = json.loads(data.get("result"))
        if (data.get("code") != 200):
            print("------实际返回结果------:" + data.get("result"))
            assert '' == r.get("result")
        result = queryBussinses.companiesQueryNoParams(self.driver)
        if result > 0:
            result = r.get("totalElements")
        print("------------纳入指示-默认检索--------------实际结果：",result)

        expectValue = int(r.get("totalElements"))
        print("------------纳入指示-默认检索--------------预期结果：",expectValue)
        assert result == expectValue

    ##    根据D/O NO查询#需要符合条件的数据存在
    def testCompaniesQueryDO(self):
        self._testMethodDoc = "纳入指示-检索-根据D/O NO检索"
        no = "12"
        rParams = {}
        rParams['doNo'] = no
        data = CompaniesRequest.queryDeliveryOrders(self, **rParams)
        r = json.loads(data.get("result"))
        if (data.get("code") != 200):
            print("------实际返回结果------:" + data.get("result"))
            assert'' == r.get("result")
        result = queryBussinses.companiesQueryDO(self.driver,no,"纳入指示-检索-根据D/O NO检索")
        if result > 0:
            result = r.get("totalElements")
        print("------------纳入指示-根据D/O NO查询--------------实际结果：",result)

        expectValue = int(r.get("totalElements"))
        print("------------纳入指示-根据D/O NO查询--------------预期结果：",expectValue)
        assert result == expectValue

    ##    根据D/O NO模糊查询#需要符合条件的数据存在
    def testCompaniesQueryDOs(self):
        self._testMethodDoc = "纳入指示-检索-根据D/O 模糊检索"
        no = "12"
        rParams = {}
        rParams['doNo'] = no
        data = CompaniesRequest.queryDeliveryOrders(self, **rParams)
        r = json.loads(data.get("result"))
        if (data.get("code") != 200):
            print("------实际返回结果------:" + data.get("result"))
            assert '' == r.get("result")
        result = queryBussinses.companiesQueryDO(self.driver,no,"纳入指示-检索-根据D/O 模糊检索")
        if result > 0:
            result = r.get("totalElements")
        print("------------纳入指示-根据D/O NO查询--------------实际结果：",result)

        expectValue = int(r.get("totalElements"))
        print("------------纳入指示-根据D/O NO查询--------------预期结果：",expectValue)
        assert result == expectValue

    ##    根据B/L NO查询#需要符合条件的数据存在
    def testCompaniesQueryBL(self):
        self._testMethodDoc = "纳入指示-检索-根据B/L NO检索"
        no = "12"
        rParams = {}
        rParams['blNo'] = no
        data = CompaniesRequest.queryDeliveryOrders(self, **rParams)
        r = json.loads(data.get("result"))
        if (data.get('code') != 200):
            print("------实际返回结果------:" + data.get("result"))
            assert '' == r.get("result")
        result = queryBussinses.companiesQueryBL(self.driver,no,self._testMethodDoc)
        if result > 0:
            result = r.get("totalElements")
        print("------------纳入指示-根据B/L NO查询--------------实际结果：",result)

        expectValue = int(r.get('totalElements'))
        print("------------纳入指示-根据B/L NO查询--------------预期结果：",expectValue)
        assert result == expectValue

    ##    根据B/L NO模糊查询#需要符合条件的数据存在
    def testCompaniesQueryBLs(self):
        self._testMethodDoc = "纳入指示-检索-根据B/L NO模糊检索"
        no = "12"
        rParams = {}
        rParams['blNo'] = no
        data = CompaniesRequest.queryDeliveryOrders(self, **rParams)
        r = json.loads(data.get("result"))
        if (data.get('code') != 200):
            print("------实际返回结果------:" + data.get("result"))
            assert '' == r.get("result")
        result = queryBussinses.companiesQueryBL(self.driver,no,self._testMethodDoc)
        if result > 0:
            result = r.get("totalElements")
        print("------------纳入指示-根据B/L NO查询--------------实际结果：",result)

        expectValue = int(r.get('totalElements'))
        print("------------纳入指示-根据B/L NO查询--------------预期结果：",expectValue)
        assert result == expectValue

    ##    根据纳入指示查询
    def testCompaniesQueryOperateDirector(self):
        self._testMethodDoc = "纳入指示-检索-根据纳入指示者检索"
        rParams = {}
        rParams['operateDirectorId'] = "7d0d3acc-e54e-40e0-aafd-267a8d68d8bb"
        data = CompaniesRequest.queryDeliveryOrders(self, **rParams)
        r = json.loads(data.get("result"))
        if (data.get('code') != 200):
            print("------实际返回结果------:" + data.get("result"))
            assert '' == r.get("result")
        result = queryBussinses.companiesQueryOperateDirector(self.driver)
        if result > 0:
            result = r.get("totalElements")
        print("------------纳入指示-根据纳入指示者查询--------------实际结果：",result)

        expectValue = int(r.get("totalElements"))
        print("------------纳入指示-根据纳入指示者查询--------------预期结果：",expectValue)
        assert result == expectValue

    ##    根据海外取引先查询
    def testCompaniesQueryPartner(self):
        self._testMethodDoc = "纳入指示-检索-根据海外取引先检索"
        rParams = {}
        rParams['partnerId'] = "c265bfd3-52b2-4bbc-92ca-a5a860a32341"
        data = CompaniesRequest.queryDeliveryOrders(self, **rParams)
        r = json.loads(data.get("result"))
        if (data.get('code') != 200):
            print("------实际返回结果------:" + data.get("result"))
            assert '' == r.get("result")
        result = queryBussinses.companiesQueryPartner(self.driver)
        if result > 0:
            result = r.get("totalElements")
        print("------------纳入指示-根据海外取引先--------------返回结果：",result)
        expectValue = int(r.get("totalElements"))
        print("------------纳入指示-根据海外取引先--------------预期结果：",expectValue)
        assert result == expectValue

    ##    根据纳入指示status查询#需要接口
    def testCompaniesQueryShowStatus(self):
        self._testMethodDoc = "纳入指示-检索-根据纳入指示status检索"
        rParams = {}
        rParams['showStatus'] = "指示Mail送信済"
        data = CompaniesRequest.queryDeliveryOrders(self, **rParams)
        r = json.loads(data.get("result"))
        if (data.get("code") != 200):
            print("------实际返回结果------:" + data.get("result"))
            assert '' == r.get('result')
        expectValue = int(r.get("totalElements"))
        result = queryBussinses.companiesQueryShowStatus(self.driver)
        if result > 0:
            result = r.get("totalElements")
        print("------------纳入指示-根据纳入指示status查询--------------返回结果：",result)
        print("------------纳入指示-根据纳入指示status查询--------------预期结果：",expectValue)
        assert result == expectValue

    ##    根据D/O status 组合查询#需要符合条件的数据存在，需要接口
    def testCompaniesQueryParams(self):
        self._testMethodDoc = "纳入指示-检索-根据D/O status 组合检索"
        doNum = "19"
        rParams = {}
        rParams['doNo'] = doNum
        rParams['showStatus'] = "指示Mail送信済"
        data = CompaniesRequest.queryDeliveryOrders(self, **rParams)
        r = json.loads(data.get("result"))
        if (data.get('code') != 200):
            print("------实际返回结果------:" + data.get("result"))
            assert '' == r.get("result")
        result = queryBussinses.companiesQueryParams(self.driver,doNum)
        if result > 0:
            result = r.get("totalElements")
        print("------------根据D/O status 组合查询--------------返回结果：",result)
        expectValue = int(r.get("totalElements"))
        print("------------纳入指示-根据纳入指示status查询--------------预期结果：", expectValue)
        assert result == expectValue
          
    #需要符合条件的D/O NO参数
    def testDetailStatusz(self):
        self._testMethodDoc = "纳入指示-点击B/L详细-状态为指示送信济时，点击详细，详细字段为空点击保存"
        result = Jiekou().getDONO()
        if (result.get("code") != 200):
            print("------实际返回结果------:" + result.get("result"))
            assert result.get("result") == "success"
        doNum = result.get("result")
        r = queryBussinses.detailStatusz(self.driver, doNum)
        assert r == "success"

    # 需要符合条件的D/O NO参数
    def testDetailStatuszy(self):
        self._testMethodDoc = "纳入指示-点击B/L详细-状态为指示送信济时，点击详细，详细字段为英文点击保存"
        result = Jiekou().getDONO()
        if (result.get("code") != 200):
            print("------实际返回结果------:" + result.get("result"))
            assert result.get("result") == "success"
        doNum = result.get("result")
        r = queryBussinses.detailStatuszy(self.driver,doNum)
        assert r == "success"

    # 需要符合条件的D/O NO参数
    def testDetailStatuszz(self):
        self._testMethodDoc = "纳入指示-点击B/L详细-状态为指示送信济时，点击详细，详细字段为中文点击保存"
        result = Jiekou().getDONO()
        if (result.get("code") != 200):
            print("------实际返回结果------:" + result.get("result"))
            assert result.get("result") == "success"
        doNum = result.get("result")
        r = queryBussinses.detailStatuszz(self.driver,doNum)
        assert r == "success"

    # 需要符合条件的D/O NO参数
    def testDetailStatuszt(self):
        self._testMethodDoc = "纳入指示-点击B/L详细-状态为指示送信济时，点击详细，详细字段为特殊符号点击保存"
        result = Jiekou().getDONO()
        if (result.get("code") != 200):
            print("------实际返回结果------:" + result.get("result"))
            assert result.get("result") == "success"
        doNum = result.get("result")
        r = queryBussinses.detailStatuszt(self.driver,doNum)
        assert r == "success"
    # 需要符合条件的D/O NO参数
    def testDetailStatusn(self):
        self._testMethodDoc = "纳入指示-点击B/L详细-状态为纳入指示济时，点击详细，详细字段为空点击保存"
        r = queryBussinses.detailStatusn(self.driver,"19S0000113")
        assert r == True

    # 需要符合条件的D/O NO参数
    def testDetailStatusnt(self):
        self._testMethodDoc = "纳入指示-点击B/L详细-状态为纳入指示济时，点击详细，详细字段特殊符号点击保存"
        r = queryBussinses.detailStatusnt(self.driver,"19S0000113")
        assert r == True

    # 需要符合条件的D/O NO参数
    def testDetailStatusnz(self):
        self._testMethodDoc = "纳入指示-点击B/L详细-状态为状态为纳入指示济时，点击详细，详细字段为中文点击保存"
        r = queryBussinses.detailStatusnz(self.driver,"19S0000113")
        assert r == True    
    # 需要符合条件的D/O NO参数
    def testDetailStatuszc(self):
        self._testMethodDoc = "纳入指示-点击B/L详细-状态为指示Mail送信済时，点击详细，点击关闭"
        result = Jiekou().getDONO()
        if (result.get("code") != 200):
            print("------实际返回结果------:" + result.get("result"))
            assert result.get("result") == "success"
        doNum = result.get("result")
        r = queryBussinses.detailStatuszc(self.driver,doNum)
        assert r == "success"
    # 需要符合条件的D/O NO参数
    def testDetailStatusnc(self):
        self._testMethodDoc = "纳入指示-点击B/L详细-状态为纳入指示济时，点击详细，点击关闭"
        r = queryBussinses.detailStatusnc(self.driver,"19S0000245")
        assert r == "success"
    # 需要符合条件的D/O NO参数
    def tearDown(self):
        self.driver.quit()    