'''
Created on 2019年5月22日

@author: chinasoft.xp.chen
'''

from time import sleep
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from business.Login import Login
from business.bl.BlOperate import BlOperate
from common.GetBl import getBl

class TestBl(unittest.TestCase):
     
    def setUp(self):
        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('window-size=1920x3000')
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(15)
        self.driver.set_script_timeout(15)
        self.driver.maximize_window()
        self.url = "https://sharpsit.jusdaglobal.com"
        
    #@unittest.skip(True)  
    def testBl01(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过B/L NO检索结果、核对全部集装箱信息送信成功"
        result = getBl().getDataBl()
        if(result[1].get("code")!=200):
            self.assertIn('送信済み', result[1].get("result"))
        bl=result[0]
        actual_text=b.bl01(driver,bl)
        self.assertIn('送信済み', actual_text)
        
    #@unittest.skip(True)    
    def testBl02(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过B/L NO检索结果、核对部分集装箱信息送信成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        actual_text=b.bl02(driver,bl)
        self.assertIn('送信済み', actual_text)
       
    #@unittest.skip(True)  
    def testBl03(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过B/L NO检索结果、不核对集装箱信息送信成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        actual_text=b.bl03(driver,bl)
        self.assertIn('送信済み',actual_text)
        
    #@unittest.skip(True)  
    def testBl04(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "没有BL附件资料送信失败"
        tip_text=b.bl04(driver,"GD558741")
        #print(tip_text)
        self.assertIn('BLまたはINV添付資料が無いので、',tip_text)
        
    #@unittest.skip(True)    
    def testBl05(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过D/O NO检索结果、核对全部集装箱信息送信成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        do = result[0]
        actual_text=b.bl05(driver,do)
        self.assertIn('送信済み', actual_text)
     
    #@unittest.skip(True)     
    def testBl06(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过D/O NO检索结果、核对部分集装箱信息送信成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        do = result[0]
        actual_text=b.bl06(driver,do)
        self.assertIn('送信済み', actual_text)    
     
    #@unittest.skip(True)  
    def testBl07(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过D/O NO检索结果、不核对集装箱信息送信成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        do = result[0]
        actual_text=b.bl07(driver,do)
        self.assertIn('送信済み', actual_text)   
        
    #以下用例都是检索条件的测试   
    
    def testBl08(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "不输入检索条件可以检索"
        num=b.bl08(driver)
        print(num)
        self.assertNotEqual(0, num)       
        
        
    def testBl09(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过海外取引先可以检索"
        getBl().getDataBl()
        num=b.bl09(driver)
        print(num)
        self.assertNotEqual(0, num) 
        
    def testBl10(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过B/L DATE检索成功"
        getBl().getDataBl()
        num=b.bl10(driver)
        print(num)
        self.assertNotEqual(0, num) 
        
    def testBl11(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过運送形態为SEA检索成功"
        getBl().getDataBl()
        num=b.bl11(driver)
        print(num)
        self.assertNotEqual(0, num)     
    
    def testBl12(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        sleep(3.5)
        b=BlOperate()
        self._testMethodDoc = "通过運送形態为AIR检索成功"
        num=b.bl12(driver)
        print(num)
        self.assertNotEqual(0, num)  
        
    def testBl13(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过送信状態为未送信检索成功"
        num=b.bl13(driver)
        print(num)
        self.assertNotEqual(0, num)  
    
    def testBl14(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过送信状態为送信済み检索成功"
        num=b.bl14(driver)
        print(num)
        self.assertNotEqual(0, num) 
        
    def testBl15(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过选择SJL輸入担当：NAOMI检索成功"
        num=b.bl15(driver)
        #print(num)
        self.assertNotEqual(0, num)
        
        
    def testBl16(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过D/O No和海外取引先组合检索成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        do = result[0]
        actual_text=b.bl16(driver,do)
        self.assertEqual(actual_text[0],do)
        self.assertEqual(actual_text[1],actual_text[2])
    
    def testBl17(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过D/O No和B/L No组合检索成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        dobl=b.bl17(driver,bl,bl)
        print(dobl)
        self.assertEqual(dobl[0],bl)
        self.assertEqual(dobl[1],bl)
        
    def testBl18(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过D/O No和B/L DATE组合检索成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        do = result[0]
        actual=b.bl18(driver,do)
        print(actual)
        self.assertEqual(actual[0],do)

   
    def testBl19(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过D/O No和運送形態组合检索成功 "
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        do = result[0]
        actual=b.bl19(driver,do)
        self.assertEqual(actual[0],do)
        self.assertEqual(actual[1],"SEA")
      
    def testBl20(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过D/O No和送信状態组合检索成功 "
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        do = result[0]
        actual=b.bl20(driver,do)
        print(actual)
        self.assertEqual(actual[0],do)
        self.assertEqual(actual[1],"未送信")   
        
    def testBl21(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过B/L No和海外取引先组合检索成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        actual=b.bl21(driver,bl)
        self.assertEqual(actual[0],bl)
        self.assertEqual(actual[1],actual[2])
        
    def testBl22(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过B/L No和B/L DATE组合检索成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        actual=b.bl22(driver,bl)
        #print(actual)
        self.assertEqual(actual[0],bl)
        # self.assertEqual(actual[1][-1:],actual[2][0:1])
    
    def testBl23(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过B/L No和運送形態组合检索成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        actual=b.bl23(driver,bl)
        #print(actual)
        self.assertEqual(actual[0],bl)
        self.assertEqual(actual[1],"SEA") 
    
    def testBl24(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过B/L No和送信状態组合检索成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        actual=b.bl24(driver,bl)
        #print(actual)
        self.assertEqual(actual[0],bl)
        self.assertEqual(actual[1],"未送信")
     
    def testBl25(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过输入所有条件检索成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        actual=b.bl25(driver,bl,bl)
        #print(actual)
        self.assertEqual(actual[0],actual[7])
        self.assertEqual(actual[1],bl)
        self.assertEqual(actual[2],bl)
        self.assertEqual(actual[4],"SEA")
        self.assertEqual(actual[5],"未送信")
      
    def testBl26(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过错误的B/L NO检索无结果"
        tip=b.bl26(driver,"21whdsafb")
        #print(tip)
        self.assertEqual(tip,"No data available")   
    
    def testBl27(self):
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(driver)
        b=BlOperate()
        self._testMethodDoc = "通过错误的D/O NO检索无结果"
        tip=b.bl27(driver,"21whdsafb")
        #print(tip)
        self.assertEqual(tip,"No data available")   

          
    def tearDown(self):
        self.driver.quit()
      
