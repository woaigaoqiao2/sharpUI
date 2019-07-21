'''
Created on 2019年7月4日

@author: chinasoft.yy.zhang
'''

import unittest
from time import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from business.ShippingAdvice.ShippingAdviceOperate import ShippingAdviceOperate

class TestShippingAdvice(unittest.TestCase):
     
    def setUp(self):
        # options = Options()
        # options.add_argument('window-size=1920x1080')
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(15)
        self.driver.set_script_timeout(15)
        self.driver.maximize_window()
        self.url = "https://sharpsit.jusdaglobal.com"

    def testT008096(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)根据依賴日时间段搜索数据，能正确搜索"
        #登录并点击“S/A登録”
        SA=ShippingAdviceOperate()
        SA.Login_and_ShippingAdvice(driver)
        #选择依頼日时间段执行查询
        date_list = SA.query_by_rely_date(driver)
        rely_start_date = date_list[0]
        rely_end_date = date_list[1]
        #检查查询结果
        SA.check_rely_date_result(driver, rely_start_date, rely_end_date)

    def testT008097(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)ETA时间在ETD之前不能新建Shipping Advice数据"
        #登录并点击“S/A登録”
        SA=ShippingAdviceOperate()
        SA.Login_and_ShippingAdvice(driver)
        #追加情报
        SA.random_add_information(driver)
        #判断ETD日期前一天不可点击
        SA.check_ETAdate_status(driver)

    def testT008098(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)新建Shipping Advice，添加2个積出港不同的数据，追加失败"
        #登录并点击“S/A登録”
        SA=ShippingAdviceOperate()
        SA.Login_and_ShippingAdvice(driver)
        #追加情报(不同積出港)
        SA.add_info_by_diff_delivery_port(driver)
        #检查错误提示
        SA.check_failed_tip(driver)

    def testT008099(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)新建Shipping Advice，添加2个陸揚港不同的数据，追加失败"
        #登录并点击“S/A登録”
        SA=ShippingAdviceOperate()
        SA.Login_and_ShippingAdvice(driver)
        #追加情报(不同陸揚港)
        SA.add_info_by_diff_unloading_port(driver)
        #检查错误提示
        SA.check_failed_tip(driver)

    def testT008100(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)新建时选择货物拆分，用多个集装箱装货，可以成功保存"
        BLnumber = str(time())[:-8]
        #登录并点击“S/A登録”
        SA=ShippingAdviceOperate()
        SA.Login_and_ShippingAdvice(driver)
        #追加情报
        SA.random_add_information(driver)
        #点击行分け按钮，验证数据增加一条
        SA.check_PL_number(driver)
        #保存運送情報,检查成功提示
        SA.save_transport_info(driver, BLnumber)
        # 检查状态变为SA一時保存
        SA.check_status(driver, BLnumber)

    def testT008102(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)延用以前的数据信息创建一条積出港和陸揚港相同的海关数据，能成功创建"
        BLnumber = str(time())[:-8]
        #登录并点击“S/A登録”
        SA=ShippingAdviceOperate()
        SA.Login_and_ShippingAdvice(driver)
        #点击參照新規作成
        SA.reference_create(driver)
        #清除積出港陸揚港默认值
        SA.clear_port__data(driver)
        #追加情报(相同積出港相同陸揚港)
        SA.add_info_by_same_port(driver, BLnumber)

    def testT008103(self):
        driver = self.driver
        driver.get(self.url)
        self._testMethodDoc = "(zyy)编辑时选择货物拆分，用多个集装箱装货，可以成功保存"
        BLnumber = str(time())[:-8]
        # 登录并点击“S/A登録”
        SA = ShippingAdviceOperate()
        SA.Login_and_ShippingAdvice(driver)
        # 点击編集
        SA.click_edit_button(driver)
        # 点击行分け按钮
        SA.click_sorting_button(driver)
        #保存運送情報,检查成功提示
        SA.save_transport_info(driver, BLnumber)
        #检查状态变为SA一時保存
        SA.check_status(driver, BLnumber)


    def tearDown(self):
        self.driver.quit()
      
