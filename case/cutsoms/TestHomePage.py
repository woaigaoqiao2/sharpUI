"""
编写人：陈博华
"""
from selenium import webdriver
import unittest
from time import sleep
from business.Login import Login
from datetime import datetime
from business.test_customs.HomePage import HomePage


class TestHomePage(unittest.TestCase):


    def setUp(self):
        # option = Options()
        # option.add_argument('----headless')
        # option.add_argument('--no-sandbox')
        # option.add_argument('window-size=1920x1080')
        # self.driver = webdriver.Chrome(chrome_options=option)
        self.driver = webdriver.Chrome()
        self.url = "https://sharpsit.jusdaglobal.com"
        # self.driver.implicitly_wait(15)
        # self.driver.set_page_load_timeout(15)
        # self.driver.set_script_timeout(15)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()


    def test_BL_NO_search(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]海关新建海运送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        homepage = HomePage()
        actual_list,expect_value = homepage.BL_No_search(driver)
        for i in actual_list:
            self.assertIn(expect_value,i)


    def test_BL_issuance_date_search01(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]首页BL开始日检索，查看数据是否符合条件"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        homepage = HomePage()
        actual_list,expect_value = homepage.BL_issuance_start_date_search(driver)
        d1 = datetime.strptime(expect_value,"%Y-%m-%d")
        for i in actual_list:
            d2 = datetime.strptime(i,"%Y-%m-%d")
            delta = d2 - d1
            self.assertTrue(delta.days + 1)


    def test_BL_issuance_date_search02(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]首页BL结束日检索，查看数据是否符合条件"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        homepage = HomePage()
        actual_list,expect_value = homepage.BL_issuance_end_date_search(driver)
        d1 = datetime.strptime(expect_value,"%Y-%m-%d")
        for i in actual_list:
            d2 = datetime.strptime(i,"%Y-%m-%d")
            delta = d1 - d2
            self.assertTrue(delta.days + 1)


    def test_BL_issuance_date_search03(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]首页BL开始和结束日检索，查看数据是否符合条件"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        homepage = HomePage()
        actual_list,expect_value1,expect_value2 = homepage.BL_issuance_date_search(driver)
        d1 = datetime.strptime(expect_value1,"%Y-%m-%d")
        d3 = datetime.strptime(expect_value2,"%Y-%m-%d")
        for i in actual_list:
            d2 = datetime.strptime(i,"%Y-%m-%d")
            delta1 = d2 - d1
            delta2 = d3 - d2
            self.assertTrue(delta1.days + 1)
            self.assertTrue(delta2.days + 1)


    def test_ETA_date_search01(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]首页ETA开始日检索，查看数据是否符合条件"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        homepage = HomePage()
        actual_list,expect_value = homepage.ETA_start_date_search(driver)
        d1 = datetime.strptime(expect_value,"%Y-%m-%d")
        for i in actual_list:
            d2 = datetime.strptime(i,"%Y-%m-%d")
            delta = d2 - d1
            self.assertTrue(delta.days + 1)


    def test_ETA_date_search02(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]首页ETA结束日检索，查看数据是否符合条件"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        homepage = HomePage()
        actual_list,expect_value = homepage.ETA_end_date_search(driver)
        d1 = datetime.strptime(expect_value,"%Y-%m-%d")
        for i in actual_list:
            d2 = datetime.strptime(i,"%Y-%m-%d")
            delta = d1 - d2
            self.assertTrue(delta.days + 1)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestHomePage('test_ETA_date_search01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)