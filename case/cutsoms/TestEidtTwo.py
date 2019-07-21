from business.test_customs.editTwo import Edit
import unittest
from selenium import webdriver
from util.ElementUtil import ElementUtil
from selenium.webdriver.chrome.options import Options
from business.Login import Login
from time import sleep

class TestEidt(unittest.TestCase,Edit):

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

    def test_editLoadPort(self):
        u'''[txq]-3编辑状态为SA一時保存的数据，添加積出港不同的数据'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        text = self.editLoadPort(driver)    #弹框提示内容
        self.assertEqual(text,'S/Aの積出港・陸揚港とINVの積出港・陸揚港が不一致のため、再度確認してください')

    def test_editToPort(self):
        u'''[txq]-4编辑状态为SA一時保存的数据，添加陸揚港不同的数据'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        text = self.editToPort(driver)    #弹框提示内容
        self.assertEqual(text,'S/Aの積出港・陸揚港とINVの積出港・陸揚港が不一致のため、再度確認してください')

    def test_editCancel(self):
        u'''[txq]-90编集数据时返回'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        flag = self.editCancel(driver)  # 返回假
        self.assertFalse(flag)

    def test_editStartGreaterEnd(self):
        u'''[txq]-75编辑状态为SA一時保存的数据，修改Carton Start No和Carton end No，且start>end'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        flag = self.editStartGreaterEnd(driver)  # 返回假
        self.assertFalse(flag)

    def test_editCancelContainer(self):
        u'''[txq]-83取消多个集装箱装货'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        flag = self.editCancelContainer(driver)
        self.assertTrue(flag)

    def test_editLetterCancel(self):
        u'''[txq]-77编辑状态为SA一時保存的数据，只填写必填项，送信时取消'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        flag = self.editLetterCancel(driver)  # 返回假
        self.assertFalse(flag)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestEidt('test_editCancelContainer'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)