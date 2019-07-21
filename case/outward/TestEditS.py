'''
Created on 2019年6月24日

@author: chinasoft.jl.ma
'''
import unittest
from selenium import webdriver
from util.init import init
from business.outward.Edit import Edit
from time import sleep



class TestEditS(unittest.TestCase):


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
    
    ##修改到达港   由于功能原因 无法保存数据  导致无法断言
    def testEditToport(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "修改到达港"
        e = Edit()
        e.editToport(driver)



#------------------------------------------------------------------------1
        
    ##修改20F集装箱数量
    def testEditTwoF(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "修改20F集装箱数量"
        e = Edit()
        e.editTwoF(driver)

         
#------------------------------------------------------------------------2
         
         
    ##修改40F集装箱数量
    def testEditFourF(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "修改40F集装箱数量"
        e = Edit()
        e.editFourF(driver)
        sleep(2)

         
#------------------------------------------------------------------------3
         
    ##修改40H集装箱数量
    def testEditFourH(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "修改40H集装箱数量"
        e = Edit()
        e.editFourH(driver)
        sleep(2)

         
#------------------------------------------------------------------------4
         
    ##修改到岗开始时间
    def testEditStartDate(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "修改开始到港时间"
        e = Edit()
        e.editStartDate(driver)
        #断言  调完接口断言
         
#------------------------------------------------------------------------5
         
    ##修改到岗结束时间
    def testEditEndDate(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "修改结束到港时间"
        e = Edit()
        e.editEndDate(driver)
        #断言  调完接口断言
         
#------------------------------------------------------------------------6
         
    ##修改到岗结束时间后返回
    def testEditEndDateR(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "不保存修改开始到港时间"
        e = Edit()
        e.editEndDateR(driver)
        #断言  调完接口断言
#------------------------------------------------------------------------7
    
    def tearDown(self):
        self.driver.quit()


