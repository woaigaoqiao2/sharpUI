'''
Created on 2019年7月4日

@author: chinasoft.jl.ma
DO确定
'''
import unittest
from selenium import webdriver
from util.init import init
from business.doinfo.DODetermine import DODetermine



class TestDODetermine(unittest.TestCase):


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


    def testDODeterm(self):
        driver = self.driver
        self._testMethodDoc = "DO确定"
        driver.get(self.url)
        dt = DODetermine()
        dt.doDeterm(driver)
        #断言
        #根据DO NO找到修改的信息 把状态换成确定济  点击检索
        
        #取出状态
        #断言状态是否是确定济
    

    def tearDown(self):
        self.driver.quit()

