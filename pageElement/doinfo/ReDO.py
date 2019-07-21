'''
Created on 2019年7月4日

@author: chinasoft.jl.ma
DO解除
'''
from selenium.webdriver.common.by import By


class ReDO():
    #首页的 D/O确定
    DOElement = (By.XPATH,'//main[@class="v-content"]//div[text()="D/O確定"]')
    #按状态检索  D确定済
    DOstatusElement = (By.XPATH,'//label[text()="ステータス"]/..')
    selDOstatusElement = (By.XPATH,'//div[text()="DO確定済"]')
    #检索
    selElement = (By.XPATH,'//main//button[@class="btn-search v-btn theme--light"]')
    #选择要修改得数据
    selDateElement = (By.XPATH,'//tbody/tr[1]//div[@class="v-input--selection-controls__ripple"]')
    #DO解除申请
    reDOReqElement = (By.XPATH,'//div[text()="D/O解除申請"]')
    #申请理由
    beaucElement = (By.XPATH,'//input[@aria-label="Ｑ１解除する理由を入力："]')
    #选项1
    optElement1 = (By.XPATH,'//label[text()="Ｂ．検収されていない"]')
    #选项2
    optElement2 = (By.XPATH,'//label[text()="Ａ．はい"]')
    #解除申请
    reReqElement = (By.XPATH,'//DIV[text()="解除申請"]')
    
