"""
INV P/L登録模块
author:cjp
"""
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from business.Login import Login
from business.pllogin.PlFreePay import PlLogin
import time
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

class TestPlLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(30)
        self.driver.maximize_window()
        self.url = "https://sharpsit.jusdaglobal.com"
        number = 3
        success = False
        while number > 0 and not success:
            try:
                self.driver.get(self.url)
                success = True
            except TimeoutException as e:
                print('1111111111111111111111111111111111')
                number = number-1
                self.driver.quit()

        self.driver.implicitly_wait(30)
        time.sleep(2)
        self.login = Login()
        self.login.test_click_login_btn(self.driver)
        time.sleep(3)


    def tearDown(self):
        self.driver.quit()

    # @unittest.skip(u"无条件跳过此用例")
    def test001PayFree(self):
        self._testMethodDoc = "無償商品登録行追加无条件检索功能验证"
        p = PlLogin(self.driver)
        actualvalue = p.testFreePay()
        respectvalue = '無償商品登録行追加'
        self.assertEqual(actualvalue, respectvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test002SheNeiInsert(self):
        self._testMethodDoc = "社内品番检索功能验证"
        p = PlLogin(self.driver)
        respectvalue = 'DUNTK9890FMW0'
        actualvalue = p.sheneiinsert()
        self.assertEqual(actualvalue, respectvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test003SheNeiNodata(self):
        self._testMethodDoc = "社内品番无效检索功能验证"
        p = PlLogin(self.driver)
        respectvalue = 'No data available'
        actualvalue = p.sheneiNoData()
        self.assertEqual(actualvalue, respectvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test004SheWaiInsert(self):
        self._testMethodDoc = "社外品番检索功能验证"
        p = PlLogin(self.driver)
        respectvalue = 'DUNTK9890FMW0'
        actualvalue = p.shewaiinsert()
        self.assertEqual(actualvalue, respectvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test005SheWaiNodata(self):
        self._testMethodDoc = "社外品番无效检索功能验证"
        p = PlLogin(self.driver)
        respectvalue = 'No data available'
        actualvalue = p.shenwaiNoData()
        self.assertEqual(actualvalue, respectvalue)

   # @unittest.skip(u"无条件跳过此用例")
    def test006SheNeiWaiInsert(self):
        self._testMethodDoc = "社内品番和社外品番同时输入值验证"
        p = PlLogin(self.driver)
        respectvalue = 'MOCKUP'
        actualvalue = p.sheneiwaiinsert()
        self.assertIn(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test007PlLoginOne(self):
        self._testMethodDoc = "无偿新规P/L登出功能验证"
        p = PlLogin(self.driver)
        respectvalue = '1-1 of 1'
        actualvalue = p.PldengchuOne()
        self.assertEqual(respectvalue, actualvalue)

    def test008PlLoginTwo(self):
        self._testMethodDoc = "P/L登陆-添加多条功能验证"
        p = PlLogin(self.driver)
        respectvalue = '1-2 of 2'
        actualvalue = p.PlLoginTwo()
        self.assertEqual(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test009libiaoshuliang(self):
        self._testMethodDoc = "列表数据数量添加功能验证 "
        p = PlLogin(self.driver)
        respectvalue = '10'
        actualvalue = p.Plliebiaoshuliang()
        self.assertEqual(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test010fbodanjia(self):
        self._testMethodDoc = "列表数据FOB单面添加功能验证"
        p = PlLogin(self.driver)
        respectvalue = '100.00'
        actualvalue = p.PLfbodanjia()
        self.assertEqual(respectvalue, actualvalue)


    #@unittest.skip(u"无条件跳过此用例")
    def test011yuanchanguo(self):
        self._testMethodDoc = "列表数据原产国添加功能验证"
        p = PlLogin(self.driver)
        respectvalue = '日本'
        actualvalue = p.PLyuanchanguo()
        self.assertEqual(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test012shibiefanhao(self):
        self._testMethodDoc = "输入识别番号功能验证"
        p = PlLogin(self.driver)
        respectvalue = '999'
        actualvalue = p.PLshibiefanhao()
        self.assertEqual(respectvalue, actualvalue)


   # @unittest.skip(u"无条件跳过此用例")
    def test013CartonNo(self):
        self._testMethodDoc = "输入Carton Start No和输入Carton End No功能验证"
        p = PlLogin(self.driver)
        respectvalue = '50'
        actualvalue = p.PLcartonno()
        self.assertEqual(respectvalue, actualvalue)


    #@unittest.skip(u"无条件跳过此用例")
    def test014NW(self):
        self._testMethodDoc = "输入N/W功能验证"
        p = PlLogin(self.driver)
        respectvalue = '1'
        actualvalue = p.PLNW()
        self.assertEqual(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test015GW(self):
        self._testMethodDoc = "输入G/W功能验证"
        p = PlLogin(self.driver)
        respectvalue = '1'
        actualvalue = p.PLGW()
        self.assertEqual(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test016M3(self):
        self._testMethodDoc = "输入M3功能验证"
        p = PlLogin(self.driver)
        respectvalue = '1'
        actualvalue = p.PLM3()
        self.assertEqual(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test017ListXiaoChu(self):
        self._testMethodDoc = "List消除功能验证"
        p = PlLogin(self.driver)
        respectvalue = '削除成功しました。'
        actualvalue = p.PLlistxiaochu()
        self.assertEqual(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test018CancleListXiaoChu(self):
        self._testMethodDoc = "List消除功能验证"
        p = PlLogin(self.driver)
        respectvalue = 'RJ63ACL1D'
        actualvalue = p.PLcanclelistxiaochu()
        self.assertEqual(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test019PlPackageFengHang(self):
        self._testMethodDoc = "PL行分功能"
        p = PlLogin(self.driver)
        respectvalue = '1-2 of 2'
        actualvalue = p.PlPackageFenHang()
        self.assertEqual(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test020PackageListandINVOICE(self):
        self._testMethodDoc = "Package List详细和INVOICE 详细数量属性相同保存"
        p = PlLogin(self.driver)
        respectvalue = '保存が完了しました。'
        actualvalue = p.testPackageListandINVOICE()
        self.assertEqual(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test021PackageListandINVOICEUndifferent(self):
        self._testMethodDoc = "Package List详细和INVOICE数量属性不同同保存"
        p = PlLogin(self.driver)
        respectvalue = 'PO出荷数量とPOのPackingList数量が不一致のため、保存できません。'
        actualvalue = p.testPackageListandINVOICEunsame()
        self.assertEqual(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test022InsertUnexistIvo(self):
        self._testMethodDoc = "I/V NO保存功能验证"
        p = PlLogin(self.driver)
        respectvalue = '保存が完了しました。'
        actualvalue = p.testInsertUnexistIvo()
        self.assertEqual(respectvalue, actualvalue)

    #@unittest.skip(u"无条件跳过此用例")
    def test023InsertIvoNotsame(self):
        self._testMethodDoc = "I/V NO不重复功能验证"
        p = PlLogin(self.driver)
        respectvalue = 'INV番号はすでに存在しています。'
        actualvalue = p.InsertIvoNotsame()
        self.assertEqual(respectvalue, actualvalue)


    # def test024ZhongliangDenglu(self):
        # self._testMethodDoc = "重量登录功能验证"
        # p = PlLogin(self.driver)
        # respectvalue = '保存が完了しました。'
        # actualvalue = p.Plzhongliagndenglu()
        # self.assertEqual(respectvalue, actualvalue)


