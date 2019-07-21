"""
编写人:陈博华
"""
import os
from time import time
from common.Wait import Wait
from business.test_customs.method import choose_date
from common.Browser import Browser
from selenium.webdriver.common.keys import Keys
from pageElement.SAlogin.HomePage import HomePageElement
from pageElement.SAlogin.newlyBuild import NewlyBuildElement
from util.ElementUtil import ElementUtil


class NewlyBuild(HomePageElement,NewlyBuildElement):


    def __init__(self):
        self.IV_NO = "1"
        file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.path = os.path.join(file_path, "data", "test.xlsx")


    def newlyBuilt01(self, driver):
        """
        新建海运，送信
        """
        Browser(driver,10).click(self.SA_button_element)
        Browser(driver,10).click(self.newlyBuilt_element)
        Browser(driver,10).click(self.INV_add_element)
        Browser(driver,10).click(self.IV_NO_element)
        Browser(driver,10).click(self.IV_NO_search_element)
        Browser(driver,10).choice_check_box(self.choose_click_element)
        Browser(driver,10).click(self.IV_list_add_element)
        message = 'test'+str(time())[-6:]
        Browser(driver,10).click(self.Master_BL_NO_element)
        Browser(driver,10).send_keys(self.Master_BL_NO_element,message)
        Browser(driver,10).send_keys(self.House_BL_NO_element,message)
        choose_date(driver,self.trust_day_element,self.trust_day_click_element,self.trust_day_month_element)
        choose_date(driver,self.issue_date_element,self.issue_date_click_element,self.issue_month_click_element)
        choose_date(driver,self.ETA_element,self.ETA_click_element,self.ETA_month_clikc_element)
        choose_date(driver,self.export_declaration_date_element,self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        Browser(driver,10).click(self.shipping_co_element)
        Browser(driver,10).choice_select(self.shipping_co_choice_element)
        transport_text = Browser(driver,10).get_text(self.transport_mode_element)
        if transport_text != "SEA":
            Browser(driver,10).click(self.transport_type_clear_element)
            Browser(driver,10).send_keys(self.transport_type_element,Keys.ENTER)
            Browser(driver,10).click(self.SEA_element)
        Browser(driver,10).send_keys(self.loading_method_element,Keys.ENTER)
        Browser(driver,10).choice_select(self.loading_method_choice_elements)
        driver.find_element(*self.ships_name_element).send_keys('master')
        driver.find_element(*self.VOYAGE_NO_element).send_keys('qaz007')
        driver.find_element(*self.SI_NO_element).send_keys('qaz007')
        Browser(driver,10).click(self.customs_broker_element)
        Browser(driver,10).choice_select(self.customs_broker_choice_element)
        Browser(driver,10).click(self.cargo_type_element)
        Browser(driver,10).choice_select(self.cargo_type_choice_element)
        Browser(driver,10).send_keys(self.INV_checklist_element,Keys.SPACE)
        Browser(driver,10).get_text(self.loading_method_get_element)
        element_text = Browser(driver,10).get_text(self.loading_method_get_element)
        if element_text == 'FCL':
            NO_elements = driver.find_elements(*self.container_NO_element)
            size_elements = driver.find_elements(*self.container_size_element)
            for no in range(len(NO_elements)):
                NO_elements[no].send_keys('New Practice 2')
                size_elements[no].click()
                Browser(driver,10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        Browser(driver,10).click(self.file_upload_element)
        Browser(driver,10).send_keys(self.INV_upload_element,Keys.SPACE)
        Browser(driver,10).send_keys(self.upload_button_element,self.path)
        Browser(driver,10).send_keys(self.close_button_element,Keys.ENTER)
        Browser(driver,10).send_keys(self.BL_upload_element,Keys.SPACE)
        Browser(driver,10).send_keys(self.upload_button_element,self.path)
        Browser(driver,10).send_keys(self.close_button_element,Keys.ENTER)
        Browser(driver,10).click(self.popup_return_element)
        Browser(driver,10).click(self.temporary_saving_element)
        Browser(driver,10).click(self.confirm_button_element)
        Wait(driver,10).elementwait(lambda x:x.find_element(*self.return_element))
        button = Browser(driver,10).get_attribute(self.sending_confirmation_element,"style")
        if button == "display: none;":
            Browser(driver,10).click(self.saving_element)
        else:
            Browser(driver,10).click(self.sending_confirmation_element)
        Browser(driver,10).click(self.sure_button_element)
        tips = Browser(driver,10).get_text(self.windows_tips_element)
        Browser(driver,10).click(self.confirm_element)
        Browser(driver,10).click(self.return_element)
        return message,tips



    def newlyBuilt02(self, driver):
        """
        新建空运，送信
        """
        Browser(driver,10).click(self.SA_button_element)
        Browser(driver,10).click(self.newlyBuilt_element)
        Browser(driver,10).click(self.INV_add_element)
        Browser(driver,10).click(self.IV_NO_element)
        Browser(driver,10).click(self.IV_NO_search_element)
        Browser(driver,10).choice_check_box(self.choose_click_element)
        Browser(driver,10).click(self.IV_list_add_element)
        message = 'test'+str(time())[-6:]
        Browser(driver,10).click(self.Master_BL_NO_element)
        Browser(driver,10).send_keys(self.Master_BL_NO_element,message)
        Browser(driver,10).send_keys(self.House_BL_NO_element,message)
        choose_date(driver,self.trust_day_element,self.trust_day_click_element,self.trust_day_month_element)
        choose_date(driver,self.issue_date_element,self.issue_date_click_element,self.issue_month_click_element)
        choose_date(driver,self.ETA_element,self.ETA_click_element,self.ETA_month_clikc_element)
        choose_date(driver,self.export_declaration_date_element,self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        Browser(driver,10).click(self.shipping_co_element)
        Browser(driver,10).choice_select(self.shipping_co_choice_element)
        transport_text = Browser(driver,10).get_text(self.transport_mode_element)
        if transport_text != "AIR":
            Browser(driver,10).click(self.transport_type_clear_element)
            Browser(driver,10).send_keys(self.transport_type_element,Keys.ENTER)
            Browser(driver,10).click(self.AIR_element)
        Browser(driver,10).send_keys(self.flying_No_element,"qaz007")
        Browser(driver,10).send_keys(self.SI_NO_element,"qaz007")
        Browser(driver,10).click(self.customs_broker_element)
        Browser(driver,10).choice_select(self.customs_broker_choice_element)
        Browser(driver,10).click(self.cargo_type_element)
        Browser(driver,10).choice_select(self.cargo_type_choice_element)
        Browser(driver,10).send_keys(self.INV_checklist_element,Keys.SPACE)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        Browser(driver,10).click(self.file_upload_element)
        Browser(driver,10).send_keys(self.INV_upload_element,Keys.SPACE)
        Browser(driver,10).send_keys(self.upload_button_element,self.path)
        Browser(driver,10).send_keys(self.close_button_element,Keys.ENTER)
        Browser(driver,10).send_keys(self.BL_upload_element,Keys.SPACE)
        Browser(driver,10).send_keys(self.upload_button_element,self.path)
        Browser(driver,10).send_keys(self.close_button_element,Keys.ENTER)
        Browser(driver,10).click(self.popup_return_element)
        Browser(driver,10).click(self.temporary_saving_element)
        Browser(driver,10).click(self.confirm_button_element)
        Wait(driver,10).elementwait(lambda x:x.find_element(*self.return_element))
        button = Browser(driver,10).get_attribute(self.sending_confirmation_element,"style")
        if button == "display: none;":
            Browser(driver,10).click(self.saving_element)
        else:
            Browser(driver,10).click(self.sending_confirmation_element)
        Browser(driver,10).click(self.sure_button_element)
        tips = Browser(driver,10).get_text(self.windows_tips_element)
        Browser(driver,10).click(self.confirm_element)
        Browser(driver,10).click(self.return_element)
        return message,tips


    def INV_search01(self, driver):
        Browser(driver,10).click(self.SA_button_element)
        Browser(driver,10).click(self.newlyBuilt_element)
        Browser(driver,10).click(self.INV_add_element)
        Wait(driver,10).elementwait(lambda x:x.find_element(*self.IV_NO_element))
        Browser(driver,10).send_keys(self.IV_NO_element,self.IV_NO)
        Browser(driver,10).click(self.IV_NO_search_element)
        Wait(driver,10).elementwait(lambda the_driver:the_driver.find_element(*self.IV_NO_get_element))
        element_list = driver.find_elements(*self.IV_NO_get_element)
        datas = []
        for i in element_list:
            datas.append(i.text)
        return datas,self.IV_NO


    def newlyBuilt03(self, driver):
        ElementUtil.click(self, driver, 5, "[陈博华]新建海关数据，保存", *self.SA_button_element)
        ElementUtil.click(self, driver, 5, "[陈博华]新建海关数据，保存", *self.newlyBuilt_element)
        ElementUtil.click(self, driver, 5, "[陈博华]新建海关数据，保存", *self.INV_add_element)
        ElementUtil.click(self, driver, 5, "[陈博华]新建海关数据，保存", *self.IV_NO_element)
        ElementUtil.click(self, driver, 5, "[陈博华]新建海关数据，保存", *self.IV_NO_search_element)
        Browser(driver,10).choice_check_box(self.choose_click_element)
        Browser(driver,10).click(self.IV_list_add_element)
        message = 'test'+str(time())[-6:]
        ElementUtil.click(self, driver, 5, "[陈博华]新建海关数据，保存", *self.Master_BL_NO_element)
        ElementUtil.send_keys(self, driver, 5,message, "[陈博华]新建海关数据，保存", *self.Master_BL_NO_element)
        ElementUtil.send_keys(self, driver, 5, message,"[陈博华]新建海关数据，保存", *self.House_BL_NO_element)
        choose_date(driver,self.trust_day_element,self.trust_day_click_element,self.trust_day_month_element)
        choose_date(driver,self.issue_date_element,self.issue_date_click_element,self.issue_month_click_element)
        choose_date(driver,self.ETA_element,self.ETA_click_element,self.ETA_month_clikc_element)
        choose_date(driver,self.export_declaration_date_element,self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        ElementUtil.click(self, driver, 5, "[陈博华]新建海关数据，保存", *self.shipping_co_element)
        Browser(driver,10).choice_select(self.shipping_co_choice_element)
        ElementUtil.send_keys(self, driver, 5, Keys.ENTER, "[陈博华]新建海关数据，保存",*self.loading_method_element)
        Browser(driver,10).choice_select(self.loading_method_choice_elements)
        transport_mode = ElementUtil.getText(self, driver, 5, "[陈博华]新建海关数据，保存", *self.transport_mode_element)
        if transport_mode == "SEA":
            ElementUtil.send_keys(self, driver, 5,'master',  "[陈博华]新建海关数据，保存",*self.ships_name_element)
            ElementUtil.send_keys(self, driver, 5, 'qaz007', "[陈博华]新建海关数据，保存",*self.VOYAGE_NO_element)
        else:
            ElementUtil.send_keys(self, driver, 5, 'qaz007', "[陈博华]新建海关数据，保存",*self.flying_No_element)
        ElementUtil.send_keys(self, driver, 5, 'qaz007',"[陈博华]新建海关数据，保存", *self.SI_NO_element)
        ElementUtil.click(self, driver, 5, "[陈博华]新建海关数据，保存", *self.customs_broker_element)
        Browser(driver,10).choice_select(self.customs_broker_choice_element)
        ElementUtil.click(self, driver, 5, "[陈博华]新建海关数据，保存", *self.cargo_type_element)
        Browser(driver,10).choice_select(self.cargo_type_choice_element)
        ElementUtil.send_keys(self, driver, 5, Keys.SPACE,"[陈博华]新建海关数据，保存", *self.INV_checklist_element)
        element_text = Browser(driver,10).get_attribute(self.loading_method_element,"value")
        if element_text == 'FCL':
            NO_elements = driver.find_elements(*self.container_NO_element)
            size_elements = driver.find_elements(*self.container_size_element)
            for no in range(len(NO_elements)):
                NO_elements[no].send_keys('New Practice 2')
                size_elements[no].click()
                Browser(driver,10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 10, "[陈博华]新建海关数据，保存", *self.temporary_saving_element)
        ElementUtil.click(self, driver, 10, "[陈博华]新建海关数据，保存", *self.confirm_button_element)
        ElementUtil.click(self, driver, 10, "[陈博华]新建海关数据，保存", *self.return_element)
        return message


    def newlyBuilt04(self, driver):
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，空运，House B/L NO是否为必填项", *self.SA_button_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，空运，House B/L NO是否为必填项", *self.newlyBuilt_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，空运，House B/L NO是否为必填项", *self.INV_add_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，空运，House B/L NO是否为必填项", *self.IV_NO_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，空运，House B/L NO是否为必填项", *self.IV_NO_search_element)
        Browser(driver,10).choice_check_box(self.choose_click_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，空运，House B/L NO是否为必填项", *self.IV_list_add_element)
        transport_mode = ElementUtil.getText(self, driver, 5, "[陈博华]验证新建时，空运，House B/L NO是否为必填项", *self.transport_mode_element)
        if transport_mode != "AIR":
            ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，空运，House B/L NO是否为必填项", *self.transport_type_clear_element)
            ElementUtil.send_keys(self, driver, 5, Keys.ENTER,"[陈博华]验证新建时，空运，House B/L NO是否为必填项", *self.transport_type_element)
            ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，空运，House B/L NO是否为必填项", *self.AIR_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，空运，House B/L NO是否为必填项", *self.temporary_saving_element)
        tips = ElementUtil.getText(self, driver, 5, "[陈博华]验证新建时，空运，House B/L NO是否为必填项", *self.tips_element)
        return tips


    def newlyBuilt05(self, driver):
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.SA_button_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.newlyBuilt_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.INV_add_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.IV_NO_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.IV_NO_search_element)
        Browser(driver,10).choice_check_box(self.choose_click_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.IV_list_add_element)
        transport_mode = ElementUtil.getText(self, driver, 5, "[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.transport_mode_element)
        if transport_mode != "SEA":
            ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.transport_type_clear_element)
            ElementUtil.send_keys(self, driver, 5, Keys.ENTER,"[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.transport_type_element)
            ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.SEA_element)
        ElementUtil.send_keys(self, driver, 5, Keys.ENTER,"[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.loading_method_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.FCL_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.temporary_saving_element)
        tips = ElementUtil.getText(self, driver, 5, "[陈博华]验证新建时，海运整箱，Master B/L NO是否为必填项", *self.tips_element)
        return tips


    def newlyBuilt06(self, driver):
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.SA_button_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.newlyBuilt_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.INV_add_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.IV_NO_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.IV_NO_search_element)
        Browser(driver,10).choice_check_box(self.choose_click_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.IV_list_add_element)
        transport_mode = ElementUtil.getText(self, driver, 5, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.transport_mode_element)
        if transport_mode != "SEA":
            ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.transport_type_clear_element)
            ElementUtil.send_keys(self, driver, 5, Keys.ENTER, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.transport_type_element)
            ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.SEA_element)
        ElementUtil.send_keys(self, driver, 5 ,Keys.ENTER, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.loading_method_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.LCL_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.temporary_saving_element)
        tips = ElementUtil.getText(self, driver, 5, "[陈博华]验证新建时，海运拼箱，House B/L NO是否为必填项", *self.tips_element)
        return tips


    def newlyBuilt07(self, driver):
        """重複B/L No.が存在します。"""
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，重复B/L NO是否校验", *self.SA_button_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，重复B/L NO是否校验", *self.newlyBuilt_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，重复B/L NO是否校验", *self.INV_add_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，重复B/L NO是否校验", *self.IV_NO_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，重复B/L NO是否校验", *self.IV_NO_search_element)
        Browser(driver,10).choice_check_box(self.choose_click_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，重复B/L NO是否校验", *self.IV_list_add_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，重复B/L NO是否校验", *self.Master_BL_NO_element)
        transport_mode = ElementUtil.getText(self, driver, 5, "[陈博华]验证新建时，重复B/L NO是否校验", *self.transport_mode_element)
        if transport_mode == "SEA":
            ElementUtil.send_keys(self, driver, 5 ,Keys.ENTER, "[陈博华]验证新建时，重复B/L NO是否校验", *self.loading_method_element)
            Browser(driver,10).choice_select(self.loading_method_choice_elements)
            driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.send_keys(self, driver, 5 ,"test70014", "[陈博华]验证新建时，重复B/L NO是否校验", *self.Master_BL_NO_element)
        ElementUtil.send_keys(self, driver, 5 ,"test70014", "[陈博华]验证新建时，重复B/L NO是否校验", *self.House_BL_NO_element)
        ElementUtil.click(self, driver, 5, "[陈博华]验证新建时，重复B/L NO是否校验", *self.temporary_saving_element)
        windows_tips = ElementUtil.getText(self, driver, 5, "[陈博华]验证新建时，重复B/L NO是否校验", *self.windows_tips_element)
        return windows_tips


    def newlyBuilt08(self, driver):
        """
        新建海运，送信
        """
        Browser(driver,10).click(self.SA_button_element)
        Browser(driver,10).click(self.newlyBuilt_element)
        Browser(driver,10).click(self.INV_add_element)
        Browser(driver,10).click(self.IV_NO_element)
        Browser(driver,10).click(self.IV_NO_search_element)
        Browser(driver,10).choice_check_box(self.choose_click_element)
        Browser(driver,10).click(self.IV_list_add_element)
        message = 'test'+str(time())[-6:]
        Browser(driver,10).click(self.Master_BL_NO_element)
        Browser(driver,10).send_keys(self.Master_BL_NO_element,message)
        Browser(driver,10).send_keys(self.House_BL_NO_element,message)
        choose_date(driver,self.trust_day_element,self.trust_day_click_element,self.trust_day_month_element)
        choose_date(driver,self.issue_date_element,self.issue_date_click_element,self.issue_month_click_element)
        choose_date(driver,self.ETA_element,self.ETA_click_element,self.ETA_month_clikc_element)
        choose_date(driver,self.export_declaration_date_element,self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        Browser(driver,10).click(self.shipping_co_element)
        Browser(driver,10).choice_select(self.shipping_co_choice_element)
        transport_text = driver.find_element(*self.transport_mode_element).text
        if transport_text != "SEA":
            Browser(driver,10).click(self.transport_type_clear_element)
            Browser(driver,10).send_keys(self.transport_type_element,Keys.ENTER)
            Browser(driver,10).click(self.SEA_element)
        Browser(driver,10).send_keys(self.loading_method_element,Keys.ENTER)
        Browser(driver,10).choice_select(self.loading_method_choice_elements)
        Browser(driver,10).send_keys(self.SI_NO_element,"test007")
        Browser(driver,10).click(self.customs_broker_element)
        Browser(driver,10).choice_select(self.customs_broker_choice_element)
        Browser(driver,10).click(self.cargo_type_element)
        Browser(driver,10).choice_select(self.cargo_type_choice_element)
        Browser(driver,10).send_keys(self.INV_checklist_element,Keys.SPACE)
        Browser(driver,10).get_text(self.loading_method_get_element)
        element_text = Browser(driver,10).get_text(self.loading_method_get_element)
        if element_text == 'FCL':
            NO_elements = driver.find_elements(*self.container_NO_element)
            size_elements = driver.find_elements(*self.container_size_element)
            for no in range(len(NO_elements)):
                NO_elements[no].send_keys('New Practice 2')
                size_elements[no].click()
                Browser(driver,10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        Browser(driver,10).click(self.file_upload_element)
        Browser(driver,10).send_keys(self.INV_upload_element,Keys.SPACE)
        Browser(driver,10).send_keys(self.upload_button_element,self.path)
        Browser(driver,10).send_keys(self.close_button_element,Keys.ENTER)
        Browser(driver,10).send_keys(self.BL_upload_element,Keys.SPACE)
        Browser(driver,10).send_keys(self.upload_button_element,self.path)
        Browser(driver,10).send_keys(self.close_button_element,Keys.ENTER)
        Browser(driver,10).click(self.popup_return_element)
        Browser(driver,10).click(self.temporary_saving_element)
        Browser(driver,10).click(self.confirm_button_element)
        Wait(driver,10).elementwait(lambda x:x.find_element(*self.return_element))
        button = Browser(driver,10).get_attribute(self.sending_confirmation_element,"style")
        if button == "display: none;":
            Browser(driver,10).click(self.saving_element)
        else:
            Browser(driver,10).click(self.sending_confirmation_element)
        Browser(driver,10).click(self.sure_button_element)
        tips = Browser(driver,10).get_text(self.windows_tips_element)
        Browser(driver,10).click(self.confirm_element)
        Browser(driver,10).click(self.return_element)
        return message,tips


    def newlyBuilt09(self, driver):
        """
        新建海运，送信
        """
        Browser(driver,10).click(self.SA_button_element)
        Browser(driver,10).click(self.newlyBuilt_element)
        Browser(driver,10).click(self.INV_add_element)
        Browser(driver,10).click(self.IV_NO_element)
        Browser(driver,10).click(self.IV_NO_search_element)
        Browser(driver,10).choice_check_box(self.choose_click_element)
        Browser(driver,10).click(self.IV_list_add_element)
        message = 'test'+str(time())[-6:]
        Browser(driver,10).click(self.Master_BL_NO_element)
        Browser(driver,10).send_keys(self.Master_BL_NO_element,message)
        Browser(driver,10).send_keys(self.House_BL_NO_element,message)
        choose_date(driver,self.trust_day_element,self.trust_day_click_element,self.trust_day_month_element)
        choose_date(driver,self.issue_date_element,self.issue_date_click_element,self.issue_month_click_element)
        choose_date(driver,self.ETA_element,self.ETA_click_element,self.ETA_month_clikc_element)
        choose_date(driver,self.export_declaration_date_element,self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        Browser(driver,10).click(self.shipping_co_element)
        Browser(driver,10).choice_select(self.shipping_co_choice_element)
        transport_text = driver.find_element(*self.transport_mode_element).text
        if transport_text != "AIR":
            Browser(driver,10).click(self.transport_type_clear_element)
            Browser(driver,10).send_keys(self.transport_type_element,Keys.ENTER)
            Browser(driver,10).click(self.AIR_element)
        Browser(driver,10).send_keys(self.SI_NO_element,"test007")
        Browser(driver,10).click(self.customs_broker_element)
        Browser(driver,10).choice_select(self.customs_broker_choice_element)
        Browser(driver,10).click(self.cargo_type_element)
        Browser(driver,10).choice_select(self.cargo_type_choice_element)
        Browser(driver,10).send_keys(self.INV_checklist_element,Keys.SPACE)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        Browser(driver,10).click(self.file_upload_element)
        Browser(driver,10).send_keys(self.INV_upload_element,Keys.SPACE)
        Browser(driver,10).send_keys(self.upload_button_element,self.path)
        Browser(driver,10).send_keys(self.close_button_element,Keys.ENTER)
        Browser(driver,10).send_keys(self.BL_upload_element,Keys.SPACE)
        Browser(driver,10).send_keys(self.upload_button_element,self.path)
        Browser(driver,10).send_keys(self.close_button_element,Keys.ENTER)
        Browser(driver,10).click(self.popup_return_element)
        Browser(driver,10).click(self.temporary_saving_element)
        Browser(driver,10).click(self.confirm_button_element)
        Wait(driver,10).elementwait(lambda x:x.find_element(*self.return_element))
        button = Browser(driver,10).get_attribute(self.sending_confirmation_element,"style")
        if button == "display: none;":
            Browser(driver,10).click(self.saving_element)
        else:
            Browser(driver,10).click(self.sending_confirmation_element)
        Browser(driver,10).click(self.sure_button_element)
        tips = Browser(driver,10).get_text(self.windows_tips_element)
        Browser(driver,10).click(self.confirm_element)
        Browser(driver,10).click(self.return_element)
        return message,tips


    def newlyBuilt10(self, driver):
        """
        新建海运，送信
        """
        Browser(driver,10).click(self.SA_button_element)
        Browser(driver,10).click(self.newlyBuilt_element)
        Browser(driver,10).click(self.INV_add_element)
        Browser(driver,10).click(self.IV_NO_element)
        Browser(driver,10).click(self.IV_NO_search_element)
        Browser(driver,10).choice_check_box(self.choose_click_element)
        Browser(driver,10).click(self.IV_list_add_element)
        message = 'test'+str(time())[-6:]
        Browser(driver,10).click(self.Master_BL_NO_element)
        Browser(driver,10).send_keys(self.Master_BL_NO_element,message)
        Browser(driver,10).send_keys(self.House_BL_NO_element,message)
        choose_date(driver,self.trust_day_element,self.trust_day_click_element,self.trust_day_month_element)
        choose_date(driver,self.issue_date_element,self.issue_date_click_element,self.issue_month_click_element)
        choose_date(driver,self.ETA_element,self.ETA_click_element,self.ETA_month_clikc_element)
        choose_date(driver,self.export_declaration_date_element,self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        Browser(driver,10).click(self.shipping_co_element)
        Browser(driver,10).choice_select(self.shipping_co_choice_element)
        transport_text = driver.find_element(*self.transport_mode_element).text
        if transport_text == "SEA":
            Browser(driver,10).send_keys(self.loading_method_element,Keys.SPACE)
            Browser(driver,10).choice_select(self.loading_method_choice_elements)
            driver.find_element(*self.ships_name_element).send_keys('master')
            driver.find_element(*self.VOYAGE_NO_element).send_keys('qaz007')
            driver.find_element(*self.SI_NO_element).send_keys('qaz007')
            element_text = Browser(driver,10).get_text(self.loading_method_get_element)
            if element_text == 'FCL':
                NO_elements = driver.find_elements(*self.container_NO_element)
                size_elements = driver.find_elements(*self.container_size_element)
                for no in range(len(NO_elements)):
                    NO_elements[no].send_keys('New Practice 2')
                    size_elements[no].click()
                    Browser(driver,10).choice_select(self.container_size_choice_element)
        else:
            Browser(driver,10).send_keys(self.flying_No_element,'qaz007')
        Browser(driver,10).click(self.customs_broker_element)
        Browser(driver,10).choice_select(self.customs_broker_choice_element)
        Browser(driver,10).click(self.cargo_type_element)
        Browser(driver,10).choice_select(self.cargo_type_choice_element)
        Browser(driver,10).send_keys(self.INV_checklist_element,Keys.SPACE)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        Browser(driver,10).click(self.file_upload_element)
        Browser(driver,10).send_keys(self.INV_upload_element,Keys.SPACE)
        Browser(driver,10).send_keys(self.upload_button_element,self.path)
        Browser(driver,10).send_keys(self.close_button_element,Keys.ENTER)
        Browser(driver,10).send_keys(self.BL_upload_element,Keys.SPACE)
        Browser(driver,10).send_keys(self.upload_button_element,self.path)
        Browser(driver,10).send_keys(self.close_button_element,Keys.ENTER)
        Browser(driver,10).click(self.popup_return_element)
        Browser(driver,10).click(self.temporary_saving_element)
        Browser(driver,10).click(self.confirm_button_element)
        Wait(driver,10).elementwait(lambda x:x.find_element(*self.return_element))
        button = Browser(driver,10).get_attribute(self.sending_confirmation_element,"style")
        if button == "display: none;":
            Browser(driver,10).click(self.saving_element)
        else:
            Browser(driver,10).click(self.sending_confirmation_element)
        Browser(driver,10).click(self.sending_cancel_element)
        Browser(driver,10).click(self.return_element)
        return message


    def newlyBuilt11(self, driver):
        """
        新建海运，送信
        """
        Browser(driver,10).click(self.SA_button_element)
        Browser(driver,10).click(self.newlyBuilt_element)
        Browser(driver,10).click(self.INV_add_element)
        Browser(driver,10).click(self.IV_NO_element)
        Browser(driver,10).click(self.IV_NO_search_element)
        Browser(driver,10).choice_check_box(self.choose_click_element)
        Browser(driver,10).click(self.IV_list_add_element)
        message = 'test'+str(time())[-6:]
        Browser(driver,10).click(self.Master_BL_NO_element)
        Browser(driver,10).send_keys(self.Master_BL_NO_element,message)
        Browser(driver,10).send_keys(self.House_BL_NO_element,message)
        choose_date(driver,self.trust_day_element,self.trust_day_click_element,self.trust_day_month_element)
        choose_date(driver,self.issue_date_element,self.issue_date_click_element,self.issue_month_click_element)
        choose_date(driver,self.ETA_element,self.ETA_click_element,self.ETA_month_clikc_element)
        choose_date(driver,self.export_declaration_date_element,self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        Browser(driver,10).click(self.shipping_co_element)
        Browser(driver,10).choice_select(self.shipping_co_choice_element)
        transport_text = driver.find_element(*self.transport_mode_element).text
        if transport_text == "SEA":
            Browser(driver,10).send_keys(self.loading_method_element,Keys.SPACE)
            Browser(driver,10).choice_select(self.loading_method_choice_elements)
            element_text = Browser(driver,10).get_text(self.loading_method_get_element)
            if element_text == 'FCL':
                NO_elements = driver.find_elements(*self.container_NO_element)
                size_elements = driver.find_elements(*self.container_size_element)
                for no in range(len(NO_elements)):
                    NO_elements[no].send_keys('New Practice 2')
                    size_elements[no].click()
                    Browser(driver,10).choice_select(self.container_size_choice_element)
        Browser(driver,10).send_keys(self.SI_NO_element,"test007")
        Browser(driver,10).click(self.customs_broker_element)
        Browser(driver,10).choice_select(self.customs_broker_choice_element)
        Browser(driver,10).click(self.cargo_type_element)
        Browser(driver,10).choice_select(self.cargo_type_choice_element)
        Browser(driver,10).send_keys(self.INV_checklist_element,Keys.SPACE)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        Browser(driver,10).click(self.file_upload_element)
        Browser(driver,10).send_keys(self.INV_upload_element,Keys.SPACE)
        Browser(driver,10).send_keys(self.upload_button_element,self.path)
        Browser(driver,10).send_keys(self.close_button_element,Keys.ENTER)
        Browser(driver,10).send_keys(self.BL_upload_element,Keys.SPACE)
        Browser(driver,10).send_keys(self.upload_button_element,self.path)
        Browser(driver,10).send_keys(self.close_button_element,Keys.ENTER)
        Browser(driver,10).click(self.popup_return_element)
        Browser(driver,10).click(self.temporary_saving_element)
        Browser(driver,10).click(self.confirm_button_element)
        Wait(driver,10).elementwait(lambda x:x.find_element(*self.return_element))
        button = Browser(driver,10).get_attribute(self.sending_confirmation_element,"style")
        if button == "display: none;":
            Browser(driver,10).click(self.saving_element)
        else:
            Browser(driver,10).click(self.sending_confirmation_element)
        Browser(driver,10).click(self.sending_cancel_element)
        Browser(driver,10).click(self.return_element)
        print(message)
        return message
