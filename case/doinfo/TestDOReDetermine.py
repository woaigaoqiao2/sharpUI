'''
Created on 2019年7月4日

@author: chinasoft.jl.ma
DO解除确定
'''
import unittest
from selenium import webdriver
from util.init import init
from business.doinfo.DOReDetermineb import DOReDetermineb
from pageElement.doinfo.DOReDetermine import DOReDetermine
from util.ElementUtil import ElementUtil
from selenium.webdriver.chrome.options import Options

class TestDOReDetermine(unittest.TestCase,DOReDetermine):


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

    ##此方法不执行
    def BtestDOReDeter(self):
        driver = self.driver
        self._testMethodDoc = "DO解除确定"
        driver.get(self.url)
        eu = ElementUtil()
        drd = DOReDetermineb()
        drd.doReDeter(driver)
        #断言
        #输入DO NO
#         eu.send_keys(driver, 5, 'DO NO',*self.DONOElement)
#         #检索数据
#         eu.click(driver, 5,*self.selElement)
#         #获取状态
#         actualResult = driver.find_element_by_xpath('//tbody/tr[1]/td[5]')
#         #检查状态是否为DO解除济
#         self.assertEqual('DO確定済s', actualResult)
        


    def tearDown(self):
        self.driver.quit()
