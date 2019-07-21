from selenium.webdriver.common.by import By



class ConfirmAcceptance():
    
    
    confirm_accept_element = [By.XPATH,'//main/div/div[1]/div/div[2]/div/div/div/div[2]/div[3]']
    place_of_delivery_element = [By.XPATH,'//main//form/div/div/div[1]/div/div/div[1]/div[1]/input']
    place_of_delivery_choice_element = [By.XPATH,'//div[@class="v-menu__content theme--light menuable__content__active v-autocomplete__content"]//a']
    ETD_start_element = [By.XPATH,'//main//form/div/div/div[7]/div/div[1]/div/div/div/div/div[1]/div[1]/input']
    ETD_start_click_element = [By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[4]/td[6]/button']
    ETD_end_element = [By.XPATH,'//main//form/div/div/div[7]/div/div[2]/div/div/div/div/div[1]/div[1]/input']
    ETD_end_click_element = [By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[4]/td[6]/button']
    ETA_start_element = [By.XPATH,'//main//form/div/div/div[8]/div/div[1]/div/div/div/div/div[1]/div[1]/input']
    ETA_start_click_element = [By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/button']
    ETA_end_element = [By.XPATH,'//main//form/div/div/div[8]/div/div[2]/div/div[1]/div/div/div[1]/div[1]/input']
    ETA_end_click_element = [By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/button']
    status_element = [By.XPATH,'//main//form/div/div/div[11]/div/div/div[1]/div[1]/div[1]/input']
    status_choice_element = [By.XPATH,'//div[@class="v-menu__content theme--light menuable__content__active"]/div/div/div[1]/a']
    search_button_element = [By.XPATH,'//div[@class="pb-2 v-card theme--light"]//button[1]']
    element = '//main//table/tbody/tr/td[1]/div/div/div/div/input'
    DO_NO_choice_element = [By.XPATH,element]
    confirm_accept_button_element = [By.XPATH,'//main/div/div[1]/div[1]/div[2]/button[3]']
    confirm_button_element = [By.XPATH,'//div[@class="v-dialog v-dialog--active"]//button']
#     message_element = element.split('/td')[0]+r'/td[6]'
#     get_assert_message_element = [By.XPATH,message_element]
    