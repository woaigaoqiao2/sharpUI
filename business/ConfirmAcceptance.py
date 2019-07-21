from pageElement.ConfirmAcceptance import ConfirmAcceptance
from time import sleep
from random import choice
from selenium.webdriver.common.keys import Keys


class ConfirmAcceptance(ConfirmAcceptance):
    
    
    def __init__(self):
        None
        
        
    def confirmAcceptance(self, driver):
        driver.find_element(*self.confirm_accept_element).click()
        sleep(1)
        driver.find_element(*self.place_of_delivery_element).send_keys("西神")
        sleep(0.5)
        driver.find_element(*self.place_of_delivery_choice_element).click()
        driver.find_element(*self.ETD_start_element).click()
        sleep(0.7)
        driver.find_element(*self.ETD_start_click_element).click()
        driver.find_element(*self.ETD_end_element).click()
        sleep(0.7)
        driver.find_element(*self.ETD_end_click_element).click()
        driver.find_element(*self.ETA_start_element).click()
        sleep(0.7)
        driver.find_element(*self.ETA_start_click_element).click()
        driver.find_element(*self.ETA_end_element).click()
        sleep(0.7)
        driver.find_element(*self.ETA_end_click_element).click()
        driver.find_element(*self.status_element).send_keys(Keys.SPACE)
        sleep(0.7)
        driver.find_element(*self.status_choice_element).click()
        driver.find_element(*self.search_button_element).click()
        sleep(1)
        driver.find_element(*self.DO_NO_choice_element).send_keys(Keys.SPACE)
        sleep(0.5)
        driver.find_element(*self.confirm_accept_button_element).click()
        sleep(1)
        driver.find_element(*self.confirm_button_element).click()
#         return driver.find_element(*self.get_assert_message_element).text
        