"""
@author: wangqi
"""
import unittest
import os
from time import sleep
from selenium import webdriver
from business.Login import Login
from business.pllogin.PaidLogic import Logic
from util import log
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service


class PaidTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(30)
        self.driver.maximize_window()
        self.url = "https://sharpsit.jusdaglobal.com"
        # 登录
        try:
            self.driver.get(self.url)
        except TimeoutException as e:
            self.driver.quit()
            self.driver.get(self.url)
        sleep(3)
        self.login = Login()
        self.login.test_click_login_btn(self.driver)
        sleep(2)

    def test1DetaileddataAddition(self):
        #报告中的用例描述
        self._testMethodDoc = "INVOICE 详细数据添加";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test1(driver);
        # 验证arg1 != arg2, 相等则fail
        self.assertNotEqual('No data available', sucess_text)

    def test2NOretrieval(self):
        #报告中的用例描述
        self._testMethodDoc = "P/O NO检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test2(driver);
        # 验证arg1 != arg2, 相等则fail
        self.assertNotEqual('No data available', sucess_text)

    def test3InvalidRetrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "P/O NO无效检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test3(driver);
        # 验证arg1=arg2，不等则fail
        self.assertEqual('No data available', sucess_text)

    # @unittest.skip("用例不执行")
    def test4BusinessUnitScreeningAddData(self):
        #报告中的用例描述
        self._testMethodDoc = "事业本部筛选添加数据";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test4(driver);
        # 验证arg1 != arg2, 相等则fail
        self.assertNotEqual('No data available', sucess_text)

    def test5ScreeningAddData(self):
        #报告中的用例描述
        self._testMethodDoc = "LOT NO筛选添加数据";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test5(driver);
        # 验证arg1 != arg2, 相等则fail
        self.assertNotEqual('No data available', sucess_text)

    def test6InsidetheCommunityPinfan(self):
        #报告中的用例描述
        self._testMethodDoc = "社内品番筛选添加数据";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test6(driver);
        # 验证arg1 != arg2, 相等则fail
        self.assertNotEqual('No data available', sucess_text)

    def test7OffsitePinfan(self):
        #报告中的用例描述
        self._testMethodDoc = "社外品番筛选添加数据";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test7(driver);
        # 验证arg1 != arg2, 相等则fail
        self.assertNotEqual('No data available', sucess_text)

    def test8ScreeningAddData(self):
        #报告中的用例描述
        self._testMethodDoc = "SI.NO筛选添加数据"
        logs = log.log_message()
        driver = self.driver;
        sucess_text = Logic(driver).test8(driver)
        # 验证arg1 != arg2, 相等则fail
        self.assertNotEqual('No data available', sucess_text)


    def test9MultipleConstructionSearchAdditions(self):
        #报告中的用例描述
        self._testMethodDoc = "多条建检索添加";
        logs = log.log_message()
        driver = self.driver
        sucess_text = Logic(driver).test9(driver)
        # 验证arg1 != arg2, 相等则fail
        self.assertNotEqual('No data available', sucess_text)

    def test10MultipleConstructionSearchAdditions(self):
        #报告中的用例描述
        self._testMethodDoc = "多条建检索添加";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test10(driver);
        # 验证arg1=arg2，不等则fail
        self.assertEqual('No data available', sucess_text)

    def test11PLlandingfunction(self):
        #报告中的用例描述
        self._testMethodDoc = "P/L登陆功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test11(driver);
        # 验证arg1=arg2，不等则fail
        self.assertNotEqual('No data available', sucess_text)


    def test12PLloginAddMultipleFunctions(self):
        #报告中的用例描述
        self._testMethodDoc = "P/L登陆-添加多条功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test12(driver);
        # 验证arg1=arg2，不等则fail
        self.assertNotEqual('No data available', sucess_text)


    def test13ListDataQuantityModificationFunction(self):
        #报告中的用例描述
        self._testMethodDoc = "列表数据'数量'修改功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test13(driver);
        # 验证arg1=arg2，不等则fail
        self.assertNotEqual('No data available', sucess_text)


    def test14ListDataCountryofOriginModificationFunction(self):
        #报告中的用例描述
        self._testMethodDoc = "列表数据原产国修改功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test14(driver);
        # 验证arg1=arg2，不等则fail
        self.assertNotEqual('香港', sucess_text)


    def test15ListDataInputIdentificationNumberFunction(self):
        #报告中的用例描述
        self._testMethodDoc = "列表数据输入识别番号功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test15(driver);
        # 验证arg1=arg2，不等则fail
        self.assertNotEqual('No data available', sucess_text)


    def test16TypewritingStartEnd(self):
        #报告中的用例描述
        self._testMethodDoc = "输入Carton Start No和输入Carton End No功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test16(driver);
        # 验证arg1=arg2，不等则fail
        self.assertNotEqual('No data available', sucess_text)

    def test17inputNW(self):
        #报告中的用例描述
        self._testMethodDoc = "输入N/W功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test17(driver);
        # 验证arg1=arg2，不等则fail
        self.assertNotEqual('No data available', sucess_text)

    def test18EliminationFunction(self):
        #报告中的用例描述
        self._testMethodDoc = "消除功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test18(driver);
        # 验证arg1=arg2，不等则fail
        self.assertEqual('No data available', sucess_text)

    def test19EliminateCancellationFunction(self):
        #报告中的用例描述
        self._testMethodDoc = "消除取消功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test19(driver)
        # 验证arg1 != arg2, 相等则fail
        self.assertNotEqual('No data available', sucess_text)


    def test20PLBranchFunction(self):
        #报告中的用例描述
        self._testMethodDoc = "PL行分功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test20(driver);
        # 验证arg1 != arg2, 相等则fail
        self.assertNotEqual('No data available', sucess_text)


    def test21SaveQuantitativeAttributesSame(self):
        #报告中的用例描述
        self._testMethodDoc = "数量属性相同保存";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test21(driver);
        # 验证arg1=arg2，不等则fail
        self.assertEqual('保存が完了しました。', sucess_text)


    def test22QuantitativeAttributesArePreservedWithDifferentAttributes(self):
        #报告中的用例描述
        self._testMethodDoc = "数量属性不同同保存";
        logs = log.log_message()
        driver = self.driver;
        sucess_text = Logic(driver).test22(driver)
        # 	验证arg1=arg2，不等则fail
        self.assertEqual('PO出荷数量とPOのPackingList数量が不一致のため、保存できません。', sucess_text)


    def test23WeightloginFunction(self):
        #报告中的用例描述
        self._testMethodDoc = "重量登录功能"
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test23(driver)
        # 验证arg1 != arg2, 相等则fail
        self.assertNotEqual('No data available', sucess_text)


    def test24NonrepetitiveValidation(self):
        #报告中的用例描述
        self._testMethodDoc = "I/V NO不重复验证";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test24(driver);
        # 验证arg1=arg2，不等则fail
        self.assertEqual('INV番号はすでに存在しています。', sucess_text)



    def test25NOfunction(self):
        # 报告中的用例描述
        self._testMethodDoc = "I/V NO功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test25(driver);
        # 验证arg1=arg2，不等则fail
        self.assertEqual('保存が完了しました。', sucess_text)


    def test26inputGW(self):
        #报告中的用例描述
        self._testMethodDoc = "输入G/W功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test26(driver);
        # 验证arg1=arg2，不等则fail
        self.assertNotEqual('No data available', sucess_text)


    def test27inputM(self):
        #报告中的用例描述
        self._testMethodDoc = "输入M3功能";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic(driver).test27(driver);
        # 验证arg1=arg2，不等则fail
        self.assertNotEqual('No data available', sucess_text)


    def tearDown(self):
        self.driver.quit()


