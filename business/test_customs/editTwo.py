from pageElement.customs.EditElement import EditElement,NewlyBuildElement
from time import sleep
from business.Login import Login
from selenium import webdriver
from util.element_exits import isElementExist
import random
from util.ElementUtil import ElementUtil
from business.test_customs.NewData import NewData
from util.interface_data import demo


class Edit(EditElement,NewlyBuildElement):

    def editLoadPort(self,driver):
        '''编辑装运港不同的数据'''
        elUtil = ElementUtil()
        new = NewData()
        d = demo()

        # 获取masterNO和HouseNO
        Master_BL_NO, House_BL_NO = new.create_data(driver)

        # 输入Master B/L NO清除
        elUtil.send_keys(driver,30, Master_BL_NO, '输入Master B/L NO：%s'%Master_BL_NO,*self.master_no_element)

        # 输入House NO清除
        elUtil.send_keys(driver,30, House_BL_NO,'输入HouseB/L NO：%s'%House_BL_NO, *self.house_no_element)

        # 点击搜索
        elUtil.click(driver,30,'点击搜索', *self.searchElement)
        sleep(1.5)

        # 选择表第一条数据
        elUtil.click(driver,30,'选择搜索数据', *self.fistCheckElement)
        sleep(1.5)

        #点击编辑
        elUtil.click(driver,30, '点击编辑',*self.editElement)
        sleep(1.5)

        #修改積出港数据
        elUtil.click(driver,5,'修改積出港',*self.loading_port_element)
        elUtil.click(driver,5,'修改積出港',*self.loading_port_choice_elements)
        sleep(1.5)

        #点击追加
        elUtil.click(driver,30, '点击追加',*self.addElement)
        sleep(1.5)

        # 获取新数据
        data = d.test()
        r_data = data.get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver,30, '清除之前数据',*self.IVNoElement)
        elUtil.send_keys(driver,30, r_data,'输入invoiceNo%s'%r_data, *self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索',*self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30,'勾选数据', *self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30,'点击追加', *self.dialogAddElement)
        sleep(1.5)

        #获取弹框内容
        text= driver.find_element(*self.inconformityElement).text
        sleep(2)

        #点击弹框确定
        # driver.find_element(*self.enterElement).click()
        # sleep(2)

        return text

    def editToPort(self,driver):
        '''编辑陆扬港不同的数据'''

        elUtil = ElementUtil()
        new = NewData()
        d = demo()

        # 获取masterNO和HouseNO
        Master_BL_NO, House_BL_NO = new.create_data(driver)

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

        # 修改陆扬港数据
        elUtil.click(driver,30, '修改陆扬港数据',*self.loading_port_clear_element)
        sleep(1.5)

        # 点击追加
        elUtil.click(driver,30, '点击追加', *self.addElement)
        sleep(1.5)

        # 获取新数据
        data = d.test()
        r_data = data.get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver,30, '清除之前数据', *self.IVNoElement)
        elUtil.send_keys(driver,30, r_data, '输入invoiceNo%s' % r_data, *self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索', *self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30, '勾选数据', *self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30, '点击追加', *self.dialogAddElement)
        sleep(1.5)

        # 获取弹框内容
        text = driver.find_element(*self.inconformityElement).text
        sleep(2)

        return text


    def editStartGreaterEnd(self,driver):
        '''start>end'''
        elUtil = ElementUtil()
        new = NewData()

        # 获取masterNO和HouseNO
        Master_BL_NO, House_BL_NO = new.create_data(driver)

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

        #勾选NV P/L信息第一条数据,获取P/O NO,判断startNo是否小于endNo,进行修改
        poNo = driver.find_element(*self.INVFistPoElement).get_attribute('value')

        startNo = driver.find_element(*self.Carton_start_No_element).get_attribute('value')
        sleep(2)
        startNo= int(startNo)
        endNo = driver.find_element(*self.Carton_end_No_element).get_attribute('value')
        endNo = int(endNo)
        if startNo <= endNo:
            elUtil.clear(driver,5,'清除startNo',*self.Carton_start_No_element)
            elUtil.send_keys(driver,5,1000,'输入startNo',*self.Carton_start_No_element)
        startNo1 = driver.find_element(*self.Carton_start_No_element).get_attribute('value')
        sleep(2)

        # 点击临时保存
        tempSaveEl = driver.find_element(*self.temporary_saving_element)
        driver.execute_script("arguments[0].click();", tempSaveEl)
        sleep(1.5)

        # 点击 弹框确定按钮
        tempEnsureEl = driver.find_element(*self.confirm_button_element)
        driver.execute_script("arguments[0].click();", tempEnsureEl)
        sleep(1.5)

        #比较修改前与修改后的startNo是否相等
        startNo2 = driver.find_element(*self.Carton_start_No_element).get_attribute('value')
        flag = None
        if startNo1 == startNo2:
            flag = False
        return flag


    def editCancel(self,driver):
        '''修改数据，点击取消，修改失败'''

        elUtil = ElementUtil()
        new = NewData()

        # 获取masterNO和HouseNO
        Master_BL_NO, House_BL_NO = new.create_data(driver)

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
        elUtil.clear(driver,5,'清除startNo',*self.startNoElement)
        elUtil.send_keys(driver,5,8888,'输入startNo',*self.startNoElement)
        startNo1 = driver.find_element(*self.startNoElement).get_attribute('value')
        sleep(1.5)

        #点击取消
        conreturn_el = driver.find_element(*self.return_element)
        driver.execute_script("arguments[0].click();", conreturn_el)
        sleep(1.5)

        # 输入Master B/L NO清除
        elUtil.send_keys(driver,30, Master_BL_NO, '输入Master_BL_NO：%s'%Master_BL_NO,*self.master_no_element)

        # 输入House NO清除
        elUtil.send_keys(driver,30, House_BL_NO, '输入House_BL_NO：%s'%House_BL_NO,*self.house_no_element)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索',*self.searchElement)
        sleep(1.5)

        # 选择表第一条数据
        elUtil.click(driver,30, '勾选数据',*self.fistCheckElement)
        sleep(1.5)

        # 点击编辑
        elUtil.click(driver,30, '点击编辑',*self.editElement)
        sleep(1.5)

        #再次startNo内容和修改后的比对，不一致说明修改失败，返回False
        startNo2 = driver.find_element(*self.startNoElement).get_attribute('value')
        flag = None
        if startNo1 != startNo2:
            flag = False
        return flag

    def editLetterCancel(self,driver):
        '''填写送信必填内容，送信取消'''
        elUtil = ElementUtil()
        new = NewData()
        d = demo()

        # 获取masterNO和HouseNO
        Master_BL_NO, House_BL_NO = new.create_data(driver)

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

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver,30, '点击INV P/L情報下追加按钮', *self.addElement)
        sleep(1.5)

        # 获取新数据
        r_data = d.test().get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver,30, '清除invoiceNo',*self.IVNoElement)
        elUtil.send_keys(driver,30, r_data,'输入invoiceNo：%s'%r_data, *self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索',*self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30,'选择第一条数据' ,*self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30, '点击对话框追加' ,*self.dialogAddElement)
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
        # #点击文件上传按钮
        # elUtil.click(driver,30, *self.file_upload_element)
        # sleep(1.5)
        #
        # # 文件上传路径
        # FilePath = fileExists()
        # driver.find_element(*self.upload_button_element).send_keys(FilePath)
        # sleep(1.5)
        #
        # # 点击文件上传完毕 关闭按钮
        # closeBtn = driver.find_element(*self.close_button_element)
        # driver.execute_script("arguments[0].click();", closeBtn)
        # sleep(1.5)
        #
        # #关闭弹窗
        # popup_return_el = driver.find_element(*self.popup_return_element)
        # driver.execute_script("arguments[0].click();", popup_return_el)
        # sleep(1.5)

        #点击临时保存

        try:
            tempSaveEl = driver.find_element(*self.temporary_saving_element)
            driver.execute_script("arguments[0].click();", tempSaveEl)
            sleep(1.5)
            # 点击 弹框确定按钮
            tempEnsureEl = driver.find_element(*self.confirm_button_element)
            driver.execute_script("arguments[0].click();", tempEnsureEl)
            sleep(1.5)

            #判断点击确定发信按钮是否存在,不存在点击保存
            text = None
            flag0 = isElementExist(driver,self.sending_confirmation_element)
            if flag0:
                #点击确定发信按钮
                ensureLettersEl=driver.find_element(*self.sending_confirmation_element)
                driver.execute_script("arguments[0].click();", ensureLettersEl)
                sleep(2)
                inv_flag = isElementExist(driver,self.inv_incomplete_element)   #inv资料不齐全
                if inv_flag:
                    text = driver.find_element(*self.inv_incomplete_element).get_attribute('innerHTML') #获取inv资料不齐全
                    inv_incomplete_el = driver.find_element(*self.inv_incomplete_element)
                    driver.execute_script("arguments[0].click();", inv_incomplete_el)
                    driver.find_element(*self.inv_sure_element).click()                         #点击确定

            #点击取消
            elUtil.click(driver,30,'点击取消', *self.return_element)   #取消
            sleep(2)

            flag = True
            if 'INV P/L情報が不整備です、ご確認お願いします。' in text:
                flag = False
        except Exception as e:
            print('')
        else:
            return flag

    def editCancelContainer(self,driver):
        '''取消多个集装箱装货'''

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

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver,30, '点击编辑',*self.addElement)
        sleep(1.5)

        # 获取新数据
        r_data = d.test().get('invoiceNo')

        # 输入新数据
        elUtil.clear(driver,30,'清除invoiceNo', *self.IVNoElement)
        elUtil.send_keys(driver,30, r_data,'输入invoiceNo：%s'%r_data, *self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30, '点击搜索',*self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30,'勾选第一条数据', *self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30,'点击对话框追加', *self.dialogAddElement)
        sleep(1.5)

        # 选择inv pl表第一条数据
        elUtil.click(driver,30,'选择inv pl表第一条数据', *self.INVFistCheckElement)
        sleep(1.5)

        #点击分类
        elUtil.click(driver,30, '点击分类',*self.classifyElement)
        sleep(1.5)

        #获取INV PL表数据量
        table = driver.find_element(*self.tableTbodyElement)
        rows1 = len(table.find_elements_by_tag_name('tr'))

        # 勾选第一条数据
        elUtil.click(driver,30,'勾选第一条数据' ,*self.INVFistCheckElement)
        sleep(1.5)

        #点击行政分工
        elUtil.click(driver,30, '点击行政分工',*self.cancelAdminElement)
        sleep(1.5)

        # 获取INV PL表数据量
        table = driver.find_element(*self.tableTbodyElement)
        rows2 = len(table.find_elements_by_tag_name('tr'))

        #点击临时保存
        # sleep(3)
        # elUtile.click(driver,30, *self.tempSaveElement)
        # sleep(2)
        # elUtile.click(driver,30, *self.tempEnsureElement)

        flag = False
        if rows1!=rows2:
            flag = True
        return flag


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://sharpsit.jusdaglobal.com/')
    login = Login()
    login.test_click_login_btn(driver)
    sleep(5)
    edit = Edit()
    print(edit.editCancelContainer(driver))