import unittest
from business.test_customs.NewBuilt import NewBuilt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from business.Login import Login
from time import sleep

class TestNewBuilt(unittest.TestCase,NewBuilt):

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

    def test_newBuiltLoadPort(self):
        u'''[txq]-78參照新規作成，添加2条積出港不同的数据'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        text = self.newBuiltLoadPort(driver)  # 弹框提示内容
        self.assertEqual(text, 'S/Aの積出港・陸揚港とINVの積出港・陸揚港が不一致のため、再度確認してください')

    def test_newBuiltToPort(self):
        u'''[txq]-79參照新規作成，添加2条積出港不同的数据'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        text = self.newBuiltToPort(driver)  # 弹框提示内容
        self.assertEqual(text, 'S/Aの積出港・陸揚港とINVの積出港・陸揚港が不一致のため、再度確認してください')

    def test_newBuiltStartGreaterEnd(self):
        u'''[txq]-81參照新規作成，新建INV数据，修改Carton Start No和Carton end No，且start>end'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        flag = self.newBuiltStartGreaterEnd(driver)
        self.assertFalse(flag)

    def test_newBuiltCancel(self):
        u'''[txq]-87新建数据时返回'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        text = self.newBuiltCancel(driver)  # 弹框提示内容
        self.assertEqual(text, 'No data available')

    def test_newBuiltReferLoadPort(self):
        u'''[txq]-88延用以前的数据信息追加積出港不同的数据'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        text = self.newBuiltReferLoadPort(driver)  # 弹框提示内容
        self.assertEqual(text, 'S/Aの積出港・陸揚港とINVの積出港・陸揚港が不一致のため、再度確認してください')

    def test_newBuiltReferToPort(self):
        u'''[txq]-89延用以前的数据信息追加陸揚港不同的数据'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        text = self.newBuiltReferToPort(driver)  # 弹框提示内容
        self.assertEqual(text, 'S/Aの積出港・陸揚港とINVの積出港・陸揚港が不一致のため、再度確認してください')

    def test_newBuiltAgoneAdd(self):
        u'''[txq]-91延用以前的数据信息创建新数据时返回'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        flag = self.newBuiltAgoneAdd(driver)
        self.assertTrue(flag)

    def test_newBuiltModify(self):
        u'''[txq]-85新建Shipping Advice数据，修改Carton Start No和Carton end No，且start>end'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        flag = self.newBuiltModify(driver)
        self.assertFalse(flag)

    def test_newBuiltUnfilled(self):
        u'''[txq]-86新建数据时必填项有一个未填，送信'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        text = self.newBuiltUnfilled(driver)  # 弹框提示内容
        self.assertEqual(text, 'House B/L NO必要である')
        # self.assertEqual(text[1],'有償INVが無いと、SAを作成できません。')

    def test_newBuiltLetters(self):
        u'''[txq]-82參照新規作成，只填写必填项，送信时取消'''
        driver = self.driver
        driver.get(self.url)
        login = Login()
        login.test_click_login_btn(self.driver)
        sleep(5)
        text=self.newBuiltLetters(driver)
        self.assertIn(text, '重複B/L No.が存在します。poNo:')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(TestNewBuilt('test_newBuiltLetters'))
#     runner = unittest.TextTestRunner()
#     runner.run(suite)