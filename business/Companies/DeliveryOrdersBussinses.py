

from business.Login import Login
from pageElement.CompaniesPageElement import CompaniesPageElement
from util.ElementUtil import ElementUtil
import time
"""
纳入场所一括登录
"""

class DeliveryOrdersBussinses(CompaniesPageElement):


    #   不选择数据，直接点击按钮
    def openWindow(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        #   进入到纳入指示页面
        des='"纳入指示_纳入场所一括登录_不输入数据时点击纳入场所一括登录"'
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   点击按钮
        r = ElementUtil.is_enabled(self,driver,15,des,*self.deliveryOrdersStar)
        return r


    def openWindowb(self,driver):
        des='纳入指示_纳入场所一括登录_纳入指示status为纳入指示剂时选择多条点击纳入场所一括登录'
        login = Login()
        login.test_click_login_btn(driver)

        #   进入到纳入指示页面
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   选择納入指示済，点击查询
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusListn)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选择数据，点击按钮
        ElementUtil.click(self,driver,15,des,*self.tableCheckData)
        r = ElementUtil.is_enabled(self,driver,15,des,*self.deliveryOrdersStar)
        return r

    def openWindowe(self,driver):
        des="纳入指示_纳入场所一括登录_纳入指示status为纳入指示剂时选择一条点击纳入场所一括登录"
        login = Login()
        login.test_click_login_btn(driver)

        #   进入到纳入指示页面
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   选择納入指示済，点击查询
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusListn)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选择数据，点击按钮
        ElementUtil.click(self,driver,15,des,*self.tableFristData)
        r = ElementUtil.is_enabled(self,driver,15,des,*self.deliveryOrdersStar)
        return r

    def openWindowc(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        des='"纳入指示_纳入场所一括登录_纳入指示status为指示Mail送信済时选择多条点击纳入场所一括登录"'
        #   进入到纳入指示页面
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   选择納入指示済，点击查询
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusList)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选择数据，点击按钮
        ElementUtil.click(self,driver,15,des,*self.tableCheckData)
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersStar)
        return 'success'

    def openWindowd(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        des='"纳入指示_纳入场所一括登录_纳入指示status为指示Mail送信済时选择一条点击纳入场所一括登录"'
        #   进入到纳入指示页面
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   选择納入指示済，点击查询
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusList)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选择数据，点击按钮
        ElementUtil.click(self,driver,15,des,*self.tableFristData)
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersStar)
        return 'success'

    def openWindowDo(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        des='"纳入指示_追加_纳入指示status指示Mail送信済时，纳入场所、纳入予定时间、时间为空时，点击追加"'
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   选择納入指示済，点击查询
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusList)
        ElementUtil.send_keys(self,driver,15,doNum,des,*self.queryDOInput)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选择数据，点击按钮
        ElementUtil.click(self,driver,15,des,*self.tableCheckData)
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersStar)
        #清空时间
        ElementUtil.clear(self,driver,15,des,*self.deliveryOrdersTime)
        r = ElementUtil.is_enabled(self,driver,15,des,*self.deliveryOrderszj)
        return r

    def openWindowDob(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        des='"纳入指示_追加_纳入指示status指示Mail送信済时，纳入场所、纳入予定时间不为空时、时间为空时，点击追加"'
            #   进入到纳入指示页面
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   选择納入指示済，点击查询
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusList)
        ElementUtil.send_keys(self,driver,15,doNum,des,*self.queryDOInput)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选择数据，点击按钮
        ElementUtil.click(self,driver,15,des,*self.tableCheckData)

        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersStar)
        #纳入场所
        ElementUtil.click(self, driver, 15, des,*self.deliveryOrdersnrcs)
        driver.execute_script("arguments[0].scrollIntoView();",
                              ElementUtil.getElement(self, driver, 15,des, *self.deliveryOrdersnrcsInput).get("element"))
        driver.execute_script('arguments[0].click()',
                              ElementUtil.getElement(self, driver, 15,des, *self.deliveryOrdersnrcsInput).get("element"))
        #   纳入予定日
        time.sleep(2)
        ElementUtil.click(self, driver, 15,des, *self.deliveryOrdersnrydr)
        #driver.execute_script("arguments[0].click();",ElementUtil.getElement(self,driver,15,*self.deliveryOrdersnrydr).get('element'))
        driver.execute_script("arguments[0].click();",ElementUtil.getElement(self,driver,15,des,*self.deliveryOrdersTimeList).get('element'))

        #   清空时间
        ElementUtil.clear(self,driver,15,des,*self.deliveryOrdersTime)
        r = ElementUtil.is_enabled(self,driver,15,des,*self.deliveryOrderszj)
        return r

    def openWindowDoc(self,driver,doNum,time,des):
        login = Login()
        login.test_click_login_btn(driver)
        #   进入到纳入指示页面
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   选择納入指示済，点击查询
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusList)
        ElementUtil.send_keys(self,driver,15,doNum,des,*self.queryDOInput)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选择数据，点击按钮
        ElementUtil.click(self,driver,15,des,*self.tableFristData)
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersStar)
        #   纳入场所
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersnrcs)
        driver.execute_script("arguments[0].scrollIntoView();",
                              ElementUtil.getElement(self,driver,15,des,*self.deliveryOrdersnrcsInput).get("element"))
        driver.execute_script('arguments[0].click()',
                              ElementUtil.getElement(self,driver,15,des,*self.deliveryOrdersnrcsInput).get("element"))
        #   纳入予定日
        ElementUtil.click(self, driver, 15,des, *self.deliveryOrdersnrydr)
        #driver.execute_script('arguments[0].click()',
                              #ElementUtil.getElement(self,driver,15,*self.deliveryOrdersnrydr).get("element"))
        driver.execute_script('arguments[0].click()',
                              ElementUtil.getElement(self,driver,15,des,*self.deliveryOrdersTimeList).get("element"))
        #   时间
        ElementUtil.send_keys(self,driver,15,time,des,*self.deliveryOrdersTime)
        r = ElementUtil.is_enabled(self,driver,15,des,*self.deliveryOrderszj)
        return r


    def openWindowDod(self,driver,doNum,time,des):
        login = Login()
        login.test_click_login_btn(driver)

        #   进入到纳入指示页面
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   选择納入指示済，点击查询
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusList)
        ElementUtil.send_keys(self,driver,15,doNum,des,*self.queryDOInput)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选择数据，点击按钮
        ElementUtil.click(self,driver,15,des,*self.tableCheckData)
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersStar)
        #   纳入场所
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersnrcs)
        driver.execute_script("arguments[0].scrollIntoView();", ElementUtil.getElement(self,driver,15,des,*self.deliveryOrdersnrcsInput).get("element"))
        driver.execute_script('arguments[0].click()', ElementUtil.getElement(self,driver,15,des,*self.deliveryOrdersnrcsInput).get("element"))
        # ElementUtil.click(self,driver,self.deliveryOrdersnrcsInput)
        #   纳入予定日
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersnrydr)
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersTimeList)
        #   时间
        ElementUtil.send_keys(self,driver,15,time,des,*self.deliveryOrdersTime)
        #ElementUtil.click(self,driver,15,*self.deliveryOrderszj)
        r = ElementUtil.is_enabled(self,driver,15,des,*self.deliveryOrderszj)
        return r
    def openWindowDoe(self,driver,doNum,time,desc,des):
        login = Login()
        login.test_click_login_btn(driver)

        #   进入到纳入指示页面
        ElementUtil.click(self,driver,15,des,*self.companiesStartElement)
        #   选择納入指示済，点击查询
        ElementUtil.click(self,driver,15,des,*self.queryShowStatus)
        ElementUtil.click(self,driver,15,des,*self.queryShowStatusList)
        ElementUtil.send_keys(self,driver,15,doNum,des,*self.queryDOInput)
        ElementUtil.click(self,driver,15,des,*self.queryButton)
        #   选择数据，点击按钮
        ElementUtil.click(self,driver,15,des,*self.tableCheckData)
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersStar)
        #   纳入场所
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersnrcs)
        driver.execute_script("arguments[0].scrollIntoView();", ElementUtil.getElement(self,driver,15,des,*self.deliveryOrdersnrcsInput).get("element"))
        driver.execute_script('arguments[0].click()', ElementUtil.getElement(self,driver,15,des,*self.deliveryOrdersnrcsInput).get("element"))
        # ElementUtil.click(self,driver,self.deliveryOrdersnrcsInput)
        #   纳入予定日
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersnrydr)
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersTimeList)
        #   时间
        ElementUtil.send_keys(self,driver,15,time,des,*self.deliveryOrdersTime)
        #   注释
        ElementUtil.click(self,driver,15,des,*self.deliveryOrdersTDesc)
        ElementUtil.clear(self,driver,15,des,*self.deliveryOrdersDesc)
        ElementUtil.send_keys(self,driver,15,desc,des,*self.deliveryOrdersDesc)

        r = ElementUtil.is_enabled(self,driver,15,des,*self.deliveryOrderszj)
        return r