"""
INV P/L登録模块中的无償新規
@author: chinasoft.tp.deng
"""
import unittest
from time import sleep
from selenium import webdriver
from business.Login import Login
from business.pllogin.FreeNewOrders import FreeNewOrders
from pageElement.pllogin.FreeNew import FreeNew
from util import log
from selenium.webdriver.chrome.options import Options

class TestFreeNewOrders(unittest.TestCase):
    """在无償新規中新建订单"""

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
        self.free = FreeNewOrders()
        self.freeEle = FreeNew()
        # 登录
        self.login.test_click_login_btn(self.driver)
        sleep(5)

    def test01CheckPOAddOne(self):
        """INV P/L登录无償新規，选择1条P/O记录进行P/L登录，Package List显示对应的记录存"""
        self._testMethodDoc = "INV P/L登录无償新規，选择1条P/O记录进行P/L登录，Package List显示对应的记录存"
        result = self.free.checkPOAddOne(self.driver)
        # print(result)
        # 断言
        # INVOICE 详细 的社内品番(期望值)
        exCoNum = self.driver.find_element(*self.freeEle.POCoNum1st_element).text
        # INVOICE 详细 的数量(期望值)
        exPLNum = result[2]
        # 实际值
        acCoNum = result[0]
        acPLNum = result[1]
        self.logs.info_log(self.assertEqual(exCoNum, acCoNum))
        self.logs.info_log(self.assertEqual(exPLNum, acPLNum))

    def test02CheckPOAddTwo(self):
        """INV P/L登录无償新規，不选择P/O记录进行P/L登录，Package List不显示对应的记录存"""
        self._testMethodDoc = "INV P/L登录无償新規，不选择P/O记录进行P/L登录，Package List不显示对应的记录存"
        result = self.free.checkPOAddTwo(self.driver)
        # 断言
        # 实际值
        expect_text = "No data available"
        actual_text = result
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test03CheckPOAddThree(self):
        """INV P/L登录无償新規，选择2条P/O记录进行P/L登录，Package List显示对应的记录存"""
        self._testMethodDoc = "INV P/L登录无償新規，选择2条P/O记录进行P/L登录，Package List显示对应的记录存"
        result = self.free.checkPOAddThree(self.driver)
        # 断言
        # INVOICE 详细 第一条的社内品番期望值)
        exCoNum1st = self.driver.find_element(*self.freeEle.POCoNum1st_element).text
        # INVOICE 详细 第二条的社内品番(期望值)
        exCoNum2nd = self.driver.find_element(*self.freeEle.POCoNum2nd_element).text
        # 实际值
        acCoNum1st = result[0]
        acCoNum2nd = result[1]
        self.logs.info_log(self.assertEqual(exCoNum1st, acCoNum1st))
        self.logs.info_log(self.assertEqual(exCoNum2nd, acCoNum2nd))

    def test04CheckPLInput(self):
        """INV P/L登录无償新規，P/O进行P/L登录，填写数量、N/W、G/W、M3"""
        self._testMethodDoc = "INV P/L登录无償新規，P/O进行P/L登录，填写数量、N/W、G/W、M3"
        result = self.free.checkPLInput(self.driver)
        # 断言
        expect_text = "OK"
        actual_text = result
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test05NotSelPODel(self):
        """INV P/L登录无償新規，P/O进行P/L登录，在INVOCIE详情中不选择P/O记录执行删除操作"""
        self._testMethodDoc = "INV P/L登录无償新規，P/O进行P/L登录，在INVOCIE详情中不选择P/O记录执行删除操作"
        result = self.free.notSelPODel(self.driver)
        # 断言
        expect_text = "OK"
        actual_text = result
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test06NotSelPLDel(self):
        """INV P/L登录无償新規，P/O进行P/L登录，在Package List详细中不选择P/O记录执行删除操作"""
        self._testMethodDoc = "INV P/L登录无償新規，P/O进行P/L登录，在Package List详细中不选择P/O记录执行删除操作"
        result = self.free.notSelPLDel(self.driver)
        # 断言
        expect_text = "OK"
        actual_text = result
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test07FreeNewSuc(self):
        """INV P/L登录无偿新规，运输形态选择SEA，验证保存保存"""
        self._testMethodDoc = "INV P/L登录无偿新规，运输形态选择SEA，验证保存成功"
        result = self.free.freeNewSuc(self.driver)
        # 断言
        expect_text = result[1]
        actual_text = result[0]
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test08NotInputIV(self):
        """INV P/L登录无偿新规，I/V NO不输入保存"""
        self._testMethodDoc = "INV P/L登录无偿新规，I/V NO不输入保存"
        result = self.free.notInputIV(self.driver)
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
            self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def test09IVExceedLimit(self):
        """INV P/L登录无偿新规，IV/NO订单号长度超过7个字符"""
        self._testMethodDoc = "INV P/L登录无偿新规，IV/NO订单号长度超过7个字符"
        result = self.free.IVExceedLimit(self.driver)
        # 断言
        expect_text = "INV.Noは7桁以内でご記入ください。"
        actual_text = result
        self.logs.info_log(self.assertEqual(expect_text, actual_text))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
