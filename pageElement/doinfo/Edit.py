'''
Created on 2019年7月1日

@author: chinasoft.jl.ma
在订单确定之前  修改信息
'''
from selenium.webdriver.common.by import By
class Edit():
    
    #首页的 D/O确定
    DOElement = (By.XPATH,'//main[@class="v-content"]//div[text()="D/O確定"]')
    DONOElement = (By.XPATH,'//input[@aria-label="D/O NO"]')
    #按状态检索  DO諸掛登録済
    DOstatusElement = (By.XPATH,'//label[text()="ステータス"]/..')
    selDOstatusElement = (By.XPATH,'//div[text()="DO諸掛登録済"]')
    #检索
    selElement = (By.XPATH,'//main//button[@class="btn-search v-btn theme--light"]')
    #选择要修改得数据
    selDateElement = (By.XPATH,'//tbody/tr[1]//div[@class="v-input--selection-controls__ripple"]')
    #配送再确认
    reconDoElement = (By.XPATH,'//div[text()="配送パターン再確認"]')
    #纳入予定日
    inclusionDateElement = (By.XPATH,'//input[@aria-label="納入予定日"]/..')
    selInclusionDateElement = (By.XPATH,'//div[text()="6日"]')
    #纳入时间
    inclusionTimeElement = (By.XPATH,'//input[@aria-label="時間"]')
    #配送者
    distributorElement = (By.XPATH,'//input[@aria-label="配送業者"]')
    selDistributorElement = (By.XPATH,'//span[text()="大和"]/..')
    #搬送服务
    conveElement = (By.XPATH,'//input[@aria-label="搬送サービス"]/..')
    selConveElement = (By.XPATH,'//div[contains(@class,"menuable")]/div[1]//div[text()="チャーター"]')
    #保存
    saveElement = (By.XPATH,'//main//div[@class="v-card__actions"]/button[1]/div')
    #返回
    returnElement = (By.XPATH,'//main//div[@class="v-card__actions"]/button[3]/div')
    #点击确定
    determineElement = (By.XPATH,'//div[@class="v-dialog__content v-dialog__content--active"]//button')

    #搜索
    seachElement = [By.XPATH,'//main//i[text()="search"]/../..']
    #选择配送模式
    disModelEelemet = [By.XPATH,'//input[@aria-label="配送パターン"]/..//div[@class="v-input__icon v-input__icon--append"]']  # //input[@aria-label="配送パターン"]/..
    selDisModelEelemet = [By.XPATH,'//div[contains(@class,"v-menu__content theme--light menuable__content__active")]//div[@class="v-list theme--light"]/div[1]']
    #保存配送模式
    saveDisElement = [By.XPATH,'//div[@class="v-dialog__content v-dialog__content--active"]//form/div/div[3]//div[text()="保存"]/..']
    #DO NO
    DONOElement = (By.XPATH, '//input[@aria-label="D/O NO"]')
