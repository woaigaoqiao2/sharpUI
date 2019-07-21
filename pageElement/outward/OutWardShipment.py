'''
Created on 2019年5月22日
@author: chinasoft.jl.ma
运赁外货登录
'''
from selenium.webdriver.common.by import By

class OutWardShipment(object):
    #首页 做成
    outWardElement = [By.XPATH,'//div[@class="seq" and text()="7"]']                            
    #BL提单号
    BLNoEelement = [By.XPATH,'//input[@aria-label="B/L NO"]']
    
    #海外取引先
    overseasSupElement = [By.XPATH,'//input[@aria-label="海外取引先"]']
    #选择海外取引先查询
    selOverseasSupElement  = [By.XPATH,'//div[contains(@class,"menuable__content__active")]//div[@class="v-list theme--light"]/div[1]'] 
    
    #B/L开始发行日
    BLStartDateElement = [By.XPATH,'//input[@aria-label="B/L発行日"]']
    #选择发行日开始日期
    selBLStartDateElement = [By.XPATH,'//div[text()="20日"]/../..']
    #B/L结束日期
    BLEndDateElement = [By.XPATH,'//div[@class="layout row wrap"]/div[3]//input[@aria-label="~"]']
    #选择B/L结束日期
    SelBLEndDateElement = [By.XPATH,'//div[@class="application theme--light"]/div[1]//div[text()="21日"]']     
    
    #输送形态
    transportElement = [By.XPATH,'//input[@aria-label="輸送形態"]/..']
    #选择输送状态为SEA
    selTransportElement = [By.XPATH,'//div[text()="SEA"]']
    
    #積出港
    fromportElement = [By.XPATH,'//input[@aria-label="積出港"]/..']
    #选择出发港为AMSTERDAM
    selFromportElement = [By.XPATH,'//div[contains(@class,"menuable__content__active")]//div[@class="v-list theme--light"]/div[2]']
    
    #到达港
    toportElement = [By.XPATH,'//input[@aria-label="陸揚港"]/..']
    #选择到达港ANCHORAGE
    selToportElement = [By.XPATH,'//div[contains(@class,"menuable__content__active")]//div[@class="v-list theme--light"]/div[2]']
    
    #开始日期ETD
    startDateElement = [By.XPATH,'//input[@aria-label="ETD"]/..']
    #选择开始日期20日
    selStartDateElement = [By.XPATH,'//div[text()="20日"]']

    
    #结束日期ETA
    endDateElement = [By.XPATH,'//input[@aria-label="ETA"]/..']
    #选择结束日期为22
    selEndDateElement = [By.XPATH,'//div[@class="application theme--light"]/div[1]//div[text()="20日"]']
    #选择结束日期为19
    selEndDate1Element = [By.XPATH,'//div[@class="application theme--light"]/div[1]//div[text()="19日"]']
    
    #本船名
    shipElement = [By.XPATH,'//input[@aria-label="本船名"]']
    
    #船社或航空社
    shippingElement = [By.XPATH,'//input[@aria-label="船社・航空会社"]/..']
    selShippingElement = [By.XPATH,'//div[contains(@class,"menuable__content__active")]//div[@class="v-list theme--light"]/div[1]']
    #检索按钮
    searchElement = [By.XPATH,'//main//button']
    #选择数据打勾框
    selDataElement = [By.XPATH,'//td[text()="mjl001"]/..//input']
    #海上，航空运凭计算按钮
    transportationElement = [By.XPATH,'//div[@class="v-btn__content" and text()="海上・航空運賃計算"]']
    #FEE金额,先清空费用再进行修改
    FEEElement = [By.XPATH,'//*[@id="app"]/div[32]/main/div/div[1]/div[4]/div[2]/div/div/table/tbody/tr[1]/td[2]/div/div/div[1]/div/input']
                            
    #保存
    preserveElement = [By.XPATH,'//div[@class="v-btn__content" and text()="保存"]']
