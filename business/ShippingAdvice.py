from pageElement.ShippingAdvice import ShippingAdvice
from time import sleep,time
from selenium.webdriver.common.keys import Keys
from random import random, choice
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



class ShippingAdvice(ShippingAdvice):
    
    
    def __init__(self):
        None
        
        
    def newlyBuilt(self, driver):
        driver.find_element(*self.SA_button_element).click()
        sleep(2)
        driver.find_element(*self.newlyBuilt_element).click()
        sleep(1)
        driver.find_element(*self.INV_add_element).click()
        sleep(1)
        driver.find_element(*self.IV_NO_element).send_keys("20190524132100")
        driver.find_element(*self.search_element).click()
        sleep(1)
        driver.find_element(*self.choose_click_element).send_keys(Keys.SPACE)
        driver.find_element(*self.IV_list_add_element).click()
        sleep(0.3)
        message = 'test'+str(time())[-5:]
        driver.find_element(*self.Master_BL_NO_element).send_keys(message)
        driver.find_element(*self.House_BL_NO_element).send_keys(message)
        driver.find_element(*self.trust_day_element).click()
        sleep(0.5)
        driver.find_element(*self.trust_day_click_element).click()
        driver.find_element(*self.issue_date_element).click()
        sleep(1)
        driver.find_element(*self.issue_date_click_element).click()
        sleep(0.5)
        driver.find_element(*self.ETA_element).click()
        sleep(0.5)
        driver.find_element(*self.ETA_click_element).click()
        driver.find_element(*self.loading_method_element).send_keys(Keys.SPACE)
        sleep(0.5)
        element_list = driver.find_elements(*self.loading_method_choice_elements)
        element = choice(element_list)
        element.click()
        element_text = element.text
        driver.find_element(*self.export_declaration_date_element).click()
        sleep(0.5)
        driver.find_element(*self.export_declaration_date_click_element).click()
        driver.find_element(*self.shipping_co_element).send_keys('japan')
        sleep(1)
        try:
            element_list = driver.find_elements(*self.shipping_co_choice_element2)
            choice(element_list).click()
        except:
            element_list = driver.find_elements(*self.shipping_co_choice_element1)
            choice(element_list).click()
        sleep(0.5)
        driver.find_element(*self.ships_name_element).send_keys('master')
        driver.find_element(*self.VOYAGE_NO_element).send_keys('qaz007')
        driver.find_element(*self.SI_NO_element).send_keys('qaz007')
        driver.find_element(*self.customs_broker_element).click()
        sleep(0.5)
        try:
            element_list = driver.find_elements(*self.customs_broker_choice_element2)
            choice(element_list).click()
        except:
            element_list = driver.find_elements(*self.customs_broker_choice_element1)
            choice(element_list).click()
        driver.find_element(*self.cargo_type_element).click()
        sleep(0.5)
        try:
            element_list = driver.find_elements(*self.cargo_type_choice_element2)
            choice(element_list).click()
        except:
            element_list = driver.find_elements(*self.cargo_type_choice_element1)
            choice(element_list).click()
        driver.find_element(*self.INV_checklist_element).send_keys(Keys.SPACE)
        if element_text == 'FCL':
            driver.find_element(*self.container_NO_element).send_keys('New Practice 2')
            element_list = driver.find_elements(*self.container_size_element)
            sleep(1)
            choice(element_list).click()
        driver.find_element(*self.PID_element).send_keys('5')
        sleep(0.5)
        driver.find_element(*self.temporary_saving_element).click()
        sleep(1)
        driver.find_element(*self.confirm_button_element).click()
        sleep(1)
        driver.find_element(*self.file_upload_element).click()
        sleep(1)
        element_list = driver.find_elements(*self.upload_choice_element)
        choice(element_list).send_keys(Keys.SPACE)
        sleep(0.7)
        driver.find_element(*self.upload_button_element).send_keys(r'D:\Users\chinasoft.bh.chen\Desktop\test.xlsx')
        sleep(1.5)
        driver.find_element(*self.close_button_element).send_keys(Keys.ENTER)
        sleep(0.5)
        driver.find_element(*self.sending_confirmation_element).click()
        sleep(1)
        driver.find_element(*self.sure_button_element).click()
        
        
        
        
        
        
    