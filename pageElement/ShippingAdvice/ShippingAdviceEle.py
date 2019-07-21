'''
Created on 2019年7月4日

@author: chinasoft.yy.zhang
'''

from selenium.webdriver.common.by import By

class ShippingAdviceEle():
    #S/A登録 按钮
    SA_element = [By.XPATH,"//main//div[text()='S/A登録']/.."]
    #依頼日开始时间输入框
    rely_start_date_box_element = [By.XPATH,"//div[@class='v-menu' and@label='依頼日']"]
    #依頼日开始时间日期栏
    rely_start_date_element = [By.XPATH,"//div[contains(@class,'active')]//strong/.."]
    #依頼日开始时间年
    rely_start_year_element = [By.XPATH,"//li[text()='2019年']"]
    #依頼日开始时间月
    rely_start_month_element = [By.XPATH,"//tbody//td/button/div"]
    #依頼日开始时间日
    rely_start_day_element = [By.XPATH,"//tbody//td/button/div"]
    #依頼日结束时间输入框
    rely_end_date_box_element = [By.XPATH,"//div[@class='v-menu' and@label='依頼日']/../../div[2]"]
    #依頼日结束时间日期栏
    rely_end_date_element = [By.XPATH,"//div[contains(@class,'active')]//strong/.."]
    #依頼日结束时间年
    rely_endyear_element = [By.XPATH,"//li[text()='2019年']"]
    #依頼日结束时间月
    rely_endmonth_element = [By.XPATH,"//div[contains(@class,'active')]//td/button[not(contains(@class ,'disabled'))]/div"]
    #依頼日结束时间日
    rely_endday_element = [By.XPATH,"//div[contains(@class,'active')]//td/button[not(contains(@class ,'disabled'))]/div"]
    #"検索"按钮
    search_element = [By.XPATH,"//main//button[1]"]
    #实际依頼日
    actual_rely_data = [By.XPATH,"//main//tr/td[10]"]
    #新規按钮
    new_rule_element = [By.XPATH,"//main//a[1]"]
    #追加按钮
    add_element = [By.XPATH,"//main//div[3]/div[2]/button[1]"]
    #I/V List検索按钮
    IVlist_search_element = [By.XPATH,"//div[text()='検索']/.."]
    #I/V List勾选框
    IVlist_checkbox_list_element = [By.XPATH,"//div[contains(@class,'active')]//tbody/tr/td[1]"]
    #I/V List追加按钮
    IVlist_add_element = [By.XPATH,"//div[contains(@class,'active')]//button/div[text()='追加']"]
    #ETD 时间
    ETD_element = [By.XPATH,"//main//label[text()='ETD']/../input"]
    #ETA输入框
    ETA_box_element = [By.XPATH,"//main//label[text()='ETA']/../input"]
    #ETA时间日期栏
    ETA_date_element = [By.XPATH,"//div[@id='app']/div[1]//strong"]
    #ETA时间年
    ETA_year_element = [By.XPATH,"//li[text()='%s']"]
    #ETA时间月
    ETA_month_element = [By.XPATH,"//div[contains(@class,'active')]//div[text()='%s']"]
    #ETA时间日
    ETAend_day_element = [By.XPATH,"//div[contains(@class,'active')]//div[text()='%s']/.."]
    #失败提示
    failed_tip_element = [By.XPATH,"//div[contains(@class,'active')]//div[text()='確定']/../../../div[2]"]
    #I/V List 行
    tr_element = [By.XPATH,"//div[contains(@class,'active')]//tbody/tr"]
    #積出港
    delivery_port_element = [By.XPATH,"//div[contains(@class,'active')]//tbody/tr[%s]/td[3]"]
    #下一页按钮
    next_page_element = [By.XPATH,'//div[@class="elevation-0"]//button[2]//i']
    #I/V List勾选框
    IVlist_checkbox_element = [By.XPATH,"//tbody/tr[%s]//input"]
    #陸揚港
    unloading_port_element = [By.XPATH,"//div[contains(@class,'active')]//tbody/tr[%s]/td[4]"]
    #INV P/L勾选框
    PLcheck_box_list_elelment = [By.XPATH,"//main//tbody//td[1]"]
    #INV P/L情報列表
    PL_list_elelment = [By.XPATH,"//main//tbody/tr"]
    #行分け按钮
    sorting_button_element = [By.XPATH,"//div[3]//button[3]"]
    #Master B/L NO输入框
    Master_BLnumber_elelment = [By.XPATH, "//input[@aria-label='Master B/L NO']"]
    #House B/L NO输入框
    House_BLnumber_elelment = [By.XPATH, "//input[@aria-label='House B/L NO']"]
    #輸送形態输入框
    shipping_type_element = [By.XPATH, "//div[9]//div[contains(@class,'comma')]"]
    #積み方输入框
    loading_box_element = [By.XPATH,'//div[@role="combobox"and @label="積み方"]']
    #積み方选项
    loading_element = [By.XPATH, "//div[contains(@class ,'active')] // a"]
    #一時保存按钮
    save_button_element = [By.XPATH, "//main//button[1]"]
    #提示文本
    tip_element = [By.XPATH, "//div[contains(@class,'active')]//div[text()='確定']/../../../div[2]"]
    #確定按钮
    sure_button_element = [By.XPATH, "//div[contains(@class,'active')]//button"]
    #戻る(返回)按钮
    back_elemnet = [By.XPATH, "//div[text()='一時保存']/../..//div[text()='戻る']"]
    #B/L NO输入框
    BLnumber_box_element = [By.XPATH, "//label[text()='B/L NO']/../input"]
    #状態显示栏
    status_element = [By.XPATH, "//tr[1]/td[7]"]
    #勾选框
    check_box_list_element = [By.XPATH, "//main//tbody/tr/td[1]/div"]
    #参照新規作成按钮
    ref_create_button_element = [By.XPATH, "//button/div[text()='参照新規作成']"]
    #積出港输入框
    delivery_port_box_element = [By.XPATH, "//form//div[6]//input"]
    #積出港清除按钮
    delivery_clear_element = [By.XPATH,"//form//div[6]//i/.."]
    #陸揚港输入框
    unloading_port_box_element = [By.XPATH, "//form//div[11]//input"]
    #陸揚港清除按钮
    unloading_clear_element = [By.XPATH, "//form//div[11]//i/.."]
    #編集按钮
    edit_button_element = [By.XPATH, "//main//button[2]"]