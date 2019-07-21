"""
编写人：陈博华
"""
import unittest
from time import sleep
from selenium import webdriver
from business.Login import Login
from common.Browser import Browser
from business.test_customs.HomePage import HomePage
from business.test_customs.NewlyBuild import NewlyBuild
from pageElement.SAlogin.HomePage import HomePageElement
# from common.Decorator import decorator
from util.ElementUtil import ElementUtil

class TestShippingAdvice(unittest.TestCase):


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
        # self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()


    def test_newly_built1(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]海关新建海运送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = NewlyBuild()
        BL_No,tips = bussiness.newlyBuilt01(driver)
        sleep(1.5)
        homepage = HomePage()
        homepage.BL_No_search(driver, BL_No)
        sleep(1.5)
        locate = HomePageElement()
        status_element = locate.locate_status(BL_No)
        actual_status = Browser(driver,10).get_text(status_element)
        if "有償INVが無いと、SAを作成できません。" in tips:
            self.assertEqual("SA一時保存",actual_status)
        else:
            self.assertEqual("SA登録済",actual_status)


    def test_newly_built2(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]海关新建空运送信"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = NewlyBuild()
        BL_No,tips = bussiness.newlyBuilt02(driver)
        sleep(1.5)
        homepage = HomePage()
        homepage.BL_No_search(driver, BL_No)
        sleep(1.5)
        locate = HomePageElement()
        status_element = locate.locate_status(BL_No)
        actual_status = Browser(driver,10).get_text(status_element)
        if "有償INVが無いと、SAを作成できません。" in tips:
            self.assertEqual("SA一時保存",actual_status)
        else:
            self.assertEqual("SA登録済",actual_status)


    def test_INV_search01(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]I/V NO搜索"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = NewlyBuild()
        actual_values,search_value = bussiness.INV_search01(driver)
        for i in actual_values:
            self.assertIn(search_value,i)


    def test_newly_built3(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]新建海关数据，保存"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = NewlyBuild()
        BL_No = bussiness.newlyBuilt03(driver)
        sleep(1.5)
        homepage = HomePage()
        homepage.BL_No_search(driver, BL_No)
        sleep(1.5)
        locate = HomePageElement()
        status_element = locate.locate_status(BL_No)
        sleep(1.5)
        actual_status = ElementUtil.getText(self, driver,5,"[陈博华]新建海关数据，保存", *status_element)
        self.assertEqual("SA一時保存",actual_status)


    def test_newly_built4(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证新建时，空运，House B/L NO是否为必填项"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = NewlyBuild()
        actual_text = bussiness.newlyBuilt04(driver)
        self.assertEqual("House B/L NO必要である",actual_text)


    def test_newly_built5(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = NewlyBuild()
        actual_text = bussiness.newlyBuilt05(driver)
        self.assertEqual("Master B/L NO必要である",actual_text)


    def test_newly_built6(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = NewlyBuild()
        actual_text = bussiness.newlyBuilt06(driver)
        self.assertEqual("House B/L NO必要である",actual_text)


    def test_newly_built7(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = u"[陈博华]验证新建时，重复B/L NO是否校验"
        sleep(1.5)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        bussiness = NewlyBuild()
        actual_text = bussiness.newlyBuilt07(driver)
        self.assertIn("重複B/L No.が存在します。", actual_text)


    # def test_newly_built8(self):
    #     driver = self.driver
    #     driver.get(self.url)
    #     self._testMethodDoc = u"[陈博华]海关新建海运，填写必填项，送信"
    #     sleep(1.5)
    #     login = Login()
    #     login.test_click_login_btn(driver)
    #     sleep(5)
    #     bussiness = NewlyBuild()
    #     BL_No,tips = bussiness.newlyBuilt08(driver)
    #     sleep(1.5)
    #     homepage = HomePage()
    #     homepage.BL_No_search(driver, BL_No)
    #     sleep(1.5)
    #     locate = HomePageElement()
    #     status_element = locate.locate_status(BL_No)
    #     actual_status = Browser(driver,10).get_text(status_element)
    #     if "有償INVが無いと、SAを作成できません。" in tips:
    #         self.assertEqual("SA一時保存",actual_status)
    #     else:
    #         self.assertEqual("SA登録済",actual_status)
    #
    #
    # def test_newly_built9(self):
    #     driver = self.driver
    #     driver.get(self.url)
    #     self._testMethodDoc = u"[陈博华]海关新建空运，填写必填项，送信"
    #     sleep(1.5)
    #     login = Login()
    #     login.test_click_login_btn(driver)
    #     sleep(5)
    #     bussiness = NewlyBuild()
    #     BL_No,tips = bussiness.newlyBuilt09(driver)
    #     sleep(1.5)
    #     homepage = HomePage()
    #     homepage.BL_No_search(driver, BL_No)
    #     sleep(1.5)
    #     locate = HomePageElement()
    #     status_element = locate.locate_status(BL_No)
    #     sleep(1.5)
    #     actual_status = Browser(driver,10).get_text(status_element)
    #     if "有償INVが無いと、SAを作成できません。" in tips:
    #         self.assertEqual("SA一時保存",actual_status)
    #     else:
    #         self.assertEqual("SA登録済",actual_status)
    #
    #
    # def test_newly_built10(self):
    #     driver = self.driver
    #     driver.get(self.url)
    #     self._testMethodDoc = u"[陈博华]海关新建海运，送信时取消，查看状态是否变化"
    #     sleep(1.5)
    #     login = Login()
    #     login.test_click_login_btn(driver)
    #     sleep(5)
    #     bussiness = NewlyBuild()
    #     BL_No = bussiness.newlyBuilt10(driver)
    #     sleep(1.5)
    #     homepage = HomePage()
    #     homepage.BL_No_search(driver, BL_No)
    #     sleep(1.5)
    #     locate = HomePageElement()
    #     status_element = locate.locate_status(BL_No)
    #     sleep(1.5)
    #     actual_status = Browser(driver,10).get_text(status_element)
    #     self.assertEqual("SA一時保存",actual_status)
    #
    #
    # def test_newly_built11(self):
    #     driver = self.driver
    #     driver.get(self.url)
    #     self._testMethodDoc = u"[陈博华]海关新建空运，送信时取消，查看状态是否变化"
    #     sleep(1.5)
    #     login = Login()
    #     login.test_click_login_btn(driver)
    #     sleep(5)
    #     bussiness = NewlyBuild()
    #     BL_No = bussiness.newlyBuilt11(driver)
    #     sleep(1.5)
    #     homepage = HomePage()
    #     homepage.BL_No_search(driver, BL_No)
    #     sleep(1.5)
    #     locate = HomePageElement()
    #     status_element = locate.locate_status(BL_No)
    #     sleep(1.5)
    #     actual_status = Browser(driver,10).get_text(status_element)
    #     self.assertEqual("SA一時保存",actual_status)
    #
    #

