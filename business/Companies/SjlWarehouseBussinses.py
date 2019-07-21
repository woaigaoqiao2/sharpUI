from time import sleep

from business.Login import Login
from pageElement.CompaniesPageElement import CompaniesPageElement
from util.ElementUtil import ElementUtil

class SjlWarehouseBussinses(CompaniesPageElement):


    def openWindow(self,driver,des,**params):
        r = "success"
        login = Login()
        login.test_click_login_btn(driver)

        #   1.点击纳入指示菜单
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   2.判断是否需要输入doNo
        if('doNo' in params.keys() and params['doNo'] != ""):
            ElementUtil.send_keys(self,driver,15,params['doNo'],des,*self.queryDOInput)
        #   3.判断是否需要选择纳入指示status
        if('status' in params.keys() and params['status'] != ""):
            ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
            if(params['status'] == "指示Mail送信済"):
                ElementUtil.click(self,driver,15,des,*self.queryShowStatusList)
            if(params['status'] == "納入指示済"):
                ElementUtil.click(self,driver,15,des,*self.queryShowStatusListn)
        #   4.判断是否需要点击查询按钮
        if('query' in params.keys() and params['query'] != ""):
            ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   15.判断是否需要选中数据
        if('checkData' in params.keys() and params['checkData'] != ""):
            if(params['checkData'] == "many"):
                ElementUtil.click(self,driver,15,des,*self.tableCheckData)
            if(params['checkData'] == "one"):
                ElementUtil.click(self,driver,15,des,*self.tableFristData)
        #   6.纳入场所指定按钮是否可点击
        if('click' in params.keys() and params['click'] != ""):
            if(params['click'] == True):
                ElementUtil.click(self,driver,15,des,*self.companiesAddButtonElement)
            if(params['click'] == False):
                r = ElementUtil.is_enabled(self,driver,15,des,*self.companiesAddButtonElement)
        #   7.判断是否需要继续走流程
        if('end' in params.keys() and params['end'] != ""):
            if(params['end'] == True):
                return r
        #   15.判断最终纳入场所是否需要输入值
        ElementUtil.clear(self,driver,15,des,*self.companieCustomsInput)
        if('input' in params.keys() and params['input'] != ""):
            driver.execute_script('arguments[0].click()',
                                  ElementUtil.getElement(self,driver,15,des,*self.companieCustoms).get('element'))
            driver.execute_script("arguments[0].scrollIntoView();",
                                  ElementUtil.getElement(self,driver,15,des,*self.companieCustomsList).get('element'))
            driver.execute_script('arguments[0].click()',
                                  ElementUtil.getElement(self,driver,15,des,*self.companieCustomsList).get('element'))
        #   9.判断纳入予定日是否需要输入值
        ElementUtil.click(self,driver,15,des,*self.companieTimeInput)
        if('date' in params.keys() and params['date'] != ""):
            driver.execute_script('arguments[0].click()',
                                  ElementUtil.getElement(self,driver,15,des,*self.companieTime).get('element'))
            driver.execute_script('arguments[0].click()',
                                  ElementUtil.getElement(self,driver,15,des,*self.companieTimeList).get('element'))
        #   10.判断时间是否需要输入值
        driver.execute_script("arguments[0].value=''",
                              ElementUtil.getElement(self,driver,15,des,*self.companieDateInput))
        if('time' in params.keys() and params['time'] != ""):
            ElementUtil.send_keys(self,driver,15,params['time'],des,*self.companieDateInput)
        #   11.判断是否需要点击保存按钮
        if('save' in params.keys() and params['save'] != ""):
            if(params['save'] == True):
                ElementUtil.click(self,driver,15,des,*self.saveButton)
            if(params['save'] == False):
                r = ElementUtil.is_enabled(self,driver,15,des,*self.saveButton)
        #   12.判断是否需要点击关闭按钮
        if('close' in params.keys() and params['close'] != ""):
            if(params['close'] == True):
                ElementUtil.click(self,driver,15,des,*self.colseButton)
            if(params['close'] == False):
                r = ElementUtil.is_enabled(self,driver,15,des,*self.colseButton)
        return r