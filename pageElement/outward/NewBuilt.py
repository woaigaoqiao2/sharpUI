'''
Created on 2019年6月24日

@author: chinasoft.jl.ma
新规页面元素
'''
from selenium.webdriver.common.by import By

class NewBuilt():
    #首页 做成
    outWardElement = [By.XPATH,'//div[@class="seq" and text()="7"]']
    #新规
    newBuiltElement = [By.XPATH,'//main//button[@class="v-btn theme--light"]']                       
    #BL提单号
    BLNoEelement = [By.XPATH,'//input[@aria-label="B/L NO"]']
    #海外取引先
    overseasSupElement = [By.XPATH,'//input[@aria-label="海外取引先"]']
    #选择海外取引先
    selOverseasSupElement  = [By.XPATH,'//div[text()="70040:GROUP SENSE LTD."]']
    #B/L开始发行日
    BLDateElement = [By.XPATH,'//input[@aria-label="B/L発行日"]']
    #选择发行日开始日期
    selBLStartDateElement = [By.XPATH,'//div[text()="1日"]/../..']
    
    #積出港
    fromportElement = [By.XPATH,'//input[@aria-label="積出港"]/..']
    #选择出发港为AMSTERDAM
    selFromportElement = [By.XPATH,'//div[text()="AMM:ＡＭＭＡＮ"]']
    
    #到达港
    toportElement = [By.XPATH,'//input[@aria-label="陸揚港"]/..']
    #选择到达港ANCHORAGE
    selToportElement = [By.XPATH,'//div[text()="ADL:ＡＤＥＬＡＩＤＥ"]']
    
    #开始日期ETD
    startDateElement = [By.XPATH,'//input[@aria-label="ETD"]/..']
    #选择开始日期20日
    selStartDateElement = [By.XPATH,'//div[text()="20日"]']

    #结束日期ETA
    endDateElement = [By.XPATH,'//input[@aria-label="ETA"]/..']
    #选择结束日期为22
    selEndDateElement = [By.XPATH,'//div[@class="application theme--light"]/div[1]//div[text()="20日"]']
    
    #本船名
    shipElement = [By.XPATH,'//input[@aria-label="本船名"]']
    
    #船社或航空社
    shippingElement = [By.XPATH,'//input[@aria-label="船社・航空会社"]/..']
    #选择船社
    selShippingElement = [By.XPATH,'//div[text()="F00001:SJL-One Japan"]']
    
    #选择货物类型
    carGoTypeElement = [By.XPATH,'//input[@aria-label="貨物タイプ"]/..']
    #选择货物为一般品
    selCarGoTypeElement = [By.XPATH,'//div[contains(@class,"v-autocomplete__content")]//div[text()="一般品"]']
    #选择报关者
    customsElement = [By.XPATH,'//input[@aria-label="通関業者"]/..']
    selCustomsElement = [By.XPATH,'//div[text()="029001:SJL（株）－南海エクスプレス"]']
    
    #输送形态
    transportElement = [By.XPATH,'//input[@aria-label="輸送形態"]/..']
    #选择输送状态为SEA
    selTransportElement = [By.XPATH,'//div[text()="SEA"]']
    
    #选择建值
    keyVElement = [By.XPATH,'//input[@aria-label="建值"]/..']
    selKyeVElement = [By.XPATH,'//div[text()="運送人渡条件"]']
    
    #选择装法
    loadingElement= [By.XPATH,'//input[@aria-label="積み方"]/..']
    selLoadingElement = [By.XPATH,'//div[text()="FCL"]']
    
    #选择货币
    doriElement = [By.XPATH,'//input[@aria-label="通貨"]/..']
    selDoriElement = [By.XPATH,'//div[text()="USD"]']
    
    #20F
    cwElement = [By.XPATH,'//input[@aria-label="コンテナ20F-本数"]']
    #40F
    gwElement = [By.XPATH,'//input[@aria-label="コンテナ40F-本数"]']
    #40H
    nwElement = [By.XPATH,'//input[@aria-label="コンテナ40H-本数"]']
    
    #保存
    saveElement = [By.XPATH,'//div[text()="保存"]']
    #确定
    doElement = [By.XPATH,'//div[text()="確定"]']
    
    saveOevrElement = [By.XPATH,'//div[text()="保存が完了しました。"]']
    
   
    
    
