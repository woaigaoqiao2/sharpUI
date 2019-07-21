"""
INV P/L登録模块中的无償新規
@author: 王琪
"""

import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from business.Login import Login
from business.pllogin.InvRegistrationLogic import Logic
from util import log


class InvRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
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
        sleep(4)
        self.login = Login()
        self.login.test_click_login_btn(self.driver)
        sleep(1)

    def test1UnconditionalRetrieval(self):
        #报告中的用例描述
        self._testMethodDoc = "无条件检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test1(driver);
        # 验证arg1 != arg2, 相等则fail
        self.assertNotEqual('No data available', sucess_text)

    def test2IVNote(self):
        #报告中的用例描述
        self._testMethodDoc = "I/V NO检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test2(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('5024040', sucess_text));


    def test3OverseasCitationFirstRetrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "海外取引先检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test3(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('77512 - FIH(HONG KONG)LIMITED', sucess_text));

    def test4IVNOInvalidRetrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "I/V NO无效检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test4(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # 验证arg1=arg2，不等则fail
        logs.info_log(self.assertEqual('No data available', sucess_text));

    def test5retrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "P/O NO检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test5(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # 验证arg1 != arg2, 相等则fail
        logs.info_log(self.assertNotEqual('No data available', sucess_text));

    def test6InvalidRetrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "P/O NO无效检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test6(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        logs.info_log("实际运行结果为：" + sucess_text);
        # 验证arg1=arg2，不等则fail
        logs.info_log(self.assertEqual('No data available', sucess_text));

    def test7AccumulatedOutboundSearch(self):
        # 报告中的用例描述
        self._testMethodDoc = "积出港检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test7(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('SHA - ＳＨＡＮＧＨＡＩ', sucess_text));



    def test8TransportMorphologicalRetrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "输送形态检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test8(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('SEA', sucess_text));

    def test9FinalInclusionInSiteRetrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "最终纳入场所检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test9(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # 验证arg1是arg2的子串，不是则fail
        logs.info_log(self.assertIn('（健康環境）サービスパーツ倉庫', sucess_text));

    def test10LuyangPortSearch(self):
        # 报告中的用例描述
        self._testMethodDoc = "陸揚港检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test10(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # 验证arg1是arg2的子串，不是则fail
        logs.info_log(self.assertIn('OSK - 大阪港', sucess_text));


    def test11InvolvedPlaceActorRetrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "纳入场所担当者检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test11(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('No data available', sucess_text))


    def test12EstablishedValueRetrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "建值检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test12(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('FCA', sucess_text));


    def test13CurrencyRetrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "通货检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test13(driver);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('FCA', sucess_text));

    def test14MultiConditionalRetrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "多条件检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test14(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('FCA', sucess_text));

    # @unittest.skip("用例不执行")
    def test15NORetrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "Lot NO检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test15(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # 验证arg1 != arg2, 相等则fail
        logs.info_log(self.assertNotEqual('No data available', sucess_text));

    def test16ETDretrieval(self):
        # 报告中的用例描述
        self._testMethodDoc = "ETD检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test16(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # 验证arg1 != arg2, 相等则fail
        logs.info_log(self.assertNotEqual('No data available', sucess_text));


    def test17MakeDailySearch(self):
        # 报告中的用例描述
        self._testMethodDoc = "I/V做成日检索";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test17(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # 验证arg1 != arg2, 相等则fail
        logs.info_log(self.assertNotEqual('No data available', sucess_text));


    def test18TimeMultiConditionalQuery(self):
        # 报告中的用例描述
        self._testMethodDoc = "时间多条件查询";
        logs = log.log_message();
        driver = self.driver;
        sucess_text = Logic().test18(driver);
        logs.info_log("实际运行结果为：" + sucess_text);
        # 验证arg1 != arg2, 相等则fail
        logs.info_log(self.assertNotEqual('No data available', sucess_text));

    def tearDown(self):
        self.driver.quit()

