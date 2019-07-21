"""
@author: yangjun
"""
from selenium.webdriver.common.by import By
from time import strftime


class RequiredFieldElement():
    nowdate = strftime("%d")
    # 依赖日为空返回值
    trust_day_value_element = [By.XPATH, '//div[text()="依頼日必要である"]']
    # LCL B/L発行日为空返回值
    issue_day_value_element = [By.XPATH, '//div[text()="B/L発行日必要である"]']
    # FCL B/L発行日为空返回值
    issue_day_FCL_value_element = [By.XPATH, '//div[text()="INV P/L情報が不整備です、ご確認お願いします。"]']
    # ETA为空返回值
    ETA_value_element = [By.XPATH, '//div[text()="ETA必要である"]']
    # 積み方为空返回值
    loading_method_value_element = [By.XPATH, '//div[text()="積み方必要である"]']
    # 輸出通関日为空返回值
    export_dec_date_value_element = [By.XPATH, '//div[text()="輸出通関日必要である"]']
    # 船社・航空会社为空返回值
    ship_air_company_value_element = [By.XPATH, '//div[text()="船社・航空会社必要である"]']
    # 通関業者为空返回值
    customs_broker_value_element = [By.XPATH, '//div[text()="通関業者必要である"]']
    # 貨物タイプ为空返回值
    cargo_type_value_element = [By.XPATH, '//div[text()="貨物タイプ必要である"]']
    # CONTAINER NO与..SIZE为空返回值
    container_value_element = [By.XPATH, '//div[contains(text(),"INV P/L情報が不整備です、ご確認お願いします。")]']
    # 陸揚港
    landing_port_element = [By.XPATH, '//input[@aria-label="陸揚港"]']
    # 陸揚港清除
    landing_port_clear_element = [By.XPATH, '//input[@aria-label="陸揚港"]/..//div/i']
    # 陸揚港下拉框
    landing_port_click_element = [By.XPATH, '//div[contains(@class,"menuable__content__active")]//a']
    # 通貨
    currency_element = [By.XPATH, '//input[@aria-label="通貨"]']
    # 通貨清除
    currency_clear_element = [By.XPATH, '//input[@aria-label="通貨"]/..//div/i']
    # 通貨下拉框
    currency_click_element = [By.XPATH, '//div[contains(@class,"menuable__content__active")]//a']
    # 輸送形態下拉框
    transport_mode_choice_elements = [By.XPATH,'//*[@id="app"]/div[20]/div/div/div/a']
    # 輸送形態清空按钮
    transport_mode_clear_element = [By.XPATH, '//main[@class="v-content"]//div[@class="flex md3"]//i']
    # 清空后点击輸送形態
    transport_mode_after_element = [By.XPATH, '//input[@aria-label="輸送形態"]']
    # 輸送形態-SEA
    transport_mode_SEA_element = [By.XPATH, '//*[@id="app"]/div[17]/div/div/div[1]/a/div']
    # 積み方选为FCL
    loading_method_FCL_element = [By.XPATH,
                                  '//div[contains(@class,"menuable__content__active")]//div[@class="v-list__tile__title"]']
    # AIR 确认送信后
    end_element = [By.XPATH, '//*[@id="app"]/div[25]/div/div/div[3]/button[2]/div']
    # IV List下 选择数据
    choose_data_element = (By.XPATH, '//table/tbody/tr/td')
    # 等待弹框
    dealing = [By.XPATH, '//div[@class="v-dialog v-dialog--persistent"]']
