# encoding=utf-8

'''新建Shipping Advice数据，修改Carton Start No
和Carton end No'''
from util.ElementUtil import ElementUtil
from selenium import webdriver
from pageElement.customs.AddCost import AddCost,NewlyBuildElement
from business.Login import Login
from time import sleep
import random
from util.element_exits import isElementExist
from business.test_customs.NewData import NewData
from selenium.webdriver.common.keys import Keys

class ModifyNo(AddCost,NewlyBuildElement):


    def modifyNo(self,driver):
        '''新建Shipping Advice数据，修改Carton Start No和Carton end No
        '''

        #登录
        elUtil = ElementUtil()

        #进入首页S/A登录
        elUtil.click(driver,5,'S/A登录',*self.SAElement)
        sleep(1.5)

        #点击新规
        elUtil.click(driver,30,'点击新规', *self.newRuleElement)
        sleep(1.5)

        #点击INV P/L信息中的追加
        elUtil.click(driver,30,'INV P/L信息中的追加', *self.addElement)
        sleep(2)

        #点击对话框的搜索
        elUtil.click(driver,30, '对话框的搜索',*self.dialogSearchElement)
        sleep(2)

        #点击对话框第一条数据
        elUtil.click(driver,30,'点击对话框第一条数据' ,*self.firstDataElement)
        sleep(2)

        #点击对话框追加
        elUtil.click(driver,30,'点击对话框追加', *self.dialogAddElement)
        sleep(2)

        #定位Carton End No 输入内容
        elUtil.clear(driver,5,'清除Carton End No内容',*self.Carton_end_No_element)
        elUtil.send_keys(driver,5,1000,'输入值',*self.Carton_end_No_element)
        sleep(1.5)

        temp = driver.find_element(*self.temporary_saving_element)
        driver.execute_script("arguments[0].click();",temp)
        elUtil.click(driver,5,'将光标移开',*self.PID_element) #将光标移动到其他地方去
        endNo = driver.find_element(*self.Carton_end_No_element).get_attribute('value')
        endNo = int(endNo)
        sleep(2)

        #定位start No
        startNo = driver.find_element(*self.Carton_start_No_element).get_attribute('value')
        startNo = int(startNo)
        sleep(2)

        #定位Shipped Carton
        shippedNo = driver.find_element(*self.shipped_Carton_element).get_attribute('value')
        shippedNo = int(shippedNo)
        sleep(2)
        return[startNo,endNo,shippedNo]

    def sendMessage(self,driver):
        '''送信成功'''

        elUtil  = ElementUtil()
        new = NewData()

        #获取masterNO和HouseNO
        Master_BL_NO,House_BL_NO = new.create_data(driver)

        #输入Master B/L NO清除
        # elUtil.clear(driver,5,*self.master_no_element)
        elUtil.send_keys(driver,5,Master_BL_NO,'输入Master B/L NO',*self.master_no_element)

        # 输入House NO清除
        # elUtil.clear(driver,30, *self.house_no_element)
        elUtil.send_keys(driver,30, House_BL_NO, '输入House NO',*self.house_no_element)

        # 点击搜索
        elUtil.click(driver,30, '搜索',*self.searchElement)
        sleep(3)

        # 选择表第一条数据
        # driver.execute_script("arguments[0].click();", *self.fistCheckElement)
        # driver.find_element(*self.fistCheckElement).send_keys(Keys.SPACE)
        elUtil.send_keys(driver,5,Keys.SPACE,'勾选第一条数据',*self.fistCheckElement)
        # elUtil.click(driver,30, *self.fistCheckElement)
        sleep(1.5)

        # 点击编辑
        elUtil.click(driver,30, '编辑',*self.editElement)
        sleep(1.5)


        '''masterNo'''
        Master_BL_NO_text = driver.find_element(*self.Master_BL_NO_element).get_attribute('value')
        if len(Master_BL_NO_text)==0:
            elUtil.send_keys(driver,30,random.randint(100000,999990), '输入masterNo',*self.Master_BL_NO_element)
            sleep(1.5)

        # HourseNo
        House_BL_NO_text = driver.find_element(*self.House_BL_NO_element).get_attribute('value')
        if len(House_BL_NO_text)==0:
            elUtil.send_keys(driver,30, random.randint(100000, 999990), '输入HourseNo',*self.House_BL_NO_element)
            sleep(1.5)

        #点击依赖日
        trust_day_text = driver.find_element(*self.trust_day_element).get_attribute('value')
        if len(trust_day_text) == 0:
            elUtil.click(driver,30, '点击依赖日',*self.trust_day_element)
            sleep(1.5)
            #点击依赖日
            elUtil.click(driver,30, '依赖日',*self.trust_day_click_element)
            sleep(1.5)

        # B/L発行日
        issue_date_text = driver.find_element(*self.issue_date_element).get_attribute('value')
        if len(issue_date_text) == 0:
            elUtil.click(driver,30, 'B/L発行日',*self.issue_date_element)
            sleep(1.5)
            elUtil.click(driver,5,'B/L発行日',*self.issue_month_click_element)
            sleep(1.5)
            #确定B/L発行日
            elUtil.click(driver,30,'B/L発行日', *self.issue_date_click_element)
            sleep(1.5)

        # 输送形态
        convey_text = driver.find_element(*self.conveyElement).get_attribute('value')
        if convey_text =='AIR':
            elUtil.click(driver,30, '输送形态',*self.conveyElement)
            elUtil.click(driver,30, '选择SEA',*self.seaElement)

        #点击積み方
        loading_method_el = isElementExist(driver,self.loading_method_element)
        if loading_method_el == True:
            global loading_method_text
            loading_method_text = driver.find_element(*self.loading_method_element).get_attribute('value')
            print(loading_method_text)
            if loading_method_text  in 'FCL LCL':
                #点击積み方
                loading_method = driver.find_element(*self.loading_method_element)
                driver.execute_script("arguments[0].click();", loading_method)
                sleep(1.5)
                # 填写B積み方
                loading_method_choice = driver.find_element(*self.loading_method_choice_elements)
                driver.execute_script("arguments[0].click();", loading_method_choice)
                sleep(1.5)

        # 点击ETD
        ETD_text = driver.find_element(*self.ETD_element).get_attribute('value')
        if len(ETD_text)==0:
            elUtil.click(driver,30, '点击ETD',*self.ETD_element)
            sleep(1.5)
            elUtil.click(driver,30, 'ETD',*self.ETD_month_clikc_element)
            sleep(1.5)
            elUtil.click(driver,30, '选择ETD',*self.ETD_click_element)
            sleep(1.5)

        #点击ETA
        ETA_text=driver.find_element(*self.ETA_element).get_attribute('value')
        if len(ETA_text)==0:
            elUtil.click(driver,30, '点击ETA',*self.ETA_element)
            sleep(1.5)
            elUtil.click(driver,30, '选择ETA',*self.ETA_click_element)
            sleep(1.5)


        #输出通关日
        export_declaration_date_text = driver.find_element(*self.export_declaration_date_element).get_attribute('value')
        if len(export_declaration_date_text)==0:
            elUtil.click(driver,30, '输出通关日',*self.export_declaration_date_element)
            sleep(1.5)
            elUtil.click(driver,30, '选择输出通关日',*self.export_declaration_date_click_element)
            sleep(1.5)

        #船社航空社
        shipping_co_text = driver.find_element(*self.shipping_co_element).get_attribute('value')
        if len(shipping_co_text)==0:
            elUtil.click(driver,30, '点击船社航空社',*self.shipping_co_element)
            sleep(1.5)
            elUtil.click(driver,30, '选择船社航空社',*self.shipping_co_choice_element)
            sleep(2)

        #本船名
        ships_name_text = driver.find_element(*self.ships_name_element).get_attribute('value')
        if len(ships_name_text)==0:
            elUtil.send_keys(driver,30,random.randint(10000,99999), '输入本船名',*self.ships_name_element)
            sleep(2)

        #VOYAGE NO
        VOYAGE_NO_text = driver.find_element(*self.VOYAGE_NO_element).get_attribute('value')
        if len(VOYAGE_NO_text)==0:
            elUtil.send_keys(driver,30,random.randint(10000,99999),'输入VOYAGE NO', *self.VOYAGE_NO_element)
            sleep(2)

        #S/I no
        SI_NO_text = driver.find_element(*self.SI_NO_element).get_attribute('value')
        if len(SI_NO_text)==0:
            elUtil.send_keys(driver,30,random.randint(10000,99999), '输入S/I no',*self.SI_NO_element)
            sleep(2)

        #通关者
        customs_broker_text = driver.find_element(*self.customs_broker_element).get_attribute('value')
        if len(customs_broker_text)==0:
            elUtil.click(driver,30,'点击通关者', *self.customs_broker_element)
            sleep(2)
            elUtil.click(driver,30, '选择通关者',*self.customs_broker_choice_element)
            sleep(2)

        #货物
        cargo_type_text = driver.find_element(*self.cargo_type_element).get_attribute('value')
        if len(cargo_type_text)==0:
            elUtil.click(driver,30,'点击货物', *self.cargo_type_element)
            sleep(2)
            elUtil.click(driver,30,'选择货物', *self.cargo_type_choice_element)
            sleep(2)


        # CONTAINER NO输入框
        container_NO_el = isElementExist(driver,self.container_NO_element)
        if container_NO_el == True:
            container_NO_text = driver.find_element(*self.container_NO_element).get_attribute('value')
            if len(container_NO_text)==0:
                # elUtil.clear(driver,30, *self.container_NO_element)
                elUtil.send_keys(driver,30, random.randint(1000000, 9999999), '输入CONTAINER NO',*self.container_NO_element)
                sleep(1.5)

            # CONTAINER SIZE
            container_size_text = driver.find_element(*self.container_size_element).get_attribute('value')
            if len(container_size_text)==0:
                elUtil.click(driver,30,'点击CONTAINER SIZE', *self.container_size_element)
                sleep(1.5)
                elUtil.click(driver,30, '选择CONTAINER SIZE',*self.container_size_choice_element)
                sleep(1.5)

        # 識別番号
        PID_text = driver.find_element(*self.PID_element).get_attribute('value')
        if len(PID_text)==0:
            # elUtil.clear(driver,30, *self.PID_element)
            elUtil.send_keys(driver,30, random.randint(1000000, 9999999),'输入識別番号' *self.PID_element)
            sleep(1.5)
        try:
            #确定发送
            sending_confirmation_el = driver.find_element(*self.sending_confirmation_element)
            driver.execute_script("arguments[0].click();", sending_confirmation_el)
            sleep(1.5)
            elUtil.click(driver,30, '确定送信',*self.sure_button_element)
            sleep(1.5)
            repet_flag = isElementExist(driver,self.repet_element)  #重复提交
            success_flag = isElementExist(driver,self.successElement)   #送信成功
            incomplete_flag = isElementExist(driver,self.incompleteElement) #信息不完整
            text = None
            if success_flag == True:
                text = driver.find_element(*self.successElement).get_attribute('innerHTML')
            elif repet_flag == True:
                text = driver.find_element(*self.repet_element).get_attribute('innerHTML')
            elif incomplete_flag ==True:
                text = driver.find_element(*self.incompleteElement).get_attribute('innerHTML')
            confirm_el = driver.find_element(*self.confirm_element)
            driver.execute_script("arguments[0].click();", confirm_el)
            sleep(1.5)
        except Exception as e:
                print(e)
        else:
            return text


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://sharpsit.jusdaglobal.com/')
    login = Login()
    login.test_click_login_btn(driver)
    sleep(5)
    c = ModifyNo()
    print(c.modifyNo(driver))