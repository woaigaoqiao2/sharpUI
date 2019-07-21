'''
DO解除申请
'''
from unittest import TestCase
from selenium import webdriver
from util.init import init
from business.doinfo.ReDOb import ReDOb


class TestReDO(TestCase):
    
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
        
    def testReDO(self):
        driver = self.driver
        self._testMethodDoc = "DO解除申请"
        driver.get(self.url)
        red = ReDOb()
        red.dismiss(driver)
        
        #断言  根据do no查出数据  检查状态是否为待解除
        
    def tearDown(self):
        self.driver.quit()