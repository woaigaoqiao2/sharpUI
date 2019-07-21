"""
编写人：陈博华
"""
import unittest
from time import sleep
from selenium import webdriver
from business.Login import Login
from common.Browser import Browser
from business.test_customs.Edit import Edit
from business.test_customs.HomePage import HomePage
from pageElement.SAlogin.HomePage import HomePageElement



class TestEdit(unittest.TestCase):


    def setUp(self):
        # option = Options()
        # option.add_argument('----headless')
        # option.add_argument('--no-sandbox')
        # option.add_argument('window-size=1920x1080')
        # self.driver = webdriver.Chrome(chrome_options=option)
        self.driver = webdriver.Chrome()
        self.url = "https://sharpsit.jusdaglobal.com"
        # self.url = "https://sharpuat.jusdaglobal.com"
        # self.driver.implicitly_wait(15)
        # self.driver.set_page_load_timeout(15)
        # self.driver.set_script_timeout(15)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()


    def test_edit01(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]编集状态为SA一時保存的海关数据，一時保存"
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        edit = Edit()
        text = edit.edit01(driver)
        self.assertEqual(text,1)

    def test_edit02(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]编集状态为SA一時保存的海关数据，修改Carton No，验证Shipped Carton数量是否正确"
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        edit = Edit()
        flag = edit.edit02(driver)
        self.assertTrue(flag)

    def test_edit04(self):
        self._testMethodDoc = u"[陈博华]验证编集时，空运，House B/L NO是否为必填项"
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        edit = Edit()
        actual_text = edit.edit04(driver)
        self.assertEqual("House B/L NO必要である",actual_text)

    def test_edit05(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证编集时，海运整箱，Master B/L NO是否为必填项"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = Edit()
        actual_text = bussiness.edit05(driver)
        self.assertEqual("Master B/L NO必要である",actual_text)

    def test_edit06(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证编集时，海运拼箱，House B/L NO是否为必填项"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = Edit()
        actual_text = bussiness.edit06(driver)
        self.assertEqual("House B/L NO必要である", actual_text)


    def test_edit07(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证编集时，依頼日不填能否送信"
        text = "[陈博华]验证编集时，依頼日不填能否送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = Edit()
        sleep(1.5)
        actual_text = bussiness.edit07(driver, text)
        self.assertEqual("依頼日必要である",actual_text)


    def test_edit08(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证编集时，B/L発行日不填能否送信"
        text = "[陈博华]验证编集时，B/L発行日不填能否送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = Edit()
        actual_text = bussiness.edit08(driver, text)
        self.assertEqual("B/L発行日必要である",actual_text)


    def test_edit09(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证编集时，ETA不填能否送信"
        text = "[陈博华]验证编集时，ETA不填能否送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = Edit()
        actual_text = bussiness.edit09(driver, text)
        self.assertEqual("ETA必要である",actual_text)


    def test_edit10(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证编集时，輸出通関日不填能否送信"
        text = "[陈博华]验证编集时，輸出通関日不填能否送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = Edit()
        actual_text = bussiness.edit10(driver, text)
        self.assertEqual("輸出通関日必要である",actual_text)


    def test_edit11(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证编集时，船社・航空会社不填能否送信"
        text = "[陈博华]验证编集时，船社・航空会社不填能否送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = Edit()
        actual_text = bussiness.edit11(driver, text)
        self.assertEqual("船社・航空会社必要である",actual_text)



    def test_edit12(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证编集时，通関業者不填能否送信"
        text = "[陈博华]验证编集时，通関業者不填能否送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = Edit()
        actual_text = bussiness.edit12(driver, text)
        self.assertEqual("通関業者必要である", actual_text)

    def test_edit13(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证编集时，貨物タイプ不填能否送信"
        text = "[陈博华]验证编集时，貨物タイプ不填能否送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = Edit()
        actual_text = bussiness.edit13(driver, text)
        self.assertEqual("貨物タイプ必要である", actual_text)

    def test_edit14(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证编集时，Cartainer No不填能否送信"
        text = "[陈博华]验证编集时，Cartainer No不填能否送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = Edit()
        actual_text = bussiness.edit14(driver, text)
        self.assertEqual(True, actual_text)

    def test_edit15(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证编集时，Cartainer Size不填能否送信"
        text = "[陈博华]验证编集时，Cartainer Size不填能否送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = Edit()
        actual_text = bussiness.edit15(driver, text)
        self.assertEqual(True, actual_text)

    def test_edit16(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证编集时，BL NO能否重复使用"
        text = "[陈博华]验证编集时，BL NO能否重复使用"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = Edit()
        actual_text = bussiness.edit16(driver, text)
        self.assertEqual("重複B/L No.が存在します。", actual_text)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestEdit('test_edit01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)