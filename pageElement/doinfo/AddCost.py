'''
Created on 2019年7月4日

@author: chinasoft.jl.ma
费用追加
'''
from selenium.webdriver.common.by import By

class AddCost():
    
    #首页的 D/O确定
    DOElement = (By.XPATH,'//main[@class="v-content"]//div[text()="D/O確定"]')
    #按状态检索  DO諸掛登録済
    DOstatusElement = (By.XPATH,'//label[text()="ステータス"]/..')
    selDOstatusElement = (By.XPATH,'//div[text()="DO諸掛登録済"]')
    #DO NO
    DONOElement = (By.XPATH,'//input[@aria-label="D/O NO"]')
    #检索
    selElement = (By.XPATH,'//main//button[@class="btn-search v-btn theme--light"]')
    #选择要修改得数据
    selDateElement = (By.XPATH,'//tbody/tr[1]//div[@class="v-input--selection-controls__ripple"]')
    #费用追加
    addcostElement = (By.XPATH,'//div[text()="追加費用"]')
    ##追加支私费用
    #课税1
    taxactionOneElement = (By.XPATH,'//main//div[@class="v-content__wrap"]/div[1]/div[6]//tbody/tr[1]/td[2]//input')
    #课税2
    taxactionTwoElement = (By.XPATH,'//main//div[@class="v-content__wrap"]/div[1]/div[6]//tbody/tr[2]/td[2]//input')
    #课税3
    taxactionThreeElement = (By.XPATH,'//main//div[@class="v-content__wrap"]/div[1]/div[6]//tbody/tr[3]/td[2]//input')
    #免税1
    exemptionOneElement = (By.XPATH,'//main//div[@class="v-content__wrap"]/div[1]/div[6]//tbody/tr[4]/td[2]//input')
    #免税2
    exemptionTwoElement = (By.XPATH,'//main//div[@class="v-content__wrap"]/div[1]/div[6]//tbody/tr[5]/td[2]//input')
    #免税3
    exemptionThreeElement = (By.XPATH,'//main//div[@class="v-content__wrap"]/div[1]/div[6]//tbody/tr[6]/td[2]//input')
    
    ##费用追加
    #课税1
    taxactionOneAddElement = (By.XPATH,'//main//div[@class="v-content__wrap"]/div[1]/div[7]//tbody/tr[1]/td[2]//input')
    #课税2
    taxactionTwoAddElement = (By.XPATH,'//main//div[@class="v-content__wrap"]/div[1]/div[7]//tbody/tr[2]/td[2]//input')
    #免税1
    exemptionOneAddElement = (By.XPATH,'//main//div[@class="v-content__wrap"]/div[1]/div[7]//tbody/tr[3]/td[2]//input')
    #免税2
    exemptionTwoAddElement = (By.XPATH,'//main//div[@class="v-content__wrap"]/div[1]/div[7]//tbody/tr[4]/td[2]//input')
    #通关料区分
    distinElement = (By.XPATH,'//main//input[@aria-label="通関料区分"]/..')
    selDistinElement = (By.XPATH,'//div[contains(@class,"menuable__content__active")]//div[@class="v-list theme--light"]/div[1]')
    
    #费用计算
    costCalElement = (By.XPATH,'//div[text()="諸掛費用計算"]')
    #确定
    doElement = (By.XPATH,'//div[text()="確定"]')
    
    #保存
    saveElement = (By.XPATH,'//main//div[text()="保存"]')


