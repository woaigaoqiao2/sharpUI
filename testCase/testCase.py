from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from common.login import login
from configuration.Configuration import Config
import unittest


class Test(unittest.TestCase):


    def setUp(self):
#         options = Options()
#         options.add_argument('--headless')
#         self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        config = Config()
        self.url = config.getConfigUrl()


    def tearDown(self):
        self.driver.quit()


    def testName(self):
        driver = self.driver
        driver.get(self.url)
        login(driver)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()