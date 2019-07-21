'''
Created on 2019年6月26日

@author: chinasoft.jl.ma
DO检索
'''
from unittest import TestCase
from selenium import webdriver
from util.init import init
from business.doinfo.QueryB import QueryB
from time import sleep


class TestQuery(TestCase):
    
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


    #纳入场所检索   数据不稳定
    def testInplaceQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据纳入场所检索"
        driver.get(self.url)
        QueryB().inPlaceQuery(driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)
        
#------------------------------------------------------------------------------------1
    
    #DONO检索
    def testDONoQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO检索"
        driver.get(self.url)
        QueryB().doNoQuery(driver)
        # 断言

        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#------------------------------------------------------------------------------------2

    #集装箱NO检索
    def testContainerNoQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据集装箱NO检索"
        driver.get(self.url)
        QueryB().containerNoQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#------------------------------------------------------------------------------------3

    #输送形态检索
    def testTransportQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据输送形态检索"
        driver.get(self.url)
        QueryB().transportQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)

#------------------------------------------------------------------------------------4

    #海外取引先检索
    def testOverSeaQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据海外取引先检索"
        driver.get(self.url)
        QueryB().overSeaQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
#------------------------------------------------------------------------------------5

    #到达港检索
    def testToportQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据到达港检索"
        driver.get(self.url)
        QueryB().toPortQuery(driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)
        
#------------------------------------------------------------------------------------6

    #开始时间检索
    def testStartDateQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据开始时间检索"
        driver.get(self.url)
        QueryB().startDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#------------------------------------------------------------------------------------7

    #结束时间检索
    def testEndDateQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据结束时间检索"
        driver.get(self.url)
        QueryB().endDateQuery(driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)
        
#------------------------------------------------------------------------------------8

    #B/L开始时间时间检索
    def testBLStartDateQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据BL开始时间检索"
        driver.get(self.url)
        QueryB().blStartDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#------------------------------------------------------------------------------------9

    #B/L结束时间时间检索
    def testBLEndDateQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据BL结束时间检索"
        driver.get(self.url)
        QueryB().blEndDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#------------------------------------------------------------------------------------10

    #根据担当者ID检索  数据不稳定
    def testActorIDQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据担当者检索"
        driver.get(self.url)
        QueryB().actorIDQuery(driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)
        
#------------------------------------------------------------------------------------11

    #根据状态检索
    def testStatusQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据状态检索"
        driver.get(self.url)
        QueryB().statusQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#--------------------------------------模糊检索---------------------------------------12

    #DONO模糊检索
    def testDONoLikeQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO模糊检索"
        driver.get(self.url)
        QueryB().doNoLikeQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
            
#------------------------------------------------------------------------------------13

    #集装箱NO模糊检索
    def testContainerNoLikeQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据集装箱NO 模糊检索"
        driver.get(self.url)
        QueryB().containerNoLikeQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#--------------------------------------异常场景---------------------------------------14

    #不存在的DONO检索
    def testDONoFalseQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据不存在的DO NO检索"
        driver.get(self.url)
        QueryB().doNoFalseQuery(driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)
        
#--------------------------------------异常场景---------------------------------------15

    #不存在的集装箱NO检索
    def testContainerNoFalseQuery(self):
        driver = self.driver
        self._testMethodDoc = "根据不存在的集装箱 NO检索"
        driver.get(self.url)
        QueryB().containerNoFalseQuery(driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)
        
#--------------------------------------全量检索---------------------------------------16

    #全量检索
    def testFullQuery(self):
        driver = self.driver
        self._testMethodDoc = "全量检索"
        driver.get(self.url)
        QueryB().fullQuery(driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)
        
#--------------------------------------组合检索---------------------------------------17

    #根据DO NO和集装箱NO检索
    def testDoNOAndcontainerNO(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO和集装箱NO检索"
        driver.get(self.url)
        QueryB().doNOAndContainerNoQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------18

    #根据DO NO和运输形态检索
    def testDoNOAndTransport(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO和运输状态检索"
        driver.get(self.url)
        QueryB().doNOAndTransportQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------19

    #根据DO NO和到达港检索
    def testDoNOAndToport(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO和到达港检索"
        driver.get(self.url)
        QueryB().doNOAndToportQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------20

    #根据DO NO和开始日期检索
    def testDoNOAndStartDate(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO和开始日期检索"
        driver.get(self.url)
        QueryB().doNOAndStartDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------21

    #根据DO NO和结束日期检索
    def testDoNOAndEndDate(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO和结束日期检索"
        driver.get(self.url)
        QueryB().doNOAndEndDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------22

    #根据DO NO和BL开始日期检索
    def testDoNOAndBLStartDate(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO和BL开始日期检索"
        driver.get(self.url)
        QueryB().doNOAndBLStartDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------23

    #根据DO NO和BL结束日期检索
    def testDoNOAndBLEnsDate(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO和BL结束日期检索"
        driver.get(self.url)
        QueryB().doNOAndBLEndDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------24

    #根据DO NO和状态检索
    def testDoNOAndStatus(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO和状态检索"
        driver.get(self.url)
        QueryB().doNOAndStatusQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------25

    #根据DO NO和集装箱NO，运输形态检索
    def testDoNOAndContainerTransport(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO，集装箱NO和状态检索"
        driver.get(self.url)
        QueryB().doNOAndContainerTransportQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------26

    #根据DO NO和集装箱NO，到达港检索
    def testDoNOAndContainerToport(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO，集装箱NO和到达港检索"
        driver.get(self.url)
        QueryB().doNOAndContainerToportQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------27

    #根据DO NO和开始时间和集装箱NO检索
    def testDoNOAndContainerStartDate(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO，开始时间和集装箱NO检索"
        driver.get(self.url)
        QueryB().doNOAndContainerStartDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------28

    #根据DO NO和结束时间和集装箱NO检索
    def testDoNOAndContainerEndDate(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO，结束时间和集装箱NO检索"
        driver.get(self.url)
        QueryB().doNOAndContainerEndDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------29

    #根据DO NO和集装箱NO，开始发行日检索
    def testDoNOAndContainerBLStartDate(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO，BL开始日期和集装箱NO检索"
        driver.get(self.url)
        QueryB().doNOAndContainerBLStartDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------30

    #根据DO NO和集装箱NO，BL结束日期检索
    def testDoNOAndContainerBLEndDate(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO，BL结束日期和集装箱NO检索"
        driver.get(self.url)
        QueryB().doNOAndContainerBLEndDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------31

    #根据DO NO和集装箱NO，状态检索
    def testDoNOAndContainerStatus(self):
        driver = self.driver
        self._testMethodDoc = "根据DO NO，状态和集装箱NO检索"
        driver.get(self.url)
        QueryB().doNOAndContainerStatusQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------32

    #根据开始日期和结束日期检索
    def testStartDateAndEndDate(self):
        driver = self.driver
        self._testMethodDoc = "根据开始日期和结束日期检索"
        driver.get(self.url)
        QueryB().startDateAndEndDateQuery(driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)
        
#-------------------------------------------------------------------------------------33

    #根据开始日期大于结束日期检索
    def testStartDateGreaterEndDate(self):
        driver = self.driver
        self._testMethodDoc = "根据开始日期>结束日期检索"
        driver.get(self.url)
        QueryB().startDateGreaterEndDateQuery(driver)
        #断言
        actualResult = self.driver.find_element_by_xpath('//td[text()="No data available"]').text
        self.assertEqual("No data available", actualResult)
        
#-------------------------------------------------------------------------------------34

    #根据DO NO和集装箱NO，运输形态，到达港检索
    def testdoNOContainerNOAndtransportToport(self):
        driver = self.driver
        self._testMethodDoc = "根据DONO，运输状态，到达港和集装箱NO检索"
        driver.get(self.url)
        QueryB().doNOContainerNOAndtransportToportQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------35

    #根据DO NO和集装箱NO，运输形态和ETD检索
    def testdoNOContainerNOAndtransportETD(self):
        driver = self.driver
        self._testMethodDoc = "根据DONO，运输状态，ETD和集装箱NO检索"
        driver.get(self.url)
        QueryB().doNOContainerNOAndtransportETDQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------36

    #根据DO NO和集装箱NO，运输形态和ETA检索
    def testdoNOContainerNOAndtransportETA(self):
        driver = self.driver
        self._testMethodDoc = "根据DONO，运输状态，ETA和集装箱NO检索"
        driver.get(self.url)
        QueryB().doNOContainerNOAndtransportETAQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------37

    #根据DO NO和集装箱NO，运输形态和ETD检索
    def testdoNOContainerNOAndtransportBLStartDate(self):
        driver = self.driver
        self._testMethodDoc = "根据DONO，运输状态，BL开始日期和集装箱NO检索"
        driver.get(self.url)
        QueryB().doNOContainerNOAndtransportBLStartDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------38

    #根据DONO，运输状态，BL结束日期和集装箱NO检索
    def testdoNOContainerNOAndtransportBLEndDate(self):
        driver = self.driver
        self._testMethodDoc = "根据DONO，运输状态，BL结束日期和集装箱NO检索"
        driver.get(self.url)
        QueryB().doNOContainerNOAndtransportBLEDateQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------39

    #根据DO NO和集装箱NO，运输形态和状态检索
    def testdoNOContainerNOAndtransportStatus(self):
        driver = self.driver
        self._testMethodDoc = "根据DONO，运输状态，运输形态和状态检索"
        driver.get(self.url)
        QueryB().doNOContainerNOAndtransportStatusQuery(driver)
        try:
            sleep(2)
            actualResult = self.driver.find_element_by_xpath('//div[@class="v-datatable__actions__pagination"]').text
            actualResult = str(actualResult)[7:]
            actualResult = int(actualResult)
            if actualResult != None:
                self.assertNotEqual(0, actualResult)
        except Exception as e:
            print(e)
        
#-------------------------------------------------------------------------------------40

    def tearDown(self):
        self.driver.quit()
        
