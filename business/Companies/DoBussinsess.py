"""
Created on 2019年6月24日

bussinsess操作类
@author: chinasoft.l.yu

"""

from business.Login import Login
from pageElement.CompaniesPageElement import CompaniesPageElement
from util.ElementUtil import ElementUtil
from time import sleep
class DoBussinsess(CompaniesPageElement):


    #  实操动作
    def practical(self,driver,des,**p):
        r = "success"
        login = Login()
        login.test_click_login_btn(driver)

        #   1.点击纳入指示菜单
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)

        #   2.判断是否需要输入doNo
        if('doNo' in p.keys() and p['doNo'] != ""):
            ElementUtil.send_keys(self,driver,15,p['doNo'],des,*self.queryDOInput)
        #   3.判断是否需要选择纳入指示status
        if('status' in p.keys() and p['status'] != ""):
            ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
            if(p['status'] == "指示Mail送信済"):
                ElementUtil.click(self,driver,15,des,*self.queryShowStatusList)
            if(p['status'] == "納入指示済"):
                ElementUtil.click(self,driver,15,des,*self.queryShowStatusListn)

        #   4.判断是否需要点击查询按钮
        if('query' in p.keys() and p['query'] != ""):
            ElementUtil.click(self,driver,15,des,*self.queryButton)

        #   15.判断是否需要选中数据
        if('checkData' in p.keys() and p['checkData'] != ""):
            if(p['checkData'] == "many"):
                ElementUtil.click(self,driver,15,des,*self.tableCheckData)
            if(p['checkData'] == "one"):
                ElementUtil.click(self,driver,15,des,*self.tableFristData)

        #   6.纳入指示变更按钮是否可点击
        if('click' in p.keys() and p['click'] != ""):
            if(p['click'] == True):
                ElementUtil.click(self,driver,15,des,*self.nrzsbgButton)
            if(p['click'] == False):
                r = ElementUtil.is_enabled(self,driver,15,des,*self.nrzsbgButton)

        #   7.判断是否需要继续走流程
        if('end' in p.keys() and p['end'] != ""):
            if(p['end'] == True):
                return r

        #   15.判断纳入场所是否需要输入值
        ElementUtil.clearSelectInput(self,driver,15,des,*self.siteSelectInput)
        if('input' in p.keys() and p['input'] != ""):
            ElementUtil.click(self,driver,15,des,*self.nrcsInput)
            driver.execute_script(" return arguments[0].scrollIntoView();",
                                  ElementUtil.getElement(self,driver,15,des,*self.nrcsDivValues).get("element"))
            driver.execute_script(" return arguments[0].click();",
                                  ElementUtil.getElement(self,driver,15,des,*self.nrcsDivValues).get("element"))

        #   9.判断納入予定日是否需要输入值
        ElementUtil.clearSelectInput(self,driver,15,des,*self.timeSelectInput)
        if('time' in p.keys() and p['time'] != ""):
            ElementUtil.click(self,driver,15,des,*self.timeInput)
            driver.execute_script("arguments[0].click();",
                                  ElementUtil.getElement(self,driver,15,des,*self.timeValues).get("element"))

        #   10.判断受入予定时间是否需要输入值
        ElementUtil.clear(self,driver,15,des,*self.DateInput)
        if('date' in p.keys() and p['date'] != ""):
            ElementUtil.send_keys(self,driver,15,p['date'],des,*self.DateInput)
            # driver.execute_script("arguments[0].value='"+p['date'] +"';",
            #                       ElementUtil.getElement(self,driver,self.DateInput))

        #   11.判断是否需要点击保存按钮
        if('save' in p.keys() and p['save'] != ""):
            if(p['save'] == True):
                ElementUtil.click(self,driver,15,des,*self.updateButton)
            if(p['save'] == False):
                r = ElementUtil.is_enabled(self,driver,15,des,*self.updateButton)

        #   12.判断是否需要点击关闭按钮
        if('close' in p.keys() and p['close'] != ""):
            if(p['close'] == True):
                ElementUtil.click(self,driver,15,des,*self.closeButton)
            if(p['close'] == False):
                r = ElementUtil.is_enabled(self,driver,15,des,*self.closeButton)

        return r