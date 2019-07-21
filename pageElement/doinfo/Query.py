'''
DO检索
'''
from selenium.webdriver.common.by import By
class Query():
    
    #首页的 D/O确定
    DOElement = (By.XPATH,'//main[@class="v-content"]//div[text()="D/O確定"]')
    #纳入场所
    inPlaceElement = (By.XPATH,'//input[@aria-label="納入場所"]/..')
    selInPlaceElement = (By.XPATH,'//div[contains(@class,"menuable__content__active")]//div[@class="v-list theme--light"]/div[2]')
    #DO NO
    DONOElement = (By.XPATH,'//input[@aria-label="D/O NO"]')
    #集装箱NO
    containerNOElement = (By.XPATH,'//input[@aria-label="コンテナNO"]')
    #运输形态
    transportElement = (By.XPATH,'//input[@aria-label="運送形態"]/..')
    selTransportElement = (By.XPATH,'//div[text()="SEA"]')
    #海外取引先
    overseasSupElement = (By.XPATH,'//input[@aria-label="海外取引先"]')
    #选择海外取引先查询
    selOverseasSupElement  = (By.XPATH,'//div[contains(@class,"menuable__content__active")]//div[@class="v-list theme--light"]/div[1]')
    #到达港
    toportElement = (By.XPATH,'//input[@aria-label="陸揚港"]/..')
    #选择到达港ANCHORAGE
    selToportElement = (By.XPATH,'//div[contains(@class,"menuable__content__active")]//div[@class="v-list theme--light"]/div[4]')
    #开始日期ETD
    startDateElement = (By.XPATH,'//input[@aria-label="ETD"]/..')
    #选择开始日期20日
    selStartDateElement = (By.XPATH,'//div[text()="1日"]')
    #结束日期ETA
    endDateElement = (By.XPATH,'//input[@aria-label="ETA"]/..')
    #选择结束日期为22
    selEndDateElement = (By.XPATH,'//div[@class="application theme--light"]/div[1]//div[text()="20日"]')
    #选择结束日期为19
    selEndDate1Element = (By.XPATH,'//div[@class="application theme--light"]/div[1]//div[text()="19日"]')
    #B/L发行日
    BLStartDateElement = (By.XPATH,'//input[@aria-label="B/L発行日"]')
    #选择发行日开始日期
    selBLStartDateElement = (By.XPATH,'//div[@id="app"]/div[1]//div[text()="1日"]/../..')
    #B/L结束日期
    BLEndDateElement = (By.XPATH,'//form[1]/div[1]/div[1]/div[9]/div[1]/div[2]')
    #选择B/L结束日期
    SelBLEndDateElement = (By.XPATH,'//div[@class="application theme--light"]/div[1]//div[text()="28日"]')
    #担当者ID
    actorIDElement = (By.XPATH,'//input[@aria-label="担当者ID"]/..//div[@class="v-input__icon v-input__icon--append"]')   # //input[@aria-label="担当者ID"]/..
    selActorElement = (By.XPATH,'//div[contains(@class,"menuable__content__active")]//div[@class="v-list theme--light"]/div[2]')
    #状态
    statusElement = (By.XPATH,'//input[@aria-label="ステータス"]/..')
    selStatusElement = (By.XPATH,'//div[text()="DO諸掛登録済"]')
    #检索按钮
    searchElement = [By.XPATH,'//main//button[@class="btn-search v-btn theme--light"]']
    