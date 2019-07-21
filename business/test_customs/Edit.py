"""
编写人:陈博华
"""
from time import time
from business.Login import Login
from common.Wait import Wait
from common.Browser import Browser
from selenium.webdriver.common.keys import Keys
from business.test_customs.method import date_not_None, search_and_click
from pageElement.SAlogin.HomePage import HomePageElement
from pageElement.SAlogin.newlyBuild import NewlyBuildElement
from selenium.webdriver.common.action_chains import ActionChains
from util.ElementUtil import ElementUtil
from business.test_customs.NewData import NewData
from time import sleep
from util.interface_data import demo
from selenium import webdriver
import random
from util.element_exits import isElementExist

class Edit(HomePageElement, NewlyBuildElement):

    def edit01(self, driver):
        elUtil = ElementUtil()
        news = NewData()
        d = demo()

        elUtil = ElementUtil()
        news = NewData()
        d = demo()

        # 获取masterNO和HouseNO
        Master_BL_NO, House_BL_NO = news.create_data(driver)

        # 输入Master B/L NO清除
        elUtil.send_keys(driver, 30, Master_BL_NO, '输入Master B/L NO：%s' % Master_BL_NO, *self.master_no_element)

        # 输入House NO清除
        elUtil.send_keys(driver, 30, House_BL_NO, '输入HouseB/L NO：%s' % House_BL_NO, *self.house_no_element)

        # 点击搜索
        elUtil.click(driver, 30, '点击搜索', *self.searchElement)
        sleep(1.5)

        # 选择表第一条数据
        elUtil.click(driver, 30, '选择搜索数据', *self.fistCheckElement)
        sleep(1.5)

        # 点击编辑
        elUtil.click(driver, 30, '点击编辑', *self.editElement)
        sleep(1.5)

        '''masterNo'''
        Master_BL_NO_text = random.randint(100000, 999990)
        elUtil.send_keys(driver, 30, Master_BL_NO_text, '输入masterNo', *self.Master_BL_NO_element)
        sleep(1.5)

        # HourseNo
        House_BL_NO_text = random.randint(100000, 999990)

        elUtil.send_keys(driver, 30, House_BL_NO_text, '输入HourseNo', *self.House_BL_NO_element)
        sleep(1.5)

        # 点击临时保存
        tempSaveEl = driver.find_element(*self.temporary_saving_element)
        driver.execute_script("arguments[0].click();", tempSaveEl)
        sleep(5)

        # 点击 弹框确定按钮
        # driver.find_element(*self.confirm_button_element).click()
        tempEnsureEl = driver.find_element(*self.confirm_button_element)
        driver.execute_script("arguments[0].click();", tempEnsureEl)
        sleep(1.5)

        # 点击 取消
        conreturn_el = driver.find_element(*self.return_element)
        driver.execute_script("arguments[0].click();", conreturn_el)
        sleep(1.5)

        # 输入Master B/L NO清除
        elUtil.send_keys(driver, 30, Master_BL_NO_text, '输入Master B/L NO：%s' % Master_BL_NO, *self.master_no_element)

        # 输入House NO清除
        elUtil.send_keys(driver, 30, House_BL_NO_text, '输入HouseB/L NO：%s' % House_BL_NO, *self.house_no_element)

        # 点击搜索
        elUtil.click(driver, 30, '点击搜索', *self.searchElement)
        sleep(1.5)

        # 获取INV PL表数据量
        table = driver.find_element(*self.tableTbodyElement)
        rows2 = len(table.find_elements_by_tag_name('tr'))
        return int(rows2)

    def edit02(self, driver):
        '''陈博华：编集状态为SA一時保存的海关数据，修改Carton No，验证Shipped Carton数量是否正确'''
        elUtil = ElementUtil()
        news = NewData()
        d = demo()

        elUtil = ElementUtil()
        news = NewData()
        d = demo()

        # 获取masterNO和HouseNO
        Master_BL_NO, House_BL_NO = news.create_data(driver)

        # 输入Master B/L NO清除
        elUtil.send_keys(driver,30, Master_BL_NO, '输入Master B/L NO：%s' % Master_BL_NO, *self.master_no_element)

        # 输入House NO清除
        elUtil.send_keys(driver,30, House_BL_NO, '输入HouseB/L NO：%s' % House_BL_NO, *self.house_no_element)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索', *self.searchElement)
        sleep(1.5)

        # 选择表第一条数据
        elUtil.click(driver,30, '选择搜索数据', *self.fistCheckElement)
        sleep(1.5)

        # 点击编辑
        elUtil.click(driver,30, '点击编辑', *self.editElement)
        sleep(1.5)

        # 对startNo进行修改并获取修改内容
        elUtil.clear(driver,30, '清除startNo', *self.startNoElement)
        elUtil.send_keys(driver,30, 0, '输入startNo', *self.startNoElement)
        startNo = driver.find_element(*self.startNoElement).get_attribute('value')
        elUtil.click(driver,30, '输入startNo', *self.headElement)
        sleep(1.5)
        endNo = driver.find_element(*self.endNoElement).get_attribute('value')
        ShippedNo = driver.find_element(*self.ShippedCartonElement).get_attribute('value')
        sleep(1.5)

        flag = None
        # print(ShippedNo,endNo,startNo)
        if int(ShippedNo) == int(endNo) - int(startNo) + 1:
            flag = True
        return flag


    def edit04(self, driver):
        elUtil = ElementUtil()  #
        d = demo()

        # 进入首页S/A登录
        elUtil.click(driver, 30, '进入首页S/A登录', *self.SAElement)
        sleep(1.5)

        # 点击新規按钮
        elUtil.click(driver, 30, '点击新規按钮', *self.newRuleElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver, 30, '点击INV P/L情報下追加按钮', *self.addElement)
        sleep(1.5)

        # 获取新数据
        r_data = d.test().get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver, 30, '清除invoiceNo', *self.IVNoElement)
        elUtil.send_keys(driver, 30, r_data, '输入%s' % r_data, *self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver, 30, '点击搜索按钮', *self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver, 30, '勾选数据', *self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver, 30, '点击对话框追加', *self.dialogAddElement)

        # 点击临时保存
        tempSaveEl=driver.find_element(*self.temporary_saving_element)
        driver.execute_script("arguments[0].click();", tempSaveEl)

        convey_text = driver.find_element(*self.conveyElement).get_attribute('value')
        if convey_text != 'AIR':
            elUtil.click(driver, 30, '点击输送形态', *self.conveyElement)
            elUtil.click(driver, 30, '点击AIR', *self.AIR_element)
        House_BL_NO_must_text = driver.find_element(*self.House_BL_NO_must).get_attribute('innerHTML')
        return House_BL_NO_must_text


    def edit05(self, driver):

        elUtil = ElementUtil()  #
        d = demo()

        # 进入首页S/A登录
        elUtil.click(driver, 30, '进入首页S/A登录', *self.SAElement)
        sleep(1.5)

        # 点击新規按钮
        elUtil.click(driver, 30, '点击新規按钮', *self.newRuleElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver, 30, '点击INV P/L情報下追加按钮', *self.addElement)
        sleep(1.5)

        # 获取新数据
        r_data = d.test().get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver, 30, '清除invoiceNo', *self.IVNoElement)
        elUtil.send_keys(driver, 30, r_data, '输入%s' % r_data, *self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver, 30, '点击搜索按钮', *self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver, 30, '勾选数据', *self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver, 30, '点击对话框追加', *self.dialogAddElement)

        convey_text = driver.find_element(*self.conveyElement).get_attribute('value')
        if convey_text != 'SEA':
            elUtil.click(driver, 30, '点击输送形态', *self.conveyElement)
            elUtil.click(driver, 30, '点击AIR', *self.SEA_element)

        # 点击積み方
        loading_method_el = isElementExist(driver, self.loading_method_element)
        if loading_method_el == True:
            loading_method_text = driver.find_element(*self.loading_method_element).get_attribute('value')
            if loading_method_text in 'FCL LCL':
                # 点击積み方
                loading_method = driver.find_element(*self.loading_method_element)
                driver.execute_script("arguments[0].click();", loading_method)
                sleep(1.5)
                # 填写B積み方
                loading_method_choice = driver.find_element(*self.loading_method_choice_elements)
                driver.execute_script("arguments[0].click();", loading_method_choice)
                sleep(1.5)

        # 点击临时保存
        tempSaveEl = driver.find_element(*self.temporary_saving_element)
        driver.execute_script("arguments[0].click();", tempSaveEl)

        master_BL_NO_must_text = driver.find_element(*self.master_BL_NO_must).get_attribute('innerHTML')
        return master_BL_NO_must_text


    def edit06(self, driver):
        elUtil = ElementUtil()  #
        d = demo()

        # 进入首页S/A登录
        elUtil.click(driver, 30, '进入首页S/A登录', *self.SAElement)
        sleep(1.5)

        # 点击新規按钮
        elUtil.click(driver, 30, '点击新規按钮', *self.newRuleElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver, 30, '点击INV P/L情報下追加按钮', *self.addElement)
        sleep(1.5)

        # 获取新数据
        r_data = d.test().get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver, 30, '清除invoiceNo', *self.IVNoElement)
        elUtil.send_keys(driver, 30, r_data, '输入%s' % r_data, *self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver, 30, '点击搜索按钮', *self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver, 30, '勾选数据', *self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver, 30, '点击对话框追加', *self.dialogAddElement)

        convey_text = driver.find_element(*self.conveyElement).get_attribute('value')
        if convey_text != 'SEA':
            elUtil.click(driver, 30, '点击输送形态', *self.conveyElement)
            elUtil.click(driver, 30, '点击SEA', *self.SEA_element)

        # 点击積み方
        loading_method_el = isElementExist(driver, self.loading_method_element)
        if loading_method_el == True:
            loading_method_text = driver.find_element(*self.loading_method_element).get_attribute('value')
            if loading_method_text in 'FCL LCL':
                # 点击積み方
                loading_method = driver.find_element(*self.loading_method_element)
                driver.execute_script("arguments[0].click();", loading_method)
                sleep(1.5)
                # 填写B積み方
                loading_method_choice = driver.find_element(*self.LCL_element)
                driver.execute_script("arguments[0].click();", loading_method_choice)
                sleep(1.5)

        # 点击临时保存
        tempSaveEl = driver.find_element(*self.temporary_saving_element)
        driver.execute_script("arguments[0].click();", tempSaveEl)

        House_BL_NO_must_text = driver.find_element(*self.House_BL_NO_must).get_attribute('innerHTML')
        return House_BL_NO_must_text

    def edit07(self, driver, text):
        """
        编集，修改所有数据，保存
        """
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # Browser(driver, 10).click(self.SA_button_element)
        ElementUtil.click(self, driver, 15, text, *self.search_element)
        # Browser(driver, 10).click(self.search_element)
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        search_and_click(driver, self.temporary_preservation_elements, self.next_page_element, self.display_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.edit_element)
        # Browser(driver, 10).click(self.edit_element)
        loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        if loading_port is None:
            ElementUtil.click(self, driver, 15, text, *self.loading_port_element)
            Browser(driver, 10).choice_select(self.loading_port_choice_elements)
        # ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_element)
        # # Browser(driver, 10).click(self.Master_BL_NO_element)
        # loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        # if not loading_port:
        #     ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        #     # Browser(driver, 10).click(self.INV_add_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_element)
        #     # Browser(driver, 10).click(self.IV_NO_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        #     # Browser(driver, 10).click(self.IV_NO_search_element)
        #     Browser(driver, 10).choice_check_box(self.choose_click_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        #     # Browser(driver, 10).click(self.IV_list_add_element)
        message = 'test' + str(time())[-6:]
        Master_BL_NO = Browser(driver, 10).get_attribute(self.Master_BL_NO_element, "value")
        if Master_BL_NO is not None:
            ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_clear_element)
            # Browser(driver, 10).click(self.Master_BL_NO_clear_element)
        # ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_element)
        Browser(driver, 10).send_keys(self.Master_BL_NO_element, message)
        House_BL_NO = Browser(driver, 10).get_attribute(self.House_BL_NO_element, "value")
        if House_BL_NO is not None:
            ElementUtil.click(self, driver, 15, text, *self.House_BL_NO_clear_element)
            # Browser(driver, 10).click(self.House_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.House_BL_NO_element, message)
        trust_day = Browser(driver, 10).get_attribute(self.trust_day_element, "value")
        if trust_day:
            ElementUtil.click(self, driver, 15, text, *self.trust_day_clear_element)
            # Browser(driver, 10).click(self.trust_day_clear_element)
        date_not_None(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        date_not_None(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        date_not_None(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                      self.export_declaration_month_click_element)
        shipping_co = Browser(driver, 10).get_attribute(self.shipping_co_element, "value")
        if shipping_co is None:
            ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
            # Browser(driver, 10).click(self.shipping_co_element)
            Browser(driver, 10).choice_select(self.shipping_co_choice_element)
        customs_broker = Browser(driver, 10).get_attribute(self.customs_broker_element, "value")
        if customs_broker is None:
            Browser(driver, 10).send_keys(self.customs_broker_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.customs_broker_choice_element)
        cargo_type = Browser(driver, 10).get_attribute(self.cargo_type_element, "value")
        if cargo_type is None:
            Browser(driver, 10).send_keys(self.cargo_type_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.cargo_type_choice_element)
        SI_NO = Browser(driver, 10).get_attribute(self.SI_NO_element, "value")
        if SI_NO is None:
            Browser(driver, 10).send_keys(self.SI_NO_element, "test007")
        transport_text = Browser(driver, 10).get_text(self.transport_mode_element)
        if transport_text == "SEA":
            element_text = Browser(driver, 10).get_text(self.loading_method_get_element)
            if element_text == 'FCL':
                NO_elements = driver.find_elements(*self.container_NO_element)
                size_elements = driver.find_elements(*self.container_size_element)
                for no in range(len(NO_elements)):
                    NO_elements[no].send_keys('test002')
                    size_elements[no].click()
                    Browser(driver, 10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # Browser(driver, 10).click(self.temporary_saving_element)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        # Browser(driver, 10).click(self.confirm_button_element)
        Wait(driver, 10).elementwait(lambda x: x.find_element(*self.return_element))
        button = Browser(driver, 10).get_attribute(self.sending_confirmation_element, "style")
        if button == "display: none;":
            ElementUtil.click(self, driver, 15, text, *self.saving_element)
            # Browser(driver, 10).click(self.saving_element)
        else:
            ElementUtil.click(self, driver, 15, text, *self.sending_confirmation_element)
            # Browser(driver, 10).click(self.sending_confirmation_element)
        tips = Browser(driver, 10).get_text(self.tips_element)
        return tips

    def edit08(self, driver, text):
        """
        编集，修改所有数据，保存
        """
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # Browser(driver, 10).click(self.SA_button_element)
        ElementUtil.click(self, driver, 15, text, *self.search_element)
        # Browser(driver, 10).click(self.search_element)
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        search_and_click(driver, self.temporary_preservation_elements, self.next_page_element, self.display_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.edit_element)
        # Browser(driver, 10).click(self.edit_element)
        ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_element)
        # Browser(driver, 10).click(self.Master_BL_NO_element)
        loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        if loading_port is None:
            ElementUtil.click(self, driver, 15, text, *self.loading_port_element)
            Browser(driver, 10).choice_select(self.loading_port_choice_elements)
        # loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        # if not loading_port:
        #     ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        #     # Browser(driver, 10).click(self.INV_add_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_element)
        #     # Browser(driver, 10).click(self.IV_NO_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        #     # Browser(driver, 10).click(self.IV_NO_search_element)
        #     Browser(driver, 10).choice_check_box(self.choose_click_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        #     # Browser(driver, 10).click(self.IV_list_add_element)
        message = 'test' + str(time())[-6:]
        Master_BL_NO = Browser(driver, 10).get_attribute(self.Master_BL_NO_element, "value")
        if Master_BL_NO:
            ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_clear_element)
            # Browser(driver, 10).click(self.Master_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.Master_BL_NO_element, message)
        House_BL_NO = Browser(driver, 10).get_attribute(self.House_BL_NO_element, "value")
        if House_BL_NO:
            ElementUtil.click(self, driver, 15, text, *self.House_BL_NO_clear_element)
            # Browser(driver, 10).click(self.House_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.House_BL_NO_element, message)
        date_not_None(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        issue_date = Browser(driver, 10).get_attribute(self.issue_date_element, "value")
        if issue_date:
            ElementUtil.click(self, driver, 15, text, *self.issue_date_clear_element)
            # Browser(driver, 10).click(self.issue_date_clear_element)
        date_not_None(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        date_not_None(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                      self.export_declaration_month_click_element)
        shipping_co = Browser(driver, 10).get_attribute(self.shipping_co_element, "value")
        if shipping_co is None:
            ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
            # Browser(driver, 10).click(self.shipping_co_element)
            Browser(driver, 10).choice_select(self.shipping_co_choice_element)
        customs_broker = Browser(driver, 10).get_attribute(self.customs_broker_element, "value")
        if customs_broker is None:
            Browser(driver, 10).send_keys(self.customs_broker_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.customs_broker_choice_element)
        cargo_type = Browser(driver, 10).get_attribute(self.cargo_type_element, "value")
        if cargo_type is None:
            Browser(driver, 10).send_keys(self.cargo_type_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.cargo_type_choice_element)
        SI_NO = Browser(driver, 10).get_attribute(self.SI_NO_element, "value")
        if SI_NO is None:
            Browser(driver, 10).send_keys(self.SI_NO_element, "test007")
        transport_text = Browser(driver, 10).get_text(self.transport_mode_element)
        if transport_text == "SEA":
            element_text = Browser(driver, 10).get_text(self.loading_method_get_element)
            if element_text == 'FCL':
                NO_elements = driver.find_elements(*self.container_NO_element)
                size_elements = driver.find_elements(*self.container_size_element)
                for no in range(len(NO_elements)):
                    NO_elements[no].send_keys('test002')
                    size_elements[no].click()
                    Browser(driver, 10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # Browser(driver, 10).click(self.temporary_saving_element)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        # Browser(driver, 10).click(self.confirm_button_element)
        Wait(driver, 10).elementwait(lambda x: x.find_element(*self.return_element))
        button = Browser(driver, 10).get_attribute(self.sending_confirmation_element, "style")
        if button == "display: none;":
            ElementUtil.click(self, driver, 15, text, *self.saving_element)
            # Browser(driver, 10).click(self.saving_element)
        else:
            ElementUtil.click(self, driver, 15, text, *self.sending_confirmation_element)
            # Browser(driver, 10).click(self.sending_confirmation_element)
        tips = Browser(driver, 10).get_text(self.tips_element)
        return tips

    def edit09(self, driver, text):
        """
        编集，修改所有数据，保存
        """
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # Browser(driver, 10).click(self.SA_button_element)
        ElementUtil.click(self, driver, 15, text, *self.search_element)
        # Browser(driver, 10).click(self.search_element)
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        search_and_click(driver, self.temporary_preservation_elements, self.next_page_element, self.display_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.edit_element)
        # Browser(driver, 10).click(self.edit_element)
        message = 'test' + str(time())[-6:]
        ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_element)
        # Browser(driver, 10).click(self.Master_BL_NO_element)
        loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        if loading_port is None:
            ElementUtil.click(self, driver, 15, text, *self.loading_port_element)
            Browser(driver, 10).choice_select(self.loading_port_choice_elements)
        # loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        # if not loading_port:
        #     ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        #     # Browser(driver, 10).click(self.INV_add_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_element)
        #     # Browser(driver, 10).click(self.IV_NO_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        #     # Browser(driver, 10).click(self.IV_NO_search_element)
        #     Browser(driver, 10).choice_check_box(self.choose_click_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        #     # Browser(driver, 10).click(self.IV_list_add_element)
        Master_BL_NO = Browser(driver, 10).get_attribute(self.Master_BL_NO_element, "value")
        if Master_BL_NO:
            ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_clear_element)
            # Browser(driver, 10).click(self.Master_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.Master_BL_NO_element, message)
        House_BL_NO = Browser(driver, 10).get_attribute(self.House_BL_NO_element, "value")
        if House_BL_NO:
            ElementUtil.click(self, driver, 15, text, *self.House_BL_NO_clear_element)
            # Browser(driver, 10).click(self.House_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.House_BL_NO_element, message)
        date_not_None(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        date_not_None(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        ETA = Browser(driver, 10).get_attribute(self.ETA_element, "value")
        if ETA:
            ElementUtil.click(self, driver, 15, text, *self.ETA_clear_element)
            # Browser(driver, 10).click(self.ETA_clear_element)
        date_not_None(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                      self.export_declaration_month_click_element)
        shipping_co = Browser(driver, 10).get_attribute(self.shipping_co_element, "value")
        if shipping_co is None:
            ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
            # Browser(driver, 10).click(self.shipping_co_element)
            Browser(driver, 10).choice_select(self.shipping_co_choice_element)
        customs_broker = Browser(driver, 10).get_attribute(self.customs_broker_element, "value")
        if customs_broker is None:
            Browser(driver, 10).send_keys(self.customs_broker_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.customs_broker_choice_element)
        cargo_type = Browser(driver, 10).get_attribute(self.cargo_type_element, "value")
        if cargo_type is None:
            Browser(driver, 10).send_keys(self.cargo_type_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.cargo_type_choice_element)
        SI_NO = Browser(driver, 10).get_attribute(self.SI_NO_element, "value")
        if SI_NO is None:
            Browser(driver, 10).send_keys(self.SI_NO_element, "test007")
        transport_text = Browser(driver, 10).get_text(self.transport_mode_element)
        if transport_text == "SEA":
            element_text = Browser(driver, 10).get_text(self.loading_method_get_element)
            if element_text == 'FCL':
                NO_elements = driver.find_elements(*self.container_NO_element)
                size_elements = driver.find_elements(*self.container_size_element)
                for no in range(len(NO_elements)):
                    NO_elements[no].send_keys('test002')
                    size_elements[no].click()
                    Browser(driver, 10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # Browser(driver, 10).click(self.temporary_saving_element)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        # Browser(driver, 10).click(self.confirm_button_element)
        Wait(driver, 10).elementwait(lambda x: x.find_element(*self.return_element))
        button = Browser(driver, 10).get_attribute(self.sending_confirmation_element, "style")
        if button == "display: none;":
            ElementUtil.click(self, driver, 15, text, *self.saving_element)
            # Browser(driver, 10).click(self.saving_element)
        else:
            ElementUtil.click(self, driver, 15, text, *self.sending_confirmation_element)
            # Browser(driver, 10).click(self.sending_confirmation_element)
        tips = Browser(driver, 10).get_text(self.tips_element)
        return tips

    def edit10(self, driver, text):
        """
        编集，修改所有数据，保存
        """
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # Browser(driver, 10).click(self.SA_button_element)
        ElementUtil.click(self, driver, 15, text, *self.search_element)
        # Browser(driver, 10).click(self.search_element)
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        search_and_click(driver, self.temporary_preservation_elements, self.next_page_element, self.display_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.edit_element)
        # Browser(driver, 10).click(self.edit_element)
        ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_element)
        # Browser(driver, 10).click(self.Master_BL_NO_element)
        loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        if loading_port is None:
            ElementUtil.click(self, driver, 15, text, *self.loading_port_element)
            Browser(driver, 10).choice_select(self.loading_port_choice_elements)
        # loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        # if not loading_port:
        #     ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        #     # Browser(driver, 10).click(self.INV_add_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_element)
        #     # Browser(driver, 10).click(self.IV_NO_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        #     # Browser(driver, 10).click(self.IV_NO_search_element)
        #     Browser(driver, 10).choice_check_box(self.choose_click_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        #     # Browser(driver, 10).click(self.IV_list_add_element)
        message = 'test' + str(time())[-6:]
        Master_BL_NO = Browser(driver, 10).get_attribute(self.Master_BL_NO_element, "value")
        if Master_BL_NO is not None:
            ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_clear_element)
            # Browser(driver, 10).click(self.Master_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.Master_BL_NO_element, message)
        House_BL_NO = Browser(driver, 10).get_attribute(self.House_BL_NO_element, "value")
        if House_BL_NO is not None:
            ElementUtil.click(self, driver, 15, text, *self.House_BL_NO_clear_element)
            # Browser(driver, 10).click(self.House_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.House_BL_NO_element, message)
        date_not_None(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        date_not_None(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        date_not_None(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        export_declaration_date = Browser(driver, 10).get_attribute(self.export_declaration_date_element, "value")
        if export_declaration_date:
            ElementUtil.click(self, driver, 15, text, *self.export_declaration_date_clear_element)
            # Browser(driver, 10).click(self.export_declaration_date_clear_element)
        shipping_co = Browser(driver, 10).get_attribute(self.shipping_co_element, "value")
        if shipping_co is None:
            ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
            # Browser(driver, 10).click(self.shipping_co_element)
            Browser(driver, 10).choice_select(self.shipping_co_choice_element)
        customs_broker = Browser(driver, 10).get_attribute(self.customs_broker_element, "value")
        if customs_broker is None:
            Browser(driver, 10).send_keys(self.customs_broker_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.customs_broker_choice_element)
        cargo_type = Browser(driver, 10).get_attribute(self.cargo_type_element, "value")
        if cargo_type is None:
            Browser(driver, 10).send_keys(self.cargo_type_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.cargo_type_choice_element)
        SI_NO = Browser(driver, 10).get_attribute(self.SI_NO_element, "value")
        if SI_NO is None:
            Browser(driver, 10).send_keys(self.SI_NO_element, "test007")
        transport_text = Browser(driver, 10).get_text(self.transport_mode_element)
        if transport_text == "SEA":
            element_text = Browser(driver, 10).get_text(self.loading_method_get_element)
            if element_text == 'FCL':
                NO_elements = driver.find_elements(*self.container_NO_element)
                size_elements = driver.find_elements(*self.container_size_element)
                for no in range(len(NO_elements)):
                    NO_elements[no].send_keys('test002')
                    size_elements[no].click()
                    Browser(driver, 10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # Browser(driver, 10).click(self.temporary_saving_element)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        # Browser(driver, 10).click(self.confirm_button_element)
        Wait(driver, 10).elementwait(lambda x: x.find_element(*self.return_element))
        button = Browser(driver, 10).get_attribute(self.sending_confirmation_element, "style")
        if button == "display: none;":
            ElementUtil.click(self, driver, 15, text, *self.saving_element)
            # Browser(driver, 10).click(self.saving_element)
        else:
            ElementUtil.click(self, driver, 15, text, *self.sending_confirmation_element)
            # Browser(driver, 10).click(self.sending_confirmation_element)
        tips = Browser(driver, 10).get_text(self.tips_element)
        return tips

    def edit11(self, driver, text):
        """
        编集，修改所有数据，保存
        """
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # Browser(driver, 10).click(self.SA_button_element)
        ElementUtil.click(self, driver, 15, text, *self.search_element)
        # Browser(driver, 10).click(self.search_element)
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        search_and_click(driver, self.temporary_preservation_elements, self.next_page_element, self.display_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.edit_element)
        # Browser(driver, 10).click(self.edit_element)
        ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_element)
        # Browser(driver, 10).click(self.Master_BL_NO_element)
        loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        if loading_port is None:
            ElementUtil.click(self, driver, 15, text, *self.loading_port_element)
            Browser(driver, 10).choice_select(self.loading_port_choice_elements)
        # loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        # if not loading_port:
        #     ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        #     # Browser(driver, 10).click(self.INV_add_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_element)
        #     # Browser(driver, 10).click(self.IV_NO_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        #     # Browser(driver, 10).click(self.IV_NO_search_element)
        #     Browser(driver, 10).choice_check_box(self.choose_click_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        #     # Browser(driver, 10).click(self.IV_list_add_element)
        message = 'test' + str(time())[-6:]
        Master_BL_NO = Browser(driver, 10).get_attribute(self.Master_BL_NO_element, "value")
        if Master_BL_NO is not None:
            ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_clear_element)
            # Browser(driver, 10).click(self.Master_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.Master_BL_NO_element, message)
        House_BL_NO = Browser(driver, 10).get_attribute(self.House_BL_NO_element, "value")
        if House_BL_NO is not None:
            ElementUtil.click(self, driver, 15, text, *self.House_BL_NO_clear_element)
            # Browser(driver, 10).click(self.House_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.House_BL_NO_element, message)
        date_not_None(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        date_not_None(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        date_not_None(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        date_not_None(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                      self.export_declaration_month_click_element)
        shipping_co = Browser(driver, 10).get_attribute(self.shipping_co_element, "value")
        if shipping_co:
            ElementUtil.click(self, driver, 15, text, *self.shipping_co_clear_element)
            # Browser(driver, 10).click(self.shipping_co_clear_element)
        customs_broker = Browser(driver, 10).get_attribute(self.customs_broker_element, "value")
        if customs_broker is None:
            Browser(driver, 10).send_keys(self.customs_broker_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.customs_broker_choice_element)
        cargo_type = Browser(driver, 10).get_attribute(self.cargo_type_element, "value")
        if cargo_type is None:
            Browser(driver, 10).send_keys(self.cargo_type_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.cargo_type_choice_element)
        SI_NO = Browser(driver, 10).get_attribute(self.SI_NO_element, "value")
        if SI_NO is None:
            Browser(driver, 10).send_keys(self.SI_NO_element, "test007")
        transport_text = Browser(driver, 10).get_text(self.transport_mode_element)
        if transport_text == "SEA":
            element_text = Browser(driver, 10).get_text(self.loading_method_get_element)
            if element_text == 'FCL':
                NO_elements = driver.find_elements(*self.container_NO_element)
                size_elements = driver.find_elements(*self.container_size_element)
                for no in range(len(NO_elements)):
                    NO_elements[no].send_keys('test002')
                    size_elements[no].click()
                    Browser(driver, 10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # Browser(driver, 10).click(self.temporary_saving_element)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        # Browser(driver, 10).click(self.confirm_button_element)
        Wait(driver, 10).elementwait(lambda x: x.find_element(*self.return_element))
        button = Browser(driver, 10).get_attribute(self.sending_confirmation_element, "style")
        if button == "display: none;":
            ElementUtil.click(self, driver, 15, text, *self.saving_element)
            # Browser(driver, 10).click(self.saving_element)
        else:
            ElementUtil.click(self, driver, 15, text, *self.sending_confirmation_element)
            # Browser(driver, 10).click(self.sending_confirmation_element)
        tips = Browser(driver, 10).get_text(self.tips_element)
        return tips

    def edit12(self, driver, text):
        """
        编集，修改所有数据，通関業者不填能否送信
        """
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        ElementUtil.click(self, driver, 15, text, *self.search_element)
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        search_and_click(driver, self.temporary_preservation_elements, self.next_page_element, self.display_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.edit_element)
        # Browser(driver, 10).click(self.edit_element)
        loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        if loading_port is None:
            ElementUtil.click(self, driver, 15, text, *self.loading_port_element)
            Browser(driver, 10).choice_select(self.loading_port_choice_elements)
        # # ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_element)
        # # Browser(driver, 10).click(self.Master_BL_NO_element)
        # loading_port = Browser(self, driver, 10).get_attribute(self.loading_port_element, "value")
        # if not loading_port:
        #     ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        #     # Browser(driver, 10).click(self.INV_add_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_element)
        #     # Browser(driver, 10).click(self.IV_NO_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        #     # Browser(driver, 10).click(self.IV_NO_search_element)
        #     Browser(driver, 10).choice_check_box(self.choose_click_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        #     # Browser(driver, 10).click(self.IV_list_add_element)
        message = 'test' + str(time())[-6:]
        Master_BL_NO = Browser(driver, 10).get_attribute(self.Master_BL_NO_element, "value")
        if Master_BL_NO:
            ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_clear_element)
            # Browser(driver, 10).click(self.Master_BL_NO_clear_element)
        # Browser(driver, 10).send_keys(self.Master_BL_NO_element, message)
        ElementUtil.send_keys(self, driver, 15, message, text, *self.Master_BL_NO_element)
        House_BL_NO = Browser(driver, 10).get_attribute(self.House_BL_NO_element, "value")
        if House_BL_NO:
            ElementUtil.click(self, driver, 15, text, *self.House_BL_NO_clear_element)
            # Browser(driver, 10).click(self.House_BL_NO_clear_element)
        # Browser(driver, 10).send_keys(self.House_BL_NO_element, message)
        ElementUtil.send_keys(self, driver, 15, message, text, *self.House_BL_NO_element)
        date_not_None(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        date_not_None(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        date_not_None(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        date_not_None(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                      self.export_declaration_month_click_element)
        shipping_co = Browser(driver, 10).get_attribute(self.shipping_co_element, "value")
        if shipping_co is None:
            ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
            # Browser(driver, 10).click(self.shipping_co_element)
            Browser(driver, 10).choice_select(self.shipping_co_choice_element)
        customs_broker = Browser(driver, 10).get_attribute(self.customs_broker_element, "value")
        if customs_broker:
            ElementUtil.click(self, driver, 15, text, *self.customs_broker_clear_element)
            # Browser(driver, 10).click(self.customs_broker_clear_element)
        cargo_type = Browser(driver, 10).get_attribute(self.cargo_type_element, "value")
        if cargo_type is None:
            Browser(driver, 10).send_keys(self.cargo_type_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.cargo_type_choice_element)
        SI_NO = Browser(driver, 10).get_attribute(self.SI_NO_element, "value")
        if SI_NO is None:
            Browser(driver, 10).send_keys(self.SI_NO_element, "test007")
        transport_text = Browser(driver, 10).get_text(self.transport_mode_element)
        if transport_text == "SEA":
            element_text = Browser(driver, 10).get_text(self.loading_method_get_element)
            if element_text == 'FCL':
                NO_elements = driver.find_elements(*self.container_NO_element)
                size_elements = driver.find_elements(*self.container_size_element)
                for no in range(len(NO_elements)):
                    NO_elements[no].send_keys('test002')
                    size_elements[no].click()
                    Browser(driver, 10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # Browser(driver, 10).click(self.temporary_saving_element)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        # Browser(driver, 10).click(self.confirm_button_element)
        Wait(driver, 10).elementwait(lambda x: x.find_element(*self.return_element))
        button = Browser(driver, 10).get_attribute(self.sending_confirmation_element, "style")
        if button == "display: none;":
            ElementUtil.click(self, driver, 15, text, *self.saving_element)
            # Browser(driver, 10).click(self.saving_element)
        else:
            ElementUtil.click(self, driver, 15, text, *self.sending_confirmation_element)
            # Browser(driver, 10).click(self.sending_confirmation_element)
        tips = ElementUtil.getText(self, driver, 15, text, *self.tips_element)
        # print(tips)
        return tips

    def edit13(self, driver, text):
        """
        编集，修改所有数据，保存
        """
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # Browser(driver, 10).click(self.SA_button_element)
        ElementUtil.click(self, driver, 15, text, *self.search_element)
        # Browser(driver, 10).click(self.search_element)
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        search_and_click(driver, self.temporary_preservation_elements, self.next_page_element, self.display_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.edit_element)
        # Browser(driver, 10).click(self.edit_element)
        # ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_element)
        # Browser(driver, 10).click(self.Master_BL_NO_element)
        loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        if loading_port is None:
            ElementUtil.click(self, driver, 15, text, *self.loading_port_element)
            Browser(driver, 10).choice_select(self.loading_port_choice_elements)
        message = 'test' + str(time())[-6:]
        Master_BL_NO = Browser(driver, 10).get_attribute(self.Master_BL_NO_element, "value")
        if Master_BL_NO is not None:
            ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_clear_element)
            # Browser(driver, 10).click(self.Master_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.Master_BL_NO_element, message)
        House_BL_NO = Browser(driver, 10).get_attribute(self.House_BL_NO_element, "value")
        if House_BL_NO is not None:
            ElementUtil.click(self, driver, 15, text, *self.House_BL_NO_clear_element)
            # Browser(driver, 10).click(self.House_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.House_BL_NO_element, message)
        date_not_None(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        date_not_None(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        date_not_None(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        date_not_None(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                      self.export_declaration_month_click_element)
        shipping_co = Browser(driver, 10).get_attribute(self.shipping_co_element, "value")
        if shipping_co is None:
            ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
            # Browser(driver, 10).click(self.shipping_co_element)
            Browser(driver, 10).choice_select(self.shipping_co_choice_element)
        customs_broker = Browser(driver, 10).get_attribute(self.customs_broker_element, "value")
        if customs_broker is None:
            Browser(driver, 10).send_keys(self.customs_broker_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.customs_broker_choice_element)
        cargo_type = Browser(driver, 10).get_attribute(self.cargo_type_element, "value")
        if cargo_type:
            ElementUtil.click(self, driver, 15, text, *self.cargo_type_clear_element)
            # Browser(driver, 10).click(self.cargo_type_clear_element)
        SI_NO = Browser(driver, 10).get_attribute(self.SI_NO_element, "value")
        if SI_NO is None:
            Browser(driver, 10).send_keys(self.SI_NO_element, "test007")
        # transport_text = Browser(driver, 10).get_text(self.transport_mode_element)
        transport_text = ElementUtil.getText(self, driver, 15, text, *self.transport_mode_element)
        if transport_text == "SEA":
            element_text = ElementUtil.getText(self, driver, 15, text, *self.loading_method_get_element)
            # element_text = Browser(driver, 10).get_text(self.loading_method_get_element)
            if element_text == 'FCL':
                NO_elements = driver.find_elements(*self.container_NO_element)
                size_elements = driver.find_elements(*self.container_size_element)
                for no in range(len(NO_elements)):
                    NO_elements[no].send_keys('test002')
                    size_elements[no].click()
                    Browser(driver, 10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # Browser(driver, 10).click(self.temporary_saving_element)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        # Browser(driver, 10).click(self.confirm_button_element)
        Wait(driver, 10).elementwait(lambda x: x.find_element(*self.return_element))
        button = Browser(driver, 10).get_attribute(self.sending_confirmation_element, "style")
        if button == "display: none;":
            ElementUtil.click(self, driver, 15, text, *self.saving_element)
            # Browser(driver, 10).click(self.saving_element)
        else:
            ElementUtil.click(self, driver, 15, text, *self.sending_confirmation_element)
            # Browser(driver, 10).click(self.sending_confirmation_element)
        tips = ElementUtil.getText(self, driver, 15, text, *self.tips_element)
        # tips = Browser(driver, 10).get_text(self.tips_element)
        # print(tips)
        return tips

    def edit14(self, driver, text):
        """
        编集，修改所有数据，保存
        """
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # Browser(driver, 10).click(self.SA_button_element)
        ElementUtil.click(self, driver, 15, text, *self.search_element)
        # Browser(driver, 10).click(self.search_element)
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        search_and_click(driver, self.temporary_preservation_elements, self.next_page_element, self.display_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.edit_element)
        # Browser(driver, 10).click(self.edit_element)
        loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        if loading_port is None:
            ElementUtil.click(self, driver, 15, text, *self.loading_port_element)
            Browser(driver, 10).choice_select(self.loading_port_choice_elements)
        # ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_element)
        # # Browser(driver, 10).click(self.Master_BL_NO_element)
        # loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        # if not loading_port:
        #     ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        #     # Browser(driver, 10).click(self.INV_add_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_element)
        #     # Browser(driver, 10).click(self.IV_NO_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        #     # Browser(driver, 10).click(self.IV_NO_search_element)
        #     Browser(driver, 10).choice_check_box(self.choose_click_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        #     # Browser(driver, 10).click(self.IV_list_add_element)
        message = 'test' + str(time())[-6:]
        Master_BL_NO = Browser(driver, 10).get_attribute(self.Master_BL_NO_element, "value")
        if Master_BL_NO is not None:
            ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_clear_element)
            # Browser(driver, 10).click(self.Master_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.Master_BL_NO_element, message)
        House_BL_NO = Browser(driver, 10).get_attribute(self.House_BL_NO_element, "value")
        if House_BL_NO is not None:
            ElementUtil.click(self, driver, 15, text, *self.House_BL_NO_clear_element)
            # Browser(driver, 10).click(self.House_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.House_BL_NO_element, message)
        date_not_None(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        date_not_None(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        date_not_None(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        date_not_None(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                      self.export_declaration_month_click_element)
        shipping_co = Browser(driver, 10).get_attribute(self.shipping_co_element, "value")
        if shipping_co is None:
            ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
            # Browser(driver, 10).click(self.shipping_co_element)
            Browser(driver, 10).choice_select(self.shipping_co_choice_element)
        customs_broker = Browser(driver, 10).get_attribute(self.customs_broker_element, "value")
        if customs_broker is None:
            Browser(driver, 10).send_keys(self.customs_broker_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.customs_broker_choice_element)
        cargo_type = Browser(driver, 10).get_attribute(self.cargo_type_element, "value")
        if cargo_type is None:
            Browser(driver, 10).send_keys(self.cargo_type_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.cargo_type_choice_element)
        SI_NO = Browser(driver, 10).get_attribute(self.SI_NO_element, "value")
        if SI_NO is None:
            Browser(driver, 10).send_keys(self.SI_NO_element, "test007")
        transport_text = Browser(driver, 10).get_text(self.transport_mode_element)
        if transport_text != "SEA":
            ElementUtil.click(self, driver, 15, text, *self.transport_mode_element)
            # Browser(driver, 10).click(self.transport_mode_element)
            ElementUtil.click(self, driver, 15, text, *self.SEA_element)
            # Browser(driver, 10).click(self.SEA_element)
        element_text = Browser(driver, 10).get_text(self.loading_method_get_element)
        if element_text != 'FCL':
            Browser(driver, 10).send_keys(self.loading_method_element, Keys.ENTER)
            ElementUtil.click(self, driver, 15, text, *self.FCL_element)
            # Browser(driver, 10).click(self.FCL_element)
        NO_elements = driver.find_elements(*self.container_NO_element)
        size_elements = driver.find_elements(*self.container_size_element)
        for no in range(len(NO_elements)):
            NO_elements[no].send_keys(Keys.CONTROL, "a")
            NO_elements[no].send_keys(Keys.DELETE)
            size_elements[no].click()
            Browser(driver, 10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # Browser(driver, 10).click(self.temporary_saving_element)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        # Browser(driver, 10).click(self.confirm_button_element)
        Wait(driver, 10).elementwait(lambda x: x.find_element(*self.return_element))
        button = Browser(driver, 10).get_attribute(self.sending_confirmation_element, "style")
        if button == "display: none;":
            ElementUtil.click(self, driver, 15, text, *self.saving_element)
            # Browser(driver, 10).click(self.saving_element)
        else:
            ElementUtil.click(self, driver, 15, text, *self.sending_confirmation_element)
            # Browser(driver, 10).click(self.sending_confirmation_element)
        tips = Browser(driver, 10).get_text(self.windows_tips_element)
        tip = "INV P/L情報が不整備です、ご確認お願いします。"
        # print(tips)
        if tip in tips:
            return True

    def edit15(self, driver, text):
        """
        编集，修改所有数据，保存
        """
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # Browser(driver, 10).click(self.SA_button_element)
        ElementUtil.click(self, driver, 15, text, *self.search_element)
        # Browser(driver, 10).click(self.search_element)
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        search_and_click(driver, self.temporary_preservation_elements, self.next_page_element, self.display_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.edit_element)
        # Browser(driver, 10).click(self.edit_element)
        loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        if loading_port is None:
            ElementUtil.click(self, driver, 15, text, *self.loading_port_element)
            Browser(driver, 10).choice_select(self.loading_port_choice_elements)
        # ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_element)
        # # Browser(driver, 10).click(self.Master_BL_NO_element)
        # loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        # if not loading_port:
        #     ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        #     # Browser(driver, 10).click(self.INV_add_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_element)
        #     # Browser(driver, 10).click(self.IV_NO_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        #     # Browser(driver, 10).click(self.IV_NO_search_element)
        #     Browser(driver, 10).choice_check_box(self.choose_click_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        #     # Browser(driver, 10).click(self.IV_list_add_element)
        message = 'test' + str(time())[-6:]
        Master_BL_NO = Browser(driver, 10).get_attribute(self.Master_BL_NO_element, "value")
        if Master_BL_NO is not None:
            ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_clear_element)
            # Browser(driver, 10).click(self.Master_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.Master_BL_NO_element, message)
        House_BL_NO = Browser(driver, 10).get_attribute(self.House_BL_NO_element, "value")
        if House_BL_NO is not None:
            ElementUtil.click(self, driver, 15, text, *self.House_BL_NO_clear_element)
            # Browser(driver, 10).click(self.House_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.House_BL_NO_element, message)
        date_not_None(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        date_not_None(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        date_not_None(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        date_not_None(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                      self.export_declaration_month_click_element)
        shipping_co = Browser(driver, 10).get_attribute(self.shipping_co_element, "value")
        if shipping_co is None:
            ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
            # Browser(driver, 10).click(self.shipping_co_element)
            Browser(driver, 10).choice_select(self.shipping_co_choice_element)
        customs_broker = Browser(driver, 10).get_attribute(self.customs_broker_element, "value")
        if customs_broker is None:
            Browser(driver, 10).send_keys(self.customs_broker_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.customs_broker_choice_element)
        cargo_type = Browser(driver, 10).get_attribute(self.cargo_type_element, "value")
        if cargo_type is None:
            Browser(driver, 10).send_keys(self.cargo_type_element, Keys.ENTER)
            Browser(driver, 10).choice_select(self.cargo_type_choice_element)
        SI_NO = Browser(driver, 10).get_attribute(self.SI_NO_element, "value")
        if SI_NO is None:
            Browser(driver, 10).send_keys(self.SI_NO_element, "test007")
        # transport_text = Browser(driver, 10).get_text(self.transport_mode_element)
        transport_text = ElementUtil.getText(self, driver, 15, text, *self.transport_mode_element)
        if transport_text != "SEA":
            ElementUtil.click(self, driver, 15, text, *self.transport_mode_element)
            # Browser(driver, 10).click(self.transport_mode_element)
            ElementUtil.click(self, driver, 15, text, *self.SEA_element)
            # Browser(driver, 10).click(self.SEA_element)
        # element_text = Browser(self, driver, 10).get_text(self.loading_method_get_element)
        element_text = ElementUtil.getText(self, driver, 15, text, *self.loading_method_get_element)
        if element_text != 'FCL':
            Browser(driver, 10).send_keys(self.loading_method_element, Keys.ENTER)
            ElementUtil.click(self, driver, 15, text, *self.FCL_element)
            # Browser(driver, 10).click(self.FCL_element)
        NO_elements = driver.find_elements(*self.container_NO_element)
        size_elements = driver.find_elements(*self.container_size_element)
        for no in range(len(NO_elements)):
            if NO_elements[no].get_attribute("value"):
                NO_elements[no].send_keys(Keys.CONTROL, "a")
                NO_elements[no].send_keys(Keys.DELETE)
            if not size_elements[no].get_attribute("value"):
                size_elements[no].click()
                Browser(driver, 10).choice_select(self.container_size_choice_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # Browser(driver, 10).click(self.temporary_saving_element)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        # Browser(driver, 10).click(self.confirm_button_element)
        Wait(driver, 10).elementwait(lambda x: x.find_element(*self.return_element))
        button = Browser(driver, 10).get_attribute(self.sending_confirmation_element, "style")
        if button == "display: none;":
            ElementUtil.click(self, driver, 15, text, *self.saving_element)
            # Browser(driver, 10).click(self.saving_element)
            ElementUtil.click(self, driver, 15, text, *self.sure_button_element)
            # Browser(driver, 10).click(self.sure_button_element)
        else:
            ElementUtil.click(self, driver, 15, text, *self.sending_confirmation_element)
            # Browser(driver, 10).click(self.sending_confirmation_element)
        tips = Browser(driver, 10).get_text(self.windows_tips_element)
        tip = "INV P/L情報が不整備です、ご確認お願いします。"
        # print(tips)
        if tip in tips:
            return True

    def edit16(self, driver, text):

        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # Browser(driver, 10).click(self.SA_button_element)
        ElementUtil.click(self, driver, 15, text, *self.BL_NO_element)
        # Browser(driver, 10).click(self.BL_NO_element)
        ElementUtil.click(self, driver, 15, text, *self.search_element)
        # Browser(driver, 10).click(self.search_element)
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        search_and_click(driver, self.temporary_preservation_elements, self.next_page_element, self.display_element)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        ElementUtil.click(self, driver, 15, text, *self.edit_element)
        # Browser(driver, 10).click(self.edit_element)
        loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        if loading_port is None:
            ElementUtil.click(self, driver, 15, text, *self.loading_port_element)
            Browser(driver, 10).choice_select(self.loading_port_choice_elements)
        # ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_element)
        # # Browser(driver, 10).click(self.Master_BL_NO_element)
        # loading_port = Browser(driver, 10).get_attribute(self.loading_port_element, "value")
        # if not loading_port:
        #     ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        #     # Browser(driver, 10).click(self.INV_add_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_element)
        #     # Browser(driver, 10).click(self.IV_NO_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        #     # Browser(driver, 10).click(self.IV_NO_search_element)
        #     Browser(driver, 10).choice_check_box(self.choose_click_element)
        #     ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        #     # Browser(driver, 10).click(self.IV_list_add_element)
        ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_element)
        # Browser(driver, 10).click(self.Master_BL_NO_element)
        Master_BL_NO = Browser(driver, 10).get_attribute(self.Master_BL_NO_element, "value")
        House_BL_NO = Browser(driver, 10).get_attribute(self.House_BL_NO_element, "value")
        message = "test011"
        if message == Master_BL_NO or message == House_BL_NO:
            message = "test010"
        if Master_BL_NO:
            ElementUtil.click(self, driver, 15, text, *self.Master_BL_NO_clear_element)
            # Browser(driver, 10).click(self.Master_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.Master_BL_NO_element, message)
        if House_BL_NO:
            ElementUtil.click(self, driver, 15, text, *self.House_BL_NO_clear_element)
            # Browser(driver, 10).click(self.House_BL_NO_clear_element)
        Browser(driver, 10).send_keys(self.House_BL_NO_element, message)
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # Browser(driver, 10).click(self.temporary_saving_element)
        tips = Browser(driver, 10).get_text(self.windows_tips_element)
        return tips


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://sharpsit.jusdaglobal.com/')
    login = Login()
    login.test_click_login_btn(driver)
    sleep(5)
    edit = Edit()
    print(edit.edit01(driver))