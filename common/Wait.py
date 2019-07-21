# coding=utf-8
"""
编写人：陈博华
"""
import time
from selenium.common import exceptions


class Wait(object):


    def __init__(self, driver, timeout, interval_time=None):
        """
        timeout超时设置
        interval_time 间歇等待时间
        """
        self._driver = driver
        self._timeout = timeout
        self._interval_time = interval_time
        if not self._interval_time:
            self._interval_time = 1
        self._end_time = time.time() + self._timeout


    def until(self, method, message=''):
        """
        对定位元素进行操作
        :param method:方法（建议用lambda函数）
        :param message:报错信息
        """
        if time.time() > self._end_time:
            raise exceptions.TimeoutException(message)
        else:
            try:
                value = method(self._driver)
                if value:
                    return value
            except exceptions.WebDriverException:
                time.sleep(self._interval_time)
                return self.until(method)


    def elementwait(self, method, message=''):
        """
        搜索元素
        """
        if time.time() > self._end_time:
            raise exceptions.TimeoutException(message)
        else:
            try:
                value = method(self._driver)
                if value:
                    return value
            except exceptions.NoSuchElementException:
                time.sleep(self._interval_time)
                return self.elementwait(method)


    def elementdisplay(self, message=''):
        """
        等待页面加载
        """
        flag = self._driver.execute_script("return document.readyState")
        while True:
            if flag == "complete":
                return True
            else:
                time.sleep(self._interval_time)
                flag = self._driver.execute_script("return document.readyState")
            if time.time() > self._end_time:
                break
        raise exceptions.TimeoutException(message)
