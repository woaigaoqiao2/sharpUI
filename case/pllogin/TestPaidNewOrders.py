"""
INV P/L登録模块中的有償新規
@author: chinasoft.tp.deng
"""
import unittest
from time import sleep
from selenium import webdriver
from business.Login import Login
from business.pllogin.PaidNewOrders import PaidNewOrders
from pageElement.pllogin.PaidNew import PaidNew
from util import log
from selenium.webdriver.chrome.options import Options

class TestPaidNewOrders(unittest.TestCase):
    """在有償新規中新建订单"""

    def setUp(self):
        # 无头
        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument("--start-maximized")
        # self.driver = webdriver.Chrome(chrome_options=options)
        # Windows
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(15)
        self.driver.set_script_timeout(15)
        self.driver.maximize_window()
        self.url = "https://sharpsit.jusdaglobal.com"
        # self.url = "https://sharpuat.jusdaglobal.com"
        self.driver.get(self.url)
        self.logs = log.log_message()
        self.login = Login()
        self.paid = PaidNewOrders()
        self.paidEle = PaidNew()
        # 登录
        self.login.test_click_login_btn(self.driver)
        sleep(3)

    def test01PaidNewSuc(self):
        """INV P/L登录有偿新规，验证有偿新规新增成功"""
        self._testMethodDoc = "INV P/L登录有偿新规，验证有偿新规新增成功"
        result = self.paid.paidNewSuc(self.driver)
        # 断言
        expect_text = result[1]
        actual_text = result[0]
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test02NotFillIV(self):
        """INV P/L登录有偿新规，I/V NO不填保存"""
        self._testMethodDoc = "INV P/L登录有偿新规，I/V NO不填保存"
        result = self.paid.notFillIV(self.driver)
        if result == "":
            # 断言
            expect_text = ""
            actual_text = result
            self.logs.info_log(self.assertEqual(expect_text, actual_text))
        elif result == None:
            # 断言
            expect_text = None
            actual_text = result
            self.logs.info_log(self.assertEqual(expect_text, actual_text))
        else:
            # 断言
            expect_text = "未知エラーが発生しましたので、IT担当に問い合わせください。"
            actual_text = result
            # print(f"断言\n预期值:{expect_text}\n实际值{actual_text}")
            self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test03NoMarket(self):
        """INV P/L登录有偿新规，建值不选择保存"""
        self._testMethodDoc = "INV P/L登录有偿新规，建值不选择保存"
        result = self.paid.noMarket(self.driver)
        # 断言
        expect_text = "OK"
        actual_text = result
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test04CheckPOAdd(self):
        """INV P/L登录有偿新规，选择商品进行P/L登录，Package List详细中数据同步"""
        self._testMethodDoc = "INV P/L登录有偿新规，选择商品进行P/L登录，Package List详细中数据同步存"
        result = self.paid.checkPOAdd(self.driver)
        # 断言
        # INVOICE 详细 第一条的P/O NO、社内品番、品種期望值)
        exPONO = self.driver.find_element(*self.paidEle.PONO1st_element).text
        exCoNum = self.driver.find_element(*self.paidEle.POCoNum1st_element).text
        exKind = self.driver.find_element(*self.paidEle.POKind1st_element).text
        # 实际值
        acPONO = result[0]
        acCoNum = result[1]
        acKind = result[2]
        self.logs.info_log(self.assertEqual(exPONO, acPONO))
        self.logs.info_log(self.assertEqual(exCoNum, acCoNum))
        self.logs.info_log(self.assertEqual(exKind, acKind))

    def test05ChangeTrans(self):
        """选择新增的运输形态为Sea的I/V NO记录,修改运输形态为Air"""
        self._testMethodDoc = "选择新增的运输形态为Sea的I/V NO记录,修改运输形态为Air"
        result = self.paid.changeTrans(self.driver)
        if result == "":
            # 断言
            expect_text = ""
            actual_text = result
            self.logs.info_log(self.assertEqual(expect_text, actual_text))
        elif result == None:
            # 断言
            expect_text = None
            actual_text = result
            self.logs.info_log(self.assertEqual(expect_text, actual_text))
        else:
            # 断言
            expect_text = "保存が完了しました。"
            actual_text = result
            self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test06PaidDfaultSuc(self):
        """INV P/L登录有偿新规，有偿新规默认新增成功"""
        self._testMethodDoc = "INV P/L登录有偿新规，有偿新规默认新增成功"
        result = self.paid.paidDfaultSuc(self.driver)
        # 断言
        expect_text = result[1]
        actual_text = result[0]
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test07CheckPOAddNoNum(self):
        """INV P/L登录有偿新规，选择商品不修改数量进行P/L登录，Package List详细中数据同步"""
        self._testMethodDoc = "INV P/L登录有偿新规，选择商品不修改数量进行P/L登录，Package List详细中数据同步存"
        result = self.paid.checkPOAddNoNum(self.driver)
        # 断言
        # INVOICE 详细 第一条的P/O NO、社内品番、品種期望值)
        exPONO = self.driver.find_element(*self.paidEle.PONO1st_element).text
        exCoNum = self.driver.find_element(*self.paidEle.POCoNum1st_element).text
        exKind = self.driver.find_element(*self.paidEle.POKind1st_element).text
        # 实际值
        acPONO = result[0]
        acCoNum = result[1]
        acKind = result[2]
        self.logs.info_log(self.assertEqual(exPONO, acPONO))
        self.logs.info_log(self.assertEqual(exCoNum, acCoNum))
        self.logs.info_log(self.assertEqual(exKind, acKind))

    def test08AddConNo(self):
        """INV P/L登录有償新規P/L登录后,填写识别番号"""
        self._testMethodDoc = "INV P/L登录有償新規P/L登录后,填写识别番号"
        result = self.paid.addConNo(self.driver)
        # 断言
        expect_text = "OK"
        actual_text = result
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test09AddConSt(self):
        """INV P/L登录有償新規P/L登录后,填写集装箱开始号"""
        self._testMethodDoc = "INV P/L登录有償新規P/L登录后,填写集装箱开始号"
        result = self.paid.addConSt(self.driver)
        # 断言
        expect_text = "OK"
        actual_text = result
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test10AddConEd(self):
        """INV P/L登录有償新規P/L登录后,填写集装箱结束号"""
        self._testMethodDoc = "INV P/L登录有償新規P/L登录后,填写集装箱结束号"
        result = self.paid.addConEd(self.driver)
        # 断言
        expect_text = "OK"
        actual_text = result
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test11AddConNW(self):
        """INV P/L登录有償新規P/L登录后,填写净重"""
        self._testMethodDoc = "INV P/L登录有償新規P/L登录后,填写净重"
        result = self.paid.addConNW(self.driver)
        # 断言
        expect_text = "OK"
        actual_text = result
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test12AddConGW(self):
        """INV P/L登录有償新規P/L登录后,填写毛重"""
        self._testMethodDoc = "INV P/L登录有償新規P/L登录后,填写毛重"
        result = self.paid.addConGW(self.driver)
        # 断言
        expect_text = "OK"
        actual_text = result
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test13AddConM3(self):
        """INV P/L登录有償新規P/L登录后,填写体积"""
        self._testMethodDoc = "INV P/L登录有償新規P/L登录后,填写体积"
        result = self.paid.addConM3(self.driver)
        # 断言
        expect_text = "OK"
        actual_text = result
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
