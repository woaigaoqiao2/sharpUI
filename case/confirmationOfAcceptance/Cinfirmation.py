import unittest
from selenium import webdriver
from time import sleep
from business.confirmationOfAcceptance.ConfirmationLogic import Logic
from business.Login import Login

class ConfirmationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # options = Options()
        # options.add_argument('window-size=1920x1080')
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # self.driver = webdriver.Chrome(chrome_options=options)

        self.url = "https://sharpsit.jusdaglobal.com/"
        
        
    def test1(self):
        #报告中的用例描述
        self._testMethodDoc = "选择ステータス进行检索"
        driver = self.driver
        driver.get(self.url)
        Login().test_click_login_btn(driver)
        try:
            sucess_text = Logic().test1(driver)
            self.assertNotEqual('No data available', sucess_text)
        except Exception as e:
            print(e)
        
        
    def test2(self):
        #报告中的用例描述
        self._testMethodDoc = "选择陆扬港进行检索"
        driver = self.driver
        driver.get(self.url)
        Login().test_click_login_btn(driver)
        try:
            sucess_text = Logic().test2(driver)
            self.assertNotEqual('No data available', sucess_text)
        except Exception as e:
            print(e)
        
        
    def test3(self):
        #报告中的用例描述
        self._testMethodDoc = "选择纳入场所进行检索"
        driver = self.driver
        driver.get(self.url)
        Login().test_click_login_btn(driver)

        
        
    def test4(self):
        #报告中的用例描述
        self._testMethodDoc = "输入纳入指示结束日进行检索"
        driver = self.driver
        driver.get(self.url)
        Login().test_click_login_btn(driver)
        sleep(3)
        sucess_text = Logic().test4(driver)
        try:
            self.assertNotEqual('No data available', sucess_text)
        except Exception as e:
            print(e)

    def test5 (self):
        #报告中的用例描述
        self._testMethodDoc = "输入纳入指示开始日期进行检索"
        driver = self.driver
        driver.get(self.url)
        Login().test_click_login_btn(driver)
        sleep(3)
        sucess_text = Logic().test5(driver)
        try:
            self.assertEqual('No data available', sucess_text)
        except Exception as e:
            print(e)
        
        
    def test6 (self):
        #报告中的用例描述
        self._testMethodDoc = "输入纳入指示开始、结束日期进行检索"
        driver = self.driver
        driver.get(self.url)
        Login().test_click_login_btn(driver)
        sleep(3)
        sucess_text = Logic().test6(driver)
        try:
            self.assertEqual('No data available', sucess_text)
        except Exception as e:
            print(e)
    
    
    def test7 (self):
        #报告中的用例描述
        self._testMethodDoc = "选择輸送形態进行检索"
        driver = self.driver
        driver.get(self.url)
        Login().test_click_login_btn(driver)
        sleep(3)
        sucess_text = Logic().test7(driver)
        try:
            self.assertEqual('No data available', sucess_text)
        except Exception as e:
            print(e)
        
        
    def test8 (self):
        #报告中的用例描述
        self._testMethodDoc = "选择状态为受入確認済的数据进行受入確認解除"
        driver = self.driver
        driver.get(self.url)
        Login().test_click_login_btn(driver)
        sleep(3)
        sucess_text = Logic().test8(driver)
        try:
            self.assertIn('OK', sucess_text)
        except Exception as e:
            print(e)
    
    
    def test9(self):
        
        #报告中的用例描述
        self._testMethodDoc = "选择状态为納入指示済的数据修改配送模式"
        driver = self.driver
        driver.get(self.url)
        Login().test_click_login_btn(driver)
        sleep(3)
        Logic().test9(driver)

    def tearDown(self):
        self.driver.quit()