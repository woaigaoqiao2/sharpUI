'''
配送再确认信息修改
'''
from pageElement.doinfo.Edit import Edit
from business.Login import Login
from time import sleep
import datetime
from selenium.webdriver import ActionChains

class Edit(Edit):
    
    ##修改最终纳入场所   系统有bug无法保存
    
    ##修改纳入日期 保存
    def editDate(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #按状态检索
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #点击检索
        driver.find_element(*self.selElement).click()
        sleep(1)
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击配送再确定
        driver.find_element(*self.reconDoElement).click()
        sleep(5)
        #修改纳入日期
        driver.find_element(*self.inclusionDateElement).click()
        sleep(1)
        driver.find_element(*self.selInclusionDateElement).click()
        #点击保存
        driver.find_element(*self.saveElement).click()
        sleep(1)
        #确定
        driver.find_element(*self.determineElement).click()
        
    ##修改纳入日期 返回
    def editDateR(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #按状态检索
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #点击检索
        driver.find_element(*self.selElement).click()
        sleep(1)
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击配送再确定
        driver.find_element(*self.reconDoElement).click()
        sleep(5)
        #修改纳入日期
        driver.find_element(*self.inclusionDateElement).click()
#         d = driver.find_element(*self.inclusionDateElement)
#         driver.execute_script('arguments[0].removeAttribute("readonly")', d)
#         driver.find_element(*self.inclusionDateElement).send_keys('1234')
        sleep(1)
        driver.find_element(*self.selInclusionDateElement).click()
        #点击保存
        driver.find_element(*self.returnElement).click()
        
    ##修改纳入时间 保存
    def editTime(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #按状态检索
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #点击检索
        driver.find_element(*self.selElement).click()
        sleep(1)
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击配送再确定
        driver.find_element(*self.reconDoElement).click()
        sleep(5)
        #修改纳入时间
        time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        time = time[8:12]
        action = ActionChains(driver)
        ele = driver.find_element(*self.inclusionTimeElement)
        action.double_click(ele).perform()
        driver.find_element(*self.inclusionTimeElement).send_keys(time)
        #点击保存
        driver.find_element(*self.saveElement).click()
        sleep(1)
        #确定
        driver.find_element(*self.determineElement).click()
        
    ##修改纳入时间 返回
    def editTimeR(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #按状态检索
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #点击检索
        driver.find_element(*self.selElement).click()
        sleep(1)
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击配送再确定
        driver.find_element(*self.reconDoElement).click()
        sleep(5)
        #修改纳入时间
        time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        time = time[8:12]
        action = ActionChains(driver)
        ele = driver.find_element(*self.inclusionTimeElement)
        action.double_click(ele).perform()
        driver.find_element(*self.inclusionTimeElement).send_keys(time)
        #点击保存
        driver.find_element(*self.returnElement).click()
        
    ##修改纳入日期和时间 保存
    def editDateAndTime(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        sleep(5)
        #点击首页DO确定
        driver.find_element(*self.DOElement).click()
        sleep(5)
        #按状态检索
        driver.find_element(*self.DOstatusElement).click()
        driver.find_element(*self.selDOstatusElement).click()
        #点击检索
        driver.find_element(*self.selElement).click()
        sleep(1)
        #选择数据
        driver.find_element(*self.selDateElement).click()
        #点击配送再确定
        driver.find_element(*self.reconDoElement).click()
        sleep(5)
        #修改纳入日期
        driver.find_element(*self.inclusionDateElement).click()
        sleep(1)
        driver.find_element(*self.selInclusionDateElement).click()
        #修改纳入时间
        time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        time = time[8:12]
        action = ActionChains(driver)
        ele = driver.find_element(*self.inclusionTimeElement)
        action.double_click(ele).perform()
        driver.find_element(*self.inclusionTimeElement).send_keys(time)
        #点击保存
        driver.find_element(*self.saveElement).click()
        sleep(1)
        #确定
        driver.find_element(*self.determineElement).click()
        
        