"""
编写人：陈博华
"""
from .Wait import Wait
from random import choice
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from time import sleep


class Browser(object):


    def __init__(self, driver, timeout,interval_time=None):
        """
        :param driver: 驱动实例
        :param timeout: 超时时间
        :param interval_time:间隔时间
        """
        self._driver = driver
        self._timeout = timeout
        self._interval_time = interval_time


    def click(self, locator):
        Wait(self._driver,self._timeout,self._interval_time).elementdisplay()
        Wait(self._driver,self._timeout,self._interval_time).elementwait(lambda x:x.find_element(*locator))
        return Wait(self._driver,self._timeout,self._interval_time).until(lambda x:x.find_element(*locator).click())


    def send_keys(self, locator, value):
        Wait(self._driver,self._timeout,self._interval_time).elementdisplay()
        Wait(self._driver,self._timeout,self._interval_time).elementwait(lambda x:x.find_element(*locator))
        return Wait(self._driver,self._timeout,self._interval_time).until(lambda x:x.find_element(*locator).send_keys(value))


    def clear(self, locator):
        # print(locator)
        # print("------------搜索元素------------")
        Wait(self._driver,self._timeout,self._interval_time).elementwait(lambda x:x.find_element(*locator))
        # print("-----------元素已找到-----------")
        Wait(self._driver,self._timeout,self._interval_time).until(lambda x:x.find_element(*locator).send_keys(Keys.CONTROL,"a"))
        return Wait(self._driver,self._timeout,self._interval_time).until(lambda x:x.find_element(*locator).send_keys(Keys.DELETE))


    def choice_select(self, locator):
        """随机下拉框选取"""
        # print(locator)
        # print("------------搜索元素------------")
        Wait(self._driver,self._timeout,self._interval_time).elementwait(lambda x:x.find_element(*locator))
        # print("-----------元素已找到-----------")
        elements = self._driver.find_elements(*locator)
        while elements != []:
            try:
                return choice(elements).click()
            except WebDriverException:
                sleep(1)
                return choice(elements).click()


    def choice_check_box(self, locator):
        """随机输入框勾选"""
        # print(locator)
        # print("------------搜索元素------------")
        Wait(self._driver,self._timeout,self._interval_time).elementwait(lambda x:x.find_element(*locator))
        # print("-----------元素已找到-----------")
        elements = self._driver.find_elements(*locator)
        while elements != []:
            try:
                return choice(elements).send_keys(Keys.SPACE)
            except WebDriverException:
                sleep(1)
                return choice(elements).send_keys(Keys.SPACE)


    def get_attribute(self, locator, attribute):
        # print(locator)
        # print("----------等待元素加载----------")
        Wait(self._driver,self._timeout,self._interval_time).elementdisplay()
        # print("------------搜索元素------------")
        Wait(self._driver,self._timeout,self._interval_time).elementwait(lambda x:x.find_element(*locator))
        # print("-----------元素已找到-----------")
        return Wait(self._driver,self._timeout,self._interval_time).until(lambda x:x.find_element(*locator).get_attribute(attribute))


    def get_text(self, locator):
        # print(locator)
        # print("----------等待元素加载----------")
        Wait(self._driver,self._timeout,self._interval_time).elementdisplay()
        # print("------------搜索元素------------")
        Wait(self._driver,self._timeout,self._interval_time).elementwait(lambda x:x.find_element(*locator))
        # print("-----------元素已找到-----------")
        return Wait(self._driver,self._timeout,self._interval_time).until(lambda x:x.find_element(*locator).text)