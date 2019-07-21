from selenium.webdriver.common.by import By



class ConfirmAcceptance():
    
    # 受入确认模块
    confirm_accept_element = [By.XPATH,'//main//div[text()="受入確認"]/..']
    # 纳入场所
    place_of_delivery_element = [By.XPATH,'//main//input[@aria-label="納入場所"]']
    # 纳入场所下拉框所有元素
    place_of_delivery_choice_element = [By.XPATH,'//div[contains(@class,"menuable__content__active")]//a']
    # ETD开始时间输入框
    ETD_start_element = [By.XPATH,'//input[@aria-label="ETD"]']  
    # ETD开始时间选择
    ETD_start_click_element = [By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[4]/td[6]/button']
    # ETD结束时间
    ETD_end_element = [By.XPATH,'//div[@label="ETD"]/../../div[@class="flex md6 pl-2"]//input'] 
    # ETD结束时间选择
    ETD_end_click_element = [By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[4]/td[6]/button']
    # ETA开始时间输入框
    ETA_start_element = [By.XPATH,'//main//input[@aria-label="ETA"]']
    # ETA开始时间选择
    ETA_start_click_element = [By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/button']
    # ETA结束时间输入框
    ETA_end_element = [By.XPATH,'//main//div[@label="ETA"]/../../div[@class="flex md6 pl-2"]//input']
    # ETA结束时间选择
    ETA_end_click_element = [By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/button']
    # ステータス状态
    status_element = [By.XPATH,'//main//input[@aria-label="ステータス"]']
    # ステータス下拉框
    status_choice_element = [By.XPATH,'//div[contains(@class,"menuable__content__active")]//a']
    # 検索
    search_button_element = [By.XPATH,'//div[text()="検索"]/..']
    # 
#     element = '//main//table/tbody/tr/td[1]/div/div/div/div/input'
#     DO_NO_choice_element = [By.XPATH,element]
    # 
    confirm_accept_button_element = [By.XPATH,'//main/div/div[1]/div[1]/div[2]/button[3]']
    confirm_button_element = [By.XPATH,'//div[@class="v-dialog v-dialog--active"]//button']
    