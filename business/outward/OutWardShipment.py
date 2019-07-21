'''
Created on 2019年5月22日
@author: chinasoft.jl.ma
运赁外货登录  第一版冒烟用例
'''

from business.Login import Login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageElement.outward.OutWardShipment import OutWardShipment
from time import sleep
from selenium.webdriver import ActionChains

class OutWardShipment(OutWardShipment):
    
    def outWard(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        
        sleep(5)
        #点击 フレイトI/V作成
        driver.find_element(*self.outWardElement).click()
        sleep(2)
        #清空提单号
        driver.find_element(*self.BLNoEelement).click()
        driver.find_element(*self.BLNoEelement).clear()
        #输入提单号
        driver.find_element(*self.BLNoEelement).send_keys('mjl001')
        #点击检索
        driver.find_element(*self.searchElement).click()
        sleep(2)
        #选择需要勾选的数据
        driver.find_element(*self.selDataElement).send_keys(Keys.SPACE)
        #点击海上，航空运凭计算
        driver.find_element(*self.transportationElement).click()
        sleep(5)#加载时间较长  时间短容易造成找不到元素
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.FEEElement)
        action.double_click(on_element).perform()
        sleep(2)
        #输入FEE金额
        driver.find_element(*self.FEEElement).send_keys(1000)
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        sleep(1)
        #点击保存
        driver.find_element(*self.preserveElement).click()
        sleep(2)
        
      

    
