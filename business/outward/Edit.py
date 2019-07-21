'''
Created on 2019年6月24日

@author: chinasoft.jl.ma  
编辑订单信息
'''
from business.Login import Login
from pageElement.outward.EditElement import EditElement
from util.ElementUtil import ElementUtil
from selenium.webdriver.common.keys import Keys
from business.outward.GetBLNO import GetBLNO



class Edit(EditElement):
    gb = GetBLNO()
    DONO = gb.test()
    
    
    ##修改到达港
    def editToport(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击做成
        eu.click(driver, 15,'修改到达港',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.DONO,'修改到达港',*self.BLNoEelement)
        #点击检索
        eu.click(driver, 15,'修改到达港',*self.selElement)
        #选择数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)

        #点击编辑
        eu.click(driver, 15,'修改到达港',*self.editElement)
        #点击运费计算
        eu.click(driver, 15,'修改到达港',*self.costCalElement)
        #点击确定
        eu.click(driver, 15,'修改到达港',*self.doElement)
        
        
    ##修改20F集装箱数量
    def editTwoF(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击做成
        eu.click(driver, 15,'修改20F集装箱',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.DONO,'修改20F集装箱',*self.BLNoEelement)
        #点击检索
        eu.click(driver, 15,'修改20F集装箱',*self.selElement)
        #选择数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        # 点击编辑
        eu.click(driver, 15, '修改20F集装箱',*self.editElement)
        # 点击运费计算
        eu.click(driver, 15, '修改20F集装箱',*self.costCalElement)
        # 点击确定
        eu.click(driver, 15, '修改20F集装箱',*self.doElement)


    ##修改40F集装箱数量
    def editFourF(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击做成
        eu.click(driver, 15,'修改40F集装箱',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.DONO,'修改40F集装箱',*self.BLNoEelement)
        #点击检索
        eu.click(driver, 15,'修改40F集装箱',*self.selElement)
        #选择数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        # 点击编辑
        eu.click(driver, 15, '修改40F集装箱',*self.editElement)
        # 点击运费计算
        eu.click(driver, 15, '修改40F集装箱',*self.costCalElement)
        # 点击确定
        eu.click(driver, 15, '修改40F集装箱',*self.doElement)
        
    ##修改40H集装箱数量
    def editFourH(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击做成
        eu.click(driver, 15,'修改40F集装箱',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.DONO,'修改40F集装箱',*self.BLNoEelement)
        #点击检索
        eu.click(driver, 15,'修改40F集装箱',*self.selElement)
        #选择数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        # 点击编辑
        eu.click(driver, 15, '修改40F集装箱',*self.editElement)
        # 点击运费计算
        eu.click(driver, 15,'修改40F集装箱', *self.costCalElement)
        # 点击确定
        eu.click(driver, 15,'修改40F集装箱', *self.doElement)
        
    ##修改到岗开始时间后保存
    def editStartDate(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击做成
        eu.click(driver, 15,'修改到岗开始时间',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.DONO,'修改到岗开始时间',*self.BLNoEelement)
        #点击检索
        eu.click(driver, 15,'修改到岗开始时间',*self.selElement)
        #选择数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        # 点击编辑
        eu.click(driver, 15, '修改到岗开始时间',*self.editElement)
        # 点击运费计算
        eu.click(driver, 15, '修改到岗开始时间',*self.costCalElement)
        # 点击确定
        eu.click(driver, 15, '修改到岗开始时间',*self.doElement)
        
    ##修改到岗结束时间后保存
    def editEndDate(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击做成
        eu.click(driver, 15,'修改到岗开始时间',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.DONO,'修改到岗开始时间',*self.BLNoEelement)
        #点击检索
        eu.click(driver, 15,'修改到岗开始时间',*self.selElement)
        #选择数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        # 点击编辑
        eu.click(driver, 15, '修改到岗开始时间',*self.editElement)
        # 点击运费计算
        eu.click(driver, 15, '修改到岗开始时间',*self.costCalElement)
        # 点击确定
        eu.click(driver, 15, '修改到岗开始时间',*self.doElement)
    
    ##修改到岗结束时间后返回
    def editEndDateR(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        # 点击做成
        eu.click(driver, 15, '修改到岗开始时间',*self.outWardElement)
        # 输入B/L NO
        eu.send_keys(driver, 15, self.DONO, '修改到岗开始时间', *self.BLNoEelement)
        # 点击检索
        eu.click(driver, 15, '修改到岗开始时间',*self.selElement)
        # 选择数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        # 点击编辑
        eu.click(driver, 15, '修改到岗开始时间',*self.editElement)
        # 点击运费计算
        eu.click(driver, 15, '修改到岗开始时间',*self.costCalElement)
        # 点击确定
        eu.click(driver, 15, '修改到岗开始时间',*self.doElement)
        

