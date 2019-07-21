'''
Created on 2019年7月4日

@author: chinasoft.jl.ma
费用追加
'''
from pageElement.doinfo.AddCost import AddCost
from util.ElementUtil import ElementUtil
from case.doinfo.getDONO1 import GetDONO1
from business.outward.GetBLNO import GetBLNO
from time import sleep
class AddCostB(AddCost):

    ##追加付款请求费  课税1
    def addTaxActionOne(self,driver):
        gb = GetBLNO()
        DONO = gb.test()
        gd = GetDONO1()
        gd.getDisDO(driver,DONO)
        eu = ElementUtil()
        #点击检索
        eu.click(driver, 15, '课税1',*self.selElement)
        #选择数据
        eu.click(driver, 15, '课税1',*self.selDateElement)
        #点击费用追加
        eu.click(driver, 15, '课税1',*self.addcostElement)
        # #输入课税1费用为1000
        # action = ActionChains(driver)
        # ele = driver.find_element(*self.taxactionOneElement)
        # action.double_click(ele).perform()
        # driver.find_element(*self.taxactionOneElement).send_keys(1000)
        # #滚动条拉到顶端
        # scro="document.documentElement.scrollTop=0"
        # driver.execute_script(scro)
        #选择通关料区分
        eu.click(driver, 15, '课税1',*self.distinElement)
        eu.click(driver, 15, '课税1',*self.selDistinElement)
        #点击费用计算
        eu.click(driver, 15, '课税1',*self.costCalElement)
        sleep(5)
        # 点击确定
        eu.click(driver, 15, '课税1',*self.doElement)
        sleep(5)
        #点击保存
        eu.click(driver, 15, '课税1',*self.saveElement)


        
    ##追加付款请求费  课税2
    def addTaxActionTwo(self,driver):
        gb = GetBLNO()
        DONO = gb.test()
        gd = GetDONO1()
        gd.getDisDO(driver, DONO)
        eu = ElementUtil()
        #点击检索
        eu.click(driver, 15, '课税2',*self.selElement)
        #选择数据
        eu.click(driver, 15, '课税2',*self.selDateElement)
        #点击费用追加
        eu.click(driver, 15, '课税2',*self.addcostElement)
        # #输入课税1费用为1000
        # action = ActionChains(driver)
        # ele = driver.find_element(*self.taxactionTwoElement)
        # action.double_click(ele).perform()
        # driver.find_element(*self.taxactionTwoElement).send_keys(1000)
        # #滚动条拉到顶端
        # scro="document.documentElement.scrollTop=0"
        # driver.execute_script(scro)
        #选择通关料区分
        eu.click(driver, 15, '课税2',*self.distinElement)
        eu.click(driver, 15, '课税2',*self.selDistinElement)
        #点击费用计算
        eu.click(driver, 15, '课税2',*self.costCalElement)
        sleep(5)
        #点击确定
        eu.click(driver, 15, '课税2',*self.doElement)
        sleep(5)
        #点击保存
        eu.click(driver, 15, '课税2',*self.saveElement)
        
    ##追加付款请求费  课税3
    def addTaxActionThree(self,driver):
        gb = GetBLNO()
        DONO = gb.test()
        gd = GetDONO1()
        gd.getDisDO(driver, DONO)
        eu = ElementUtil()
        #点击检索
        eu.click(driver, 15, '课税3',*self.selElement)
        #选择数据
        eu.click(driver, 15, '课税3',*self.selDateElement)
        #点击费用追加
        eu.click(driver, 15, '课税3',*self.addcostElement)
        # #输入课税1费用为1000
        # action = ActionChains(driver)
        # ele = driver.find_element(*self.taxactionThreeElement)
        # action.double_click(ele).perform()
        # driver.find_element(*self.taxactionThreeElement).send_keys(1000)
        # #滚动条拉到顶端
        # scro="document.documentElement.scrollTop=0"
        # driver.execute_script(scro)
        #选择通关料区分
        eu.click(driver, 15, '课税3',*self.distinElement)
        eu.click(driver, 15, '课税3',*self.selDistinElement)
        #点击费用计算
        eu.click(driver, 15, '课税3',*self.costCalElement)
        sleep(5)
        # 点击确定
        eu.click(driver, 15, '课税3',*self.doElement)
        sleep(5)
        #点击保存
        eu.click(driver, 15, '课税3',*self.saveElement)

        
    ##追加付款请求费  免税1
    def addExemptionOne(self,driver):
        gb = GetBLNO()
        DONO = gb.test()
        gd = GetDONO1()
        gd.getDisDO(driver, DONO)
        eu = ElementUtil()
        #点击检索
        eu.click(driver, 15, '免税1',*self.selElement)
        #选择数据
        eu.click(driver, 15, '免税1',*self.selDateElement)
        #点击费用追加
        eu.click(driver, 15, '免税1',*self.addcostElement)
        # #输入课税1费用为1000
        # action = ActionChains(driver)
        # ele = driver.find_element(*self.exemptionOneElement)
        # action.double_click(ele).perform()
        # driver.find_element(*self.exemptionOneElement).send_keys(1000)
        # #滚动条拉到顶端
        # scro="document.documentElement.scrollTop=0"
        # driver.execute_script(scro)
        #选择通关料区分
        eu.click(driver, 15, '免税1',*self.distinElement)
        eu.click(driver, 15, '免税1',*self.selDistinElement)
        #点击费用计算
        eu.click(driver, 15, '免税1',*self.costCalElement)
        sleep(5)
        #点击确定
        eu.click(driver, 15, '免税1',*self.doElement)
        sleep(5)
        #点击保存
        eu.click(driver, 15, '免税1',*self.saveElement)
        
    ##追加付款请求费  免税2
    def addExemptionTwo(self,driver):
        gb = GetBLNO()
        DONO = gb.test()
        gd = GetDONO1()
        gd.getDisDO(driver, DONO)
        eu = ElementUtil()
        #点击检索
        eu.click(driver, 15, '免税2',*self.selElement)
        #选择数据
        eu.click(driver, 15, '免税2',*self.selDateElement)
        #点击费用追加
        eu.click(driver, 15, '免税2',*self.addcostElement)
        # #输入课税1费用为1000
        # action = ActionChains(driver)
        # ele = driver.find_element(*self.exemptionTwoElement)
        # action.double_click(ele).perform()
        # driver.find_element(*self.exemptionTwoElement).send_keys(1000)
        # #滚动条拉到顶端
        # scro="document.documentElement.scrollTop=0"
        # driver.execute_script(scro)
        #选择通关料区分
        eu.click(driver, 15, '免税2',*self.distinElement)
        eu.click(driver, 15, '免税2',*self.selDistinElement)
        #点击费用计算
        eu.click(driver, 15, '免税2',*self.costCalElement)
        sleep(5)
        #点击确定
        eu.click(driver, 15, '免税2',*self.doElement)
        sleep(5)
        #点击保存
        eu.click(driver, 15, '免税2',*self.saveElement)
        
    ##追加付款请求费  免税3
    def addExemptionThree(self,driver):
        gb = GetBLNO()
        DONO = gb.test()
        gd = GetDONO1()
        gd.getDisDO(driver, DONO)
        eu = ElementUtil()
        #点击检索
        eu.click(driver, 15, '免税3',*self.selElement)
        #选择数据
        eu.click(driver, 15, '免税3',*self.selDateElement)
        #点击费用追加
        eu.click(driver, 15, '免税3', *self.addcostElement)
        # #输入课税1费用为1000
        # action = ActionChains(driver)
        # ele = driver.find_element(*self.exemptionThreeElement)
        # action.double_click(ele).perform()
        # driver.find_element(*self.exemptionThreeElement).send_keys(1000)
        # #滚动条拉到顶端
        # scro="document.documentElement.scrollTop=0"
        # driver.execute_script(scro)
        #选择通关料区分
        eu.click(driver, 15, '免税3', *self.distinElement)
        eu.click(driver, 15, '免税3', *self.selDistinElement)
        #点击费用计算
        eu.click(driver, 15, '免税3', *self.costCalElement)
        sleep(5)
        #点击确定
        eu.click(driver, 15, '免税3', *self.doElement)
        sleep(5)
        #点击保存
        eu.click(driver, 15, '免税3', *self.saveElement)
        
    ##追加求费  课税1
    def addTaxActionTOne(self,driver):
        gb = GetBLNO()
        DONO = gb.test()
        gd = GetDONO1()
        gd.getDisDO(driver, DONO)
        eu = ElementUtil()
        #点击检索
        eu.click(driver, 15,  '追加课税1',*self.selElement)
        #选择数据
        eu.click(driver, 15, '追加课税1',*self.selDateElement)
        #点击费用追加
        eu.click(driver, 15, '追加课税1',*self.addcostElement)
        # #输入课税1费用为1000
        # action = ActionChains(driver)
        # ele = driver.find_element(*self.taxactionOneAddElement)
        # action.double_click(ele).perform()
        # driver.find_element(*self.taxactionOneAddElement).send_keys(1000)
        # #滚动条拉到顶端
        # scro="document.documentElement.scrollTop=0"
        # driver.execute_script(scro)
        #选择通关料区分
        eu.click(driver, 15, '追加课税1',*self.distinElement)
        eu.click(driver, 15, '追加课税1',*self.selDistinElement)
        #点击费用计算
        eu.click(driver, 15, '追加课税1',*self.costCalElement)
        sleep(5)
        #点击确定
        eu.click(driver, 15, '追加课税1',*self.doElement)
        sleep(5)
        #点击保存
        eu.click(driver, 15, '追加课税1',*self.saveElement)
        
    ##追加求费  课税2
    def addTaxActionTTwo(self,driver):
        gb = GetBLNO()
        DONO = gb.test()
        gd = GetDONO1()
        gd.getDisDO(driver, DONO)
        eu = ElementUtil()
        #点击检索
        eu.click(driver, 15, '追加课税2',*self.selElement)
        #选择数据
        eu.click(driver, 15, '追加课税2',*self.selDateElement)
        #点击费用追加
        eu.click(driver, 15, '追加课税2',*self.addcostElement)
        # #输入课税1费用为1000
        # action = ActionChains(driver)
        # ele = driver.find_element(*self.taxactionTwoAddElement)
        # action.double_click(ele).perform()
        # driver.find_element(*self.taxactionTwoAddElement).send_keys(1000)
        # #滚动条拉到顶端
        # scro="document.documentElement.scrollTop=0"
        # driver.execute_script(scro)
        #选择通关料区分
        eu.click(driver, 15, '追加课税2',*self.distinElement)
        eu.click(driver, 15, '追加课税2',*self.selDistinElement)
        #点击费用计算
        eu.click(driver, 15,'追加课税2', *self.costCalElement)
        sleep(5)
        #点击确定
        eu.click(driver, 15, '追加课税2',*self.doElement)
        sleep(5)
        #点击保存
        eu.click(driver, 15, '追加课税2',*self.saveElement)
        
    ##追加请求  免税1
    def addExemptionTOne(self,driver):
        gb = GetBLNO()
        DONO = gb.test()
        gd = GetDONO1()
        gd.getDisDO(driver, DONO)
        eu = ElementUtil()
        #点击检索
        eu.click(driver, 15, '追加免税1',*self.selElement)
        #选择数据
        eu.click(driver, 15, '追加免税1',*self.selDateElement)
        #点击费用追加
        eu.click(driver, 15, '追加免税1',*self.addcostElement)
        # #输入课税1费用为1000
        # action = ActionChains(driver)
        # ele = driver.find_element(*self.exemptionOneAddElement)
        # action.double_click(ele).perform()
        # driver.find_element(*self.exemptionOneAddElement).send_keys(1000)
        # #滚动条拉到顶端
        # scro="document.documentElement.scrollTop=0"
        # driver.execute_script(scro)
        #选择通关料区分
        eu.click(driver, 15, '追加免税1',*self.distinElement)
        eu.click(driver, 15, '追加免税1',*self.selDistinElement)
        #点击费用计算
        eu.click(driver, 15, '追加免税1',*self.costCalElement)
        sleep(5)
        #点击确定
        eu.click(driver, 15, '追加免税1',*self.doElement)
        sleep(5)
        #点击保存
        eu.click(driver, 15, '追加免税1',*self.saveElement)
        
    ##追加请求  免税2
    def addExemptionTTwo(self,driver):
        gb = GetBLNO()
        DONO = gb.test()
        gd = GetDONO1()
        gd.getDisDO(driver, DONO)
        eu = ElementUtil()
        # 点击检索
        eu.click(driver, 15, '追加免税2',*self.selElement)
        # 选择数据
        eu.click(driver, 15, '追加免税2',*self.selDateElement)
        # 点击费用追加
        eu.click(driver, 15, '追加免税2',*self.addcostElement)
        # #输入课税1费用为1000
        # action = ActionChains(driver)
        # ele = driver.find_element(*self.exemptionTwoAddElement)
        # action.double_click(ele).perform()
        # driver.find_element(*self.exemptionTwoAddElement).send_keys(1000)
        # # 滚动条拉到顶端
        # scro = "document.documentElement.scrollTop=0"
        # driver.execute_script(scro)
        #选择通关料区分
        eu.click(driver, 15, '追加免税2',*self.distinElement)
        eu.click(driver, 15, '追加免税2',*self.selDistinElement)
        #点击费用计算
        eu.click(driver, 15, '追加免税2',*self.costCalElement)
        sleep(5)
        #点击确定
        eu.click(driver, 15, '追加免税2',*self.doElement)
        sleep(5)
        #点击保存
        eu.click(driver, 15, '追加免税2',*self.saveElement)