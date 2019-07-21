'''
Created on 2019年7月4日

@author: chinasoft.jl.ma
'''
from selenium.webdriver.common.by import By

class DOReDetermine():
    
    #首页的 D/O确定
    DOElement = (By.XPATH,'//main[@class="v-content"]//div[text()="D/O確定"]')
    #按状态检索  D确定済
    DOstatusElement = (By.XPATH,'//label[text()="ステータス"]/..')
    selDOstatusElement = (By.XPATH,'//div[text()="DO解除承認待ち"]')
    #检索
    selElement = (By.XPATH,'//main//button[@class="btn-search v-btn theme--light"]')
    #选择要修改得数据
    selDateElement = (By.XPATH,'//tbody/tr[1]//div[@class="v-input--selection-controls__ripple"]')
    #DO解除申请
    reDOReqElement = (By.XPATH,'//div[text()="D/O解除確認"]')
    #确定
    deterElement = (By.XPATH,'//div[contains(@class,"content--active")]//div[text()="確定"]')
    