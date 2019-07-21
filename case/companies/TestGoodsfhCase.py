"""Created on 2019年7月8日

case操作类
@author: chinasoft.c.deng"""
import unittest
from selenium import webdriver
from business.Companies.GoodsfhBussinses import GoodsfhBussinses
GoodsfhBussinses=GoodsfhBussinses()
class TestGoodsfhCase(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.url = "https://sharpsit.jusdaglobal.com"
        driver = self.driver
        driver.get(self.url)
    def test01GoodsfNodata(self):
        self._testMethodDoc = "纳入指示_D/O分け_未选择任何数据时，点击D/O分け"
        r=GoodsfhBussinses.goodsfenNoData(self.driver)
        assert r is False
    def test02GoodsfManydata(self):
        self._testMethodDoc = "纳入指示_D/O分け_选择多条数据时，点击D/O分け"
        r=GoodsfhBussinses.goodsfManyData(self.driver)
        assert r is False
    def test03GoodsfNR(self):
        self._testMethodDoc = "纳入指示_D/O分け_纳入指示status为納入指示済时，点击D/O分け"
        r=GoodsfhBussinses.goodsfNR(self.driver)
        assert r is False
    #需要stackTypeId为null的特殊数据
    def test04GoodsfZS(self):
        self._testMethodDoc = "纳入指示_D/O分け_纳入指示status为指示Mail送信済时，点击D/O分け"
        exceptValue='詳細情報'
        doNum='19A0000484'
        r=GoodsfhBussinses.goodsfZS(self.driver,doNum)
        assert r == exceptValue
    # 需要stackTypeId为null的特殊数据
    def test05NoOperationSave(self):
        self._testMethodDoc = "纳入指示_D/O分け_详细情报页中无任何操作,点击保存"
        doNum='19A0000484'
        r = GoodsfhBussinses.NoOperationSave(self.driver,doNum)
        assert r is False
    # 需要stackTypeId为null的特殊数据
    def test06NoChoseSplit(self):
        self._testMethodDoc = "纳入指示_D/O分け_详细情报页中不选择任何数据,点击split"
        doNum = '19A0000484'
        expectValue = '少なくとも1つの項目を選んでください'
        r = GoodsfhBussinses.NoChoseSplit(self.driver,doNum)
        print(r)
        assert r == expectValue
    # 需要stackTypeId为null的特殊数据
    def test07ChoseDataSplit(self):
        self._testMethodDoc = "纳入指示_D/O分け_详细情报页中选择所有数据，点击split"
        doNum= '19A0000484'
        expectValue = '削除DO枝番'
        r = GoodsfhBussinses.ChoseDataSplit(self.driver,doNum)
        assert r == expectValue

    # 需要stackTypeId为null的特殊数据
    def test08ChoseDataSplitone(self):
        self._testMethodDoc = "纳入指示_D/O分け_详细情报页中选择一条数据，点击split"
        doNum= '19A0000484'
        expectValue = '削除DO枝番'
        r = GoodsfhBussinses.ChoseDataSplitone(self.driver,doNum)
        assert r == expectValue
    # 需要stackTypeId为null的特殊数据
    def test09SplitSave(self):
        self._testMethodDoc = "纳入指示_D/O分け_详细情报页中选择所有数据，点击split,点击保存"
        doNum='19S0000060'
        expectValue = '保存が完了しました。'
        r = GoodsfhBussinses.SplitSave(self.driver,doNum)
        assert r == expectValue
    #需要先有分け的货物的特殊数据,必须先执行testSplitSave用例,后执行此用例
    def test10GoodshZS(self):
        self._testMethodDoc = "纳入指示_D/O合併_指示Mail送信济时，选择一条数据，点击D/O合併"
        expectValue = '合併に成功する'
        doNum = '19S0000060'
        r = GoodsfhBussinses.GoodshZS(self.driver,doNum)
        assert r == expectValue
    def test11GoodshNoData(self):
        self._testMethodDoc = "纳入指示_D/O合併_未选择任何数据时，点击D/O合併"
        r=GoodsfhBussinses.goodshNoData(self.driver)
        assert r is False
    def test12GoodshManyData(self):
        self._testMethodDoc = "纳入指示_D/O合併_选择多条数据时，点击D/O合併"
        r=GoodsfhBussinses.goodshManyData(self.driver)
        assert r is False
    def test13GoodshNR(self):
        self._testMethodDoc = "纳入指示_D/O分け_纳入指示status为納入指示済时，点击D/O合併"
        r=GoodsfhBussinses.goodshNR(self.driver)
        assert r is False
    def test14Splitquit(self):
        self._testMethodDoc = "纳入指示_D/O分け_详细情报页中,点击退出"
        doNum='19A0000484'
        expectValue='納入指示'
        r = GoodsfhBussinses.SplitQuit(self.driver,doNum)
        assert r == expectValue

    def tearDown(self):
        self.driver.quit()