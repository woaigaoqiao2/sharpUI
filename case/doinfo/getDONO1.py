''''
获取点击完配送再确认的DOno
'''
from pageElement.doinfo.Edit import Edit
from business.Login import Login
from util.ElementUtil import ElementUtil
from pageElement.doinfo.AddCost import AddCost
from pageElement.doinfo.ReDO import ReDO
from time import sleep
from pageElement.doinfo.DODetermine import DODetermine


class GetDONO1(Edit,AddCost,DODetermine,ReDO):


    def getDisDO(self,driver,DONO):
        # 登录
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        sleep(3)
        # 点击首页DO确定
        eu.click(driver, 15, '课税1',*self.DOElement)
        sleep(3)
        # 输入DONO
        eu.send_keys(driver, 15, DONO, '课税1', *self.DONOElement)
        # 点击检索
        eu.click(driver, 15, '课税1',*self.selElement)
        sleep(5)
        # 选择数据
        eu.click(driver, 15, '课税1',*self.selDateElement)
        # 点击配送再确定
        eu.click(driver, 15, '课税1',*self.reconDoElement)
        sleep(3)
        # 修改纳入日期
        eu.click(driver, 15, '课税1',*self.inclusionDateElement)
        eu.click(driver, 15, '课税1',*self.selInclusionDateElement)
        # 纳入时间
        eu.send_keys(driver, 15, 1800, '课税1',*self.inclusionTimeElement)
        # 搜索配送模式
        eu.click(driver, 15, '课税1', *self.seachElement)
        sleep(3)
        # 选择配送模式
        eu.click(driver, 15, '课税1', *self.disModelEelemet)
        eu.click(driver, 15, '课税1', *self.selDisModelEelemet)
        # 保存配送模式
        eu.click(driver, 15, '课税1', *self.saveDisElement)
        sleep(3)
        # 点击保存
        eu.click(driver, 15, '课税1', *self.saveElement)
        sleep(3)
        # 确定
        eu.click(driver, 15, '课税1',*self.determineElement)

    def addCost(self,driver):
        eu = ElementUtil()
        # 点击检索
        eu.click(driver, 15, '课税1',*self.selElement)
        sleep(5)
        # 选择数据
        eu.click(driver, 15, '课税1',*self.selDateElement)
        # 点击费用追加
        eu.click(driver, 15, '课税1',*self.addcostElement)
        sleep(3)
        # #输入课税1费用为1000
        # action = ActionChains(driver)
        # ele = driver.find_element(*self.taxactionOneElement)
        # action.double_click(ele).perform()
        # driver.find_element(*self.taxactionOneElement).send_keys(1000)
        # #滚动条拉到顶端
        # scro="document.documentElement.scrollTop=0"
        # driver.execute_script(scro)
        # 选择通关料区分
        eu.click(driver, 15, '课税1',*self.distinElement)
        eu.click(driver, 15, '课税1',*self.selDistinElement)
        # 点击费用计算
        eu.click(driver, 15, '课税1',*self.costCalElement)
        sleep(5)
        # 点击确定
        eu.click(driver, 15, '课税1',*self.doElement)
        sleep(5)
        # 点击保存
        eu.click(driver, 15, '课税1',*self.saveElement)

    def doSure(self,driver):

        eu = ElementUtil()
        # 点击检索
        eu.click(driver, 15, '课税1',*self.selElement)
        sleep(5)
        # 选择数据
        eu.click(driver, 15, '课税1',*self.selDateElement)
        # 点击DO确定
        eu.click(driver, 15, '课税1',*self.DODetermineElement)
        sleep(3)
        # 点击确定
        eu.click(driver, 15, '课税1',*self.determineElement)








