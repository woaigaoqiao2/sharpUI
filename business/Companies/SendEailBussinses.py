'''
Created on 2019年6月25日
送信
@author: chinasoft.l.yu
'''
from time import sleep

from business.Login import Login
from pageElement.CompaniesPageElement import CompaniesPageElement
from util.ElementUtil import ElementUtil


class SendEailBussinses(CompaniesPageElement):

    #   未选择数据时，点击送信
    def noCheckData(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        #   进入到纳入指示页面
        des="纳入指示_送信_未选择任何数据时，送信"
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   检索
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   点击送信
        r = ElementUtil.is_enabled(self,driver,15,des,*self.sendEail)
        return r

    #   纳入指示剂时，选择多条数据点击送信
    def checkManyDatan(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        #   进入到纳入指示页面
        des='纳入指示剂时，选择多条数据点击送信'
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   检索(纳入指示剂状态下)
        ElementUtil.send_keys(self,driver,15,doNum,des,*self.queryDOInput)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusListn)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选中多条数据点击送信
        ElementUtil.click(self,driver,15,des,*self.tableCheckData)
        ElementUtil.click(self,driver,15,des,*self.sendEail)
        #   提示报错信息1(纳入指示剂)
        ele = ElementUtil.getElement(self,driver,15,des,*self.sendEailError1)
        return ele.get("element").text


    #   纳入指示剂时，选择单条数据点击送信
    def checkManyDatano(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        des='纳入指示剂时，选择单条数据点击送信'
        #   进入到纳入指示页面
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   检索(纳入指示剂状态下)
        ElementUtil.send_keys(self,driver,15,doNum,des,*self.queryDOInput)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusListn)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选中多条数据点击送信
        ElementUtil.click(self,driver,15,des,*self.tableCheckData)
        ElementUtil.click(self,driver,15,des,*self.sendEail)
        #   提示报错信息1(纳入指示剂)
        ele = ElementUtil.getElement(self,driver,15,des,*self.sendEailError1)
        return ele.get('element').text



    #   指示Mail送信済时，纳入场所、予定日、时间为空点击送信
    def checkDatazn(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        #   进入到纳入指示页面
        des='指示Mail送信済时，纳入场所、予定日、时间为空点击送信'
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   检索(指示Mail送信済状态下)
        ElementUtil.send_keys(self,driver,15,doNum,des,*self.queryBLInput)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusList)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选中多条数据点击送信
        ElementUtil.click(self,driver,15,des,*self.tableCheckData)
        ElementUtil.click(self,driver,15,des,*self.sendEail)
        #   提示报错信息2
        ele = ElementUtil.getElement(self,driver,15,des,*self.sendEailError3)
        return ele.get('element').text

    #   指示Mail送信済时，纳入场所、予定日、时间不为空点击送信
    def checkDataz(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        #   进入到纳入指示页面
        des="纳入指示_送信_指示Mail送信済时，纳入场所、予定日、时间不为空，送信"
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   检索(指示Mail送信済状态下)
        ElementUtil.send_keys(self,driver,15,doNum,des,*self.queryDOInput)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusList)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选中单条数据
        ElementUtil.click(self,driver,15,des,*self.tableFristData)
        #   填写纳入予定日，时间
        ElementUtil.click(self, driver, 15,des, *self.companiesAddButtonElement)
        #   填写予定日期
        ElementUtil.click(self, driver, 15,des, *self.companieTimeInput)
        driver.execute_script('arguments[0].click()',
                              ElementUtil.getElement(self, driver, 15,des, *self.companieTime).get('element'))
        driver.execute_script('arguments[0].click()',
                              ElementUtil.getElement(self, driver, 15,des, *self.companieTimeList).get('element'))
        #   填写时间
        driver.execute_script("arguments[0].value=''",
                              ElementUtil.getElement(self, driver, 15,des, *self.companieDateInput))
        ElementUtil.send_keys(self, driver, 15, 2300,des, *self.companieDateInput)
        #   点击保存
        sleep(2)
        ElementUtil.click(self, driver, 15,des, *self.saveButton)
        #   点击确定
        ElementUtil.click(self, driver, 15,des, *self.saveTipssaveButton)
        #   点击关闭
        ElementUtil.click(self, driver, 15,des, *self.colseButton)
        #   输入dono搜索
        ElementUtil.send_keys(self, driver, 15, doNum,des, *self.queryDOInput)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        #   送信
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        ElementUtil.click(self,driver,15,des,*self.tableFristData)

        ElementUtil.click(self,driver,15,des,*self.sendEail)
        #   提示成功
        ele = ElementUtil.getElement(self,driver,15,des,*self.sendEailSuccess)
        return ele.get('element').text
