"""
Created on 2019年7月8日

bussinsess操作类
@author: chinasoft.c.deng

"""
from pageElement.CompaniesPageElement import CompaniesPageElement
from time import sleep
from util.ElementUtil import ElementUtil
from business.Login import Login

class GoodsfhBussinses(CompaniesPageElement):
    def goodsfenNoData(self,driver):
        des="纳入指示_D/O分け_未选择任何数据时，点击D/O分け"
        login = Login()
        login.test_click_login_btn(driver)

        # 进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des,*self.companiesStartElement)
        # 点击D/O分け
        r=ElementUtil.is_enabled(self,driver,15, des,*self.DOfenButton)
        return r
    def goodsfManyData(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示_D/O分け_选择多条数据时，点击D/O分け"
        # 进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        # 点击检索，选择多条数据
        ElementUtil.click(self, driver, 15, des, *self.queryButton)
        ElementUtil.click(self, driver, 15, des, *self.tableCheckData)
        sleep(2)
        # 点击D/O分
        r=ElementUtil.is_enabled(self,driver,15, des,*self.DOfenButton)
        return r
    def goodsfNR(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        des = "纳入指示_D/O分け_纳入指示status为納入指示済时，点击D/O分け"
        # 进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        # 选择纳入指示status为納入指示済
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatusListn)
        sleep(2)
        #点击D/O分
        r = ElementUtil.is_enabled(self, driver, 15, des, *self.DOfenButton)
        return r

    def goodsfZS(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        des = "纳入指示_D/O分け_纳入指示status为指示Mail送信済时，点击D/O分け"
        # 进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        # 选择纳入指示status为指示Mail送信済,输入可拆分的D/O No参数
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatusList)
        ElementUtil.send_keys(self,driver,15, doNum,des,*self.queryDOInput)
        # 检索
        ElementUtil.click(self, driver, 15, des, *self.queryButton)
        # 选择一条数据
        ElementUtil.click(self, driver, 15, des, *self.tableFristData)
        # 点击D/O分
        ElementUtil.click(self, driver, 15, des, *self.DOfenButton)
        # 进入详情页
        sleep(2)
        ele = ElementUtil.getElement(self,driver,15, des,*self.Headlinexq)
        r=ele.get('element').text
        return r
    def goodshNoData(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示_D/O合併_未选择任何数据时，点击D/O合併"
        # 点击进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        # 点击D/O合併
        r = ElementUtil.is_enabled(self, driver, 15, des, *self.DOheButton)
        return r
    def goodshManyData(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示_D/O合併_选择多条数据时，点击D/O合併"
        # 点击进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        # 点击检索，选择多条数据
        ElementUtil.click(self, driver, 15, des, *self.queryButton)
        ElementUtil.click(self, driver, 15, des, *self.tableCheckData)
        sleep(2)
        # 点击D/O分
        r = ElementUtil.is_enabled(self, driver, 15, des, *self.DOheButton)
        return r
    def goodshNR(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示_D/O分け_纳入指示status为納入指示済时，点击D/O合併"
        # 进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        # 选择纳入指示status为納入指示済
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatusListn)
        sleep(2)
        # 点击D/O合
        r = ElementUtil.is_enabled(self, driver, 15, des, *self.DOheButton)
        return r
    def NoOperationSave(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示_D/O分け_详细情报页中无任何操作,点击保存"
        # 进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        # 选择纳入指示status为指示Mail送信済,输入可分け的D/O No参数
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatusList)
        ElementUtil.send_keys(self, driver, 15,  doNum, des,*self.queryDOInput)
        # 检索
        ElementUtil.click(self, driver, 15, des, *self.queryButton)
        # 选择一条数据
        ElementUtil.click(self, driver, 15, des, *self.tableFristData)
        # 点击D/O分
        ElementUtil.click(self, driver, 15, des, *self.DOfenButton)
        sleep(3)
        #点击保存
        r = ElementUtil.is_enabled(self,driver,15, des,*self.SaveButton)
        return r
    def NoChoseSplit(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示_D/O分け_详细情报页中不选择任何数据,点击split"
        # 进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        # 选择纳入指示status为指示Mail送信済,输入可拆分的D/O No参数
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatusList)
        ElementUtil.send_keys(self, driver, 15, doNum, des, *self.queryDOInput)
        # 检索
        ElementUtil.click(self, driver, 15, des, *self.queryButton)
        # 选择一条数据
        ElementUtil.click(self, driver, 15, des, *self.tableFristData)
        # 点击D/O分
        ElementUtil.click(self, driver, 15, des, *self.DOfenButton)
        ElementUtil.click(self, driver, 15, des, *self.SplitButton)
        ele = ElementUtil.getElement(self, driver, 15, des, *self.NoChosePrompt)
        r = ele.get('element').text
        print(r)
        return r
    def ChoseDataSplit(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示_D/O分け_详细情报页中选择所有数据，点击split"
        # 进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        # 选择纳入指示status为指示Mail送信済,输入可拆分的D/O No参数
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatusList)
        ElementUtil.send_keys(self, driver, 15, doNum, des, *self.queryDOInput)
        # 检索
        ElementUtil.click(self, driver, 15, des, *self.queryButton)
        # 选择一条数据
        ElementUtil.click(self, driver, 15, des, *self.tableFristData)
        # 点击D/O分
        ElementUtil.click(self, driver, 15, des, *self.DOfenButton)
        # 选择详细列表数据
        sleep(1)
        ElementUtil.click(self,driver, 15, des, *self.XQchackBoxData)
        # 点击split
        ElementUtil.click(self,driver, 15, des, *self.SplitButton)
        r=ElementUtil.getElement(self,driver, 15, des, *self.SplitXC).get('element').text
        return r

    def ChoseDataSplitone(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示_D/O分け_详细情报页中选择一条数据，点击split"
        # 进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        # 选择纳入指示status为指示Mail送信済,输入可拆分的D/O No参数
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatusList)
        ElementUtil.send_keys(self, driver, 15, doNum, des, *self.queryDOInput)
        # 检索
        ElementUtil.click(self, driver, 15, des, *self.queryButton)
        # 选择一条数据
        ElementUtil.click(self, driver, 15, des, *self.tableFristData)
        # 点击D/O分
        ElementUtil.click(self, driver, 15, des, *self.DOfenButton)
        # 选择详细列表数据
        sleep(1)
        ElementUtil.click(self,driver, 15, des, *self.XQchackFirstData)
        # 点击split
        ElementUtil.click(self,driver, 15, des, *self.SplitButton)
        r=ElementUtil.getElement(self,driver, 15, des, *self.SplitXC).get('element').text
        return r

    def SplitSave(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示_D/O分け_详细情报页中选择所有数据，点击split,点击保存"
        # 进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        sleep(2)
        # 选择纳入指示status为指示Mail送信済,输入可拆分的D/O No参数
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatusList)
        ElementUtil.send_keys(self, driver, 15, doNum, des, *self.queryDOInput)
        # 检索
        ElementUtil.click(self, driver, 15, des, *self.queryButton)
        sleep(1)
        # 选择一条数据
        ElementUtil.click(self, driver, 15, des, *self.tableFristData)
        # 点击D/O分
        ElementUtil.click(self, driver, 15, des, *self.DOfenButton)
        # 选择详细列表数据
        sleep(1)
        ElementUtil.click(self, driver, 15, des, *self.XQchackBoxData)
        # 点击split
        ElementUtil.click(self, driver, 15, des, *self.SplitButton)
        # 点击保存
        ElementUtil.click(self,driver,15, des,*self.XQsave)
        sleep(2)
        a = ElementUtil.getElement(self,driver,15, des,*self.XQsaveCG)
        r=a.get('element').text
        return r
    def GoodshZS(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        # 进入到纳入指示页面
        des="纳入指示_D/O合併_指示Mail送信济时，选择一条数据，点击D/O合併"
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        sleep(3)
        # 选择纳入指示status为指示Mail送信済,输入合并的包裹的D/O No参数
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatusList)
        ElementUtil.send_keys(self, driver, 15, doNum, des, *self.queryDOInput)
        # 检索
        ElementUtil.click(self, driver, 15, des, *self.queryButton)
        sleep(3)
        # 选择一条数据
        ElementUtil.click(self, driver, 15, des, *self.tableFristData)
        # 点击D/O合併
        ElementUtil.click(self,driver,15, des,*self.DOheButton)
        sleep(5)
        a= ElementUtil.getElement(self,driver,15, des,*self.DOheCG)
        sleep(1)
        r=a.get('element').text
        return r
    def SplitQuit(self,driver,doNum):
        login = Login()
        login.test_click_login_btn(driver)
        des="纳入指示_D/O分け_详细情报页中,点击退出"
        # 进入到纳入指示页面
        ElementUtil.click(self, driver, 15, des, *self.companiesStartElement)
        # 选择纳入指示status为指示Mail送信済,输入可分け的D/O No参数
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatus)
        ElementUtil.click(self, driver, 15, des, *self.queryShowStatusList)
        ElementUtil.send_keys(self, driver, 15, doNum, des, *self.queryDOInput)
        # 检索
        ElementUtil.click(self, driver, 15, des, *self.queryButton)
        # 选择一条数据
        ElementUtil.click(self, driver, 15, des, *self.tableFristData)
        # 点击D/O分
        ElementUtil.click(self, driver, 15, des, *self.DOfenButton)
        ElementUtil.click(self, driver, 15, des, *self.QuitButton)
        sleep(1)
        ele=ElementUtil.getElement(self, driver, 15, des, *self.QXNRTittle)
        r=ele.get('element').text
        return r