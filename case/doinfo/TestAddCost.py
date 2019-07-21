'''
Created on 2019年7月4日

@author: chinasoft.jl.ma
'''
import unittest
from selenium import webdriver
from util.init import init
from business.doinfo.AddCostB import AddCostB
from pageElement.doinfo.AddCost import AddCost
from util.ElementUtil import ElementUtil
from selenium.webdriver.chrome.options import Options



class TestAddCost(unittest.TestCase,AddCost):


    def setUp(self):
        self.driver = webdriver.Chrome()

        # options = Options()
        # options.add_argument('window-size=1920x1080')
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # self.driver = webdriver.Chrome(chrome_options=options)

        self.url = "https://sharpsit.jusdaglobal.com/"
        init(self.driver)

    ##追加支払請求費用课税1
    def testAddTaxOne(self):
        driver = self.driver
        self._testMethodDoc = "追加支払請求費用课税1"
        driver.get(self.url)
        eu = ElementUtil()
        ac = AddCostB()
        ac.addTaxActionOne(driver)
        # #断言
        # #点击检索
        # eu.click(driver, 5, *self.selElement)
        # #选择数据
        # eu.click(driver, 5, *self.selDateElement)
        # #点击追加费用
        # eu.click(driver, 5, *self.addcostElement)
        # #取出实际结果
        # try:
        #     actualResult = driver.find_element(*self.taxactionOneElement).get_attribute('value')
        #     actualResult = int(actualResult)
        #     self.assertEqual(1000, actualResult)
        # except Exception as e:
        #     print(e)
        
#-------------------------------------------------------------------------------1
    
    ##追加支払請求費用课税2
    def testAddTaxTwo(self):
        driver = self.driver
        self._testMethodDoc = "追加支払請求費用课税2"
        driver.get(self.url)
        eu = ElementUtil()
        ac = AddCostB()
        ac.addTaxActionTwo(driver)
        # #断言
        # #点击检索
        # eu.click(driver, 5, *self.selElement)
        # #选择数据
        # eu.click(driver, 5, *self.selDateElement)
        # #点击追加费用
        # eu.click(driver, 5, *self.addcostElement)
        # #取出实际结果
        # actualResult = driver.find_element(*self.taxactionTwoElement).get_attribute('value')
        # actualResult = int(actualResult)
        # self.assertEqual(1000, actualResult)
        
#-------------------------------------------------------------------------------2
        
    ##追加支払請求費用课税3
    def testAddTaxThree(self):
        driver = self.driver
        self._testMethodDoc = "追加支払請求費用课税3"
        driver.get(self.url)
        eu = ElementUtil()
        ac = AddCostB()
        ac.addTaxActionThree(driver)
        # #断言
        # #点击检索
        # eu.click(driver, 5, *self.selElement)
        # #选择数据
        # eu.click(driver, 5, *self.selDateElement)
        # #点击追加费用
        # eu.click(driver, 5, *self.addcostElement)
        # #取出实际结果
        # try:
        #     actualResult = driver.find_element(*self.taxactionOneElement).get_attribute('value')
        #     actualResult = int(actualResult)
        #     self.assertEqual(1000, actualResult)
        # except Exception as e:
        #     print(e)
    
#-------------------------------------------------------------------------------3

    ##追加支払請求費用免税1  
    def testAddExemptionOne(self):
        driver = self.driver
        self._testMethodDoc = "追加支払請求費用免税1"
        driver.get(self.url)
        eu = ElementUtil()
        ac = AddCostB()
        ac.addExemptionOne(driver)
        #断言
        # #点击检索
        # eu.click(driver, 5, *self.selElement)
        # #选择数据
        # eu.click(driver, 5, *self.selDateElement)
        # #点击追加费用
        # eu.click(driver, 5, *self.addcostElement)
        # #取出实际结果
        # try:
        #     actualResult = driver.find_element(*self.taxactionOneElement).get_attribute('value')
        #     actualResult = int(actualResult)
        #     self.assertEqual(1000, actualResult)
        # except Exception as e:
        #     print(e)
        
#-------------------------------------------------------------------------------4
        
    ##追加支払請求費用免税2
    def testAddExemptionTwo(self):
        driver = self.driver
        self._testMethodDoc = "追加支払請求費用免税2"
        driver.get(self.url)
        eu = ElementUtil()
        ac = AddCostB()
        ac.addExemptionTwo(driver)
        #断言
        #点击检索
        # eu.click(driver, 5, *self.selElement)
        # #选择数据
        # eu.click(driver, 5, *self.selDateElement)
        # #点击追加费用
        # eu.click(driver, 5, *self.addcostElement)
        # #取出实际结果
        # try:
        #     actualResult = driver.find_element(*self.taxactionOneElement).get_attribute('value')
        #     actualResult = int(actualResult)
        #     self.assertEqual(1000, actualResult)
        # except Exception as e:
        #     print(e)
        
#-------------------------------------------------------------------------------5
        
    ##追加支払請求費用免税3
    def testAddExemptionThree(self):
        driver = self.driver
        self._testMethodDoc = "追加支払請求費用免税3"
        driver.get(self.url)
        eu = ElementUtil()
        ac = AddCostB()
        ac.addExemptionThree(driver)
        #断言
        #点击检索
        # eu.click(driver, 5, *self.selElement)
        # #选择数据
        # eu.click(driver, 5, *self.selDateElement)
        # #点击追加费用
        # eu.click(driver, 5, *self.addcostElement)
        # #取出实际结果
        # try:
        #     actualResult = driver.find_element(*self.taxactionOneElement).get_attribute('value')
        #     actualResult = int(actualResult)
        #     self.assertEqual(1000, actualResult)
        # except Exception as e:
        #     print(e)
        
#-------------------------------------------------------------------------------6
        
    ##追加請求课税1
    def testAddTaxTOne(self):
        driver = self.driver
        self._testMethodDoc = "追加請求课税1"
        driver.get(self.url)
        eu = ElementUtil()
        ac = AddCostB()
        ac.addTaxActionTOne(driver)
        #断言
        # #点击检索
        # eu.click(driver, 5, *self.selElement)
        # #选择数据
        # eu.click(driver, 5, *self.selDateElement)
        # #点击追加费用
        # eu.click(driver, 5, *self.addcostElement)
        # #取出实际结果
        # try:
        #     actualResult = driver.find_element(*self.taxactionOneElement).get_attribute('value')
        #     actualResult = int(actualResult)
        #     self.assertEqual(1000, actualResult)
        # except Exception as e:
        #     print(e)
        
#-------------------------------------------------------------------------------7
        
    ##追加請求课税2
    def testAddTaxTTwo(self):
        driver = self.driver
        self._testMethodDoc = "追加請求课税2"
        driver.get(self.url)
        eu = ElementUtil()
        ac = AddCostB()
        ac.addTaxActionTTwo(driver)
        #断言
        # #点击检索
        # eu.click(driver, 5, *self.selElement)
        # #选择数据
        # eu.click(driver, 5, *self.selDateElement)
        # #点击追加费用
        # eu.click(driver, 5, *self.addcostElement)
        # #取出实际结果
        # try:
        #     actualResult = driver.find_element(*self.taxactionOneElement).get_attribute('value')
        #     actualResult = int(actualResult)
        #     self.assertEqual(1000, actualResult)
        # except Exception as e:
        #     print(e)
        
#-------------------------------------------------------------------------------8
        
    ##追加請求免税1
    def testAddExemptionTOne(self):
        driver = self.driver
        self._testMethodDoc = "追加請求費用免税1"
        driver.get(self.url)
        eu = ElementUtil()
        ac = AddCostB()
        ac.addExemptionTOne(driver)
        #断言
        # #点击检索
        # eu.click(driver, 5, *self.selElement)
        # #选择数据
        # eu.click(driver, 5, *self.selDateElement)
        # #点击追加费用
        # eu.click(driver, 5, *self.addcostElement)
        # #取出实际结果
        # try:
        #     actualResult = driver.find_element(*self.taxactionOneElement).get_attribute('value')
        #     actualResult = int(actualResult)
        #     self.assertEqual(1000, actualResult)
        # except Exception as e:
        #     print(e)
        
#-------------------------------------------------------------------------------9
        
    ##追加請求免税2
    def testAddExemptionTTwo(self):
        driver = self.driver
        self._testMethodDoc = "追加請求費用免税2"
        driver.get(self.url)
        eu = ElementUtil()
        ac = AddCostB()
        ac.addExemptionTTwo(driver)
        # #断言
        # #点击检索
        # eu.click(driver, 5, *self.selElement)
        # #选择数据
        # eu.click(driver, 5, *self.selDateElement)
        # #点击追加费用
        # eu.click(driver, 5, *self.addcostElement)
        # #取出实际结果
        # try:
        #     actualResult = driver.find_element(*self.taxactionOneElement).get_attribute('value')
        #     actualResult = int(actualResult)
        #     self.assertEqual(1000, actualResult)
        # except Exception as e:
        #     print(e)
        
#-------------------------------------------------------------------------------10
    
    def tearDown(self):
        self.driver.quit()


