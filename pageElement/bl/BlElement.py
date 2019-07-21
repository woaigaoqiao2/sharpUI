'''
Created on 2019年5月20日

@author: chinasoft.xp.chen
'''
from selenium.webdriver.common.by import By

class BlElement(object):
    #BL確認完了送信
    BL_element=[By.XPATH,'//main//div[@class="flex nav xs6"][1]//div[2]//div[@class="name"]']
    #海外取引先
    foreignguests_element=[By.XPATH,"(//input[@type='text'])[6]"]
    #海外取引先的下拉菜单
    Choice_forei=[By.XPATH,'//span[@class="v-list__tile__mask"]']
    #D/O NO
    DOno_element=[By.XPATH,"(//input[@type='text'])[7]"]
    #B/L NO
    BLno_element=[By.XPATH,"(//input[@type='text'])[8]"]
    #B/L DATE
    start_date=[By.XPATH,"(//input[@type='text'])[9]"]
    #BLenddata
    end_date=[By.XPATH,"(//input[@type='text'])[10]"]
    #开始日期的向前按钮<
    left_element=[By.XPATH,'//div[@label="B/L DATE"]//i[text()="chevron_left"]']
    #结束日期的向前按钮<
    left_element1=[By.XPATH,'//div[@label="~"]//i[text()="chevron_left"]/../..']
    #>
    right_element=[By.XPATH,'//div[@label="B/L DATE"]//i[text()="chevron_right"]']
    #开始日期1日
    startdate_1=[By.XPATH,'//div[@label="B/L DATE"]//div[text()="{}"]'.format("1日")]
    #结束日期5日
    enddate_5=[By.XPATH,'//div[@label="~"]//div[text()="{}"]'.format("5日")]
    enddate_8=[By.XPATH,'//div[@label="~"]//div[text()="{}"]'.format("8日")]
    #开始选择14日
    startdate_14=[By.XPATH,'//div[@label="B/L DATE"]//div[text()="{}"]'.format("14日")]
    #开始选择25日
    startdate_25=[By.XPATH,'//div[@label="B/L DATE"]//div[text()="{}"]'.format("25日")]
    #开始日期选择3日
    startdate_3=[By.XPATH,'//div[@label="B/L DATE"]//div[text()="{}"]'.format("3日")]
    startdate_8=[By.XPATH,'//div[@label="B/L DATE"]//div[text()="{}"]'.format("8日")]
    #开始日期选择11日
    startdate_11=[By.XPATH,'//div[@label="B/L DATE"]//div[text()="{}"]'.format("11日")]
    #结束选择14日
    enddate_14=[By.XPATH,'//div[@label="~"]//div[text()="{}"]'.format("14日")]
    #结束选择11日
    enddate_11=[By.XPATH,'//div[@label="~"]//div[text()="{}"]'.format("11日")]
    #结束选择25日
    enddate_25=[By.XPATH,'//div[@label="~"]//div[text()="{}"]'.format("25日")]
    #结束日期3日
    enddate_3=[By.XPATH,'//div[@label="~"]//div[text()="{}"]'.format("3日")]
    #運送形態
    Shochin_element=[By.XPATH,"(//main//input[@type='text'])[6]/.."]
    #SEA
    SEA_element=[By.XPATH,'(//div[contains(@class,"menuable__content__active")]//div[@class="v-list__tile__title"])[1]']
    #AIR
    AIR_element=[By.XPATH,'(//div[contains(@class,"menuable__content__active")]//div[@class="v-list__tile__title"])[2]']
    #送信状態
    Sendingstate_element=[By.XPATH,"(//main//input[@type='text'])[7]/.."]
    #送信済み
    Sendemail_element=[By.XPATH,'(//div[contains(@class,"menuable__content__active")]//div[@class="v-list__tile__title"])[1]']
    #未送信
    notsend_element=[By.XPATH,'(//div[contains(@class,"menuable__content__active")]//div[@class="v-list__tile__title"])[2]']  
    #SJL輸入担当
    SJL_element=[By.XPATH,"(//input[@type='text'])[13]"]
    #SJL选择
    choice_sjl=[By.XPATH,'//span[@class="v-list__tile__mask"]'] 
    #检索
    Search_element=[By.XPATH,'//main//button[contains(@class,"btn-search")]']  
    #勾选框
    Option_element=[By.XPATH,"//td/div/div/div/div/div"]
    #ActualInfo Input按钮
    ActualInfo_element=[By.XPATH,"(//main//button[2])[1]"]
    #输入Air C/W Actual
    CW=[By.XPATH,'(//form//input)[3]']
    #输入G/W
    GW=[By.XPATH,'(//form//input)[4]']
    #输入M3
    M3=[By.XPATH,'(//form//input)[5]']
    #集装箱信息保存
    Preserve=[By.XPATH,'((//div[@class="v-card theme--light"])[2]//div[@class="v-btn__content"])[1]']
    #集装箱核对弹窗ok确定
    Sure=[By.XPATH,'(//button[@type="button" and @class="v-btn theme--light"])[7]']
    #確認完了通知メール按钮
    Inform_element=[By.XPATH,"//main//button[3]"]
    #送信弹窗确定按钮（有时候不出现这个弹窗）
    Sure_element=[By.XPATH,'//div[text()="はい"]']
    # mail送信
    mail=[By.XPATH,'//div[text()="Mail送信"]']
    sendok = [By.XPATH, '//div[text()="確定"]']
    #OK确定
    sure=[By.XPATH,'//div[contains(@class,"v-dialog--active")]//button']
    #弹窗的文本
    alert=[By.XPATH,'(//div[@class="v-card__text text-xs-center"])[2]']
    #送信成功弹窗关闭
    Close_element=[By.XPATH,'//div[contains(@class,"v-dialog--active")]//div[@class="v-btn__content"]']
    #获取提示需要添加B/L附件资料
    tip=[By.XPATH,'(//div[@class="v-card__text text-xs-center"])[3]']
    #获取提示需要添加B/L附件资料的确定按钮
    Bl_sure=[By.XPATH,'//div[text()="確定"]']
    #获取检索结果的页码
    index_element=[By.XPATH,'//div[@class="v-datatable__actions__pagination"]']
    #获取检索结果D/O no的值
    actual_do=[By.XPATH,'//table[contains(@class,"theme--light")]/tbody/tr/td[3]']
    #获取检索结果B/L no的值
    actual_bl=[By.XPATH,'//table[contains(@class,"theme--light")]/tbody/tr/td[4]']
    #获取检索结果的B/L date
    atcual_date=[By.XPATH,'//table[contains(@class,"theme--light")]/tbody/tr/td[6]']
    #获取搜索结果的運送形態
    actual_shochin=[By.XPATH,'//table[contains(@class,"theme--light")]/tbody/tr/td[7]']
    #获取搜索结果的海外引取先
    actual_foreignguest=[By.XPATH,'//table[contains(@class,"theme--light")]/tbody/tr/td[2]'] 
    #获取送信状態的结果
    actual_sendingstate=[By.XPATH,'//table[contains(@class,"theme--light")]/tbody/tr/td[5]']
    #nodata
    nodata=[By.XPATH,'//tbody//td[@class="text-xs-center"]']
    
    