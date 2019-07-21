"""
@author: yangjun
"""
import random
from random import choice
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from business.Login import Login
from business.test_customs.method import choose_date
from common.Browser import Browser
from common.Iv_No import IV_NO
from pageElement.SAlogin.HomePage import HomePageElement
from pageElement.SAlogin.newlyBuild import NewlyBuildElement
from pageElement.SAlogin.RequiredFieldPage import RequiredFieldElement
from util.ElementUtil import ElementUtil


class RequiredField(HomePageElement, NewlyBuildElement, RequiredFieldElement):
    """新建Shipping Advice数据,必填项验证"""

    def no_requested_date(self, driver):
        """依赖日不填"""
        # 点击SA登录
        data = IV_NO.yj_randoms().get('invoiceNo')
        ElementUtil.click(self, driver, 15, "点击SA登录", *self.SA_button_element)
        # 点击新规
        ElementUtil.click(self, driver, 15, "点击新规", *self.newlyBuilt_element)
        # 点击INV P/L情报下 追加
        ElementUtil.click(self, driver, 15, "点击INV P/L情报下 追加", *self.INV_add_element)
        # 输入I/V NO
        ElementUtil.send_keys(self, driver, 15, data, "输入I/V NO", *self.IV_NO_element)
        # 点击IV List下 検索
        sleep(0.5)
        ElementUtil.click(self, driver, 15, "点击IV List下 検索", *self.IV_NO_search_element)
        # IV List下 选择数据
        sleep(1)
        ElementUtil.click(self, driver, 15, "IV List下 勾选数据", *self.choose_data_element)
        # Browser(driver, 15).choice_check_box(self.choose_click_element)
        # 点击IV List下 追加
        ElementUtil.click(self, driver, 15, "点击IV List下 追加", *self.IV_list_add_element)
        # 输入Master B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(100000, 999999), "输入Master B/L NO", *self.Master_BL_NO_element)
        # 输入House B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(999999, 9999999), "输入House B/L NO", *self.House_BL_NO_element)
        # 选择B/L発行日
        choose_date(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        # 选择ETA
        choose_date(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        # 輸出通関日
        choose_date(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        # 根据輸送形態选择積み方
        sleep(0.5)
        transport_text = ElementUtil.getText(self, driver, 15, "获取輸送形態的文本", *self.transport_mode_element)
        # print(transport_text)
        if transport_text == "SEA":
            ElementUtil.send_keys(self, driver, 15, Keys.SPACE, "点击積み方", *self.loading_method_element)
            sleep(0.5)
            element_SEA = driver.find_elements(*self.loading_method_choice_elements)
            choice(element_SEA).click()
            # 判断積み方选择
            sleep(0.5)
            element_text = ElementUtil.getText(self, driver, 15, "获取積み方文本",*self.loading_method_get_element)
            # print(element_text)
            if element_text == 'FCL':
                container_NO = driver.find_elements(*self.container_NO_element)
                container_size = driver.find_elements(*self.container_size_element)
                for no in range(len(container_NO)):
                    container_NO[no].send_keys('container No')
                    container_size[no].click()
                    sleep(0.5)
                    element_container_size = driver.find_elements(*self.container_size_choice_element)
                    choice(element_container_size).click()
                    # 識別番号
                    element_PID = driver.find_elements(*self.PID_element)
                    element_PID[no].send_keys('666')
            # 回到顶部
            driver.execute_script("window.scrollTo(0,0)")
            # 本船名
            ElementUtil.send_keys(self, driver, 15, 'shipsname', "输入本船名", *self.ships_name_element)
            # VOYAGE NO
            ElementUtil.send_keys(self, driver, 15, 'vo1001', "输入VOYAGE NO", *self.VOYAGE_NO_element)
        if transport_text == 'AIR':
            # フライトNO
            ElementUtil.send_keys(self, driver, 15, 'No0003', "输入フライトNO", *self.flying_No_element)
        # 选择船社・航空会社
        ElementUtil.click(self, driver, 15, "选择船社・航空会社", *self.shipping_co_element)
        sleep(0.5)
        element_group = driver.find_elements(*self.shipping_co_choice_element)
        choice(element_group).click()
        # S/I NO
        ElementUtil.send_keys(self, driver, 15, 'si1122', "输入S/I NO", *self.SI_NO_element)
        # 通関業者
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, "选择通関業者", *self.customs_broker_element)
        sleep(0.5)
        element_customs = driver.find_elements(*self.customs_broker_choice_element)
        choice(element_customs).click()
        # 貨物タイプ
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, "选择貨物タイプ", *self.cargo_type_element)
        sleep(0.5)
        element_cargo = driver.find_elements(*self.cargo_type_choice_element)
        choice(element_cargo).click()

        # 回到顶部
        driver.execute_script("window.scrollTo(0,0)")

        # 点击一時保存
        ElementUtil.click(self, driver, 15, "点击一時保存", *self.temporary_saving_element)
        sleep(1)
        # 点击弹框确定
        ElementUtil.click(self, driver, 15, "点击弹框确定", *self.confirm_button_element)
        try:
            # 点击確定送信
            sleep(0.5)
            submit = driver.find_elements(*self.sending_confirmation_element)
            if submit == []:
                # 没有確定送信,点击保存
                ElementUtil.click(self, driver, 15, "点击確定送信", *self.saving_element)
            else:
                submit[0].click()
            # 获取返回值 依頼日必要である
            sleep(0.5)
            trust_text = ElementUtil.getText(self, driver, 15, "获取返回值", *self.trust_day_value_element)
            expect = "依頼日必要である"
            if expect == trust_text:
                return True
        except Exception as e:
            return e

    def no_issue_date(self, driver, text):
        """不填写B/L発行日"""
        # 点击SA登录
        # sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # 点击新规
        ElementUtil.click(self, driver, 15, text, *self.newlyBuilt_element)
        # 点击INV P/L情报下 追加
        ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        # 输入I/V NO
        ElementUtil.send_keys(self, driver, 15, IV_NO.yj_randoms().get('invoiceNo'), text, *self.IV_NO_element)
        # 点击IV List下 検索
        sleep(0.5)
        ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        sleep(1)
        # IV List下 选择数据
        ElementUtil.click(self, driver, 15, text, *self.choose_data_element)
        # Browser(driver, 15).choice_check_box(self.choose_click_element)
        # 点击IV List下 追加
        ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        # 输入Master B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(10000, 99999), text, *self.Master_BL_NO_element)
        # 输入House B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(99999, 999999), text, *self.House_BL_NO_element)
        # 选择依赖日
        choose_date(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        # 选择ETA
        choose_date(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        # 輸出通関日
        choose_date(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        # 根据輸送形態选择積み方
        sleep(0.5)
        transport_text = ElementUtil.getText(self, driver, 15, text, *self.transport_mode_element)
        # print(transport_text)
        if transport_text == "SEA":
            ElementUtil.send_keys(self, driver, 15, Keys.SPACE, text, *self.loading_method_element)
            sleep(0.5)
            element_SEA = driver.find_elements(*self.loading_method_choice_elements)
            choice(element_SEA).click()
            # 判断積み方选择
            sleep(0.5)
            element_text = ElementUtil.getText(self, driver, 15, text, *self.loading_method_get_element)
            # print(element_text)
            if element_text == 'FCL':
                container_NO = driver.find_elements(*self.container_NO_element)
                container_size = driver.find_elements(*self.container_size_element)
                for no in range(len(container_NO)):
                    container_NO[no].send_keys('container No')
                    container_size[no].click()
                    sleep(0.5)
                    element_container_size = driver.find_elements(*self.container_size_choice_element)
                    choice(element_container_size).click()
                    # 識別番号
                    element_PID = driver.find_elements(*self.PID_element)
                    element_PID[no].send_keys('666')
            # 回到顶部
            driver.execute_script("window.scrollTo(0,0)")
            # 本船名
            ElementUtil.send_keys(self, driver, 15, 'shipsname', text, *self.ships_name_element)
            # VOYAGE NO
            ElementUtil.send_keys(self, driver, 15, 'vo1001', text, *self.VOYAGE_NO_element)
        if transport_text == 'AIR':
            # フライトNO
            ElementUtil.send_keys(self, driver, 15, 'No0003', text, *self.flying_No_element)
        # 选择船社・航空会社
        ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
        sleep(0.5)
        element_group = driver.find_elements(*self.shipping_co_choice_element)
        choice(element_group).click()
        # S/I NO
        ElementUtil.send_keys(self, driver, 15, 'si1122', text, *self.SI_NO_element)
        # 通関業者
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.customs_broker_element)
        sleep(0.5)
        element_customs = driver.find_elements(*self.customs_broker_choice_element)
        choice(element_customs).click()
        # 貨物タイプ
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.cargo_type_element)
        sleep(0.5)
        element_cargo = driver.find_elements(*self.cargo_type_choice_element)
        choice(element_cargo).click()

        # 回到顶部
        driver.execute_script("window.scrollTo(0,0)")

        # 点击一時保存
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # 点击弹框确定
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        try:
            # 点击確定送信
            sleep(0.5)
            submit = driver.find_elements(*self.sending_confirmation_element)
            if submit == []:
                # 没有確定送信,点击保存
                ElementUtil.click(self, driver, 15, *self.saving_element)
            else:
                submit[0].click()
            # 获取返回值
            sleep(0.5)
            issue_text = ElementUtil.getText(self, driver, 15, text, *self.issue_day_value_element)
            expect = "B/L発行日必要である"
            if expect == issue_text:
                return True
        except Exception as e:
            return e

    def no_ETA(self, driver, text):
        """不填写ETA"""
        # 点击SA登录
        # sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # 点击新规
        ElementUtil.click(self, driver, 15, text, *self.newlyBuilt_element)
        # 点击INV P/L情报下 追加
        ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        # 输入I/V NO
        ElementUtil.send_keys(self, driver, 15, IV_NO.yj_randoms().get('invoiceNo'), text, *self.IV_NO_element)
        # 点击IV List下 検索
        sleep(0.5)
        ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        # IV List下 选择数据
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.choose_data_element)
        # Browser(driver, 15).choice_check_box(self.choose_click_element)
        # 点击IV List下 追加
        ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        # 输入Master B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(10000, 99999), text, *self.Master_BL_NO_element)
        # 输入House B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(99999, 999999), text, *self.House_BL_NO_element)
        # 选择依赖日
        choose_date(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        # 选择B/L発行日
        choose_date(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        # 輸出通関日
        choose_date(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        # 根据輸送形態选择積み方
        sleep(0.5)
        transport_text = ElementUtil.getText(self, driver, 15, text, *self.transport_mode_element)
        # print(transport_text)
        if transport_text == "SEA":
            ElementUtil.send_keys(self, driver, 15, Keys.SPACE, text, *self.loading_method_element)
            sleep(0.5)
            element_SEA = driver.find_elements(*self.loading_method_choice_elements)
            choice(element_SEA).click()
            # 判断積み方选择
            sleep(0.5)
            element_text = ElementUtil.getText(self, driver, 15, text, *self.loading_method_get_element)
            # print(element_text)
            if element_text == 'FCL':
                container_NO = driver.find_elements(*self.container_NO_element)
                container_size = driver.find_elements(*self.container_size_element)
                for no in range(len(container_NO)):
                    container_NO[no].send_keys('container No')
                    container_size[no].click()
                    sleep(0.5)
                    element_container_size = driver.find_elements(*self.container_size_choice_element)
                    choice(element_container_size).click()
                    # 識別番号
                    element_PID = driver.find_elements(*self.PID_element)
                    element_PID[no].send_keys('666')
            # 回到顶部
            driver.execute_script("window.scrollTo(0,0)")
            # 本船名
            ElementUtil.send_keys(self, driver, 15, 'shipsname', text, *self.ships_name_element)
            # VOYAGE NO
            ElementUtil.send_keys(self, driver, 15, 'vo1001', text, *self.VOYAGE_NO_element)
        if transport_text == 'AIR':
            # フライトNO
            ElementUtil.send_keys(self, driver, 15, 'No0003', text, *self.flying_No_element)
        # 选择船社・航空会社
        ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
        sleep(0.5)
        element_group = driver.find_elements(*self.shipping_co_choice_element)
        choice(element_group).click()
        # S/I NO
        ElementUtil.send_keys(self, driver, 15, 'si1122', text, *self.SI_NO_element)
        # 通関業者
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.customs_broker_element)
        sleep(0.5)
        element_customs = driver.find_elements(*self.customs_broker_choice_element)
        choice(element_customs).click()
        # 貨物タイプ
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.cargo_type_element)
        sleep(0.5)
        element_cargo = driver.find_elements(*self.cargo_type_choice_element)
        choice(element_cargo).click()

        # 回到顶部
        driver.execute_script("window.scrollTo(0,0)")

        # 点击一時保存
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # 点击弹框确定
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        try:
            # 点击確定送信
            sleep(0.5)
            submit = driver.find_elements(*self.sending_confirmation_element)
            if submit == []:
                # 没有確定送信,点击保存
                ElementUtil.click(self, driver, 15, text, *self.saving_element)
            else:
                submit[0].click()
            # 获取返回值
            sleep(0.5)
            ETA_text = ElementUtil.getText(self, driver, 15, text, *self.ETA_value_element)
            expect = "ETA必要である"
            if expect == ETA_text:
                return True
        except Exception as e:
            return e

    def no_loading_method(self, driver, text):
        """不填写積み方"""
        # 点击SA登录
        # sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # 点击新规
        ElementUtil.click(self, driver, 15, text, *self.newlyBuilt_element)
        # 点击INV P/L情报下 追加
        ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        # 输入I/V NO
        ElementUtil.send_keys(self, driver, 15, IV_NO.yj_randoms().get('invoiceNo'), text, *self.IV_NO_element)
        # 点击IV List下 検索
        sleep(0.5)
        ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        # IV List下 选择数据
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.choose_data_element)
        # Browser(driver, 15).choice_check_box(self.choose_click_element)
        # 点击IV List下 追加
        ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        # 输入Master B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(10000, 99999), text, *self.Master_BL_NO_element)
        # 输入House B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(99999, 999999), text, *self.House_BL_NO_element)
        # 选择依赖日
        choose_date(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        # 选择B/L発行日
        choose_date(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        # 选择ETA
        choose_date(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        # 輸出通関日
        choose_date(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        # 判断輸送形態
        sleep(0.5)
        transport_text = ElementUtil.getText(self, driver, 15, text, *self.transport_mode_element)
        # print(transport_text)
        if transport_text == 'AIR':
            # 将輸送形態变为SEA
            ElementUtil.click(self, driver, 15, text, *self.transport_mode_element)
            ElementUtil.click(self, driver, 15, text, *self.transport_mode_SEA_element)
        # 本船名
        ElementUtil.send_keys(self, driver, 15, 'shipsname', text, *self.ships_name_element)
        # VOYAGE NO
        ElementUtil.send_keys(self, driver, 15, 'vo1001', text, *self.VOYAGE_NO_element)
        # 选择船社・航空会社
        ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
        sleep(0.5)
        element_group = driver.find_elements(*self.shipping_co_choice_element)
        choice(element_group).click()
        # S/I NO
        ElementUtil.send_keys(self, driver, 15, 'si1122', text, *self.SI_NO_element)
        # 通関業者
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.customs_broker_element)
        sleep(0.5)
        element_customs = driver.find_elements(*self.customs_broker_choice_element)
        choice(element_customs).click()
        # 貨物タイプ
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.cargo_type_element)
        sleep(0.5)
        element_cargo = driver.find_elements(*self.cargo_type_choice_element)
        choice(element_cargo).click()
        # 回到顶部
        driver.execute_script("window.scrollTo(0,0)")
        try:
            # 点击一時保存
            ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
            # 获取返回值
            sleep(0.5)
            loading_method_text = ElementUtil.getText(self, driver, 15, text, *self.loading_method_value_element)
            expect = "積み方必要である"
            if expect == loading_method_text:
                return True
        except Exception as e:
            return e

    def no_export_declaration_date(self, driver, text):
        """不填写輸出通関日"""
        # 点击SA登录
        # sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # 点击新规
        ElementUtil.click(self, driver, 15, text, *self.newlyBuilt_element)
        # 点击INV P/L情报下 追加
        ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        # 输入I/V NO
        ElementUtil.send_keys(self, driver, 15, IV_NO.yj_randoms().get('invoiceNo'), text, *self.IV_NO_element)
        # 点击IV List下 検索
        sleep(0.5)
        ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        # IV List下 选择数据
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.choose_data_element)
        # Browser(driver, 15).choice_check_box(self.choose_click_element)
        # 点击IV List下 追加
        ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        # 输入Master B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(10000, 99999), text, *self.Master_BL_NO_element)
        # 输入House B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(99999, 999999), text, *self.House_BL_NO_element)
        # 选择依赖日
        choose_date(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        # 选择B/L発行日
        choose_date(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        # 选择ETA
        choose_date(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        # 根据輸送形態选择積み方
        sleep(0.5)
        transport_text = ElementUtil.getText(self, driver, 15, text, *self.transport_mode_element)
        # print(transport_text)
        if transport_text == "SEA":
            ElementUtil.send_keys(self, driver, 15, Keys.SPACE, text, *self.loading_method_element)
            sleep(0.5)
            element_SEA = driver.find_elements(*self.loading_method_choice_elements)
            choice(element_SEA).click()
            # 判断積み方选择
            sleep(0.5)
            element_text = ElementUtil.getText(self, driver, 15, text, *self.loading_method_get_element)
            # print(element_text)
            if element_text == 'FCL':
                container_NO = driver.find_elements(*self.container_NO_element)
                container_size = driver.find_elements(*self.container_size_element)
                for no in range(len(container_NO)):
                    container_NO[no].send_keys('container No')
                    container_size[no].click()
                    sleep(0.5)
                    element_container_size = driver.find_elements(*self.container_size_choice_element)
                    choice(element_container_size).click()
                    # 識別番号
                    element_PID = driver.find_elements(*self.PID_element)
                    element_PID[no].send_keys('666')
            # 回到顶部
            driver.execute_script("window.scrollTo(0,0)")
            # 本船名
            ElementUtil.send_keys(self, driver, 15, 'shipsname', text, *self.ships_name_element)
            # VOYAGE NO
            ElementUtil.send_keys(self, driver, 15, 'vo1001', text, *self.VOYAGE_NO_element)
        if transport_text == 'AIR':
            # フライトNO
            ElementUtil.send_keys(self, driver, 15, 'No0003', text, *self.flying_No_element)
        # 选择船社・航空会社
        ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
        sleep(0.5)
        element_group = driver.find_elements(*self.shipping_co_choice_element)
        choice(element_group).click()
        # S/I NO
        ElementUtil.send_keys(self, driver, 15, 'si1122', text, *self.SI_NO_element)
        # 通関業者
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.customs_broker_element)
        sleep(0.5)
        element_customs = driver.find_elements(*self.customs_broker_choice_element)
        choice(element_customs).click()
        # 貨物タイプ
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.cargo_type_element)
        sleep(0.5)
        element_cargo = driver.find_elements(*self.cargo_type_choice_element)
        choice(element_cargo).click()

        # 回到顶部
        driver.execute_script("window.scrollTo(0,0)")

        # 点击一時保存
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # 点击弹框确定
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        try:
            # 点击確定送信
            sleep(0.5)
            submit = driver.find_elements(*self.sending_confirmation_element)
            if submit == []:
                # 没有確定送信,点击保存
                ElementUtil.click(self, driver, 15, text, *self.saving_element)
            else:
                submit[0].click()
            # 获取返回值
            sleep(0.5)
            export_dec_date_text = ElementUtil.getText(self, driver, 15, text, *self.export_dec_date_value_element)
            expect = "輸出通関日必要である"
            if expect == export_dec_date_text:
                return True
        except Exception as e:
            return e

    def no_ship_air_company(self, driver, text):
        """不填写船社・航空会社"""
        # 点击SA登录
        # sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # 点击新规
        ElementUtil.click(self, driver, 15, text, *self.newlyBuilt_element)
        # 点击INV P/L情报下 追加
        ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        # 输入I/V NO
        ElementUtil.send_keys(self, driver, 15, IV_NO.yj_randoms().get('invoiceNo'), text, *self.IV_NO_element)
        # 点击IV List下 検索
        sleep(0.5)
        ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        # IV List下 选择数据
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.choose_data_element)
        # Browser(driver, 15).choice_check_box(self.choose_click_element)
        # 点击IV List下 追加
        ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        # 输入Master B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(10000, 99999), text, *self.Master_BL_NO_element)
        # 输入House B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(99999, 999999), text, *self.House_BL_NO_element)
        # 选择依赖日
        choose_date(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        # 选择B/L発行日
        choose_date(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        # 选择ETA
        choose_date(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        # 輸出通関日
        choose_date(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        # 根据輸送形態选择積み方
        sleep(0.5)
        transport_text = ElementUtil.getText(self, driver, 15, text, *self.transport_mode_element)
        # print(transport_text)
        if transport_text == "SEA":
            ElementUtil.send_keys(self, driver, 15, Keys.SPACE, text, *self.loading_method_element)
            sleep(0.5)
            element_SEA = driver.find_elements(*self.loading_method_choice_elements)
            choice(element_SEA).click()
            # 判断積み方选择
            sleep(0.5)
            element_text = ElementUtil.getText(self, driver, 15, text, *self.loading_method_get_element)
            # print(element_text)
            if element_text == 'FCL':
                container_NO = driver.find_elements(*self.container_NO_element)
                container_size = driver.find_elements(*self.container_size_element)
                for no in range(len(container_NO)):
                    container_NO[no].send_keys('container No')
                    container_size[no].click()
                    sleep(0.5)
                    element_container_size = driver.find_elements(*self.container_size_choice_element)
                    choice(element_container_size).click()
                    # 識別番号
                    element_PID = driver.find_elements(*self.PID_element)
                    element_PID[no].send_keys('666')
            # 回到顶部
            driver.execute_script("window.scrollTo(0,0)")
            # 本船名
            ElementUtil.send_keys(self, driver, 15, 'shipsname', text, *self.ships_name_element)
            # VOYAGE NO
            ElementUtil.send_keys(self, driver, 15, 'vo1001', text, *self.VOYAGE_NO_element)
        if transport_text == 'AIR':
            # フライトNO
            ElementUtil.send_keys(self, driver, 15, 'No0003', text, *self.flying_No_element)
        # S/I NO
        ElementUtil.send_keys(self, driver, 15, 'si1122', text, *self.SI_NO_element)
        # 通関業者
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.customs_broker_element)
        sleep(0.5)
        element_customs = driver.find_elements(*self.customs_broker_choice_element)
        choice(element_customs).click()
        # 貨物タイプ
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.cargo_type_element)
        sleep(0.5)
        element_cargo = driver.find_elements(*self.cargo_type_choice_element)
        choice(element_cargo).click()

        # 回到顶部
        driver.execute_script("window.scrollTo(0,0)")

        # 点击一時保存
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # 点击弹框确定
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        try:
            # 点击確定送信
            sleep(0.5)
            submit = driver.find_elements(*self.sending_confirmation_element)
            if submit == []:
                # 没有確定送信,点击保存
                ElementUtil.click(self, driver, 15, text, *self.saving_element)
            else:
                submit[0].click()
            # 获取返回值
            sleep(0.5)
            ship_air_company_text = ElementUtil.getText(self, driver, 15, text, *self.ship_air_company_value_element)
            expect = "船社・航空会社必要である"
            if expect == ship_air_company_text:
                return True
        except Exception as e:
            return e

    def no_customs_broker(self, driver, text):
        """不填写通関業者"""
        # 点击SA登录
        # sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # 点击新规
        ElementUtil.click(self, driver, 15, text, *self.newlyBuilt_element)
        # 点击INV P/L情报下 追加
        ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        # 输入I/V NO
        ElementUtil.send_keys(self, driver, 15, IV_NO.yj_randoms().get('invoiceNo'), text, *self.IV_NO_element)
        # 点击IV List下 検索
        sleep(0.5)
        ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        # IV List下 选择数据
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.choose_data_element)
        # Browser(driver, 15).choice_check_box(self.choose_click_element)
        # 点击IV List下 追加
        ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        # 输入Master B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(10000, 99999), text, *self.Master_BL_NO_element)
        # 输入House B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(99999, 999999), text, *self.House_BL_NO_element)
        # 选择依赖日
        choose_date(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        # 选择B/L発行日
        choose_date(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        # 选择ETA
        choose_date(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        # 輸出通関日
        choose_date(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        # 根据輸送形態选择積み方
        sleep(0.5)
        transport_text = ElementUtil.getText(self, driver, 15, text, *self.transport_mode_element)
        # print(transport_text)
        if transport_text == "SEA":
            ElementUtil.send_keys(self, driver, 15, Keys.SPACE, text, *self.loading_method_element)
            sleep(0.5)
            element_SEA = driver.find_elements(*self.loading_method_choice_elements)
            choice(element_SEA).click()
            # 判断積み方选择
            sleep(0.5)
            element_text = ElementUtil.getText(self, driver, 15, text, *self.loading_method_get_element)
            # print(element_text)
            if element_text == 'FCL':
                container_NO = driver.find_elements(*self.container_NO_element)
                container_size = driver.find_elements(*self.container_size_element)
                for no in range(len(container_NO)):
                    container_NO[no].send_keys('container No')
                    container_size[no].click()
                    sleep(0.5)
                    element_container_size = driver.find_elements(*self.container_size_choice_element)
                    choice(element_container_size).click()
                    # 識別番号
                    element_PID = driver.find_elements(*self.PID_element)
                    element_PID[no].send_keys('666')
            # 回到顶部
            driver.execute_script("window.scrollTo(0,0)")
            # 本船名
            ElementUtil.send_keys(self, driver, 15, 'shipsname', text, *self.ships_name_element)
            # VOYAGE NO
            ElementUtil.send_keys(self, driver, 15, 'vo1001', text, *self.VOYAGE_NO_element)
        if transport_text == 'AIR':
            # フライトNO
            ElementUtil.send_keys(self, driver, 15, 'No0003', text, *self.flying_No_element)
        # 选择船社・航空会社
        ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
        sleep(0.5)
        element_group = driver.find_elements(*self.shipping_co_choice_element)
        choice(element_group).click()
        # S/I NO
        ElementUtil.send_keys(self, driver, 15, 'si1122', text, *self.SI_NO_element)
        # 貨物タイプ
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.cargo_type_element)
        sleep(0.5)
        element_cargo = driver.find_elements(*self.cargo_type_choice_element)
        choice(element_cargo).click()

        # 回到顶部
        driver.execute_script("window.scrollTo(0,0)")

        # 点击一時保存
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # 点击弹框确定
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        try:
            # 点击確定送信
            sleep(0.5)
            submit = driver.find_elements(*self.sending_confirmation_element)
            if submit == []:
                # 没有確定送信,点击保存
                ElementUtil.click(self, driver, 15, text, *self.saving_element)
            else:
                submit[0].click()
            # 获取返回值
            sleep(0.5)
            customs_broker_text = ElementUtil.getText(self, driver, 15, text, *self.customs_broker_value_element)
            expect = "通関業者必要である"
            if expect == customs_broker_text:
                return True
        except Exception as e:
            return e

    def no_cargo_type(self, driver, text):
        """不填写貨物タイプ"""
        # 点击SA登录
        # sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # 点击新规
        ElementUtil.click(self, driver, 15, text, *self.newlyBuilt_element)
        # 点击INV P/L情报下 追加
        ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        # 输入I/V NO
        ElementUtil.send_keys(self, driver, 15, IV_NO.yj_randoms().get('invoiceNo'), text, *self.IV_NO_element)
        # 点击IV List下 検索
        sleep(0.5)
        ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        # IV List下 选择数据
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.choose_data_element)
        # Browser(driver, 15).choice_check_box(self.choose_click_element)
        # 点击IV List下 追加
        ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        # 输入Master B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(10000, 99999), text, *self.Master_BL_NO_element)
        # 输入House B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(99999, 999999), text, *self.House_BL_NO_element)
        # 选择依赖日
        choose_date(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        # 选择B/L発行日
        choose_date(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        # 选择ETA
        choose_date(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        # 輸出通関日
        choose_date(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        # 根据輸送形態选择積み方
        sleep(0.5)
        transport_text = ElementUtil.getText(self, driver, 15, text, *self.transport_mode_element)
        # print(transport_text)
        if transport_text == "SEA":
            ElementUtil.send_keys(self, driver, 15, Keys.SPACE, text, *self.loading_method_element)
            sleep(0.5)
            element_SEA = driver.find_elements(*self.loading_method_choice_elements)
            choice(element_SEA).click()
            # 判断積み方选择
            sleep(0.5)
            element_text = ElementUtil.getText(self, driver, 15, text, *self.loading_method_get_element)
            # print(element_text)
            if element_text == 'FCL':
                container_NO = driver.find_elements(*self.container_NO_element)
                container_size = driver.find_elements(*self.container_size_element)
                for no in range(len(container_NO)):
                    container_NO[no].send_keys('container No')
                    container_size[no].click()
                    sleep(0.5)
                    element_container_size = driver.find_elements(*self.container_size_choice_element)
                    choice(element_container_size).click()
                    # 識別番号
                    element_PID = driver.find_elements(*self.PID_element)
                    element_PID[no].send_keys('666')
            # 回到顶部
            driver.execute_script("window.scrollTo(0,0)")
            # 本船名
            ElementUtil.send_keys(self, driver, 15, 'shipsname', text, *self.ships_name_element)
            # VOYAGE NO
            ElementUtil.send_keys(self, driver, 15, 'vo1001', text, *self.VOYAGE_NO_element)
        if transport_text == 'AIR':
            # フライトNO
            ElementUtil.send_keys(self, driver, 15, 'No0003', text, *self.flying_No_element)
        # 选择船社・航空会社
        ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
        sleep(0.5)
        element_group = driver.find_elements(*self.shipping_co_choice_element)
        choice(element_group).click()
        # S/I NO
        ElementUtil.send_keys(self, driver, 15, 'si1122', text, *self.SI_NO_element)
        # 通関業者
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.customs_broker_element)
        sleep(0.5)
        element_customs = driver.find_elements(*self.customs_broker_choice_element)
        choice(element_customs).click()

        # 回到顶部
        driver.execute_script("window.scrollTo(0,0)")

        # 点击一時保存
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # 点击弹框确定
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        try:
            # 点击確定送信
            sleep(0.5)
            submit = driver.find_elements(*self.sending_confirmation_element)
            if submit == []:
                # 没有確定送信,点击保存
                ElementUtil.click(self, driver, 15, text, *self.saving_element)
            else:
                submit[0].click()
            # 获取返回值
            sleep(0.5)
            cargo_type_text = ElementUtil.getText(self, driver, 15, text, *self.cargo_type_value_element)
            expect = "貨物タイプ必要である"
            if expect == cargo_type_text:
                return True
        except Exception as e:
            return e

    def no_container_NO(self, driver, text):
        """不填写CONTAINER NO"""
        # 点击SA登录
        # sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # 点击新规
        ElementUtil.click(self, driver, 15, text, *self.newlyBuilt_element)
        # 点击INV P/L情报下 追加
        ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        # 输入I/V NO
        ElementUtil.send_keys(self, driver, 15, IV_NO.yj_randoms().get('invoiceNo'), text, *self.IV_NO_element)
        # 点击IV List下 検索
        sleep(0.5)
        ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        # IV List下 选择数据
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.choose_data_element)
        # Browser(driver, 15).choice_check_box(self.choose_click_element)
        # 点击IV List下 追加
        ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        # 输入Master B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(10000, 99999), text, *self.Master_BL_NO_element)
        # 输入House B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(99999, 999999), text, *self.House_BL_NO_element)
        # 选择依赖日
        choose_date(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        # 选择B/L発行日
        choose_date(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        # 选择ETA
        choose_date(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        # 輸出通関日
        choose_date(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        # 改变輸送形態
        sleep(0.5)
        transport_text = ElementUtil.getText(self, driver, 15, text, *self.transport_mode_element)
        # print(transport_text)
        if transport_text == 'AIR':
            # 将輸送形態变为SEA
            ElementUtil.click(self, driver, 15, text, *self.transport_mode_clear_element)
            ElementUtil.send_keys(self, driver, 15, Keys.SPACE, text, *self.transport_mode_after_element)
            ElementUtil.click(self, driver, 15, text, *self.transport_mode_SEA_element)

        # 选择積み方
        ElementUtil.send_keys(self, driver, 15, Keys.SPACE, text, *self.loading_method_element)
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.loading_method_FCL_element)
        # 输入container_size
        container_size = driver.find_elements(*self.container_size_element)
        for no in range(len(container_size)):
            container_size[no].click()
            sleep(0.5)
            element_container_size = driver.find_elements(*self.container_size_choice_element)
            choice(element_container_size).click()
            # 識別番号
            element_PID = driver.find_elements(*self.PID_element)
            element_PID[no].send_keys('666')
        # 回到顶部
        driver.execute_script("window.scrollTo(0,0)")
        # 本船名
        ElementUtil.send_keys(self, driver, 15, 'shipsname', text, *self.ships_name_element)
        # VOYAGE NO
        ElementUtil.send_keys(self, driver, 15, 'vo1001', text, *self.VOYAGE_NO_element)
        # 选择船社・航空会社
        ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
        sleep(0.5)
        element_group = driver.find_elements(*self.shipping_co_choice_element)
        choice(element_group).click()
        # S/I NO
        ElementUtil.send_keys(self, driver, 15, 'si1122', text, *self.SI_NO_element)
        # 通関業者
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.customs_broker_element)
        sleep(0.5)
        element_customs = driver.find_elements(*self.customs_broker_choice_element)
        choice(element_customs).click()
        # 貨物タイプ
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.cargo_type_element)
        sleep(0.5)
        element_cargo = driver.find_elements(*self.cargo_type_choice_element)
        choice(element_cargo).click()

        # 回到顶部
        driver.execute_script("window.scrollTo(0,0)")

        # 点击一時保存
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # 点击弹框确定
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        try:
            # 点击確定送信
            sleep(0.5)
            submit = driver.find_elements(*self.sending_confirmation_element)
            if submit == []:
                # 没有確定送信,点击保存
                ElementUtil.click(self, driver, 15, text, *self.saving_element)
            else:
                submit[0].click()
            # 获取返回值
            sleep(0.5)
            container_text = ElementUtil.getText(self, driver, 15, text, *self.container_value_element)
            expect = "INV P/L情報が不整備です、ご確認お願いします。"
            if expect in container_text:
                return True
        except Exception as e:
            return e

    def no_container_size(self, driver, text):
        """不填写CONTAINER SIZE"""
        # 点击SA登录
        # sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.SA_button_element)
        # 点击新规
        ElementUtil.click(self, driver, 15, text, *self.newlyBuilt_element)
        # 点击INV P/L情报下 追加
        ElementUtil.click(self, driver, 15, text, *self.INV_add_element)
        # 输入I/V NO
        ElementUtil.send_keys(self, driver, 15, IV_NO.yj_randoms().get('invoiceNo'), text, *self.IV_NO_element)
        sleep(0.5)
        # 点击IV List下 検索
        ElementUtil.click(self, driver, 15, text, *self.IV_NO_search_element)
        # IV List下 选择数据
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.choose_data_element)
        # Browser(driver, 15).choice_check_box(self.choose_click_element)
        # 点击IV List下 追加
        ElementUtil.click(self, driver, 15, text, *self.IV_list_add_element)
        # 输入Master B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(10000, 99999), text, *self.Master_BL_NO_element)
        # 输入House B/L NO
        ElementUtil.send_keys(self, driver, 15, random.randint(99999, 999999), text, *self.House_BL_NO_element)
        # 选择依赖日
        choose_date(driver, self.trust_day_element, self.trust_day_click_element, self.trust_day_month_element)
        # 选择B/L発行日
        choose_date(driver, self.issue_date_element, self.issue_date_click_element, self.issue_month_click_element)
        # 选择ETA
        choose_date(driver, self.ETA_element, self.ETA_click_element, self.ETA_month_clikc_element)
        # 輸出通関日
        choose_date(driver, self.export_declaration_date_element, self.export_declaration_date_click_element,
                    self.export_declaration_month_click_element)
        # 改变輸送形態
        sleep(0.5)
        transport_text = ElementUtil.getText(self, driver, 15, text, *self.transport_mode_element)
        # print(transport_text)
        if transport_text == 'AIR':
            # 将輸送形態变为SEA
            ElementUtil.click(self, driver, 15, text, *self.transport_mode_clear_element)
            ElementUtil.send_keys(self, driver, 15, Keys.SPACE, text, *self.transport_mode_after_element)
            ElementUtil.click(self, driver, 15, text, *self.transport_mode_SEA_element)
        # 选择積み方
        ElementUtil.send_keys(self, driver, 15, Keys.SPACE, text, *self.loading_method_element)
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.loading_method_FCL_element)
        # 输入container_NO
        container_NO = driver.find_elements(*self.container_NO_element)
        for no in range(len(container_NO)):
            container_NO[no].send_keys('container No')
            # 識別番号
            element_PID = driver.find_elements(*self.PID_element)
            element_PID[no].send_keys('666')
        # 回到顶部
        driver.execute_script("window.scrollTo(0,0)")
        # 本船名
        ElementUtil.send_keys(self, driver, 15, 'shipsname', text, *self.ships_name_element)
        # VOYAGE NO
        ElementUtil.send_keys(self, driver, 15, 'vo1001', text, *self.VOYAGE_NO_element)
        # 选择船社・航空会社
        ElementUtil.click(self, driver, 15, text, *self.shipping_co_element)
        sleep(0.5)
        element_group = driver.find_elements(*self.shipping_co_choice_element)
        choice(element_group).click()
        # S/I NO
        ElementUtil.send_keys(self, driver, 15, 'si1122', text, *self.SI_NO_element)
        # 通関業者
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.customs_broker_element)
        sleep(0.5)
        element_customs = driver.find_elements(*self.customs_broker_choice_element)
        choice(element_customs).click()
        # 貨物タイプ
        ElementUtil.send_keys(self, driver, 15, Keys.ENTER, text, *self.cargo_type_element)
        sleep(0.5)
        element_cargo = driver.find_elements(*self.cargo_type_choice_element)
        choice(element_cargo).click()

        # 回到顶部
        driver.execute_script("window.scrollTo(0,0)")

        # 点击一時保存
        ElementUtil.click(self, driver, 15, text, *self.temporary_saving_element)
        # 点击弹框确定
        sleep(1)
        ElementUtil.click(self, driver, 15, text, *self.confirm_button_element)
        try:
            # 点击確定送信
            sleep(0.5)
            submit = driver.find_elements(*self.sending_confirmation_element)
            if submit == []:
                # 没有確定送信,点击保存
                ElementUtil.click(self, driver, 15, text, *self.saving_element)
            else:
                submit[0].click()
            # 获取返回值
            sleep(0.5)
            container_text = ElementUtil.getText(self, driver, 15, text, *self.container_value_element)
            expect = "INV P/L情報が不整備です、ご確認お願いします。"
            if expect in container_text:
                return True
        except Exception as e:
            return e


if __name__ == '__main__':
    url = "https://sharpsit.jusdaglobal.com"
    driver = webdriver.Chrome()
    driver.get(url)
    # driver.maximize_window()
    login = Login()
    login.test_click_login_btn(driver)
    field = RequiredField()
    text = "1234"
    # field.no_requested_date(driver)
    # field.no_issue_date(driver)
    # field.no_ETA(driver)
    # field.no_loading_method(driver)
    # field.no_export_declaration_date(driver)
    # field.no_ship_air_company(driver)
    # field.no_customs_broker(driver)
    # field.no_cargo_type(driver)
    field.no_container_NO(driver, text)
    # field.no_container_size(driver)
