'''
Created on 2019年6月215
@author: chinasoft.jl.ma
增加费用
'''
from unittest import TestCase
from util.init import init
from selenium import webdriver
from business.outward.AddCost import AddCost
from time import sleep
from pageElement.outward.AddCostElement import AddCostElement
from selenium.webdriver.common.keys import Keys
from util.ElementUtil import  ElementUtil



class TestAddCostS(TestCase):
    
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
        
        
    ##增加DOCFEE费用
    def testDocfee(self):
        driver = self.driver
        driver.get(self.url)
        ace = AddCostElement()
        eu = ElementUtil()
        addC = AddCost()
        self._testMethodDoc = "增加DOCFEE费用"
        addC.docfee(driver)
        #断言
        eu.click(driver,15,"增加DOCFEE费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCFEE费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[1]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
        
#--------------------------------------------------------------------------1
        
    ##增加DOctax费用
    def testDocTax(self):
        driver = self.driver
        driver.get(self.url)
        ace = AddCostElement()
        eu = ElementUtil()
        addC = AddCost()
        self._testMethodDoc = "增加DOCTAX费用"
        addC.docTax(driver)
        # 断言
        eu.click(driver, 15,"增加DOCTAX费用", *ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[2]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
        
#--------------------------------------------------------------------------2
        
    ##增加other charge费用
    def testOtherCharge(self):
        driver = self.driver
        driver.get(self.url)
        eu = ElementUtil()
        ace = AddCostElement()
        addC = AddCost()
        self._testMethodDoc = "增加other charge费用"
        addC.otherCharge(driver)
        # 断言
        eu.click(driver, 15, "增加DOCTAX费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[3]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
        
#--------------------------------------------------------------------------3
        
    ##增加20F费用
    def testTwoF(self):
        driver = self.driver
        driver.get(self.url)
        eu = ElementUtil()
        ace = AddCostElement()
        addC = AddCost()
        self._testMethodDoc = "增加20F费用"
        addC.TwoF(driver)
        # 断言
        eu.click(driver, 15, "增加DOCTAX费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[4]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
        
#--------------------------------------------------------------------------4
        
    ##增加40F费用
    def testFourF(self):
        driver = self.driver
        driver.get(self.url)
        eu = ElementUtil()
        ace = AddCostElement()
        addC = AddCost()
        self._testMethodDoc = "增加40F费用"
        addC.TwoF(driver)
        # 断言
        eu.click(driver, 15, "增加DOCTAX费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[4]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
         
#--------------------------------------------------------------------------15
         
    ##增加docfee和tax费用
    def testdocfeeAndTax(self):
        driver = self.driver
        driver.get(self.url)
        eu = ElementUtil()
        ace = AddCostElement()
        addC = AddCost()
        self._testMethodDoc = "增加DOCFEE和TAX费用"
        addC.docfeeAndTax(driver)
        # 断言
        eu.click(driver, 15, "增加DOCTAX费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[1]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
         
#--------------------------------------------------------------------------6
         
    ##增加docfee和other费用
    def testdocfeeAndOther(self):
        driver = self.driver
        driver.get(self.url)
        eu = ElementUtil()
        ace = AddCostElement()
        addC = AddCost()
        self._testMethodDoc = "增加DOCFEE和OTHER费用"
        addC.docfeeAndOther(driver)
        sleep(3)
        # 断言
        eu.click(driver, 15, "增加DOCTAX费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[3]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
             
#--------------------------------------------------------------------------7
         
    ##增加docfee和20F费用
    def testdocfeeAndTwoF(self):
        driver = self.driver
        driver.get(self.url)
        eu = ElementUtil()
        ace = AddCostElement()
        addC = AddCost()
        self._testMethodDoc = "增加DOCFEE和20F费用"
        addC.docfeeAndTwoF(driver)
        # 断言
        eu.click(driver, 15, "增加DOCTAX费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[4]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)

#--------------------------------------------------------------------------8
         
    ##增加docfee和40F费用
    def testdocfeeAndFourF(self):
        driver = self.driver
        driver.get(self.url)
        eu = ElementUtil()
        ace = AddCostElement()
        addC = AddCost()
        self._testMethodDoc = "增加DOCFEE和40F费用"
        addC.docfeeAndFourF(driver)
        # 断言
        eu.click(driver, 15, "增加DOCTAX费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[5]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
        
         
#--------------------------------------------------------------------------9
         
    ##增加docfee,tax和40F费用
    def testdocfeeTaxAndFourF(self):
        driver = self.driver
        driver.get(self.url)
        eu = ElementUtil()
        ace = AddCostElement()
        addC = AddCost()
        self._testMethodDoc = "增加DOCFEE,TAX和40F费用"
        addC.docfeeTaxAndFourF(driver)
        # 断言
        eu.click(driver, 15, "增加DOCTAX费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[2]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
         
#--------------------------------------------------------------------------10
         
    ##增加docfee,tax和20F费用
    def testdocfeeTaxAndTwoF(self):
        driver = self.driver
        driver.get(self.url)
        eu = ElementUtil()
        ace = AddCostElement()
        addCost = AddCost()
        self._testMethodDoc = "增加DOCFEE,TAX和20F费用"
        addCost.docfeeTaxAndTwoF(driver)
        sleep(3)
        # 断言
        eu.click(driver, 15, "增加DOCTAX费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[4]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
         
#--------------------------------------------------------------------------11
         
    ##增加docfee,40F和20F费用
    def testdocfeeFourFAndTwoF(self):
        driver = self.driver
        driver.get(self.url)
        eu = ElementUtil()
        ace = AddCostElement()
        addCost = AddCost()
        self._testMethodDoc = "增加DOCFEE,40F和20F费用"
        addCost.docfeeFourFAndTwoF(driver)
        # 断言
        eu.click(driver, 15, "增加DOCTAX费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[4]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
         
#--------------------------------------------------------------------------12
         
    ##增加docfee,other和20F费用
    def testdocfeeOtherFAndTwoF(self):
        driver = self.driver
        driver.get(self.url)
        eu = ElementUtil()
        ace = AddCostElement()
        addCost = AddCost()
        self._testMethodDoc = "增加DOCFEE,OTHER和20F费用"
        addCost.docfeeOtherAndTwoF(driver)
        # 断言
        eu.click(driver, 15, "增加DOCTAX费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(2)
        try:
            actualResult = driver.find_element_by_xpath('//tbody/tr[3]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
         
#--------------------------------------------------------------------------13
 
    ##增加所有费用
    def testFull(self):
        driver = self.driver
        driver.get(self.url)
        eu = ElementUtil()
        ace = AddCostElement()
        addCost = AddCost()
        self._testMethodDoc = "增加所有费用"
        addCost.full(driver)
        # 断言
        eu.click(driver, 15, "增加DOCTAX费用",*ace.selElement)
        el = driver.find_element(*ace.selDateElement)
        el.send_keys(Keys.SPACE)
        eu.click(driver, 15, "增加DOCTAX费用",*ace.editElement)
        sleep(5)
        try:
            # actualResult = eu.getElement(driver, 15, "增加DOCTAX费用", *ace.assertElement)
            # actualResult = actualResult.get_attribute('value')
            actualResult = driver.find_element_by_xpath('//tbody/tr[5]/td[7]/div[1]//input').get_attribute('value')
            actualResult = int(actualResult)
            self.assertEqual(1000, actualResult)
        except ElementUtil as e:
            print(e)
            
#--------------------------------------------------------------------------14

    def tearDown(self):
        self.driver.quit()
        