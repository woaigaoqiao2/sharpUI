from pageElement.customs.NewBuilt import NewBuiltElement,NewlyBuildElement
from time import sleep
from util.element_exits import isElementExist
from business.Login import Login
from selenium import webdriver
import random
from util.ElementUtil import ElementUtil
from util.interface_data import demo
from business.test_customs.NewData import NewData

class NewBuilt(NewBuiltElement,NewlyBuildElement):


    def newBuiltLoadPort(self,driver):
        '''新建运港不同的数据'''

        elUtil = ElementUtil()  #
        d = demo()

        # 进入首页S/A登录     创建一条数据数据，修改装运港
        elUtil.click(driver,30,'进入首页S/A登录', *self.SAElement)
        sleep(1.5)

        # 点击新規按钮
        elUtil.click(driver,30, '点击新規按钮',*self.newRuleElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver,30,'点击INV P/L情報下追加按钮', *self.addElement)
        sleep(1.5)

        # 获取新数据
        r_data1 = d.test().get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver,30,'清除invoiceNo', *self.IVNoElement)
        elUtil.send_keys(driver,30, r_data1,'输入invoiceNo', *self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30,'点击搜索', *self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30, '勾选第一条数据',*self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30,'点击对话框追加', *self.dialogAddElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver,30, '点击INV P/L情報下追加按钮',*self.addElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30, '点击对话框追加',*self.dialogAddElement)
        sleep(1.5)

        #弹框提示不一致
        text = driver.find_element(*self.inconformityElement).text
        return text

    def newBuiltToPort(self,driver):
        '''新建陆扬港不同的数据'''

        elUtil = ElementUtil()  #
        d = demo()

        # 进入首页S/A登录     创建一条数据数据，修改装运港
        elUtil.click(driver,30, '进入首页S/A登录', *self.SAElement)
        sleep(1.5)

        # 点击新規按钮
        elUtil.click(driver,30, '点击新規按钮', *self.newRuleElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver,30, '点击INV P/L情報下追加按钮', *self.addElement)
        sleep(1.5)

        # 获取新数据
        r_data1 = d.test().get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver,30, '清除invoiceNo', *self.IVNoElement)
        elUtil.send_keys(driver,30, r_data1, '输入invoiceNo', *self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索', *self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30, '勾选第一条数据', *self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30, '点击对话框追加', *self.dialogAddElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver,30, '点击INV P/L情報下追加按钮', *self.addElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30, '点击对话框追加', *self.dialogAddElement)
        sleep(1.5)

        # 弹框提示不一致
        text = driver.find_element(*self.inconformityElement).text
        return text

    def newBuiltStartGreaterEnd(self,driver):
        '''start>end'''

        elUtil = ElementUtil()  #

        # 进入首页S/A登录
        elUtil.click(driver,30, '进入首页S/A登录',*self.SAElement)
        sleep(1.5)

        # 点击新規按钮
        elUtil.click(driver,30,'点击新規按钮', *self.newRuleElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver,30,'点击INV P/L情報下追加按钮', *self.addElement)
        sleep(1.5)

        # 输入新数据
        elUtil.clear(driver,30,'输入新数据', *self.IVNoElement)

        # 点击搜索
        elUtil.click(driver,30,'点击搜索', *self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        table = driver.find_element(*self.dialogContentElement)
        rows = table.find_elements_by_tag_name('tr')  # 本页数据行数
        rows_checkbox = rows[0].find_elements_by_tag_name('td')[0]  # 表格第一条
        rows_checkbox.click()   #点击勾选

        # 点击对话框追加
        elUtil.click(driver,30, '点击对话框追加',*self.dialogAddElement)
        sleep(1.5)

        # 判断startNo是否小于endNo,进行修改
        startNo = driver.find_element(*self.startNoElement).get_attribute('value')
        startNo = int(startNo)
        endNo = driver.find_element(*self.endNoElement).get_attribute('value')
        endNo = int(endNo)
        if startNo <= endNo:
            elUtil.clear(driver,5,'清除startNo',*self.startNoElement)
            elUtil.send_keys(driver,5,1000,'输入startNo',*self.startNoElement)    #修改startno
        modify_startno = driver.find_element(*self.startNoElement).get_attribute('value')
        # 点击临时保存
        temp = driver.find_element(*self.temporary_saving_element)
        driver.execute_script("arguments[0].click();", temp)
        sleep(2)

        # 比较修改前与修改后的startNo是否相等
        modify_after_startno = driver.find_element(*self.startNoElement).get_attribute('value')
        # print(startNo1,startNo)
        flag = None
        if modify_after_startno == modify_startno:
            flag = False
        return flag

    def newBuiltCancel(self,driver):
        '''新建取消'''
        elUtil = ElementUtil()  #

        # 进入首页S/A登录
        elUtil.click(driver,30, '进入首页S/A登录', *self.SAElement)
        sleep(1.5)

        # 点击新規按钮
        elUtil.click(driver,30, '点击新規按钮', *self.newRuleElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver,30, '点击INV P/L情報下追加按钮', *self.addElement)
        sleep(1.5)

        # 输入新数据
        elUtil.clear(driver,30, '输入新数据', *self.IVNoElement)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索', *self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        table = driver.find_element(*self.dialogContentElement)
        rows = table.find_elements_by_tag_name('tr')  # 本页数据行数
        rows_checkbox = rows[0].find_elements_by_tag_name('td')[0]  # 表格第一条
        rows_checkbox.click()  # 点击勾选

        # 点击对话框追加
        elUtil.click(driver,30,'追加', *self.dialogAddElement)
        sleep(1.5)

        '''masterNo'''
        Master_BL_NO_text = driver.find_element(*self.Master_BL_NO_element).get_attribute('value')
        if len(Master_BL_NO_text)==0:
            global Master_BL_NO
            Master_BL_NO = random.randint(100000,999990)
            elUtil.send_keys(driver,30,Master_BL_NO, '输入masterNo',*self.Master_BL_NO_element)
            sleep(1.5)

        # HourseNo
        House_BL_NO_text = driver.find_element(*self.House_BL_NO_element).get_attribute('value')
        if len(House_BL_NO_text)==0:
            global House_BL_NO
            House_BL_NO = random.randint(100000, 999990)
            elUtil.send_keys(driver,30,House_BL_NO , '输入HourseNo',*self.House_BL_NO_element)
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

        #点击取消
        elUtil.click(driver,30, '点击取消',*self.return_element)
        sleep(1.5)

        # 输入Master B/L NO清除
        masterNo = None
        if len(Master_BL_NO_text)==0 :
            masterNo = Master_BL_NO
        else:
            masterNo = Master_BL_NO_text
        elUtil.send_keys(driver,30, masterNo,'输入masterNo', *self.master_no_element)

        # 输入House NO清除
        houseNo = None
        if len(House_BL_NO_text)==0:
            houseNo = House_BL_NO
        else:
            houseNo = House_BL_NO_text
        elUtil.send_keys(driver,30, houseNo, '输入houseNo',*self.house_no_element)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索',*self.searchElement)
        sleep(3)

        # 表都有哪些数据
        table = driver.find_element(*self.contentElement)
        rows = table.find_elements_by_tag_name('tr')  # 本页数据行数
        empty = rows[0].find_elements_by_tag_name('td')[0].text #返回空数据 No data available
        return empty

    def newBuiltReferLoadPort(self,driver):
        '''以前追加装运港不同的数据'''
        try:

            elUtil = ElementUtil()  #
            d = demo()

            # 进入首页S/A登录     创建一条数据数据，修改装运港
            elUtil.click(driver,30, '进入首页S/A登录',*self.SAElement)
            sleep(1.5)

            # 点击新規按钮
            elUtil.click(driver,30, '点击新規按钮',*self.newRuleElement)
            sleep(1.5)

            # 点击INV P/L情報下追加按钮
            elUtil.click(driver,30, '点击INV P/L情報下追加按钮',*self.addElement)
            sleep(1.5)

            # 获取新数据
            r_data = d.test().get('invoiceNo')

            # 输入新数据
            elUtil.clear(driver,30, '清除数据',*self.IVNoElement)
            elUtil.send_keys(driver,30, r_data, '输入新数据',*self.IVNoElement)
            sleep(1.5)

            # 点击搜索
            elUtil.click(driver,30, '点击搜索',*self.dialogSearchElement)
            sleep(1.5)

            # 勾选第一条数据
            elUtil.click(driver,30, '勾选第一条数据',*self.firstDataElement)
            sleep(1.5)

            # 点击对话框追加
            elUtil.click(driver,30, '点击对话框追加',*self.dialogAddElement)
            sleep(1.5)

            '''masterNo'''
            Master_BL_NO_text = driver.find_element(*self.Master_BL_NO_element).get_attribute('value')
            if len(Master_BL_NO_text) == 0:
                elUtil.send_keys(driver,30, random.randint(100000, 999990),'masterNo', *self.Master_BL_NO_element)
                global Master_BL_NO
                Master_BL_NO = driver.find_element(*self.Master_BL_NO_element).get_attribute('value')
                sleep(1.5)

            # HourseNo
            House_BL_NO_text = driver.find_element(*self.House_BL_NO_element).get_attribute('value')
            if len(House_BL_NO_text) == 0:
                # elUtil.clear(driver,30, *self.House_BL_NO_clear_element)
                elUtil.send_keys(driver,30, random.randint(100000, 999990),'HourseNo', *self.House_BL_NO_element)
                global House_BL_NO
                House_BL_NO = driver.find_element(*self.House_BL_NO_element).get_attribute('value')
                sleep(1.5)

            # 输送形态
            convey_text = driver.find_element(*self.conveyElement).get_attribute('value')
            if convey_text == 'AIR':
                elUtil.click(driver,30,'输送形态', *self.conveyElement)
                elUtil.click(driver,30, 'SEA',*self.seaElement)

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

            # 修改積出港数据
            elUtil.click(driver,30, '積出港数据',*self.loading_port_element)
            elUtil.click(driver,30, '选择積出港数据',*self.loading_port_choice_elements)
            sleep(1.5)
            # 点击临时保存
            tempSaveEl = driver.find_element(*self.temporary_saving_element)
            driver.execute_script("arguments[0].click();", tempSaveEl)
            sleep(1.5)

            # 点击 弹框确定按钮
            tempEnsureEl = driver.find_element(*self.confirm_button_element)
            driver.execute_script("arguments[0].click();", tempEnsureEl)
            sleep(1.5)

            # 点击 取消
            conreturn_el = driver.find_element(*self.return_element)
            driver.execute_script("arguments[0].click();", conreturn_el)
            sleep(1.5)

            # 输入Master B/L NO清除
            # elUtil.clear(driver,30, *self.master_no_element)
            elUtil.send_keys(driver,30, Master_BL_NO,'输入Master B/L NO', *self.master_no_element)

            # 输入House NO清除
            # elUtil.clear(driver,30, *self.house_no_element)
            elUtil.send_keys(driver,30, House_BL_NO, '输入House NO',*self.house_no_element)

            # 点击搜索
            elUtil.click(driver,30, '点击搜索',*self.searchElement)
            sleep(1.5)

            # 选择表第一条数据
            elUtil.click(driver,30, '选择表第一条数据',*self.fistCheckElement)
            sleep(1.5)

            # 点击参考制作
            elUtil.click(driver,30,'点击参考制作', *self.referMakeElement)
            sleep(1.5)

            # 点击追加
            elUtil.click(driver,30,'点击追加', *self.addElement)
            sleep(1.5)

            # 获取新数据
            r_data = d.test().get('invoiceNo')

            # 输入新数据
            elUtil.clear(driver,30,'清除新数据', *self.IVNoElement)
            elUtil.send_keys(driver,30, r_data, '输入新数据',*self.IVNoElement)
            sleep(1.5)

            # 点击搜索
            elUtil.click(driver,30, '点击搜索',*self.dialogSearchElement)
            sleep(1.5)

            # 勾选第一条数据
            elUtil.click(driver,30, '勾选第一条数据',*self.firstDataElement)
            sleep(1.5)

            # 点击对话框追加
            elUtil.click(driver,30, '点击对话框追加',*self.dialogAddElement)
            sleep(1.5)

            # 弹框提示不一致
            text = driver.find_element(*self.inconformityElement).get_attribute('innerHTML')
            sleep(2)
        except Exception:
            print('')
        else:
            return text

    def newBuiltReferToPort(self,driver):
        '''以前追加装运港不同的数据'''

        elUtil = ElementUtil()  #
        d = demo()

        # 进入首页S/A登录     创建一条数据数据，修改装运港
        elUtil.click(driver,30, '进入首页S/A登录', *self.SAElement)
        sleep(1.5)

        # 点击新規按钮
        elUtil.click(driver,30, '点击新規按钮', *self.newRuleElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver,30, '点击INV P/L情報下追加按钮', *self.addElement)
        sleep(1.5)

        # 获取新数据
        r_data = d.test().get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver,30, '清除数据', *self.IVNoElement)
        elUtil.send_keys(driver,30, r_data, '输入新数据', *self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索', *self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30, '勾选第一条数据', *self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30, '点击对话框追加', *self.dialogAddElement)
        sleep(1.5)

        '''masterNo'''
        Master_BL_NO_text = driver.find_element(*self.Master_BL_NO_element).get_attribute('value')
        if len(Master_BL_NO_text) == 0:
            elUtil.send_keys(driver,30, random.randint(100000, 999990), 'masterNo', *self.Master_BL_NO_element)
            global Master_BL_NO
            Master_BL_NO = driver.find_element(*self.Master_BL_NO_element).get_attribute('value')
            sleep(1.5)

        # HourseNo
        House_BL_NO_text = driver.find_element(*self.House_BL_NO_element).get_attribute('value')
        if len(House_BL_NO_text) == 0:
            # elUtil.clear(driver,30, *self.House_BL_NO_clear_element)
            elUtil.send_keys(driver,30, random.randint(100000, 999990), 'HourseNo', *self.House_BL_NO_element)
            global House_BL_NO
            House_BL_NO = driver.find_element(*self.House_BL_NO_element).get_attribute('value')
            sleep(1.5)

        # 输送形态
        convey_text = driver.find_element(*self.conveyElement).get_attribute('value')
        if convey_text == 'AIR':
            elUtil.click(driver,30, '输送形态', *self.conveyElement)
            elUtil.click(driver,30, 'SEA', *self.seaElement)

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

        # 修改陆扬港数据
        elUtil.click(driver,30, '修改陆扬港数据',*self.loading_port_clear_element)
        sleep(1.5)

        # 点击临时保存
        tempSaveEl = driver.find_element(*self.temporary_saving_element)
        driver.execute_script("arguments[0].click();", tempSaveEl)
        sleep(1.5)

        # 点击 弹框确定按钮
        tempEnsureEl = driver.find_element(*self.confirm_button_element)
        driver.execute_script("arguments[0].click();", tempEnsureEl)
        sleep(1.5)

        # 点击 取消
        conreturn_el = driver.find_element(*self.return_element)
        driver.execute_script("arguments[0].click();", conreturn_el)
        sleep(1.5)

        # 输入Master B/L NO清除
        # elUtil.clear(driver,30, *self.master_no_element)
        elUtil.send_keys(driver,30, Master_BL_NO, '输入Master B/L NO', *self.master_no_element)

        # 输入House NO清除
        # elUtil.clear(driver,30, *self.house_no_element)
        elUtil.send_keys(driver,30, House_BL_NO, '输入House NO', *self.house_no_element)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索', *self.searchElement)
        sleep(1.5)

        # 选择表第一条数据
        elUtil.click(driver,30, '选择表第一条数据', *self.fistCheckElement)
        sleep(1.5)

        # 点击参考制作
        elUtil.click(driver,30, '点击参考制作', *self.referMakeElement)
        sleep(1.5)

        # 点击追加
        elUtil.click(driver,30, '点击追加', *self.addElement)
        sleep(1.5)

        # 获取新数据
        r_data = d.test().get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver,30, '清除新数据', *self.IVNoElement)
        elUtil.send_keys(driver,30, r_data, '输入新数据', *self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索', *self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30, '勾选第一条数据', *self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30, '点击对话框追加', *self.dialogAddElement)
        sleep(1.5)

        # 弹框提示不一致
        text = driver.find_element(*self.inconformityElement).get_attribute('innerHTML')
        sleep(2)

        return text

    def newBuiltAgoneAdd(self,driver):
        '''以前的数据加新数据'''
        elUtil = ElementUtil()
        new = NewData()
        d = demo()

        # 获取masterNO和HouseNO
        Master_BL_NO, House_BL_NO = new.create_data(driver)

        # 输入Master B/L NO清除
        # elUtil.clear(driver,30, *self.master_no_element)
        elUtil.send_keys(driver,30, Master_BL_NO,'输入Master B/L NO', *self.master_no_element)

        # 输入House NO清除
        # elUtil.clear(driver,30, *self.house_no_element)
        elUtil.send_keys(driver,30, House_BL_NO, '输入House NO',*self.house_no_element)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索',*self.searchElement)
        sleep(1.5)

        # 选择表第一条数据
        elUtil.click(driver,30, '选择表第一条数据',*self.fistCheckElement)
        sleep(1.5)

        #点击参考制作
        elUtil.click(driver,30, '点击参考制作',*self.referMakeElement)
        sleep(1.5)

        #点击追加
        elUtil.click(driver,30, '点击追加',*self.addElement)
        sleep(1.5)

        # 获取新数据
        r_data = d.test().get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver,30, '清除新数据',*self.IVNoElement)
        elUtil.send_keys(driver,30, r_data, '输入新数据',*self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索',*self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30, '勾选第一条数据',*self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30, '点击对话框追加',*self.dialogAddElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30,'勾选第一条数据', *self.firstCheckElement)
        sleep(1.5)

        # 点击分类
        elUtil.click(driver,30, '点击分类',*self.classifyElement)
        sleep(1.5)

        # 修改startNo
        elUtil.clear(driver,30, '清除startNo',*self.refer_startNo)
        qty = random.randint(1, 99)
        elUtil.send_keys(driver,30, qty,'修改startNo', *self.refer_startNo)
        sleep(1.5)

        # 点击取消
        conreturn_el = driver.find_element(*self.return_element)
        driver.execute_script("arguments[0].click();", conreturn_el)
        # elUtil.click(driver,30, *self.return_element)
        sleep(1.5)

        # 输入Master B/L NO清除
        # elUtil.clear(driver,30, *self.master_no_element)
        elUtil.send_keys(driver,30, Master_BL_NO, '输入Master B/L NO',*self.master_no_element)

        # 输入House NO清除
        # elUtil.clear(driver,30, *self.house_no_element)
        elUtil.send_keys(driver,30, House_BL_NO,'输入House NO', *self.house_no_element)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索',*self.searchElement)
        sleep(1.5)

        # 选择表第一条数据
        elUtil.click(driver,30, '选择表第一条数据',*self.fistCheckElement)
        sleep(1.5)

        # 点击参考制作
        elUtil.click(driver,30,'点击参考制作', *self.referMakeElement)
        sleep(1.5)

        # 点击追加
        elUtil.click(driver,30,'点击追加', *self.addElement)
        sleep(1.5)

        # 输入新数据
        elUtil.clear(driver,30,'清除新数据', *self.IVNoElement)
        elUtil.send_keys(driver,30, r_data, '输入新数据',*self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索',*self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30, '勾选第一条数据',*self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30, '点击对话框追加',*self.dialogAddElement)
        sleep(1.5)
        # 获取修改后的数据
        qty2 = driver.find_element(*self.refer_startNo).get_attribute('value')
        print(qty, qty2)

        # 比较修改前和修改后的数据
        flag = None
        if qty != qty2:
            flag = True
        return flag

    def newBuiltUnfilled(self,driver):
        '''必填项一项未填，送信'''
        elUtil = ElementUtil()  #
        d = demo()

        # 进入首页S/A登录     创建一条数据数据，修改装运港
        elUtil.click(driver,30,'', *self.SAElement)
        sleep(1.5)

        # 点击新規按钮
        elUtil.click(driver,30,'', *self.newRuleElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver,30,'', *self.addElement)
        sleep(1.5)

        # 获取新数据
        r_data = d.test().get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver,30, '',*self.IVNoElement)
        elUtil.send_keys(driver,30, r_data, '',*self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30,'', *self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30, '',*self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30,'', *self.dialogAddElement)
        sleep(1.5)

        #点击临时保存
        tempSave=driver.find_element(*self.tempSaveElement)
        driver.execute_script("arguments[0].click();", tempSave)
        sleep(2)

        #获取houseNo必填项信息
        houseNoFill = driver.find_element(*self.newRuleHouseNoFillElement).get_attribute('innerHTML')

        '''masterNo'''
        Master_BL_NO_text = driver.find_element(*self.Master_BL_NO_element).get_attribute('value')
        if len(Master_BL_NO_text) == 0:
            # elUtil.clear(driver,30, *self.Master_BL_NO_clear_element)
            elUtil.send_keys(driver,30, random.randint(100000, 999990), '',*self.Master_BL_NO_element)
            sleep(1.5)

        # HourseNo
        House_BL_NO_text = driver.find_element(*self.House_BL_NO_element).get_attribute('value')
        if len(House_BL_NO_text) == 0:
            # elUtil.clear(driver,30, *self.House_BL_NO_clear_element)
            elUtil.send_keys(driver,30, random.randint(100000, 999990), '',*self.House_BL_NO_element)
            sleep(1.5)

        # 点击依赖日
        trust_day_text = driver.find_element(*self.trust_day_element).get_attribute('value')
        if len(trust_day_text) == 0:
            elUtil.click(driver,30, '',*self.trust_day_element)
            sleep(1.5)
            # 点击依赖日
            elUtil.click(driver,30, '',*self.trust_day_click_element)
            sleep(1.5)

        # B/L発行日
        issue_date_text = driver.find_element(*self.issue_date_element).get_attribute('value')
        if len(issue_date_text) == 0:
            elUtil.click(driver,30,'', *self.issue_date_element)
            sleep(1.5)
            elUtil.click(driver,5,'',*self.issue_month_click_element)
            sleep(1.5)
            # 确定B/L発行日
            elUtil.click(driver,30, '',*self.issue_date_click_element)
            sleep(1.5)

        # 输送形态
        convey_text = driver.find_element(*self.conveyElement).get_attribute('value')
        if convey_text == 'AIR':
            elUtil.click(driver,30, '',*self.conveyElement)
            elUtil.click(driver,30, '',*self.seaElement)

        # 点击積み方
        loading_method_el = isElementExist(driver, self.loading_method_element)
        if loading_method_el == True:
            global loading_method_text
            loading_method_text = driver.find_element(*self.loading_method_element).get_attribute('value')
            print(loading_method_text)
            if loading_method_text in 'FCL LCL':
                # 点击積み方
                loading_method = driver.find_element(*self.loading_method_element)
                driver.execute_script("arguments[0].click();", loading_method)
                sleep(1.5)
                # 填写B積み方
                loading_method_choice = driver.find_element(*self.loading_method_choice_elements)
                driver.execute_script("arguments[0].click();", loading_method_choice)
                sleep(1.5)

        # 点击ETD
        ETD_text = driver.find_element(*self.ETD_element).get_attribute('value')
        if len(ETD_text) == 0:
            elUtil.click(driver,30, '',*self.ETD_element)
            sleep(1.5)
            elUtil.click(driver,30, '',*self.ETD_month_clikc_element)
            sleep(1.5)
            elUtil.click(driver,30, '',*self.ETD_click_element)
            sleep(1.5)

        # 点击ETA
        ETA_text = driver.find_element(*self.ETA_element).get_attribute('value')
        if len(ETA_text) == 0:
            elUtil.click(driver,30, '',*self.ETA_element)
            sleep(1.5)
            elUtil.click(driver,30, '',*self.ETA_click_element)
            sleep(1.5)

        # 输出通关日
        export_declaration_date_text = driver.find_element(*self.export_declaration_date_element).get_attribute('value')
        if len(export_declaration_date_text) == 0:
            elUtil.click(driver,30, '',*self.export_declaration_date_element)
            sleep(1.5)
            elUtil.click(driver,30, '',*self.export_declaration_date_click_element)
            sleep(1.5)

        # 船社航空社
        shipping_co_text = driver.find_element(*self.shipping_co_element).get_attribute('value')
        if len(shipping_co_text) == 0:
            elUtil.click(driver,30, '',*self.shipping_co_element)
            sleep(1.5)
            elUtil.click(driver,30, '',*self.shipping_co_choice_element)
            sleep(2)

        # 本船名
        ships_name_text = driver.find_element(*self.ships_name_element).get_attribute('value')
        if len(ships_name_text) == 0:
            elUtil.clear(driver,30, '',*self.ships_name_element)
            elUtil.send_keys(driver,30, random.randint(10000, 99999),'', *self.ships_name_element)
            sleep(2)

        # VOYAGE NO
        VOYAGE_NO_text = driver.find_element(*self.VOYAGE_NO_element).get_attribute('value')
        if len(VOYAGE_NO_text) == 0:
            elUtil.clear(driver,30, '',*self.VOYAGE_NO_element)
            elUtil.send_keys(driver,30, random.randint(10000, 99999), '',*self.VOYAGE_NO_element)
            sleep(2)

        # S/I no
        SI_NO_text = driver.find_element(*self.SI_NO_element).get_attribute('value')
        if len(SI_NO_text) == 0:
            elUtil.clear(driver,30,'', *self.SI_NO_element)
            elUtil.send_keys(driver,30, random.randint(10000, 99999),'', *self.SI_NO_element)
            sleep(2)

        # 通关者
        customs_broker_text = driver.find_element(*self.customs_broker_element).get_attribute('value')
        if len(customs_broker_text) == 0:
            elUtil.click(driver,30, '',*self.customs_broker_element)
            sleep(2)
            elUtil.click(driver,30, '',*self.customs_broker_choice_element)
            sleep(2)

        # 货物
        cargo_type_text = driver.find_element(*self.cargo_type_element).get_attribute('value')
        if len(cargo_type_text) == 0:
            elUtil.click(driver,30, '',*self.cargo_type_element)
            sleep(2)
            elUtil.click(driver,30,'', *self.cargo_type_choice_element)
            sleep(2)

        # CONTAINER NO输入框
        container_NO_el = isElementExist(driver, self.container_NO_element)
        if container_NO_el == True:
            container_NO_text = driver.find_element(*self.container_NO_element).get_attribute('value')
            if len(container_NO_text) == 0:
                elUtil.clear(driver,30, '',*self.container_NO_element)
                elUtil.send_keys(driver,30, random.randint(1000000, 9999999), '',*self.container_NO_element)
                sleep(1.5)

            # CONTAINER SIZE
            container_size_text = driver.find_element(*self.container_size_element).get_attribute('value')
            if len(container_size_text) == 0:
                elUtil.click(driver,30, '',*self.container_size_element)
                sleep(1.5)
                elUtil.click(driver,30, '',*self.container_size_choice_element)
                sleep(1.5)

        # 識別番号
        PID_text = driver.find_element(*self.PID_element).get_attribute('value')
        if len(PID_text) == 0:
            elUtil.clear(driver,30, '',*self.PID_element)
            elUtil.send_keys(driver,30, random.randint(1000000, 9999999), '',*self.PID_element)
            sleep(1.5)

        # 点击临时保存
        tempSaveEl = driver.find_element(*self.temporary_saving_element)
        driver.execute_script("arguments[0].click();", tempSaveEl)
        sleep(3.5)

        # 点击 弹框确定按钮
        tempEnsureEl = driver.find_element(*self.confirm_button_element)
        driver.execute_script("arguments[0].click();", tempEnsureEl)
        sleep(1.5)

        # 确定发送
        sending_confirmation_el = driver.find_element(*self.sending_confirmation_element)
        driver.execute_script("arguments[0].click();", sending_confirmation_el)
        # sleep(1.5)
        # elUtil.click(driver,30, *self.sure_button_element)
        # sleep(1.5)
        # repet_flag = isElementExist(driver, self.repet_element)  # 重复提交
        # success_flag = isElementExist(driver, self.successElement)  # 送信成功
        # incomplete_flag = isElementExist(driver, self.incompleteElement)  # 信息不完整
        # if success_flag == True:
        #     global text
        #     text = driver.find_element(*self.successElement).get_attribute('innerHTML')
        # elif repet_flag == True:
        #     text = driver.find_element(*self.repet_element).get_attribute('innerHTML')
        # elif incomplete_flag == True:
        #     text = driver.find_element(*self.incompleteElement).get_attribute('innerHTML')
        # confirm_el = driver.find_element(*self.confirm_element)
        # driver.execute_script("arguments[0].click();", confirm_el)
        sleep(1.5)

        return houseNoFill

    def newBuiltModify(self,driver):
        '''修改startNo>endNo'''
        elUtil = ElementUtil()  #

        # 进入首页S/A登录
        elUtil.click(driver,30, '',*self.SAElement)
        sleep(1.5)

        # 点击新規按钮
        elUtil.click(driver,30, '',*self.newRuleElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver,30, '',*self.addElement)
        sleep(1.5)

        # 输入新数据
        elUtil.clear(driver,30, '',*self.IVNoElement)

        # 点击搜索
        elUtil.click(driver,30, '',*self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        table = driver.find_element(*self.dialogContentElement)
        rows = table.find_elements_by_tag_name('tr')  # 本页数据行数
        LoadPort1 = rows[0].find_elements_by_tag_name('td')[2].text  # 装运港内容
        rows[0].find_elements_by_tag_name('td')[0].click()  # 勾选表格第一条

        # 点击对话框追加
        elUtil.click(driver,30, '',*self.dialogAddElement)
        sleep(1.5)

        # 勾选NV P/L信息第一条数据,获取P/O NO,判断startNo是否小于endNo,进行修改
        startNo = driver.find_element(*self.Carton_start_No_element).get_attribute('value')
        sleep(2)
        startNo = int(startNo)

        global startNo1
        endNo = driver.find_element(*self.Carton_end_No_element).get_attribute('value')
        endNo = int(endNo)
        if startNo <= endNo:
            elUtil.clear(driver,5,'',*self.Carton_start_No_element)
            elUtil.send_keys(driver,5,random.randint(1000,9999),'',*self.Carton_start_No_element)
            startNo1 = driver.find_element(*self.Carton_start_No_element).get_attribute('value')
        sleep(1.5)
        elUtil.click(driver,5,'',*self.INVFistCheckElement)
        sleep(1.5)
        shippedNo = int(driver.find_element(*self.shipped_Carton_element).get_attribute('value'))
        flag = None
        if shippedNo <=0:
            flag = False
        return flag

    def newBuiltLetters(self,driver):
        '''參照新規作成，只填写必填项，送信时取消'''
        '''以前的数据加新数据'''
        elUtil = ElementUtil()
        news = NewData()
        d = demo()

        # 获取masterNO和HouseNO
        Master_BL_NO,House_BL_NO = news.create_data(driver)

        # 输入Master B/L NO清除
        elUtil.send_keys(driver,30, Master_BL_NO, '',*self.master_no_element)

        # 输入House NO清除
        elUtil.send_keys(driver,30, House_BL_NO, '',*self.house_no_element)

        # 点击搜索
        elUtil.click(driver,30, '',*self.searchElement)
        sleep(1.5)

        # 选择表第一条数据
        elUtil.click(driver,30, '',*self.fistCheckElement)
        sleep(1.5)

        # 点击参考制作
        elUtil.click(driver,30, '',*self.referMakeElement)
        sleep(1.5)

        # 点击追加
        elUtil.click(driver,30, '',*self.addElement)
        sleep(1.5)

        # 获取新数据
        r_data = d.test().get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver,30, '',*self.IVNoElement)
        elUtil.send_keys(driver,30, r_data, '',*self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30, '',*self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30, '',*self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30, '',*self.dialogAddElement)
        sleep(1.5)

        '''masterNo'''
        Master_BL_NO_text = driver.find_element(*self.Master_BL_NO_element).get_attribute('value')
        if len(Master_BL_NO_text) == 0:
            elUtil.clear(driver,30, '',*self.Master_BL_NO_clear_element)
            elUtil.send_keys(driver,30, random.randint(100000, 999990), '',*self.Master_BL_NO_element)
            sleep(1.5)

        # HourseNo
        House_BL_NO_text = driver.find_element(*self.House_BL_NO_element).get_attribute('value')
        if len(House_BL_NO_text) == 0:
            elUtil.clear(driver,30, *self.House_BL_NO_clear_element)
            elUtil.send_keys(driver,30, random.randint(100000, 999990),'', *self.House_BL_NO_element)
            sleep(1.5)

        # 点击依赖日
        trust_day_text = driver.find_element(*self.trust_day_element).get_attribute('value')
        if len(trust_day_text) == 0:
            elUtil.click(driver,30, '',*self.trust_day_element)
            sleep(1.5)
            # 点击依赖日
            elUtil.click(driver,30,'', *self.trust_day_click_element)
            sleep(1.5)

        # B/L発行日
        issue_date_text = driver.find_element(*self.issue_date_element).get_attribute('value')
        if len(issue_date_text) == 0:
            elUtil.click(driver,30, '',*self.issue_date_element)
            sleep(1.5)
            elUtil.click(driver,30, '',*self.issue_month_click_element)
            sleep(1.5)
            # 确定B/L発行日
            elUtil.click(driver,30, '',*self.issue_date_click_element)
            sleep(1.5)

        # 输送形态
        convey_text = driver.find_element(*self.conveyElement).get_attribute('value')
        if convey_text == 'AIR':
            elUtil.click(driver,30, '',*self.conveyElement)
            elUtil.click(driver,30, '',*self.seaElement)

        # 点击積み方
        loading_method_el = isElementExist(driver, self.loading_method_element)
        if loading_method_el == True:
            global loading_method_text
            loading_method_text = driver.find_element(*self.loading_method_element).get_attribute('value')
            print(loading_method_text)
            if loading_method_text in 'FCL LCL':
                # 点击積み方
                loading_method = driver.find_element(*self.loading_method_element)
                driver.execute_script("arguments[0].click();", loading_method)
                sleep(1.5)
                # 填写B積み方
                loading_method_choice = driver.find_element(*self.loading_method_choice_elements)
                driver.execute_script("arguments[0].click();", loading_method_choice)
                sleep(1.5)

        # 点击ETD
        ETD_text = driver.find_element(*self.ETD_element).get_attribute('value')
        if len(ETD_text) == 0:
            elUtil.click(driver,30, '',*self.ETD_element)
            sleep(1.5)
            elUtil.click(driver,30, '',*self.ETD_month_clikc_element)
            sleep(1.5)
            elUtil.click(driver,30, '',*self.ETD_click_element)
            sleep(1.5)

        # 点击ETA
        ETA_text = driver.find_element(*self.ETA_element).get_attribute('value')
        if len(ETA_text) == 0:
            elUtil.click(driver,30, '',*self.ETA_element)
            sleep(1.5)
            elUtil.click(driver,30, '',*self.ETA_click_element)
            sleep(1.5)

        # 输出通关日
        export_declaration_date_text = driver.find_element(*self.export_declaration_date_element).get_attribute('value')
        if len(export_declaration_date_text) == 0:
            elUtil.click(driver,30, '',*self.export_declaration_date_element)
            sleep(1.5)
            elUtil.click(driver,30, '',*self.export_declaration_date_click_element)
            sleep(1.5)

        # 船社航空社
        shipping_co_text = driver.find_element(*self.shipping_co_element).get_attribute('value')
        if len(shipping_co_text) == 0:
            elUtil.click(driver,30, '',*self.shipping_co_element)
            sleep(1.5)
            elUtil.click(driver,30, '',*self.shipping_co_choice_element)
            sleep(2)

        # 本船名
        ships_name_text = driver.find_element(*self.ships_name_element).get_attribute('value')
        if len(ships_name_text) == 0:
            elUtil.clear(driver,30,'', *self.ships_name_element)
            elUtil.send_keys(driver,30, random.randint(10000, 99999), '',*self.ships_name_element)
            sleep(2)

        # VOYAGE NO
        VOYAGE_NO_text = driver.find_element(*self.VOYAGE_NO_element).get_attribute('value')
        if len(VOYAGE_NO_text) == 0:
            elUtil.clear(driver,30, '',*self.VOYAGE_NO_element)
            elUtil.send_keys(driver,30, random.randint(10000, 99999), '',*self.VOYAGE_NO_element)
            sleep(2)

        # S/I no
        SI_NO_text = driver.find_element(*self.SI_NO_element).get_attribute('value')
        if len(SI_NO_text) == 0:
            elUtil.clear(driver,30, '',*self.SI_NO_element)
            elUtil.send_keys(driver,30, random.randint(10000, 99999), '',*self.SI_NO_element)
            sleep(2)

        # 通关者
        customs_broker_text = driver.find_element(*self.customs_broker_element).get_attribute('value')
        if len(customs_broker_text) == 0:
            elUtil.click(driver,30, '',*self.customs_broker_element)
            sleep(2)
            elUtil.click(driver,30, '',*self.customs_broker_choice_element)
            sleep(2)

        # 货物
        cargo_type_text = driver.find_element(*self.cargo_type_element).get_attribute('value')
        if len(cargo_type_text) == 0:
            elUtil.click(driver,30, '',*self.cargo_type_element)
            sleep(2)
            elUtil.click(driver,30, '',*self.cargo_type_choice_element)
            sleep(2)

        # CONTAINER NO输入框
        container_NO_el = isElementExist(driver, self.container_NO_element)
        if container_NO_el == True:
            container_NO_text = driver.find_element(*self.container_NO_element).get_attribute('value')
            if len(container_NO_text) == 0:
                elUtil.clear(driver,30, '',*self.container_NO_element)
                elUtil.send_keys(driver,30, random.randint(1000000, 9999999),'', *self.container_NO_element)
                sleep(1.5)

            # CONTAINER SIZE
            container_size_text = driver.find_element(*self.container_size_element).get_attribute('value')
            if len(container_size_text) == 0:
                elUtil.click(driver,30, '',*self.container_size_element)
                sleep(1.5)
                elUtil.click(driver,30,'', *self.container_size_choice_element)
                sleep(1.5)

        # 識別番号
        PID_text = driver.find_element(*self.PID_element).get_attribute('value')
        if len(PID_text) == 0:
            elUtil.clear(driver,30, '',*self.PID_element)
            elUtil.send_keys(driver,30, random.randint(1000000, 9999999), '',*self.PID_element)
            sleep(1.5)

        try:
            # 点击临时保存
            tempSaveEl = driver.find_element(*self.temporary_saving_element)
            driver.execute_script("arguments[0].click();", tempSaveEl)
            sleep(3)

            # 点击 弹框确定按钮
            message = driver.find_element(*self.repet_el).get_attribute('innerHTML')
            tempEnsureEl = driver.find_element(*self.confirm_button_element)
            driver.execute_script("arguments[0].click();", tempEnsureEl)
            sleep(3)

            #修改bl
            elUtil.send_keys(driver,30, random.randint(100000, 999990), '',*self.Master_BL_NO_element)
            sleep(1.5)
            elUtil.send_keys(driver,30, random.randint(100000, 999990), '',*self.House_BL_NO_element)
            sleep(1.5)

            # 点击临时保存
            tempSaveEl = driver.find_element(*self.temporary_saving_element)
            driver.execute_script("arguments[0].click();", tempSaveEl)
            sleep(3)

            # 点击 弹框确定按钮
            tempEnsureEl = driver.find_element(*self.confirm_button_element)
            driver.execute_script("arguments[0].click();", tempEnsureEl)
            sleep(1.5)

            # 确定发送
            sending_confirmation_el = driver.find_element(*self.sending_confirmation_element)
            driver.execute_script("arguments[0].click();", sending_confirmation_el)
            sleep(3)
            elUtil.click(driver,30, '',*self.sure_button_element)
            sleep(3)
            repet_flag = isElementExist(driver, self.repet_element)  # 重复提交
            success_flag = isElementExist(driver, self.successElement)  # 送信成功
            incomplete_flag = isElementExist(driver, self.incompleteElement)  # 信息不完整
            if success_flag == True:
                global text
                text = driver.find_element(*self.successElement).get_attribute('innerHTML')
            elif repet_flag == True:
                text = driver.find_element(*self.repet_element).get_attribute('innerHTML')
            elif incomplete_flag == True:
                text = driver.find_element(*self.incompleteElement).get_attribute('innerHTML')
            confirm_el = driver.find_element(*self.confirm_element)
            driver.execute_script("arguments[0].click();", confirm_el)
            sleep(3)

            # 点击 取消
            conreturn_el = driver.find_element(*self.return_element)
            driver.execute_script("arguments[0].click();", conreturn_el)
        except Exception as e:
            print(e)
        else:
            return message


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://sharpsit.jusdaglobal.com/')
    login = Login()
    login.test_click_login_btn(driver)
    sleep(5)
    new = NewBuilt()
    print(new.newBuiltReferLoadPort(driver))