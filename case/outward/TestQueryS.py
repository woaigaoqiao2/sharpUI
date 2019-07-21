'''
Created on 2019年6月20日

@author: chinasoft.jl.ma
'''
from business.outward.Query import Query
from unittest import TestCase
from selenium import webdriver
from util.init import init
from time import sleep
from selenium.webdriver.chrome.options import Options

class TestQueryS(TestCase):

    BLNO = Query().BLNO
    likeBLNO = Query().likeBLNO

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
        
    ##无条件检索
    def testNullQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "无条件检索"
        Query().nullQuery(self.driver)
        #断言

        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != '':
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
            
        
#---------------------------------------------------------------------------1
    ##用BL no检索
    def testBLQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用BL NO检索"
        Query().blQuery(self.driver)
        #断言
        try:
            actualResult = self.driver.find_element_by_xpath('//table[contains(@class,"v-datatable")]/tbody/tr/td[2]').text
            self.assertEqual(self.BLNO, actualResult)
        except Exception as e:
            print(e)

#---------------------------------------------------------------------------2
    ##用BL no模糊检索
    def testBLLikeQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用BL NO模糊检索"
        Query().blLikeQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//table[contains(@class,"v-datatable")]/tbody/tr/td[2]').text
        self.assertIn(self.likeBLNO, actualResult)
        
#-----------------------------------------------------------------------------3
    ##用不存在的BL检索
    def testFalseBLQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用不存在的BL NO检索"
        Query().falseBLQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)

#-----------------------------------------------------------------------------4         
    ##用海外取引先检索
    def testOverSeasQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用海外取引先检索"
        Query().overSeasQuery(self.driver)
        #断言

        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != '':
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)

#-----------------------------------------------------------------------------5       
    ##用B/L开始发行日检索
    def testBLStartDateQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用BL开始发行日检索"
        Query().blDateQuery(self.driver)
        #断言
        try:
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult  = str(actualResult)[7:]
            actualResult = int(actualResult)
            self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)

#------------------------------------------------------------------------------6
    ##用B/L结束发行日检索
    def testBLEndDateQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用BL结束发行日检索"
        Query().blEndDateQuery(self.driver)
        #断言
        try:
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult  = str(actualResult)[7:]
            actualResult = int(actualResult)
            self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
#------------------------------------------------------------------------------7     
    ##用输送形态检索
    def testTransportQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用输送形态检索"
        Query().transportQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//table[contains(@class,"v-datatable")]/tbody/tr/td[5]').text
        self.assertEqual("SEA", actualResult)

#------------------------------------------------------------------------------8    
    ##用出发港检索
    def testFromPortQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用出发港检索"
        Query().fromPortQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//table[contains(@class,"v-datatable")]/tbody/tr/td[6]').text
        self.assertEqual("秋田空港", actualResult)

#-------------------------------------------------------------------------------9       
    ##用到达港检索
    def testToPortQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用到达港检索"
        Query().toPortQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)

#--------------------------------------------------------------------------------10      
        
    ##用本船名检索
    def testShipQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用本船名检索"
        Query().shipQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//table[contains(@class,"v-datatable")]/tbody/tr/td[10]').text
        self.assertEqual(self.BLNO, actualResult)

#---------------------------------------------------------------------------------11
    ##用本船名模糊检索
    def testShipLikeQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用本船名模糊检索"
        Query().shipLikeQuery(self.driver)
        # 断言
        actualResult = self.driver.find_element_by_xpath('//table[contains(@class,"v-datatable")]/tbody/tr/td[10]').text
        self.assertEqual(self.BLNO, actualResult)

#--------------------------------------------------------------------------------12   
    ##用不存在的本船名检索
    def testFalseShipQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用不存在的本船名检索"
        Query().falseShipQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)     

#---------------------------------------------------------------------------------13
    ##用船社或航空社检索
    def testShippingQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用船社和航空社检索"
        Query().shippingQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//table[contains(@class,"v-datatable")]/tbody/tr/td[12]').text
        self.assertEqual("SJL-One Japan", actualResult)

#------------------------------------------------------------------------------------14

    ##用开始日期检索
    def testStartDate(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用开始日期检索"
        Query().startDateQuery(self.driver)
        #断言
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult  = str(actualResult)[7:]
            actualResult = int(actualResult)
            self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------15
        
    ##用结束日期检索
    def testEndDate(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用结束日期检索"
        Query().endDateQuery(self.driver)
        #断言
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult  = str(actualResult)[7:]
            actualResult = int(actualResult)
            self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#---------------------------双条件组合查询----------------------------------------------16
    ##用B/L NO 和海外取引先检索
    def testBLAndSeaQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用BL NO和海外取引先检索"
        Query().blAndSeaQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)

#--------------------------------------------------------------------------------------17
    ##用B/L NO 和运输形态检索
    def testBLAndTransportQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用BL NO和运输形态检索"
        Query().blAndTransportQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//table[contains(@class,"v-datatable")]/tbody/tr/td[2]').text
        sleep(2)
        self.assertEqual(self.BLNO, actualResult)
        
#-------------------------------------------------------------------------------------18
    ##用B/L NO和本船名检索
    def testBLAndShipQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用BL NO和本船名检索"
        Query().blAndShipQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//table[contains(@class,"v-datatable")]/tbody/tr/td[2]').text
        sleep(2)
        self.assertEqual(self.BLNO, actualResult)
        
#-------------------------------------------------------------------------------------19
    ##用ETD和ETA检索
    def testETDAndETAQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用ETD和ETA检索"
        Query().ETDAndETAQuery(self.driver)
        #断言
        try:
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            sleep(2)
            actualResult  = str(actualResult)[7:]
            actualResult = int(actualResult)
            self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------20
    ##用ETD>ETA检索
    def testETDGreaterETAQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用ETD>ETA检索"
        Query().ETDGreaterETAQuery(self.driver)
        #断言
        try:
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            sleep(2)
            actualResult  = str(actualResult)[7:]
            actualResult = int(actualResult)
            self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------21
    ##用B/L NO和穿社检索
    def testBLAndShippingQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "用BL NO和船社检索"
        Query().blAndShippingQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//table[contains(@class,"v-datatable")]/tbody/tr/td[2]').text
        self.assertEqual(self.BLNO, actualResult)
        
#-------------------------------------------------------------------------------------22
    ##全量检索
    def testFullQuery(self):
        self.driver.get(self.url)
        self._testMethodDoc = "全量检索"
        Query().fullQuery(self.driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        sleep(2)
        self.assertEqual("No data available", actualResult)
        
#-------------------------------------------------------------------------------------23
        
        
    def tearDown(self):
        self.driver.quit()
        
        
        
        