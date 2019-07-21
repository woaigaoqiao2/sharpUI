'''
Created on 2019年7月4日

@author: chinasoft.jl.ma
DO解除确定
'''
from pageElement.doinfo.DOReDetermine import DOReDetermine
from business.Login import Login
from util.ElementUtil import ElementUtil


class DOReDetermineb(DOReDetermine):
    
    def doReDeter(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击首页DO确定
        eu.click(driver, 15,*self.DOElement)
        #选择状态进行检索数据
        eu.click(driver, 15,*self.DOstatusElement)
        eu.click(driver, 15,*self.selDOstatusElement)
#         #输入DO NO
#         eu.send_keys(driver, 15, 'DO NO',*self.DONOElement)
        #点击检索
        eu.click(driver, 15,*self.selElement)
        #选择数据
        eu.click(driver, 15,*self.selDateElement)
        #点击DO解除确定
        eu.click(driver, 15,*self.reDOReqElement)
        #点击确定
        eu.click(driver, 15,*self.deterElement)
        
        #断言
        #检索出数据  检查状态是否为解除济
