'''
Created on 2019年5月23日

@author: chinasoft.jl.ma
'''
from pageElement.doinfo.InfoDO import InfoDO
from selenium import webdriver
from business.Login import Login
from time import sleep
from selenium.webdriver.common.keys import Keys

class InfoDO(InfoDO):
    
    def updateDOinfo(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        
        #点击DO确认
        driver.find_element(*self.doElement).click()
        sleep(2)
        #点击检索
        driver.find_element(*self.searchElement).click()
        sleep(2)
        #选择数据
        driver.find_element(*self.seldataElement).send_keys(Keys.SPACE)
        sleep(2)
        #点击配送确认
        driver.find_element(*self.conOfdisElement).click()
        sleep(3)
        #点击保存
        driver.find_element(*self.preserveElement).click()
        sleep(2)
        #点击确定
        driver.find_element(*self.OKelement).click()

        