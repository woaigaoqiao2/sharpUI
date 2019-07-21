import time
from pageElement.SAlogin.SaSearch import SaSearch
from selenium.webdriver.common.keys import Keys
from util.ElementUtil import ElementUtil

class SaSearch(SaSearch):

    def __init__(self, driver):
        self.driver = driver
        time.sleep(3)
        ElementUtil.click(self,self.driver,10,'SaSearch每次登陆后点击第一个模块',*self.SA_button_element)   # 每次登陆后点击页面第一个模块
        time.sleep(2)


    def ETATimeSearch(self):
        time.sleep(2)
        d = self.driver.find_element_by_xpath('//input[@aria-label="ETA"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(2)
        ElementUtil.getElement(self,self.driver,10,'根据ETA 时间段搜索数据',*self.ETA_start_date_element)
        self.driver.find_element(*self.ETA_start_date_element).send_keys('2019-01-01')
        time.sleep(2)
        d = self.driver.find_element_by_xpath('//div[@label="ETA"]/../..//input[@aria-label="~"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(2)
        ElementUtil.getElement(self, self.driver, 5,'根据ETA 时间段搜索数据',*self.ETA_end_date_element)
        self.driver.find_element(*self.ETA_end_date_element).send_keys('2020-02-02')
        ElementUtil.click(self,self.driver,10,'根据ETA 时间段搜索数据',*self.search_element)
        time.sleep(2)
        result=ElementUtil.getText(self,self.driver,10,'根据ETA 时间段搜索数据',*self.SA_jieGuo)
        time.sleep(1)
        return  result


    def ETDTimeEndSearch(self):
        time.sleep(2)
        d = self.driver.find_element_by_xpath('//div[@label="ETD"]/../..//input[@aria-label="~"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(2)
        self.driver.find_element(*self.ETD_end_date_element).send_keys('2020-05-01')
        time.sleep(2)
        ElementUtil.click(self, self.driver, 5,'根据ETD结束日期搜索数据',*self.search_element)
        time.sleep(2)
        result = ElementUtil.getText(self, self.driver,10,'根据ETD结束日期搜索数据',*self.SA_jieGuo)
        return  result


    def ETDTimeStartSearch(self):
        time.sleep(2)
        d = self.driver.find_element_by_xpath('//input[@aria-label="ETD"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(2)
        self.driver.find_element(*self.ETD_start_date_element).send_keys('2019-01-01')
        time.sleep(2)
        ElementUtil.click(self,self.driver,10,'根据ETD开始日期搜索数据',*self.search_element)
        time.sleep(2)
        result = ElementUtil.getText(self, self.driver,10,'根据ETD开始日期搜索数据',*self.SA_jieGuo)
        return result


    def ETDTimeStartEndSearch(self):
        time.sleep(2)
        d = self.driver.find_element_by_xpath('//input[@aria-label="ETD"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(2)
        self.driver.find_element(*self.ETD_start_date_element).send_keys('2019-01-01')
        time.sleep(2)
        d = self.driver.find_element_by_xpath('//div[@label="ETD"]/../..//input[@aria-label="~"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(2)
        self.driver.find_element(*self.ETD_end_date_element).send_keys('2020-02-02')
        time.sleep(2)
        ElementUtil.click(self, self.driver,10,'根据ETD开始结束日期搜索数据',*self.search_element)
        time.sleep(2)
        result = ElementUtil.getText(self, self.driver,10,'根据ETD开始结束日期搜索数据',*self.SA_jieGuo)
        return result


    def InvoiceNoSearch(self):
        time.sleep(2)
        ElementUtil.clear(self,self.driver,10,'根据invoiceNo搜索数据',*self.InvoiceNo)
        time.sleep(2)
        ElementUtil.send_keys(self,self.driver,10,'15874D','根据invoiceNo搜索数据',*self.InvoiceNo)
        time.sleep(2)
        ElementUtil.click(self, self.driver,10,'根据invoiceNo搜索数据',*self.search_element)
        time.sleep(2)
        result = ElementUtil.getText(self, self.driver,10,'根据invoiceNo搜索数据',*self.SA_jieGuo)
        return result


    def VolNOSearch(self):
        time.sleep(2)
        ElementUtil.clear(self,self.driver,10,'根据Vol NO搜索数据',*self.VolNO)
        time.sleep(2)
        ElementUtil.send_keys(self, self.driver,10,'KE0862','根据Vol NO搜索数据',*self.VolNO)
        time.sleep(2)
        ElementUtil.click(self,self.driver,10,'根据Vol NO搜索数据',*self.search_element)
        time.sleep(4)
        result = ElementUtil.getText(self,self.driver,10,'根据Vol NO搜索数据',*self.SA_jieGuo)
        return result


    def BenShipping(self):
        time.sleep(2)
        ElementUtil.clear(self, self.driver,10,'根据Vol NO搜索数据',*self.benchuan)
        ElementUtil.send_keys(self,self.driver,10,'shipsname','根据本船名搜索数据',*self.benchuan)
        time.sleep(2)
        ElementUtil.click(self, self.driver,10,'根据本船名搜索数据',*self.search_element)
        time.sleep(4)
        result = ElementUtil.getText(self,self.driver,10,'根据本船名搜索数据',*self.SA_jieGuo)
        return result


    def ShippingSheSearch(self):
        time.sleep(2)
        ElementUtil.clear(self,self.driver,10,'根据船社・航空会社搜索数据',*self.ShippingShe)
        ElementUtil.send_keys(self, self.driver, 5, 'F20564','根据船社・航空会社搜索数据',*self.ShippingShe)
        self.driver.find_element(*self.ShippingShe).send_keys(Keys.ENTER)
        time.sleep(2)
        ElementUtil.click(self,self.driver,10,'根据船社・航空会社搜索数据',*self.search_element)
        time.sleep(4)
        result = ElementUtil.getText(self,self.driver,10,'根据船社・航空会社搜索数据',*self.SA_jieGuo)
        return result


    def HaiWaiQu(self):
        ElementUtil.send_keys(self,self.driver,10,'70192:TSMC','根据海外取引先搜索数据',*self.haiwaiquyinxian_element)
        time.sleep(2)
        self.driver.find_element(*self.haiwaiquyinxian_element).send_keys(Keys.ENTER)
        time.sleep(2)
        ElementUtil.click(self,self.driver,10,'根据海外取引先搜索数据',*self.search_element)
        time.sleep(4)
        result = ElementUtil.getText(self,self.driver,10,'根据海外取引先搜索数据',*self.SA_jieGuo)
        return result


    def LuYang(self):
        ElementUtil.send_keys(self,self.driver,10,'OSK','根据陸揚港搜索数据',*self.LuYang_element)
        time.sleep(2)
        self.driver.find_element(*self.LuYang_element).send_keys(Keys.ENTER)
        time.sleep(2)
        ElementUtil.click(self,self.driver,10,'根据陸揚港搜索数据',*self.search_element)
        time.sleep(4)
        result = ElementUtil.getText(self,self.driver,10,'根据陸揚港搜索数据',*self.SA_jieGuo)
        return result


    def ZheChu(self):
        ElementUtil.send_keys(self,self.driver,10,'AXT','根据積出港搜索数据',*self.ZheChu_element)
        time.sleep(2)
        self.driver.find_element(*self.ZheChu_element).send_keys(Keys.ENTER)
        time.sleep(2)
        ElementUtil.click(self, self.driver,10,'根据積出港搜索数据',*self.search_element)
        time.sleep(4)
        result = ElementUtil.getText(self,self.driver,10,'根据積出港搜索数据',*self.SA_jieGuo)
        return result


    def XingTai(self):
        time.sleep(1)
        ElementUtil.click(self,self.driver,10,'根据輸送形態搜索数据',*self.xingtai_element) # 点击形态下拉框
        ElementUtil.click(self, self.driver,10,'根据輸送形態搜索数据',*self.sea_element)
        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'根据輸送形態搜索数据',*self.search_element)
        time.sleep(4)
        result = ElementUtil.getText(self,self.driver,10,'根据輸送形態搜索数据',*self.SA_jieGuo)
        return result


    def YiLaiStart(self):
        time.sleep(2)
        d = self.driver.find_element_by_xpath('//input[@aria-label="依頼日"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(2)
        self.driver.find_element(*self.Yai_start_date_element).send_keys('2018-01-01')
        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'根据依賴开始日期搜索数据',*self.search_element)
        time.sleep(4)
        result = ElementUtil.getText(self,self.driver,10,'根据依賴开始日期搜索数据',*self.SA_jieGuo)
        return result


    def YiLaiEnd(self):
        time.sleep(2)
        d = self.driver.find_element_by_xpath('//div[@label="依頼日"]/../..//input[@aria-label="~"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(2)
        self.driver.find_element(*self.Yai_end_date_element).send_keys('2022-05-01')
        time.sleep(1)
        ElementUtil.click(self,self.driver,10,'根据依賴结束搜索数据',*self.search_element)
        time.sleep(4)
        result = ElementUtil.getText(self,self.driver,10,'根据依賴结束搜索数据',*self.SA_jieGuo)
        return result


    def YiLaiStartEnd(self):
        time.sleep(2)
        d = self.driver.find_element_by_xpath('//input[@aria-label="依頼日"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(2)
        self.driver.find_element(*self.Yai_start_date_element).send_keys('2018-01-01')
        time.sleep(2)
        d = self.driver.find_element_by_xpath('//div[@label="依頼日"]/../..//input[@aria-label="~"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(2)
        self.driver.find_element(*self.Yai_end_date_element).send_keys('2022-05-01')
        time.sleep(1)
        ElementUtil.click(self,self.driver,10,'根据依賴开始结束搜索数据',*self.search_element)
        time.sleep(4)
        result = ElementUtil.getText(self,self.driver,10,'根据依賴开始结束搜索数据',*self.SA_jieGuo)
        return result
