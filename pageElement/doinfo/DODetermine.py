'''
Created on 2019年7月4日

@author: chinasoft.jl.ma
DO确定
'''

from selenium.webdriver.common.by import By


class DODetermine():
    
    #首页的 D/O确定
    DOElement = (By.XPATH,'//main[@class="v-content"]//div[text()="D/O確定"]')
    #DO NO
    DONOElement = (By.XPATH,'//input[@aria-label="D/O NO"]')
    #选择状态  DO諸掛登録済
    DOstatusElement = (By.XPATH,'//label[text()="ステータス"]/..')
    selDOstatusElement = (By.XPATH,'//div[text()="DO諸掛登録済"]')
    #检索
    selElement = (By.XPATH,'//main//button[@class="btn-search v-btn theme--light"]')
    #选择要修改得数据
    selDateElement = (By.XPATH,'//tbody/tr[1]//div[@class="v-input--selection-controls__ripple"]')
    #DO确定
    DODetermineElement = (By.XPATH,'//main//div[text()="D/O確定"]')
    #确定
    determineElement = (By.XPATH,'//div[contains(@class,"active")]//div[contains(@class,"justify-center")]/button')
