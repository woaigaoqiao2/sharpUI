'''
Created on 2019年6月24日

@author: chinasoft.jl.ma
编辑订单信息
'''
from selenium.webdriver.common.by import By

class EditElement():
    
    #首页 做成
    outWardElement = (By.XPATH,'//div[@class="seq" and text()="7"]')
    
    #BL提单号
    BLNoEelement = (By.XPATH,'//input[@aria-label="B/L NO"]')
    #检索
    selElement = (By.XPATH,'//main//button')
    #选择要修改得数据
    selDateElement = (By.XPATH,'//tbody/tr[1]/td/div[1]//input')
    #编辑
    editElement = (By.XPATH,'//div[text()="編集"]')
    
    
    #到达港
    toportElement = (By.XPATH,'//input[@aria-label="陸揚港"]/..')
    #选择到达港AMM:AMMAN
    selToportElement = (By.XPATH,'//div[text()="ADL:ＡＤＥＬＡＩＤＥ"]')
    
    #集装箱数量
    #20F
    cwElement = (By.XPATH,'//input[@aria-label="コンテナ20F-本数"]')
    #40F
    gwElement = (By.XPATH,'//input[@aria-label="コンテナ40F-本数"]')
    #40H
    nwElement = (By.XPATH,'//input[@aria-label="コンテナ40H-本数"]')
    
    #开始时间和结束时间
    #开始日期ETD
    startDateElement = (By.XPATH,'//input[@aria-label="ETD"]/..')
    #选择开始日期20日
    selStartDateElement = (By.XPATH,'//div[text()="22日"]')

    #结束日期ETA
    endDateElement = (By.XPATH,'//input[@aria-label="ETA"]/..')
    #选择结束日期为22
    selEndDateElement = (By.XPATH,'//div[@class="application theme--light"]/div[1]//div[text()="24日"]')
    
    #保存
    saveElement = (By.XPATH,'//div[text()="保存"]')
    
    #返回
    returnElement = (By.XPATH,'//main[@class="v-content"]//div[text()="戻る"]')

    # 海上航空凭运计算
    costCalElement = [By.XPATH, '//div[text()="海上・航空運賃計算"]/..']
    # 确定
    doElement = [By.XPATH, '//div[text()="確定"]/..']
    
    
