'''
Created on 2019年5月22日

@author: chinasoft.xp.chen
'''
from selenium.webdriver.chrome.options import Options
import unittest

from selenium import webdriver

from business.Login import Login
from business.sendemail.SendOperate import SendOperate
from common.GetBl import getBl

class TestSendMail(unittest.TestCase):
    def setUp(self):
        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('window-size=1920x3000')
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.set_page_load_timeout(15)
        self.driver.set_script_timeout(15)
        self.driver.maximize_window()
        self.url='https://sharpsit.jusdaglobal.com/'
        
                
    #@unittest.skip(True)    
    def testSendMail01(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过B/L NO检索输入5个收件人和CC送信成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        actual_text=send.sendMail1(driver,bl)
        self.assertEqual('指示Mail送信済',actual_text) 
        
    #@unittest.skip(True)   
    def testSendMail02(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过B/L NO检索输入5个收件人和CC送信成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        do = result[0]
        actual_text=send.sendMail2(driver,do)
        self.assertEqual('指示Mail送信済',actual_text) 
        
    #@unittest.skip(True)    
    def testSendMail03(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过D/O NO检索输入纳入指示者1和CC送信成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        do = result[0]
        sucess_text=send.sendMail3(driver,do)
        self.assertIn('指示Mail送信済', sucess_text)
        
    #@unittest.skip(True)     
    def testSendMail04(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过B/L NO检索输入纳入指示者5和CC送信成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        sucess_text=send.sendMail4(driver,bl)
        self.assertIn('指示Mail送信済', sucess_text)

    #@unittest.skip(True) 
    def testSendMail05(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过B/L NO检索,输入1个收件人不输入CC送信成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        sucess_text=send.sendMail5(driver,bl) 
        self.assertIn('指示Mail送信済', sucess_text)
      
        
    #@unittest.skip(True)     
    def testSendMail06(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过输入所有搜索框精确检索送信成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        sucess_text=send.sendMail6(driver,bl,bl)
        self.assertIn('指示Mail送信済', sucess_text)
        
    #@unittest.skip(True)     
    def testSendMail07(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "不可以批量送信成功"
        listsucess=send.sendMail7(driver,"cxp")   #cxp006\cxp007
        #断言批量送信只送信成功1条，而非2条数据
        count=0 
        if ("指示Mail送信済" or "SA登録済")in listsucess:
            count+=1
        self.assertEqual(count,1)
    
    #@unittest.skip(True)        
    def testSendMail08(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "对已送信的可以进行送信解除"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        Remove_text=send.sendMail8(driver,bl)
        self.assertIn('指示Mail送信解除', Remove_text)     
        
    #@unittest.skip(True)        
    def testSendMail09(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "对已送信的可以批量解除送信"
        send.sendMail9(driver,"cxp")
        #self.assertEqual("指示Mail送信解除",Remove_text)
        
        
        
    #@unittest.skip(True)        
    def testSendMail10(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过B/L NO检索,不输入纳入指示者只输入CC送信失败"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        actual_text=send.sendMail10(driver,bl)
        self.assertIn("納入指示者を設定ください",actual_text)
        
    #@unittest.skip(True)        
    def testSendMail11(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过B/L NO检索,不输入纳入指示者和CC送信失败"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        actual_text=send.sendMail11(driver,bl)
        self.assertIn("納入指示者を設定ください",actual_text)    
        
    #以下都是关于检索条件的用例    
    #@unittest.skip(True)        
    def testSendMail12(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "不输入检索条件检索成功"
        actual_num=send.sendMail12(driver)
        print(actual_num)
        self.assertNotEqual(actual_num, 0)
    
    #@unittest.skip(True)        
    def testSendMail13(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过納入指示者检索成功"
        actual_num=send.sendMail13(driver)
        print(actual_num)
        self.assertNotEqual(actual_num, 0)
       
    
    #@unittest.skip(True)        
    def testSendMail14(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过纳入指示者、D/O NO组合检索成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        do = result[0]
        actual_num=send.sendMail14(driver,do)
        self.assertEqual(actual_num,do)
        
        
    #@unittest.skip(True)        
    def testSendMail15(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过纳入指示者、B/L NO组合检索成功"
        actual_num=send.sendMail15(driver,"cxp")
        self.assertIn("cxp",actual_num)
     
    #@unittest.skip(True)   
    def testSendMail16(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过纳入指示者、D/O NO、B/L NO组合检索成功"
        result = getBl().getDataBl()
        if (result[1].get("code") != 200):
            self.assertIn('送信済み', result[1].get("result"))
        bl = result[0]
        actual_num=send.sendMail16(driver,bl,bl)
        self.assertEqual(actual_num[0],bl)
        self.assertEqual(actual_num[1],bl)
        
    #@unittest.skip(True)    
    def testSendMail17(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过错误的D/O NO检索没有结果"
        nodata=send.sendMail17(driver,'QAZ5556')
        self.assertEqual(nodata,"No data available")
     
     
    #@unittest.skip(True)    
    def testSendMail18(self):
        driver=self.driver
        driver.get(self.url)
        login=Login()
        login.test_click_login_btn(driver)
        send=SendOperate()
        self._testMethodDoc = "通过错误的B/L NO检索没有结果"
        nodata=send.sendMail18(driver,'QAZ5556')
        self.assertEqual(nodata,"No data available")


    def tearDown(self):
        self.driver.quit()
      
       
        
        


