#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 9:51
# @Author  : 二部测试-陈兴川
# @File    : acceptverify.py
#@email    :chenxingchuan@chinasoftinc.com

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  common.loggen import Logger
import datetime,os,time

logger=Logger("basepage").getlog()
class Basepage:
    def __init__(self,driver):
        self.driver=driver

    def wait_elevisible(self,locator,doc='',times=30,poll_frequency=0.3):

        try:
            now=datetime.datetime.now()
            logger.info("开始等待元素：{} 可见！ ".format(locator))
            WebDriverWait(self.driver,times,poll_frequency).until(EC.visibility_of_all_elements_located(locator))
            now1=datetime.datetime.now()
            wait_time=now1-now
            logger.info("等待元素可见的时长为：{}".format(wait_time))
        except:
            logger.exception("等待元素：{} 可见失败！！".format(locator))
            self.save_sreenshort(doc)
            raise


    def save_sreenshort(self,picture_name1):
        date1=time.strftime('%Y%m%d&%H%M', time.localtime(time.time()))
        picture_name=os.path.abspath(__file__)
        picture_name=os.path.split(picture_name)[0]
        picture_name=os.path.split(picture_name)[0]+"\\screenShot\\"+picture_name1+date1+".png"
        self.driver.save_screenshot(picture_name)
        logger.info("截图成功！文件路径为：{}".format(picture_name))

    def get_element(self,locator,doc=""):
        logger.info("查找元素：{}".format(locator))
        # self.wait_elevisible(locator,doc)
        try:
            return self.driver.find_element(*locator)
        except:
            logger.exception("查找元素：{} 失败！".format(locator))
            self.save_sreenshort(doc)
            raise

    def click_element(self,locator,doc=''):
        logger.info("在{}点击元素：{}".format(doc,locator))
        ele=self.get_element(locator,doc)
        try:
            ele.click()
        except:
            logger.exception("点击元素：{} 失败！".format(locator))
            self.save_sreenshort(doc)

    def input_text(self,locator,doc='',text=''):
        logger.info("在{}对元素：{} 进行输入操作".format(doc,locator))
        ele=self.get_element(locator,doc)
        try:
            ele.clear()
            ele.send_keys(text)
        except:
            logger.exception("对元素：{} 进行输入操作失败！".format(locator))
            self.save_sreenshort(doc)
    def get_element_text(self,locator,doc=''):
        logger.info("在{}获取元素：{} 的文本内容".format(doc,locator))
        ele=self.get_element(locator,doc)
        try:
           return ele.text
        except:
            logger.exception("获取元素：{} 文本内容失败！".format(locator))
            self.save_sreenshort(doc)

# if __name__=="__main__":
#     b=Basepage()
#     b.save_sreenshort('1')

    def get_element_demo(self,locator,attribute_name,doc=""):
        logger.info("查找元素：{}".format(locator))
        # self.wait_elevisible(locator,doc)
        try:
            for i in range(5):
                time.sleep(1.5)
                try:
                    c=self.driver.find_element(*locator).get_attribute(attribute_name)
                finally:
                    if c!=None:
                        break
            return self.driver.find_element(*locator)
        except:
            logger.exception("查找元素：{} 失败！".format(locator))
            self.save_sreenshort(doc)
            raise
