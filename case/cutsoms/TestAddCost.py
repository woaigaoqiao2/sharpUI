import unittest
from selenium import webdriver
from business.test_customs.AddCost import ModifyNo
from selenium.webdriver.chrome.options import Options
from business.Login import Login
from time import sleep

class TestAddCost(unittest.TestCase,ModifyNo):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)
        self.driver.set_script_timeout(10)
        self.url = "https://sharpsit.jusdaglobal.com"
        # options = Options()
        # options.add_argument('window-size=1920x1080')
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # self.driver = webdriver.Chrome(chrome_options=options)

    def test_modifyNo(self):
        u'''[txq]-64新建Shipping Advice数据，修改Carton Start No和Carton end No'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        modify = ModifyNo()
        result = modify.modifyNo(driver)
        self.assertEqual(result[1]-result[0]+1,result[2])

    def test_sendMessage(self):
        u'''[txq]-将编辑成功的数据送信'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        text = self.sendMessage(driver)
        self.assertIn(text,'SA送信成功しました。')


    def tearDown(self):
        self.driver.quit()


# if __name__ == '__main__':
#     # unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(TestAddCost('test_sendMessage'))
#     runner = unittest.TextTestRunner()
#     runner.run(suite)