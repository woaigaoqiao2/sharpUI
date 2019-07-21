'''
Created on 2019年5月23日

@author: chinasoft.jl.ma
费用追加
'''
from time import sleep
from selenium.webdriver.common.keys import Keys

from business.Login import Login
from pageElement.AddCost import AddCost


class AddCost(AddCost):
    
    def addCost(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        #点击D/O确定
        driver.find_element(*self.doElement).click()
        sleep(2)
        #点击检索
        driver.find_element(*self.searchElement).click()
        sleep(2)
        #选择数据
        driver.find_element(*self.seldataElement).send_keys(Keys.SPACE)
        sleep(2)
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        sleep(2)
        #点击费用追加
        driver.find_element(*self.addCostElement).click()
        sleep(2)
        #选择通关料区分
        driver.find_element(*self.selMaterials).click()
        sleep(2)
        #选择7兰以上
        driver.find_element(*self.selMaterials7).click()
        #点击费用计算
        driver.find_element(*self.calCostElement).click()
        sleep(2)
        #点击确定
        driver.find_element(*self.OKElement).click()
        sleep(1)
        #点击保存
        driver.find_element(*self.preserveElement).click()
