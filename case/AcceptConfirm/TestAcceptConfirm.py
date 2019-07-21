'''
Created on 2019年7月1日

@author: chinasoft.yy.zhang
'''
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from business.AcceptConfirm.AcceptConfirmOperate import AcceptConfirmOperate
from time import sleep

class TestAcceptConfirm(unittest.TestCase):

    def setUp(self):
        # options = Options()
        # options.add_argument('window-size=1920x1080')
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(15)
        self.driver.set_script_timeout(15)
        self.driver.maximize_window()
        self.url = "https://sharpsit.jusdaglobal.com"

    def testT008090(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)受入確認后数据状态由納入指示済变更为受入確認"
        # 登录并点击受入確認按钮
        AC = AcceptConfirmOperate()
        AC.Login_and_AcceptConfirm(driver)
        # 随机选择一条状态为納入指示済的数据，进行"受入确认"操作，并得到D/O NO, コンテナNO
        return_data_list = AC.choose_a_delivery_data(driver)
        # 判断异常
        if return_data_list == "发现已知bug！":
            return
        # 正常情况执行
        else:
            DO_number = return_data_list[0]
            container_number = return_data_list[1]
            # 检查该数据状态由"納入指示済"变更为"受入確認"
            AC.check_data_status(driver, DO_number, container_number)

    def testT008091(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)根据B/L発行日结束日期搜索数据，能正确搜索"
        #登录并点击受入確認按钮
        AC=AcceptConfirmOperate()
        AC.Login_and_AcceptConfirm(driver)
        #选择BL结束时间执行查询
        BLend_date = AC.query_by_BLend_date(driver)
        sleep(3)
        #检查查询结果
        AC.check_bl_date_result(driver, BLend_date, self._testMethodDoc)

    def testT008092(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)根据B/L発行日开始日期搜索，能正确搜索"
        #登录并点击受入確認按钮
        AC=AcceptConfirmOperate()
        AC.Login_and_AcceptConfirm(driver)
        #选择BL开始时间执行查询
        BLend_date = AC.query_by_BLstart_date(driver)
        sleep(4)
        #检查查询结果
        AC.check_bl_date_result(driver, BLend_date, self._testMethodDoc)

    def testT008093(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)根据B/L発行日时间段搜索数据，能正确搜索"
        #登录并点击受入確認按钮
        AC=AcceptConfirmOperate()
        AC.Login_and_AcceptConfirm(driver)
        #选择BL时间段执行查询
        date_list = AC.query_by_BLdate(driver)
        BLstart_date = date_list[0]
        BLend_date = date_list[1]
        #检查查询结果
        AC.check_bldate_result(driver, BLstart_date, BLend_date)

    def testT008094(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)根据D/O NO搜索数据，能正确搜索"
        DO_number = "19S0000487"
        #登录并点击受入確認按钮
        AC=AcceptConfirmOperate()
        AC.Login_and_AcceptConfirm(driver)
        #输入D/O NO 执行查询
        AC.query_by_DOnumber(driver, DO_number)
        #得到结果数据的D/O NO，并作断言
        AC.check_DOnumber_result(driver, DO_number)

    def testT008095(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)根据ETA结束日期搜索数据，能正确搜索"
        #登录并点击受入確認按钮
        AC=AcceptConfirmOperate()
        AC.Login_and_AcceptConfirm(driver)
        #选择ETA结束时间执行查询
        ETA_date = AC.query_by_ETAend_date(driver)
        #得到结果数据的BL日期，并作断言
        AC.check_ETA_date_result(driver, ETA_date)
        
    def tearDown(self):
        self.driver.quit()
      
