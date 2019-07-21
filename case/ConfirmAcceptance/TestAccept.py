import unittest
from selenium import webdriver
from business.Login import Login
from business.ConfirmAcceptance.CAcceptance import CAcceptance
from time import sleep
from util import log

class TestAddCost(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.driver.set_script_timeout(20)
        self.url = "https://sharpsit.jusdaglobal.com"
        self.driver.get(self.url)
        sleep(5)
        self.login = Login()
        # 登录
        self.login.test_click_login_btn(self.driver)
        sleep(2)
        self.CAcceptance=CAcceptance()

    def test01AcceptanceContainerNoUpdate(self):
        # 报告中的用例描述
        self._testMethodDoc = "受入確認_コンテナNo修改成功"
        # logs = log.log_message();
        result = self.CAcceptance.Acceptance(self.driver)
        print(result)
        # expect=result[0]
        # axtual=result[1]
        expect=result
        axtual="OK"
        # 断言
        self.assertEqual(expect, axtual)

    def test02AcceptancePatternUpdate(self):
        # 报告中的用例描述
        self._testMethodDoc = "受入確認_配送模式修改成功"
        # logs = log.log_message();
        result = self.CAcceptance.AcceptancePattern(self.driver)
        expect=result[0]
        axtual=result[1]
        # 断言
        self.assertEqual(expect, axtual)

    def test03DeliveryContainerNoUpdate(self):
        # 报告中的用例描述
        self._testMethodDoc = "納入指示済_コンテナNo修改成功"
        # logs = log.log_message();
        result = self.CAcceptance.Delivery(self.driver)
        expect="OK"
        axtual=result
        # 断言
        self.assertEqual(expect, axtual)

    def test04DeliveryInformationUpdate(self):
        # 报告中的用例描述
        self._testMethodDoc = "納入指示済_納入情報修改成功"
        # logs = log.log_message();
        result = self.CAcceptance.DeliveryInformation(self.driver)
        expectdate=result[0]
        axtualdate=result[2]
        expecttime = result[1]
        axtualtime = (result[3])[0:4]
        # 断言
        self.assertIn(expectdate, axtualdate)
        self.assertIn(expecttime, axtualtime)


    def test05AdditionalFailure(self):
        # 报告中的用例描述
        self._testMethodDoc = "納入指示済_仅填写納入予定日追加失败"
        # logs = log.log_message();
        result = self.CAcceptance.OnlyDeliveryDateUp(self.driver)
        expect=result[0]
        axtual=result[1]
        # 断言
        self.assertEqual(expect,axtual)


    def test06AdditionalFailure(self):
        # 报告中的用例描述
        self._testMethodDoc = "納入指示済_仅填写納入予定时间追加失败"
        # logs = log.log_message();
        result = self.CAcceptance.OnlyDeliveryTimeUp(self.driver)
        expect=result[0]
        axtual=result[1]
        # 断言
        self.assertEqual(expect,axtual)

    def test07DeliveryPatternUPFailure(self):
        # 报告中的用例描述
        self._testMethodDoc = "納入指示済_配送模式修改失败"
        # logs = log.log_message();
        result = self.CAcceptance.BackDeliveryPatternUP(self.driver)
        expect=result[0]
        axtual=result[1]
        # 断言
        self.assertEqual(expect,axtual)

    def test08AcceptanceUPFailure(self):
        # 报告中的用例描述
        self._testMethodDoc = "受入確認_コンテナNo修改失败"
        # logs = log.log_message();
        result = self.CAcceptance.BackAcceptanceUP(self.driver)
        expect = result[0]
        axtual = result[1]
        # 断言
        self.assertEqual(expect, axtual)

    def test09AcceptancePatternUPFailure(self):
        # 报告中的用例描述
        self._testMethodDoc = "受入確認_配送パターン修改失败"
        # logs = log.log_message();
        result = self.CAcceptance.BackAcceptancePatternUP(self.driver)
        expect = result[0]
        axtual = result[1]
        # 断言
        self.assertEqual(expect, axtual)

    def test10DeliveryUPFailure(self):
        # 报告中的用例描述
        self._testMethodDoc = "纳入指示済_コンテナNo修改失败"
        # logs = log.log_message();
        result = self.CAcceptance.BackDeliveryUP(self.driver)
        expect = result[0]
        axtual = result[1]
        # 断言
        self.assertEqual(expect, axtual)

    def test11DeliveryInformationUPFailure(self):
        # 报告中的用例描述
        self._testMethodDoc = "纳入指示済_納入情報修改失败"
        # logs = log.log_message();
        result = self.CAcceptance.BackDeliveryInformationUP(self.driver)
        expectdata = result[0]
        axtualdata = result[2]
        expecttime = result[1]
        axtualtime = result[3]
        # 断言
        self.assertEqual(expectdata, axtualdata)
        self.assertEqual(expecttime, axtualtime)


    def tearDown(self):
        self.driver.quit()