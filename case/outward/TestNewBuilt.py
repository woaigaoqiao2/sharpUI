'''
Created on 2019年6月24日

@author: chinasoft.jl.ma
新规
'''
from unittest import TestCase
from business.outward.NewBiult import NewBuilt
from selenium import webdriver
from util.init import init
from time import sleep
from selenium.webdriver.chrome.options import Options



class TestNewBuilt(TestCase,NewBuilt):
    
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
    
    def testNewBuilt(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "新规做成"
        nb = NewBuilt()
        nb.newBuilt(driver)
        #断言
        try:
            actualResult = driver.find_element_by_xpath('//div[text()="保存が完了しました。"]').text
            self.assertEqual("保存が完了しました。", actualResult)
        except Exception as e:
            print(e)
        
    def tearDown(self):
        self.driver.quit()
        