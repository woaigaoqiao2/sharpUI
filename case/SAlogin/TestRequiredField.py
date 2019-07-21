"""
@author: yangjun
"""
import unittest
from time import sleep

from selenium import webdriver
from business.Login import Login
from business.SAlogin.RequiredField import RequiredField


class TestRequiredField(unittest.TestCase):
    """新建Shipping Advice数据,使用不合法数据测试"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        url = "https://sharpsit.jusdaglobal.com"
        # url = "https://sharpuat.jusdaglobal.com"
        self.driver.get(url)
        self.driver.maximize_window()
        self.login = Login()
        self.login.test_click_login_btn(self.driver)
        self.field = RequiredField()

    def tearDown(self):
        # sleep(1)
        self.driver.quit()

    def testNoRequestedDate(self):
        """不填写依赖日"""
        self._testMethodDoc = "新建Shipping Advice数据,必填项验证,不填写依赖日"
        status = self.field.no_requested_date(self.driver)
        # expected = "依頼日必要である"
        # self.assertEqual(expected, status)
        assert status == True

    def testNoIssueDate(self):
        """不填写B/L発行日"""
        self._testMethodDoc = "新建Shipping Advice数据,必填项验证,不填写B/L発行日"
        text = "新建Shipping Advice数据,必填项验证,不填写B/L発行日"
        status = self.field.no_issue_date(self.driver, text)
        # expected = "B/L発行日必要である"
        # self.assertEqual(expected, status)
        assert status == True

    def testNoETA(self):
        """不填写ETA"""
        self._testMethodDoc = "新建Shipping Advice数据,必填项验证,不填写ETA"
        text = "新建Shipping Advice数据,必填项验证,不填写ETA"
        status = self.field.no_ETA(self.driver, text)
        # expected = "ETA必要である"
        # self.assertEqual(expected, status)
        assert status == True

    def testNoLoadingMethod(self):
        """不填写積み方"""
        self._testMethodDoc = "新建Shipping Advice数据,必填项验证,不填写積み方"
        text = "新建Shipping Advice数据,必填项验证,不填写積み方"
        status = self.field.no_loading_method(self.driver, text)
        # expected = "積み方必要である"
        # self.assertEqual(expected, status)
        assert status == True

    def testNoExportDeclarationDate(self):
        """不填写輸出通関日"""
        self._testMethodDoc = "新建Shipping Advice数据,必填项验证,不填写輸出通関日"
        text = "新建Shipping Advice数据,必填项验证,不填写輸出通関日"
        status = self.field.no_export_declaration_date(self.driver, text)
        # expected = "輸出通関日必要である"
        # self.assertEqual(expected, status)
        assert status == True

    def testNoShipAirCompany(self):
        """不填写船社・航空会社"""
        self._testMethodDoc = "新建Shipping Advice数据,必填项验证,不填写船社・航空会社"
        text = "新建Shipping Advice数据,必填项验证,不填写船社・航空会社"
        status = self.field.no_ship_air_company(self.driver, text)
        # expected = "船社・航空会社必要である"
        # self.assertEqual(expected, status)
        assert status == True

    def testNoCustomsBroker(self):
        """不填写通関業者"""
        self._testMethodDoc = "新建Shipping Advice数据,必填项验证,不填写通関業者"
        text = "新建Shipping Advice数据,必填项验证,不填写通関業者"
        status = self.field.no_customs_broker(self.driver, text)
        # expected = "通関業者必要である"
        # self.assertEqual(expected, status)
        assert status == True

    def testNoCargoType(self):
        """不填写貨物タイプ"""
        self._testMethodDoc = "新建Shipping Advice数据,必填项验证,不填写貨物タイプ"
        text = "新建Shipping Advice数据,必填项验证,不填写貨物タイプ"
        status = self.field.no_cargo_type(self.driver, text)
        # expected = "貨物タイプ必要である"
        # self.assertEqual(expected, status)
        assert status == True

    def testNoContainerNO(self):
        """不填写CONTAINER NO"""
        self._testMethodDoc = "新建Shipping Advice数据,必填项验证,不填写CONTAINER NO"
        text = "新建Shipping Advice数据,必填项验证,不填写CONTAINER NO"
        status = self.field.no_container_NO(self.driver, text)
        # expected = "INV P/L情報が不整備です、ご確認お願いします。"
        # self.assertEqual(expected, status)
        assert status == True

    def testNoContainerSize(self):
        """不填写CONTAINER SIZE"""
        self._testMethodDoc = "新建Shipping Advice数据,必填项验证,不填写CONTAINER SIZE"
        text = "新建Shipping Advice数据,必填项验证,不填写CONTAINER SIZE"
        status = self.field.no_container_size(self.driver, text)
        # expected = "INV P/L情報が不整備です、ご確認お願いします。"
        # self.assertEqual(expected, status)
        assert status == True


if __name__ == '__main__':
    unittest.main()
