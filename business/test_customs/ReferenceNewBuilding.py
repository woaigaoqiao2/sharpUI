"""
编写人:陈博华
"""
from time import time
from common.Browser import Browser
from .method import search_and_click
from pageElement.SAlogin.HomePage import HomePageElement
from pageElement.SAlogin.newlyBuild import NewlyBuildElement



class ReferenceNewBuilding(NewlyBuildElement, HomePageElement):


    def __init__(self):
        return


    def reference_newly_built01(self, driver):
        Browser(driver,10).click(self.SA_button_element)
        Browser(driver,10).click(self.BL_NO_element)
        Browser(driver,10).send_keys(self.BL_NO_element,"test78675")
        Browser(driver,10).click(self.search_element)
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        search_and_click(driver,self.registered_elements,self.next_page_element,self.display_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        Browser(driver,10).click(self.reference_new_building_element)
        Browser(driver,10).click(self.loading_port_clear_element)
        Browser(driver,10).click(self.unloading_port_clear_element)
        Browser(driver,10).click(self.INV_add_element)
        Browser(driver,10).click(self.IV_NO_element)
        Browser(driver,10).click(self.IV_NO_search_element)
        Browser(driver,10).choice_check_box(self.choose_click_element)
        Browser(driver,10).click(self.IV_list_add_element)
        message = 'test'+str(time())[-5:]
        Browser(driver,10).click(self.Master_BL_NO_element)
        Master_BL_NO = Browser(driver,10).get_attribute(self.Master_BL_NO_element,"value")
        if Master_BL_NO:
            Browser(driver,10).click(self.Master_BL_NO_clear_element)
        Browser(driver,10).send_keys(self.Master_BL_NO_element,message)
        House_BL_NO = Browser(driver,10).get_attribute(self.House_BL_NO_element,"value")
        if House_BL_NO:
            Browser(driver,10).click(self.House_BL_NO_clear_element)
        Browser(driver,10).send_keys(self.House_BL_NO_element,message)
        transport_text = driver.find_element(*self.transport_mode_element).text
        if transport_text == "SEA":
            element_text = driver.find_element(*self.loading_method_get_element).text
            if element_text == 'FCL':
                NO_elements = driver.find_elements(*self.container_NO_element)
                size_elements = driver.find_elements(*self.container_size_element)
                for no in range(len(NO_elements)):
                    NO_elements[no].send_keys('New Practice 2')
                    size_elements[no].click()
                    Browser(driver,10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        Browser(driver,10).click(self.temporary_saving_element)
        Browser(driver,10).click(self.confirm_button_element)
        Browser(driver,10).click(self.return_element)
        return message

