'''
配送再确认信息修改
'''
from pageElement.doinfo.Edit import Edit
from business.Login import Login
from time import sleep
import datetime
from selenium.webdriver import ActionChains
from util.ElementUtil import ElementUtil
from business.outward.GetBLNO import GetBLNO

class EditB(Edit):

    def getDONO(self):
        gb = GetBLNO()
        DONO = gb.test()

        return DONO

    
    ##修改纳入日期 保存
    def editDate(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击首页DO确定
        eu.click(driver, 15,'DO编辑',*self.DOElement)
        #输入DONO
        eu.send_keys(driver,15,self.getDONO(),'DO编辑',*self.DONOElement)
        #点击检索
        eu.click(driver, 15,'DO编辑',*self.selElement)
        #选择数据
        eu.click(driver, 15,'DO编辑',*self.selDateElement)
        #点击配送再确定
        eu.click(driver, 15,'DO编辑',*self.reconDoElement)
        #修改纳入日期
        eu.click(driver, 15,'DO编辑',*self.inclusionDateElement)
        eu.click(driver, 15,'DO编辑',*self.selInclusionDateElement)
        #纳入时间
        eu.send_keys(driver,15,1800,'DO编辑',*self.inclusionTimeElement)
        #搜索配送模式
        eu.click(driver,15,'DO编辑',*self.seachElement)
        sleep(3)
        #选择配送模式
        eu.click(driver,15,'DO编辑',*self.disModelEelemet)
        eu.click(driver, 15, 'DO编辑',*self.selDisModelEelemet)
        #保存配送模式
        eu.click(driver,15,'DO编辑',*self.saveDisElement)
        #点击保存
        eu.click(driver, 15,'DO编辑',*self.saveElement)
        #确定
        eu.click(driver, 15,'DO编辑',*self.determineElement)
        
    ##修改纳入日期 返回
    def editDateR(self,driver):
        # 登录
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        # 点击首页DO确定
        eu.click(driver, 15, 'DO编辑', *self.DOElement)
        # 输入DONO
        eu.send_keys(driver, 15, self.getDONO(), 'DO编辑', *self.DONOElement)
        # 点击检索
        eu.click(driver, 15, 'DO编辑', *self.selElement)
        # 选择数据
        eu.click(driver, 15, 'DO编辑', *self.selDateElement)
        # 点击配送再确定
        eu.click(driver, 15, 'DO编辑', *self.reconDoElement)
        # 修改纳入日期
        eu.click(driver, 15, 'DO编辑', *self.inclusionDateElement)
        eu.click(driver, 15, 'DO编辑', *self.selInclusionDateElement)
        # 纳入时间
        eu.send_keys(driver, 15, 1800, 'DO编辑', *self.inclusionTimeElement)
        # 搜索配送模式
        eu.click(driver, 15, 'DO编辑', *self.seachElement)
        sleep(3)
        # 选择配送模式
        eu.click(driver, 15, 'DO编辑', *self.disModelEelemet)
        eu.click(driver, 15, 'DO编辑', *self.selDisModelEelemet)
        # 保存配送模式
        eu.click(driver, 15, 'DO编辑', *self.saveDisElement)
        #点击返回
        eu.click(driver, 15,'DO编辑',*self.returnElement)
        
        
    ##修改纳入时间 保存
    def editTime(self,driver):
        # 登录
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        # 点击首页DO确定
        eu.click(driver, 15, 'DO编辑',*self.DOElement)
        # 输入DONO
        eu.send_keys(driver, 15, self.getDONO(),'DO编辑', *self.DONOElement)
        # 点击检索
        eu.click(driver, 15, 'DO编辑',*self.selElement)
        # 选择数据
        eu.click(driver, 15, 'DO编辑',*self.selDateElement)
        # 点击配送再确定
        eu.click(driver, 15, 'DO编辑',*self.reconDoElement)
        # 修改纳入日期
        eu.click(driver, 15, 'DO编辑',*self.inclusionDateElement)
        eu.click(driver, 15, 'DO编辑',*self.selInclusionDateElement)
        # 纳入时间
        eu.send_keys(driver, 15, 1800, 'DO编辑',*self.inclusionTimeElement)
        # 搜索配送模式
        eu.click(driver, 15, 'DO编辑',*self.seachElement)
        # 选择配送模式
        eu.click(driver, 15, 'DO编辑',*self.disModelEelemet)
        eu.click(driver, 15, 'DO编辑',*self.selDisModelEelemet)
        # 保存配送模式
        eu.click(driver, 15, 'DO编辑',*self.saveDisElement)
        # 点击保存
        eu.click(driver, 15, 'DO编辑',*self.saveElement)
        # 确定
        eu.click(driver, 15, 'DO编辑',*self.determineElement)
        
    ##修改纳入时间 返回
    def editTimeR(self,driver):
        # 登录
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        # 点击首页DO确定
        eu.click(driver, 15, 'DO编辑',*self.DOElement)
        # 输入DONO
        eu.send_keys(driver, 15, self.getDONO(), 'DO编辑',*self.DONOElement)
        # 点击检索
        eu.click(driver, 15, 'DO编辑',*self.selElement)
        # 选择数据
        eu.click(driver, 15, 'DO编辑',*self.selDateElement)
        # 点击配送再确定
        eu.click(driver, 15, 'DO编辑',*self.reconDoElement)
        #修改纳入时间
        time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        time = time[8:12]
        action = ActionChains(driver)
        ele = driver.find_element(*self.inclusionTimeElement)
        action.double_click(ele).perform()
        driver.find_element(*self.inclusionTimeElement).send_keys(time)
        #点击返回
        eu.click(driver, 15,'DO编辑',*self.returnElement)
        
    ##修改纳入日期和时间 保存
    def editDateAndTime(self,driver):
        # 登录
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        # 点击首页DO确定
        eu.click(driver, 15, 'DO编辑',*self.DOElement)
        # 输入DONO
        eu.send_keys(driver, 15, self.getDONO(), 'DO编辑',*self.DONOElement)
        # 点击检索
        eu.click(driver, 15, 'DO编辑',*self.selElement)
        # 选择数据
        eu.click(driver, 15, 'DO编辑',*self.selDateElement)
        # 点击配送再确定
        eu.click(driver, 15, 'DO编辑',*self.reconDoElement)
        # 修改纳入日期
        eu.click(driver, 15, 'DO编辑',*self.inclusionDateElement)
        eu.click(driver, 15, 'DO编辑',*self.selInclusionDateElement)
        # 纳入时间
        eu.send_keys(driver, 15, 1800, 'DO编辑',*self.inclusionTimeElement)
        # 搜索配送模式
        eu.click(driver, 15, 'DO编辑',*self.seachElement)
        sleep(3)
        # 选择配送模式
        eu.click(driver, 15, 'DO编辑',*self.disModelEelemet)
        eu.click(driver, 15, 'DO编辑',*self.selDisModelEelemet)
        # 保存配送模式
        eu.click(driver, 15, 'DO编辑',*self.saveDisElement)
        # 点击保存
        eu.click(driver, 15, 'DO编辑',*self.saveElement)
        # 确定
        eu.click(driver, 15, 'DO编辑',*self.determineElement)

        
        