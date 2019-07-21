from util.interface_data import demo
from time import sleep
from util.element_exits import isElementExist
from business.Login import Login
from selenium import webdriver
import random
from util.ElementUtil import ElementUtil
from pageElement.customs.NewBuilt import NewBuiltElement,NewlyBuildElement
from pageElement.customs.AddCost import AddCost
from pageElement.customs.EditElement import EditElement

class NewData(NewBuiltElement,NewlyBuildElement,AddCost,EditElement):

    def create_data(self,driver):
        '''创建新数据'''

        elUtil = ElementUtil()  #
        d = demo()

        # 进入首页S/A登录
        elUtil.click(driver,30, '进入首页S/A登录',*self.SAElement)
        sleep(1.5)

        # 点击新規按钮
        elUtil.click(driver,30,'点击新規按钮', *self.newRuleElement)
        sleep(1.5)

        # 点击INV P/L情報下追加按钮
        elUtil.click(driver,30, '点击INV P/L情報下追加按钮',*self.addElement)
        sleep(1.5)

        #获取新数据
        r_data = d.test().get('invoiceNo')

        #输入新数据
        elUtil.clear(driver,30,'清除invoiceNo', *self.IVNoElement)
        elUtil.send_keys(driver,30, r_data,'输入%s'%r_data, *self.IVNoElement)
        sleep(1.5)

        # 点击搜索
        elUtil.click(driver,30,'点击搜索按钮', *self.dialogSearchElement)
        sleep(1.5)

        # 勾选第一条数据
        elUtil.click(driver,30,'勾选数据', *self.firstDataElement)
        sleep(1.5)

        # 点击对话框追加
        elUtil.click(driver,30, '点击对话框追加',*self.dialogAddElement)
        sleep(1.5)
        Master_BL_NO = random.randint(100000, 999990)
        House_BL_NO = random.randint(100000, 999990)

        '''masterNo'''
        Master_BL_NO_text = driver.find_element(*self.Master_BL_NO_element).get_attribute('value')
        if len(Master_BL_NO_text) == 0:
            elUtil.send_keys(driver,30, Master_BL_NO, '输入masterNo',*self.Master_BL_NO_element)

        # HourseNo
        House_BL_NO_text = driver.find_element(*self.House_BL_NO_element).get_attribute('value')
        if len(House_BL_NO_text) == 0:
            elUtil.send_keys(driver,30, House_BL_NO, '输入HourseNo',*self.House_BL_NO_element)


        # 输送形态
        convey_text = driver.find_element(*self.conveyElement).get_attribute('value')
        if convey_text == 'AIR':
            elUtil.click(driver,30, '点击输送形态',*self.conveyElement)
            elUtil.click(driver,30, '点击SEA',*self.seaElement)

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

        return Master_BL_NO,House_BL_NO

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://sharpsit.jusdaglobal.com')
    login = Login()
    login.test_click_login_btn(driver)
    sleep(5)
    new = NewData()
    print(new.create_data(driver))
