
import unittest
from selenium import webdriver
from business.Companies.SendEailBussinses import SendEailBussinses
from business.Companies.API1234 import Jiekou


sendEailBussinses = SendEailBussinses()

class TestSendEailCase(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.url = "https://sharpsit.jusdaglobal.com"
        driver = self.driver
        driver.get(self.url)
    
    
    def testNoCheckData(self):
        self._testMethodDoc = "纳入指示_送信_未选择任何数据时，送信"
        r = sendEailBussinses.noCheckData(self.driver)
        assert r == False

    #   纳入指示剂,选择多条已发送的纳入指示剂,需要设置符合条件的特殊数据D/O NO
    def testCheckManyDatan(self):
        self._testMethodDoc = "纳入指示_送信_选择多条已发送的纳入指示剂，送信"
        doNum = "19S0000200"
        r = sendEailBussinses.checkManyDatan(self.driver,doNum)
        print(r)
        assert r == "既に送信済み"

    #   纳入指示剂，选择单条已发送的纳入指示剂，需要设置符合条件的特殊数据D/O NO
    def testCheckManyDatano(self):
        self._testMethodDoc = "纳入指示_送信_选择单条已发送的纳入指示剂，送信"
        doNum = "19S0000031"
        r = sendEailBussinses.checkManyDatano(self.driver,doNum)
        assert r == "既に送信済み"

    #   指示Mail送信済时，纳入予定日时间为空，送信，需要设置符合条件的特殊参数D/O NO
    def testCheckDatazn(self):

        self._testMethodDoc = "纳入指示_送信_指示Mail送信済时，纳入予定日时间为空，送信"
        doNum = Jiekou().getDONO()
        if (doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        dn = doNum.get('result')
        r = sendEailBussinses.checkDatazn(self.driver,dn)
        assert r == "納入予定日は入力必須項目です"


    #   指示Mail送信済时，纳入场所、予定日、时间不为空点击送信  需要设置符合条件的特殊参数D/O NO
    def testCheckDataz(self):
        self._testMethodDoc = "纳入指示_送信_指示Mail送信済时，纳入场所、予定日、时间不为空，送信"
        doNum = Jiekou().getDONO()
        if (doNum.get("code") != 200):
            print("------实际返回结果------:" + doNum.get("result"))
            assert doNum.get("result") == False
        dn=doNum.get('result')
        r = sendEailBussinses.checkDataz(self.driver,dn)
        assert r == "納入指示済"

    def tearDown(self):
        self.driver.quit()