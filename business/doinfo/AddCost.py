'''
Created on 2019年7月4日

@author: chinasoft.jl.ma
费用追加
'''
from pageElement.doinfo.AddCost import AddCost
from business.Login import Login
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



class AddCostB(AddCost):
    
    ##追加付款请求费  课税1
    def addTaxActionOne(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击DO确定
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #选择状态进行检索数据
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #输入DO NO
        driver.find_element(*self.DONOElement).send_keys('DO740')
        #点击检索
        driver.find_element(*self.selElement).click()
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击费用追加
        driver.find_element(*self.addcostElement).click()
        sleep(5)
        #输入课税1费用为1000
        action = ActionChains(driver)
        ele = driver.find_element(*self.taxactionOneElement)
        action.double_click(ele).perform()
        driver.find_element(*self.taxactionOneElement).send_keys(1000)
        #滚动条拉到顶端
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #选择通关料区分
        driver.find_element(*self.distinElement).click()
        driver.find_element(*self.selDistinElement).click()
        #点击费用追加
        driver.find_element(*self.costCalElement).click()
        sleep(5)
        #点击确定
        driver.find_element(*self.doElement).click()
        sleep(5)
        #点击保存
        driver.find_element(*self.saveElement).click()
        sleep(5)
        
    ##追加付款请求费  课税2
    def addTaxActionTwo(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击DO确定
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #选择状态进行检索数据
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #输入DO NO
        driver.find_element(*self.DONOElement).send_keys('DO740')
        #点击检索
        driver.find_element(*self.selElement).click()
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击费用追加
        driver.find_element(*self.addcostElement).click()
        sleep(5)
        #输入课税1费用为1000
        action = ActionChains(driver)
        ele = driver.find_element(*self.taxactionTwoElement)
        action.double_click(ele).perform()
        driver.find_element(*self.taxactionTwoElement).send_keys(1000)
        #滚动条拉到顶端
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #选择通关料区分
        driver.find_element(*self.distinElement).click()
        driver.find_element(*self.selDistinElement).click()
        #点击费用追加
        driver.find_element(*self.costCalElement).click()
        sleep(5)
        #点击确定
        driver.find_element(*self.doElement).click()
        sleep(5)
        #点击保存
        driver.find_element(*self.saveElement).click()
        sleep(5)
        
    ##追加付款请求费  课税3
    def addTaxActionThree(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击DO确定
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #选择状态进行检索数据
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #输入DO NO
        driver.find_element(*self.DONOElement).send_keys('DO740')
        #点击检索
        driver.find_element(*self.selElement).click()
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击费用追加
        driver.find_element(*self.addcostElement).click()
        sleep(5)
        #输入课税1费用为1000
        action = ActionChains(driver)
        ele = driver.find_element(*self.taxactionThreeElement)
        action.double_click(ele).perform()
        driver.find_element(*self.taxactionThreeElement).send_keys(1000)
        #滚动条拉到顶端
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #选择通关料区分
        driver.find_element(*self.distinElement).click()
        driver.find_element(*self.selDistinElement).click()
        #点击费用追加
        driver.find_element(*self.costCalElement).click()
        sleep(5)
        #点击确定
        driver.find_element(*self.doElement).click()
        sleep(5)
        
    ##追加付款请求费  免税1
    def addExemptionOne(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击DO确定
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #选择状态进行检索数据
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #输入DO NO
        driver.find_element(*self.DONOElement).send_keys('DO740')
        #点击检索
        driver.find_element(*self.selElement).click()
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击费用追加
        driver.find_element(*self.addcostElement).click()
        sleep(5)
        #输入课税1费用为1000
        action = ActionChains(driver)
        ele = driver.find_element(*self.exemptionOneElement)
        action.double_click(ele).perform()
        driver.find_element(*self.exemptionOneElement).send_keys(1000)
        #滚动条拉到顶端
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #选择通关料区分
        driver.find_element(*self.distinElement).click()
        driver.find_element(*self.selDistinElement).click()
        #点击费用追加
        driver.find_element(*self.costCalElement).click()
        sleep(5)
        #点击确定
        driver.find_element(*self.doElement).click()
        sleep(5)
        #点击保存
        driver.find_element(*self.saveElement).click()
        sleep(5)
        
    ##追加付款请求费  免税2
    def addExemptionTwo(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击DO确定
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #选择状态进行检索数据
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #输入DO NO
        driver.find_element(*self.DONOElement).send_keys('DO740')
        #点击检索
        driver.find_element(*self.selElement).click()
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击费用追加
        driver.find_element(*self.addcostElement).click()
        sleep(5)
        #输入课税1费用为1000
        action = ActionChains(driver)
        ele = driver.find_element(*self.exemptionTwoElement)
        action.double_click(ele).perform()
        driver.find_element(*self.exemptionTwoElement).send_keys(1000)
        #滚动条拉到顶端
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #选择通关料区分
        driver.find_element(*self.distinElement).click()
        driver.find_element(*self.selDistinElement).click()
        #点击费用追加
        driver.find_element(*self.costCalElement).click()
        sleep(5)
        #点击确定
        driver.find_element(*self.doElement).click()
        sleep(5)
        #点击保存
        driver.find_element(*self.saveElement).click()
        sleep(5)
        
    ##追加付款请求费  免税3
    def addExemptionThree(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击DO确定
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #选择状态进行检索数据
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #输入DO NO
        driver.find_element(*self.DONOElement).send_keys('DO740')
        #点击检索
        driver.find_element(*self.selElement).click()
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击费用追加
        driver.find_element(*self.addcostElement).click()
        sleep(5)
        #输入课税1费用为1000
        action = ActionChains(driver)
        ele = driver.find_element(*self.exemptionThreeElement)
        action.double_click(ele).perform()
        driver.find_element(*self.exemptionThreeElement).send_keys(1000)
        #滚动条拉到顶端
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #选择通关料区分
        driver.find_element(*self.distinElement).click()
        driver.find_element(*self.selDistinElement).click()
        #点击费用追加
        driver.find_element(*self.costCalElement).click()
        sleep(5)
        #点击确定
        driver.find_element(*self.doElement).click()
        sleep(5)
        #点击保存
        driver.find_element(*self.saveElement).click()
        sleep(5)
        
    ##追加求费  课税1
    def addTaxActionTOne(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击DO确定
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #选择状态进行检索数据
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #输入DO NO
        driver.find_element(*self.DONOElement).send_keys('DO740')
        #点击检索
        driver.find_element(*self.selElement).click()
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击费用追加
        driver.find_element(*self.addcostElement).click()
        sleep(5)
        #输入课税1费用为1000
        action = ActionChains(driver)
        ele = driver.find_element(*self.taxactionOneAddElement)
        action.double_click(ele).perform()
        driver.find_element(*self.taxactionOneAddElement).send_keys(1000)
        #滚动条拉到顶端
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #选择通关料区分
        driver.find_element(*self.distinElement).click()
        driver.find_element(*self.selDistinElement).click()
        #点击费用追加
        driver.find_element(*self.costCalElement).click()
        sleep(5)
        #点击确定
        driver.find_element(*self.doElement).click()
        sleep(5)
        #点击保存
        driver.find_element(*self.saveElement).click()
        sleep(5)
        
    ##追加求费  课税2
    def addTaxActionTTwo(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击DO确定
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #选择状态进行检索数据
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #输入DO NO
        driver.find_element(*self.DONOElement).send_keys('DO740')
        #点击检索
        driver.find_element(*self.selElement).click()
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击费用追加
        driver.find_element(*self.addcostElement).click()
        sleep(5)
        #输入课税1费用为1000
        action = ActionChains(driver)
        ele = driver.find_element(*self.taxactionTwoAddElement)
        action.double_click(ele).perform()
        driver.find_element(*self.taxactionTwoAddElement).send_keys(1000)
        #滚动条拉到顶端
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #选择通关料区分
        driver.find_element(*self.distinElement).click()
        driver.find_element(*self.selDistinElement).click()
        #点击费用追加
        driver.find_element(*self.costCalElement).click()
        sleep(5)
        #点击确定
        driver.find_element(*self.doElement).click()
        sleep(5)
        #点击保存
        driver.find_element(*self.saveElement).click()
        sleep(5)
        
    ##追加请求  免税1
    def addExemptionTOne(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击DO确定
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #选择状态进行检索数据
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #输入DO NO
        driver.find_element(*self.DONOElement).send_keys('DO740')
        #点击检索
        driver.find_element(*self.selElement).click()
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击费用追加
        driver.find_element(*self.addcostElement).click()
        sleep(5)
        #输入课税1费用为1000
        action = ActionChains(driver)
        ele = driver.find_element(*self.exemptionOneAddElement)
        action.double_click(ele).perform()
        driver.find_element(*self.exemptionOneAddElement).send_keys(1000)
        #滚动条拉到顶端
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #选择通关料区分
        driver.find_element(*self.distinElement).click()
        driver.find_element(*self.selDistinElement).click()
        #点击费用追加
        driver.find_element(*self.costCalElement).click()
        sleep(5)
        #点击确定
        driver.find_element(*self.doElement).click()
        sleep(5)
        #点击保存
        driver.find_element(*self.saveElement).click()
        sleep(5)
        
    ##追加请求  免税2
    def addExemptionTTwo(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击DO确定
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #选择状态进行检索数据
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #输入DO NO
        driver.find_element(*self.DONOElement).send_keys('DO740')
        #点击检索
        driver.find_element(*self.selElement).click()
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击费用追加
        driver.find_element(*self.addcostElement).click()
        sleep(5)
        #输入课税1费用为1000
        action = ActionChains(driver)
        ele = driver.find_element(*self.exemptionTwoAddElement)
        action.double_click(ele).perform()
        driver.find_element(*self.exemptionTwoAddElement).send_keys(1000)
        #滚动条拉到顶端
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #选择通关料区分
        driver.find_element(*self.distinElement).click()
        driver.find_element(*self.selDistinElement).click()
        #点击费用追加
        driver.find_element(*self.costCalElement).click()
        sleep(5)
        #点击确定
        driver.find_element(*self.doElement).click()
        sleep(5)
        #点击保存
        driver.find_element(*self.saveElement).click()
        sleep(5)