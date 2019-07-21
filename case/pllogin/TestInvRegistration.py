"""
wuxiaodong
@author: chinasoft.tp.deng
"""

import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from business.pllogin.InvRegistrationLogic1 import Logic
from business.Login import Login
from util import log


class TestInvRegistration(unittest.TestCase):

    def setUp(self):
        # 无头
        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument("--start-maximized")
        # self.driver = webdriver.Chrome(chrome_options=options)
        # windows
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(15)
        self.driver.set_script_timeout(15)
        self.driver.maximize_window()
        self.url = "https://sharpsit.jusdaglobal.com"
        # self.url = "https://sharpuat.jusdaglobal.com"

    def test15(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录无偿新规选择P/O记录填写数量、FOB単価进行P/L登录";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(3)
        sucess_text = Logic().test15(driver);
        logs.info_log(self.assertIn('OK', sucess_text));

    def test16(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录无偿新规选择P/O记录进行P/L登录，填写Carton Start No，Carton Start No";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(3)
        sucess_text = Logic().test16(driver);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('OK', sucess_text));

    def test17(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录无偿新规选择P/O记录进行P/L登录，填写识别番号 ";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(3)
        sucess_text = Logic().test17(driver);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('OK', sucess_text));

    def test18(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录无偿新规选择P/O记录进行P/L登录，在INVOCIE详情中选择P/O记录执行删除操作";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(3)
        sucess_text = Logic().test18(driver);
        expect_result = "削除成功しました。";
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn(expect_result, sucess_text));

    def test19(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录无偿新规选择P/O记录进行P/L登录，在Package List详细中选择P/O记录执行删除操作";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(3)
        sucess_text = Logic().test19(driver);
        expect_result = "削除成功しました。";
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn(expect_result, sucess_text));

    def test20(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录无偿新规,运输形态选择AIR保存且检索成功";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(3)
        sucess_text = Logic().test20(driver);
        actual_result = sucess_text[0]
        expext_result = sucess_text[1]
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertEqual(actual_result, expext_result));

    def test21(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录选择新增的I/V NO订单记录修改通货并保存";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(3)
        sucess_text = Logic().test21(driver);
        # expect_result = "保存が完了しました。"
        expect_result = "OK"
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn(expect_result, sucess_text));

    def test22(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录选择新增的I/V NO订单记录修改建值并保存";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(3)
        sucess_text = Logic().test22(driver);
        # expect_result = "保存が完了しました。"
        expect_result = "OK"
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn(expect_result, sucess_text));

    def test23(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录选择新增的I/V NO订单记录编集不保存";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(3)
        sucess_text = Logic().test23(driver);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('OK', sucess_text));

    def test24(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录有偿新规,填写基础情报信息I/V NO、I/V作成日、ETD保存且检索成功";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(5)
        sucess_text = Logic().test24(driver);
        # expecte_result = sucess_text[0]
        # actual_result = sucess_text[1]
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        # logs.info_log(self.assertEqual(expecte_result, actual_result));
        logs.info_log(self.assertIn('OK', sucess_text))

    def test25(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录无偿新规,建值不选择保存";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(3)
        sucess_text = Logic().test25(driver);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('OK', sucess_text));

    def test26(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录无偿新规,通货不选择保存";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(3)
        sucess_text = Logic().test26(driver);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('OK', sucess_text));

    def test27(self):
        # 报告中的用例描述
        self._testMethodDoc = "INV P/L登录有偿新规输送形态不选择保存";
        logs = log.log_message();
        driver = self.driver;
        driver.get(self.url);
        Login().test_click_login_btn(driver);
        sleep(3)
        sucess_text = Logic().test27(driver);
        # self.assertIn(a,b) 判断a in b是否成立，正确则True，否则为False
        logs.info_log(self.assertIn('OK', sucess_text));

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
