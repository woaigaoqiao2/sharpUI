#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 9:42
# @Author  : 二部测试-陈兴川
# @File    : acceptverify.py
#@email    :chenxingchuan@chinasoftinc.com

from pageElement.Accept_Verify.acceptverify import Accept_Verify
from common.basepage import Basepage
from common.loggen import Logger
from selenium.webdriver.common.by import By
import time,re

logger=Logger("acceptverify.py").getlog()
class AcceptVerify(Accept_Verify,Basepage):
    def selectETA(self,etastart,etaend):
        self.wait_box()
        if etastart!="null":
            self.time_cha(etastart,self.eta_start,self.time_left,self.time_r,self.time_day,self.select_year)
            logger.info("输入EAT开始时间:{}".format(etastart))
        if etaend != "null":
            self.time_cha(etaend, self.eta_end, self.te_left, self.te_r, self.te_day, self.s_year)
            logger.info("输入EAT结束时间:{}".format(etaend))

    def click_search_buttom(self):
        self.click_element(self.search_buttom,"点击検索按钮")
        logger.info("点击検索按钮")

    def selectETD(self,etdstart,etdend):
        self.wait_box()
        if etdstart!="null":
            self.time_cha(etdstart, self.etd_start, self.etime_left, self.etime_r, self.etime_day, self.e_syear)
            logger.info("输入ETD开始时间:{}".format(etdstart))
        if etdend != "null":
            self.time_cha(etdend, self.etd_end, self.eetime_left, self.eetime_r, self.eetime_day, self.ee_syear)
            logger.info("输入ETD结束时间:{}".format(etdend))

    def input_container_no(self,containercoed):
        self.wait_box()
        self.input_text(self.container_no,"输入集装箱号",containercoed)
        logger.info("输入集装箱号码")

    def get_result(self):
        self.wait_box()
        arr = []
        # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
        table_tr_list = self.get_element(self.select_result).find_elements(By.TAG_NAME, "tr")
        logger.info("找到查询结果的表格")
        for r, tr in enumerate(table_tr_list, 1):
            # 以空格拆分成若干个(个数与列的个数相同)一维列表
            arr1 = []
            table_td_list = tr.find_elements_by_tag_name('td')
            for c, td in enumerate(table_td_list):
                arr1.append(td.text)
            arr.append(arr1)
        a = arr[2:]
        return a

    def time_cha(self,data,loc,left,reght,day,year):
        self.wait_box()
        self.click_element(loc)
        b = re.sub(r'\D', "", data)
        logger.info("{}的年月：{}".format(data,b))
        while 1:
            time.sleep(1)
            a = self.get_element_text(year)
            logger.info("时间插件上的年月：{}".format(a))
            a = re.sub(r'\D', "", a)
            if len(a) == 5:
                a = a[0:4] + "0" + a[4]
            if int(a) > int(b[:6]):
                self.click_element(left)
            elif int(a) < int(b[:6]):
                self.click_element(reght)
            else:
                break
        a = list(day)
        c = int(b[6:])
        a[1] = a[1].replace("{}", str(c))
        day = tuple(a)
        self.click_element(day)

    def wait_box(self):
        time.sleep(1)
        b=0
        while 1:
            ele=self.get_element(self.wait)
            data=ele.get_attribute("style")
            if  "display"in data:
                logger.info("等待框消失")
                time.sleep(0.5)
                break
            else:
                if b==15:
                    logger.error("等待超过15秒")
                    break
                else:
                    logger.info("等待中。。。。")
                    time.sleep(1)
                    b+=1