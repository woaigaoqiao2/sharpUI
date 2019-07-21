'''
Created on 2019年7月4日

@author: chinasoft.jl.ma
DO解除申请
'''
from pageElement.doinfo.ReDO import ReDO
from util.ElementUtil import ElementUtil
from case.doinfo.getDONO1 import GetDONO1
from business.outward.GetBLNO import GetBLNO

class ReDOb(ReDO):
    
    def dismiss(self,driver):
        gb = GetBLNO()
        DONO = gb.test()
        gd = GetDONO1()
        gd.getDisDO(driver, DONO)
        gd.addCost(driver)
        # gd.doSure(driver)

        eu = ElementUtil()
        #点击检索
        eu.click(driver, 15, 'DO申请',*self.selElement)
        #选择数据
        eu.click(driver, 15, 'DO申请',*self.selDateElement)
        #点击DO解除申请
        eu.click(driver, 15, 'DO申请',*self.reDOReqElement)
        #填写选项
        # driver.find_element(*self.beaucElement).send_keys('申请解除')
        # driver.find_element(*self.optElement1).click()
        # driver.find_element(*self.optElement2).click()
        # #点击解除申请
        # driver.find_element(*self.reReqElement).click()
