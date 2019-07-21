"""
编写人:陈博华
"""
from time import sleep
from random import choice
from common.Wait import Wait
from common.Browser import Browser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException



def date_not_None(driver,locator1,locator2,locator3):
    """
    :param driver: 驱动实例
    :param locator1:日期输入框
    :param locator2:日期
    :param locator3:翻月
    """
    export_declaration_date = Browser(driver,10).get_attribute(locator1,"value")
    if export_declaration_date is None:
        choose_date(driver,locator1,locator2,locator3)


def choose_date(driver,locator1,locator2,locator3):
    """
    :param driver: 驱动实例
    :param locator1:日期输入框
    :param locator2:日期
    :param locator3:翻月
    """
    Browser(driver,10).click(locator1)
    sleep(1)
    element_list = driver.find_elements(*locator2)
    while element_list == []:
        Browser(driver,10).click(locator3)
        sleep(1)
        element_list = driver.find_elements(*locator2)
    while element_list != []:
        try:
            return choice(element_list).click()
        except WebDriverException:
            sleep(1)
            return choice(element_list).click()


def search_and_click(driver,locator1,locator2,locator3):
    """
    :param driver:驱动实例
    :param locator1:勾选框
    :param locator2:翻页
    :param locator3:常见元素
    """
    Wait(driver,10).elementwait(lambda x:x.find_element(*locator3))
    element_list = driver.find_elements(*locator1)
    while element_list == []:
        Browser(driver,10).click(locator2)
        Wait(driver,10).elementwait(lambda x:x.find_element(*locator3))
        element_list = driver.find_elements(*locator1)
    while element_list != []:
        try:
            return choice(element_list).send_keys(Keys.SPACE)
        except WebDriverException:
            sleep(1)
            return choice(element_list).send_keys(Keys.SPACE)