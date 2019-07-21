'''
Created on 1019年3月11日

@author: chinasoft.l.yu
'''
#coding=utf-15
from pageElement.CompaniesPageElement import CompaniesPageElement
from business.Login import Login
from time import sleep
from util.ElementUtil import ElementUtil

class QueryBussinses(CompaniesPageElement):
    ###    无数据查询
    def companiesQueryNoData(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示-检索-对不存在的数据检索"
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        ElementUtil.click(self, driver, 15,des, *self.queryDOInput)
        ElementUtil.clear(self, driver, 15,des,*self.queryDOInput)
        ElementUtil.send_keys(self, driver, 15,doNum,des,*self.queryDOInput)
        ElementUtil.click(self, driver, 15,des, *self.queryButton)
        str=ElementUtil.getElement(self, driver, 15,des,*self.tableNoData).get('element')
        return str.text
    
    ###    默认查询
    def companiesQueryNoParams(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        des= "纳入指示-检索-默认检索"
        ElementUtil.click(self, driver,15,des,*self.companiesStartElement)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        sleep(6)
        a=driver.find_elements(*self.onepagedata)
        sleep(2)
        l=len(a)
        return l
        
    ###    根据D/O NO查询
    def companiesQueryDO(self,driver,doNum,des):
        login = Login()
        login.test_click_login_btn(driver)

        ElementUtil.click(self, driver,15,des,*self.companiesStartElement)
        ElementUtil.send_keys(self, driver,15,doNum,des,*self.queryDOInput)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        sleep(6)
        a = driver.find_elements(*self.onepagedata)
        sleep(2)
        l = len(a)
        return l
    
    
    ###    根据B/L NO查询
    def companiesQueryBL(self,driver,blNum,des):
        login = Login()
        login.test_click_login_btn(driver)

        ElementUtil.click(self, driver,15,des,*self.companiesStartElement)
        ElementUtil.click(self, driver,15,des,*self.queryBLInput)
        ElementUtil.send_keys(self, driver,15,blNum,des,*self.queryBLInput)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        sleep(6)
        a = driver.find_elements(*self.onepagedata)
        sleep(2)
        l = len(a)
        return l
    
    ###    根据纳入指示者查询
    def companiesQueryOperateDirector(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示-检索-根据纳入指示者检索"
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        ElementUtil.click(self,driver,15,des,*self.queryOperateDirectorId)
        sleep(2)
        driver.execute_script(" return arguments[0].scrollIntoViewIfNeeded();",
                              ElementUtil.getElement(self, driver, 15,des, *self.queryOperateDirectorList).get("element"))
        sleep(2)
        driver.execute_script(" return arguments[0].click();",
                              ElementUtil.getElement(self, driver, 15,des, *self.queryOperateDirectorList).get("element"))
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        sleep(6)
        a = driver.find_elements(*self.onepagedata)
        sleep(2)
        l = len(a)
        return l
    
    ###    根据海外取引先查询
    def companiesQueryPartner(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示-检索-根据海外取引先检索"
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        ElementUtil.click(self,driver,15,des,*self.queryPartnerId)
        sleep(1)
        #driver.find_element(*self.queryPartnerList).click()
        driver.execute_script(" return arguments[0].scrollIntoView();",
                              ElementUtil.getElement(self, driver, 15,des, *self.queryPartnerList).get("element"))
        driver.execute_script(" return arguments[0].click();",
                              ElementUtil.getElement(self, driver, 15,des, *self.queryPartnerList).get("element"))
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        sleep(6)
        a = driver.find_elements(*self.onepagedata)
        sleep(2)
        l = len(a)
        return l
    
    ###    根据纳入指示status查询
    def companiesQueryShowStatus(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示-检索-根据纳入指示status检索"
        ElementUtil.click(self, driver, 15,des, *self.companiesStartElement)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatusList)
        ElementUtil.click(self, driver, 15,des, *self.queryButton)
        sleep(6)
        a = driver.find_elements(*self.onepagedata)
        sleep(2)
        l = len(a)
        return l
    
    ###    根据D/O status 组合查询
    def companiesQueryParams(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示-检索-根据D/O status 组合检索"
        ElementUtil.click(self, driver, 15,des, *self.companiesStartElement)
        ElementUtil.click(self, driver, 15,des, *self.queryDOInput)
        ElementUtil.send_keys(self, driver, 15,doNum,des, *self.queryDOInput)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatusList)
        ElementUtil.click(self, driver, 15,des, *self.queryButton)
        sleep(6)
        a = driver.find_elements(*self.onepagedata)
        sleep(2)
        l = len(a)
        return l
              
    ###    状态为指示送信济时，点击详细，详细字段为空点击保存  19S0000198
    def detailStatusz(self,driver,doNum): 
        ### 登录
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示-点击B/L详细-状态为指示送信济时，点击详细，详细字段为空点击保存"
        ### 查询
        ElementUtil.click(self, driver,15,des,*self.companiesStartElement)
        ElementUtil.send_keys(self, driver, 15,doNum,des,*self.queryDOInput)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatusList)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        ### 点击按钮
        js = 'document.getElementsByClassName("v-table__overflow")[1].scrollLeft = 200'
        driver.execute_script(js)
        ElementUtil.click(self, driver,15,des,*self.tableDetail)
        ### 保存
        ElementUtil.clear(self,driver,15,des,*self.detailInput)
        ElementUtil.click(self, driver,15,des,*self.detailSave)
        ### 保存成功
        ElementUtil.click(self, driver,15,des,*self.detailSuccess)
        return "success"
    
    ###    状态为指示送信济时，点击详细，详细字段为英文点击保存  19S0000198
    def detailStatuszy(self,driver,doNum): 
        ### 登录
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示-点击B/L详细-状态为指示送信济时，点击详细，详细字段为英文点击保存"
        ### 查询
        ElementUtil.click(self, driver,15,des,*self.companiesStartElement)
        ElementUtil.send_keys(self, driver,15, doNum,des,*self.queryDOInput)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatusList)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        ### 点击按钮
        js = 'document.getElementsByClassName("v-table__overflow")[1].scrollLeft = 200'
        driver.execute_script(js)
        ElementUtil.click(self, driver,15,des,*self.tableDetail)
        ### 保存
        sleep(1)
        ElementUtil.clear(self,driver,15,des,*self.detailInput)
        ElementUtil.send_keys(self, driver,15, "test",des,*self.detailInput)
        ElementUtil.click(self, driver,15,des,*self.detailSave)
        ### 保存成功
        ElementUtil.click(self, driver,15,des,*self.detailSuccess)
        return "success"
    
    ###    状态为指示送信济时，点击详细，详细字段为中文点击保存  19S0000198
    def detailStatuszz(self,driver,doNum): 
        ### 登录
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示-点击B/L详细-状态为指示送信济时，点击详细，详细字段为中文点击保存"
        ### 查询
        ElementUtil.click(self, driver,15,des,*self.companiesStartElement)
        ElementUtil.send_keys(self, driver,15, doNum,des,*self.queryDOInput)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatusList)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        ### 点击按钮
        js = 'document.getElementsByClassName("v-table__overflow")[1].scrollLeft = 200'
        driver.execute_script(js)
        ElementUtil.click(self, driver,15,des,*self.tableDetail)
        ### 保存
        sleep(1)
        ElementUtil.clear(self,driver,15,des,*self.detailInput)
        ElementUtil.send_keys(self, driver,15, "测试",des,*self.detailInput)
        ElementUtil.click(self, driver,15,des,*self.detailSave)
        ### 保存成功
        ElementUtil.click(self, driver,15,des,*self.detailSuccess)
        return "success"
    
    ###    状态为指示送信济时，点击详细，详细字段为特殊符号点击保存  19S0000198
    def detailStatuszt(self,driver,doNum): 
        ### 登录
        login = Login()
        login.test_click_login_btn(driver)
        des='状态为指示送信济时，点击详细，详细字段为特殊符号点击保存'
        ### 查询
        ElementUtil.click(self, driver,15,des,*self.companiesStartElement)
        ElementUtil.send_keys(self, driver,15, doNum,des,*self.queryDOInput)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatusList)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        ### 点击按钮
        js = 'document.getElementsByClassName("v-table__overflow")[1].scrollLeft = 200'
        driver.execute_script(js)
        ElementUtil.click(self, driver,15,des,*self.tableDetail)
        ### 保存
        ElementUtil.clear(self,driver,15,des,*self.detailInput)
        ElementUtil.send_keys(self, driver, 15,"@#￥%￥￥#@",des,*self.detailInput)
        ElementUtil.click(self, driver,15,des,*self.detailSave)
        ### 保存成功
        ElementUtil.click(self, driver,15,des,*self.detailSuccess)
        return "success"
    
    ###    状态为纳入指示济时，点击详细，详细字段为空点击保存  19S0000113
    def detailStatusn(self,driver,doNum): 
        ### 登录
        login = Login()
        login.test_click_login_btn(driver)
        des='状态为纳入指示济时，点击详细，详细字段为空点击保存'
        ### 查询
        ElementUtil.click(self, driver,15,des,*self.companiesStartElement)
        ElementUtil.send_keys(self, driver,15, doNum,des,*self.queryDOInput)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatusListn)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        ### 点击按钮
        js = 'document.getElementsByClassName("v-table__overflow")[1].scrollLeft = 200'
        driver.execute_script(js)
        ElementUtil.click(self, driver,15,des,*self.tableDetail)
        ### 输入描述
        ElementUtil.send_keys(self, driver,15, "",des,*self.detailInput)
        ### 点击保存
        r = ElementUtil.is_enabled(self, driver,15,des,*self.detailSaven)
        return r
    
    ###    状态为纳入指示济时，点击详细，详细字段特殊符号点击保存  19S0000113
    def detailStatusnt(self,driver,doNum): 
        ### 登录
        login = Login()
        login.test_click_login_btn(driver)
        des='状态为纳入指示济时，点击详细，详细字段特殊符号点击保存'
        ### 查询
        ElementUtil.click(self, driver,15,des,*self.companiesStartElement)
        ElementUtil.send_keys(self, driver,15, doNum,des,*self.queryDOInput)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatusListn)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        ### 点击按钮
        js = 'document.getElementsByClassName("v-table__overflow")[1].scrollLeft = 200'
        driver.execute_script(js)
        ElementUtil.click(self, driver,15,des,*self.tableDetail)
        ### 输入描述
        ElementUtil.clear(self,driver,15,des,*self.detailInput)
        ElementUtil.send_keys(self, driver, 15,"#￥#%#",des,*self.detailInput)
        ### 点击保存
        r = ElementUtil.is_enabled(self,driver,15,des,*self.detailSaven)
        return r
    
    ###    状态为纳入指示济时，点击详细，详细字段为中文点击保存  19S0000113
    def detailStatusnz(self,driver,doNum): 
        ### 登录
        login = Login()
        login.test_click_login_btn(driver)
        des='状态为纳入指示济时，点击详细，详细字段为中文点击保存'
        ### 查询
        ElementUtil.click(self, driver,15,des,*self.companiesStartElement)
        ElementUtil.send_keys(self, driver,15, doNum,des,*self.queryDOInput)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatusListn)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        ### 点击按钮
        js = 'document.getElementsByClassName("v-table__overflow")[1].scrollLeft = 200'
        driver.execute_script(js)
        ElementUtil.click(self, driver,15,des,*self.tableDetail)
        ### 输入描述
        ElementUtil.clear(self,driver,15,des,*self.detailInput)
        ElementUtil.send_keys(self, driver, 15,"测试",des,*self.detailInput)
        ### 点击保存
        r = ElementUtil.is_enabled(self, driver,15,des,*self.detailSaven)
        return r
    
    
    ###    状态为指示Mail送信済时，点击详细，点击关闭 19S0000376
    def detailStatuszc(self,driver,doNum): 
        ### 登录
        login = Login()
        login.test_click_login_btn(driver)
        des='状态为指示Mail送信済时，点击详细，点击关闭'
        ### 查询
        ElementUtil.click(self, driver,15,des,*self.companiesStartElement)
        ElementUtil.send_keys(self, driver,15, doNum,des,*self.queryDOInput)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatusList)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        ### 点击按钮
        js = 'document.getElementsByClassName("v-table__overflow")[1].scrollLeft = 200'
        driver.execute_script(js)
        ElementUtil.click(self, driver,15,des,*self.tableDetail)
        ### 关闭
        ElementUtil.click(self, driver,15,des,*self.detailClose)
        return "success"
        
    ###    状态为纳入指示济时，点击详细，点击关闭  19S0000245
    def detailStatusnc(self,driver,doNum): 
        ### 登录
        login = Login()
        login.test_click_login_btn(driver)
        des='状态为纳入指示济时，点击详细，点击关闭'
        ### 查询
        ElementUtil.click(self, driver,15,des,*self.companiesStartElement)
        ElementUtil.send_keys(self, driver,15, doNum,des,*self.queryDOInput)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15,des, *self.queryShowStatusListn)
        ElementUtil.click(self, driver,15,des,*self.queryButton)
        ### 点击按钮
        js = 'document.getElementsByClassName("v-table__overflow")[1].scrollLeft = 200'
        driver.execute_script(js)
        ElementUtil.click(self, driver,15,des,*self.tableDetail)
        ### 关闭
        ElementUtil.click(self, driver,15,des,*self.detailClose)
        return "success"
    
        
    ###    返回列表数据总数
    def resultCountNumb(self,driver):
        des=''
        re=ElementUtil.getElement(self,driver,15,des,*self.tableCountNumb)
        result=re.get('element')
        sleep(3)
        result = str(result.text)
        print("-------------------------")
        print(result)
        return result[result.rfind('f', 1) + 1:]