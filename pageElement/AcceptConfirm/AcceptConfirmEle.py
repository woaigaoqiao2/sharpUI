'''
Created on 2019年7月1日

@author: chinasoft.yy.zhang
'''

from selenium.webdriver.common.by import By

class AcceptConfirmEle():
    #"受入確認"按钮
    AC_element = [By.XPATH,"//main//div[text()='受入確認']"]
    #ステータス（状态）选择框
    status_element = [By.XPATH,"//form//div[13]"]
    #納入指示済（完成交货指示）
    have_confirmed_element = [By.XPATH,"//div[6]//a/div/div[1][1]"]
    #受入確認済
    acceptance_confirmation_element = [By.XPATH, "//div[contains(@class,'menuable__content__active')]//div[text()='受入確認済']"]
    #"検索"按钮
    search_element = [By.XPATH,"//main//button[1]/div"]
    #勾选框列表
    check_boxs = [By.XPATH,"//main//tbody/tr/td[1]/div"]
    #对应的D/O NO
    chosen_DO_number_element = [By.XPATH,"//tr[@active='true']/td[2]"]
    #对应的コンテナNO(集装箱编号)
    chosen_container_number_element = [By.XPATH,"//tr[@active='true']/td[4]"]
    #"受入确认"按钮
    AC_button_elelment = [By.XPATH,"//button/div[text()='受入確認']"]
    #"確定"按钮
    sure_element = [By.XPATH,"//div[@class='v-dialog v-dialog--active']//div[text()='確定']"]
    #D/O NO输入框
    DO_element = [By.XPATH,"//input[@aria-label='D/O NO']"]
    #コンテナNO(集装箱编号)输入框
    container_number_element = [By.XPATH,"//input[@aria-label='コンテナNO']"]
    #ステータス（状态）清除
    delete_element = [By.XPATH,"//main//label[text()='ステータス']/..//div[contains(@class,'clear')]"]
    #受入確認日
    AC_date_element = [By.XPATH,"//tbody/tr/td[23]"]
    #实际状态
    actual_status_element = [By.XPATH,"//tbody/tr/td[6]"]
    #B/L発行日结束时间输入框
    BLend_date_box_element = [By.XPATH,"//main//div[10]/div/div[2]"]
    #B/L発行日结束时间日期栏
    BLend_date_element = [By.XPATH,"//div[contains(@class,'active')]//div/strong"]
    #B/L発行日结束时间年
    BLendyear_element = [By.XPATH,"//li[text()='2019年']"]
    #B/L発行日结束时间月
    BLendmonth_element = [By.XPATH,"//div[contains(@class,'active')]//td/button[not(contains(@class ,'disabled'))]/div"]
    #B/L発行日结束时间日
    BLendday_element = [By.XPATH,"//div[contains(@class,'active')]//td/button[not(contains(@class ,'disabled'))]/div"]
    #实际BL日期
    actual_BL_data = [By.XPATH,"//tr/td[11]"]
    #B/L発行日开始时间输入框
    BLstart_date_box_element = [By.XPATH,"//main//div[10]/div/div[1]"]
    #B/L発行日开始时间日期栏
    BLstart_date_element = [By.XPATH,"//div[contains(@class,'active')]//div/strong"]
    #B/L発行日开始时间年
    BLstart_year_element = [By.XPATH,"//li[text()='2019年']"]
    #B/L発行日开始时间月
    BLstart_month_element = [By.XPATH,"//tbody//td/button/div"]
    #B/L発行日开始时间日
    BLstart_day_element = [By.XPATH,"//tbody//td/button/div"]
    #D/O NO输入框
    DOnumber_element = [By.XPATH,"//input[@aria-label='D/O NO']"]
    #实际D/O NO
    actual_DO_number = [By.XPATH,"//main//tr/td[2]"]
    #ETA结束时间输入框
    ETAend_date_box_element = [By.XPATH,"//main//div[@class='v-menu'and @label='ETA']/../../div[2]"]
    #ETA结束时间日期栏
    ETAend_date_element = [By.XPATH,"//div[contains(@class,'active')]//div/strong"]
    #ETA结束时间年
    ETAend_year_element = [By.XPATH,"//li[text()='2019年']"]
    #ETA结束时间月
    ETAend_month_element = [By.XPATH,"//div[contains(@class,'active')]//td/button[not(contains(@class ,'disabled'))]/div"]
    #ETA结束时间日
    ETAend_day_element = [By.XPATH,"//div[contains(@class,'active')]//td/button[not(contains(@class ,'disabled'))]/div"]
    #实际ETA日期
    actual_ETAdate_element = [By.XPATH,"//tbody/tr/td[9]"]
