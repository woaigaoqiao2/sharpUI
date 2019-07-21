"""
编写人:陈博华
"""
from time import sleep
from common.Wait import Wait
from common.Browser import Browser
from pageElement.SAlogin.HomePage import HomePageElement
from util.ElementUtil import ElementUtil



class HomePage(HomePageElement):


    def __init__(self):
        self._BL_NO = "13"


    def BL_No_search(self, driver, params=None):
        explain = u"[陈博华]海关新建海运送信"
        el = ElementUtil()
        if params == None:
            params = self._BL_NO
            Browser(driver,10).click(self.SA_button_element)
        el.click(driver,5,explain, *self.BL_NO_element)
        # Browser(driver,10).click(self.BL_NO_element)
        el.clear(driver, 5, explain, *self.BL_NO_element)
        # Browser(driver,10).clear(self.BL_NO_element)
        Browser(driver,10).send_keys(self.BL_NO_element,params)
        el.click(driver, 5, explain, *self.search_element)
        # Browser(driver,10).click(self.search_element)
        BL_NO_locates = driver.find_elements(*self.BL_NO_elements)
        for i in range(5):
            if BL_NO_locates == []:
                sleep(1)
                BL_NO_locates = driver.find_elements(*self.BL_NO_elements)
            else:
                break
        BL_NO_list = []
        for i in BL_NO_locates:
            BL_NO_list.append(i.text)
        return BL_NO_list,params


    def BL_issuance_start_date_search(self, driver):
        el = ElementUtil()
        # el.click(driver, 5, *self.SA_button_element)
        Browser(driver,10).click(self.SA_button_element)
        # el.clear(driver, 5, *self.BL_issuance_start_date_element)
        Browser(driver,10).clear(self.BL_issuance_start_date_element)
        # el.click(driver, 5, *self.BL_issuance_start_date_element)
        Browser(driver,10).click(self.BL_issuance_start_date_element)
        sleep(1)
        # el.click(driver, 5, *self.BL_last_month_element)
        Browser(driver,10).click(self.BL_last_month_element)
        # el.click(driver, 5, *self.start_date_element)
        Browser(driver,10).click(self.start_date_element)
        # el.click(driver, 5, *self.BL_NO_element)
        Browser(driver,10).click(self.BL_NO_element)
        date = Browser(driver,10).get_attribute(self.BL_issuance_start_date_element,"value")
        # el.click(driver, 5, *self.search_element)
        Browser(driver,10).click(self.search_element)
        Wait(driver,10).elementwait(lambda the_driver:the_driver.find_element(*self.BL_Issuance_Date_elements))
        BL_Issuance_Date_locates = driver.find_elements(*self.BL_Issuance_Date_elements)
        BL_Issuance_Date_list = []
        for i in BL_Issuance_Date_locates:
            BL_Issuance_Date_list.append(i.text)
        return BL_Issuance_Date_list,date


    def BL_issuance_end_date_search(self, driver):
        # el = ElementUtil()
        # el.click(driver, 5, *self.SA_button_element)
        Browser(driver,10).click(self.SA_button_element)
        # el.clear(driver,5,*self.BL_issuance_end_date_element)
        Browser(driver,10).clear(self.BL_issuance_end_date_element)
        # el.click(driver, 5, *self.BL_issuance_end_date_element)
        Browser(driver,10).click(self.BL_issuance_end_date_element)
        sleep(0.7)
        # el.click(driver, 5, *self.BL_last_month_element2)
        Browser(driver,10).click(self.BL_last_month_element2)
        # el.click(driver, 5, *self.end_date_element)
        Browser(driver,10).click(self.end_date_element)
        # el.click(driver, 5, *self.BL_NO_element)
        Browser(driver,10).click(self.BL_NO_element)
        date = Browser(driver,10).get_attribute(self.BL_issuance_start_date_element,"max")
        # el.click(driver, 5, *self.search_element)
        Browser(driver,10).click(self.search_element)
        Wait(driver,10).elementwait(lambda the_driver:the_driver.find_element(*self.BL_Issuance_Date_elements))
        BL_Issuance_Date_locates = driver.find_elements(*self.BL_Issuance_Date_elements)
        BL_Issuance_Date_list = []
        for i in BL_Issuance_Date_locates:
            BL_Issuance_Date_list.append(i.text)
        return BL_Issuance_Date_list,date


    def BL_issuance_date_search(self, driver):
        Browser(driver,10).click(self.SA_button_element)
        Browser(driver,10).clear(self.BL_issuance_start_date_element)
        Browser(driver,10).click(self.BL_issuance_start_date_element)
        sleep(1)
        # Browser(driver,10).click(self.BL_last_month_element)
        Browser(driver,10).click(self.start_date_element)
        Browser(driver,10).click(self.BL_NO_element)
        Browser(driver,10).clear(self.BL_issuance_end_date_element)
        Browser(driver,10).click(self.BL_issuance_end_date_element)
        sleep(1)
        # Browser(driver,10).click(self.BL_last_month_element2)
        Browser(driver,10).click(self.end_date_element)
        Browser(driver,10).click(self.BL_NO_element)
        start_date = Browser(driver,10).get_attribute(self.BL_issuance_start_date_element,"value")
        end_date = Browser(driver,10).get_attribute(self.BL_issuance_start_date_element,"max")
        Browser(driver,10).click(self.search_element)
        Wait(driver,10).elementwait(lambda the_driver:the_driver.find_element(*self.BL_Issuance_Date_elements))
        BL_Issuance_Date_locates = driver.find_elements(*self.BL_Issuance_Date_elements)
        BL_Issuance_Date_list = []
        for i in BL_Issuance_Date_locates:
            BL_Issuance_Date_list.append(i.text)
        return BL_Issuance_Date_list,start_date,end_date

    def ETA_start_date_search(self, driver):
        en =ElementUtil()
        en.click(driver, 5, "test_ETA_date_search01", *self.SA_button_element)
        # en.clear(driver, 5, "test_ETA_date_search01", *self.ETA_start_date_element)
        en.click(driver, 5, "test_ETA_date_search01", *self.ETA_start_date_element)
        sleep(0.7)
        en.click(driver, 5, "test_ETA_date_search01", *self.start_date_element)
        en.click(driver, 5, "test_ETA_date_search01", *self.BL_NO_element)
        date = Browser(driver, 10).get_attribute(self.ETA_start_date_element, "value")
        en.click(driver, 5, "test_ETA_date_search01", *self.search_element)
        Wait(driver, 10).elementwait(lambda the_driver: the_driver.find_element(*self.ETA_date_elements))
        ETA_locates = driver.find_elements(*self.ETA_date_elements)
        ETA_Date_list = []
        for i in ETA_locates:
            ETA_Date_list.append(i.text)
        return ETA_Date_list, date

    def ETA_end_date_search(self, driver):
        en = ElementUtil()
        en.click(driver, 5, "test_ETA_date_search02", *self.SA_button_element)
        # en.clear(driver, 5, "test_ETA_date_search02", *self.ETA_end_date_element)
        sleep(2)
        en.click(driver, 5, "test_ETA_date_search02", *self.ETA_end_date_element)
        sleep(0.7)
        en.click(driver, 5, "test_ETA_date_search02", *self.end_date_element)
        en.click(driver, 5, "test_ETA_date_search02", *self.BL_NO_element)
        date = Browser(driver, 10).get_attribute(self.ETA_start_date_element, "max")
        en.click(driver, 5, "test_ETA_date_search02", *self.search_element)
        Wait(driver, 10).elementwait(lambda the_driver: the_driver.find_element(*self.ETA_date_elements))
        ETA_locates = driver.find_elements(*self.ETA_date_elements)
        ETA_Date_list = []
        for i in ETA_locates:
            ETA_Date_list.append(i.text)
        return ETA_Date_list, date
