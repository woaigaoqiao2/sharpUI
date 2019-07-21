'''
增加费用
'''
from pageElement.outward.AddCostElement import AddCostElement
from business.Login import Login
from time import sleep
from selenium.webdriver import ActionChains
from util.ElementUtil import ElementUtil
from selenium.webdriver.common.keys import Keys
from business.outward.GetBLNO import GetBLNO


class AddCost(AddCostElement):

    gb = GetBLNO()
    BLNO = gb.test()

    ##doc费用增加
    def docfee(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO 
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        sleep(3)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.DOCFEElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        eu.send_keys(driver,15,'1000','doc费用增加',*self.DOCFEElement)
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)


        
    ##tax费用增加
    def docTax(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO 
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.DOCtaxElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        driver.find_element(*self.DOCtaxElement).send_keys(1000)
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)

        
    ##other charge费用增加
    def otherCharge(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO 
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)

        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.otherElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        driver.find_element(*self.otherElement).send_keys(1000)
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)

        
    ##20F费用增加
    def TwoF(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.twoFElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        driver.find_element(*self.twoFElement).send_keys(1000)
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)

        
    ##40F费用增加
    def fourF(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.fourFElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        driver.find_element(*self.fourFElement).send_keys(1000)
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)


        
        
    ##DOC FEE和DOC tax费用增加
    def docfeeAndTax(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.DOCFEElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        driver.find_element(*self.DOCFEElement).send_keys(1000)
        
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)


        
    ##DOC FEE和other费用增加
    def docfeeAndOther(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.otherElement)
        action.double_click(on_element).perform()

        #输入DOCFEE金额为1000
        driver.find_element(*self.otherElement).send_keys(1000)
        
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)


        
        
    ##DOC FEE和20F费用增加
    def docfeeAndTwoF(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.twoFElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        driver.find_element(*self.twoFElement).send_keys(1000)
        
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)


        
    ##DOC FEE和40F费用增加
    def docfeeAndFourF(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.fourFElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        driver.find_element(*self.fourFElement).send_keys(1000)
        
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)


        
    ##DOC FEE,tax和40F费用增加
    def docfeeTaxAndFourF(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.DOCtaxElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        driver.find_element(*self.DOCtaxElement).send_keys(1000)
        
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)


        
    ##DOC FEE,tax和20F费用增加
    def docfeeTaxAndTwoF(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15,self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.twoFElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        driver.find_element(*self.twoFElement).send_keys(1000)
        
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)


        
    ##DOCFEE,40F和20F费用增加
    def docfeeFourFAndTwoF(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.twoFElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        driver.find_element(*self.twoFElement).send_keys(1000)
        
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)


        
    ##DOCFEE,other和20F费用增加
    def docfeeOtherAndTwoF(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)

        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.otherElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        driver.find_element(*self.otherElement).send_keys(1000)
        
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        # 点击确定
        eu.click(driver, 15, 'doc费用增加',*self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)

        
    ##DOCFEE,other和20F费用增加
    def full(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'doc费用增加',*self.outWardElement)
        #输入B/L NO
        eu.send_keys(driver, 15, self.BLNO,'doc费用增加',*self.BLNoEelement)
        #点击检索
        eu.click(driver,15,'doc费用增加',*self.selElement)
        #选择要修改的数据
        el = driver.find_element(*self.selDateElement)
        el.send_keys(Keys.SPACE)
        #点击编辑
        eu.click(driver,15,'doc费用增加',*self.editElement)
        
        #双击金额文本框
        action = ActionChains(driver)
        on_element = driver.find_element(*self.fourFElement)
        action.double_click(on_element).perform()
        #输入DOCFEE金额为1000
        driver.find_element(*self.fourFElement).send_keys(1000)
        
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #点击海上航空计算
        eu.click(driver,15,'doc费用增加',*self.costCalElement)
        sleep(8)
        #点击确定
        eu.click(driver, 15,'doc费用增加', *self.doElement)
        # 点击返回
        eu.click(driver, 15, 'doc费用增加',*self.backElement)
