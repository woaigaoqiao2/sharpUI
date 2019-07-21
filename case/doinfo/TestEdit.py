'''
Created on 2019年7月1日

@author: chinasoft.jl.ma
'''
import unittest
from util.init import init
from selenium import webdriver
from business.doinfo.EditB import EditB
from pageElement.doinfo.Edit import Edit
from util.ElementUtil import ElementUtil
from selenium.webdriver.chrome.options import Options

class TestEdit(unittest.TestCase):


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

    #修改纳入日期  保存
    def testEditDate(self):
        driver = self.driver
        self._testMethodDoc = "保存修改的纳入日期"
        driver.get(self.url)
        EditB().editDate(driver)



        
    #修改纳入日期  返回
    def testEditDateR(self):
        driver = self.driver
        self._testMethodDoc = "不保存修改的纳入日期"
        driver.get(self.url)
        EditB().editDateR(driver)
    
        #断言  状态变为  DO業者確認済

    
    #修改纳入时间  保存
    def testEditTime(self):
        driver = self.driver
        self._testMethodDoc = "保存修改的纳入时间"
        driver.get(self.url)
        EditB().editTime(driver)
        #断言  状态变为  DO業者確認済
#         eu.click(driver, 5,*ed.DOstatusElement)
#         eu.click(driver, 5,*ed.selDOstatusElement)
#         #点击检索  用DONO 
#         eu.click(driver, 5,*ed.selElement)
#         #拿出数据的DO NO
#         actualResult = driver.find_element_by_xpath('//tbody/tr[1]/td[2]').text
#         #判断是否是  DO業者確認済
#         self.assertEqual('DO NO', actualResult)
        
    #修改纳入时间  返回
    def testEditTimeR(self):
        driver = self.driver
        self._testMethodDoc = "不保存修改的纳入时间"
        driver.get(self.url)
        EditB().editTimeR(driver)
        #断言  无数据
        
    #修改纳入日期和时间  保存
    def testEditDateAndTime(self):
        driver = self.driver
        self._testMethodDoc = "不保存修改的纳入时间和日期"
        driver.get(self.url)
        EditB().editDateAndTime(driver)
        #断言  无数据


        

    def tearDown(self):
        self.driver.quit()


