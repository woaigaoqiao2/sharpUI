'''
Created on 2019年7月1日

@author: chinasoft.yy.zhang
'''
import datetime
import time
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from pageElement.AcceptConfirm.AcceptConfirmEle import AcceptConfirmEle
from business.Login import Login
from random import choice
from selenium import webdriver
from unittest.case import TestCase
from util.ElementUtil import ElementUtil


class AcceptConfirmOperate(AcceptConfirmEle, ElementUtil):
    # 登录并点击“受入确认”
    def Login_and_AcceptConfirm(self, driver):
        # 登录
        login = Login()
        login.test_click_login_btn(driver)
        # 点击“受入确认”
        ElementUtil.click(self, driver, 15, "受入確認", *self.AC_element)

    # 随机选择一条状态为納入指示済的数据
    def choose_a_delivery_data(self, driver):
        # 点击ステータス（状态）选择框
        ElementUtil.click(self, driver, 15, "(zyy)受入確認后数据状态由納入指示済变更为受入確認", *self.status_element)
        # 选择納入指示済（完成交货指示）
        ElementUtil.click(self, driver, 15, "(zyy)受入確認后数据状态由納入指示済变更为受入確認", *self.have_confirmed_element)
        # 点击"検索"按钮
        ElementUtil.click(self, driver, 15, "(zyy)受入確認后数据状态由納入指示済变更为受入確認", *self.search_element)
        # 随机勾选一条数据
        check_box_list = driver.find_elements(*self.check_boxs)
        choice(check_box_list).click()
        # 得到D/O NO, コンテナNO
        DO_number = ElementUtil.getText(self, driver, 15, "(zyy)受入確認后数据状态由納入指示済变更为受入確認", *self.chosen_DO_number_element)
        container_number = ElementUtil.getText(self, driver, 15, "(zyy)受入確認后数据状态由納入指示済变更为受入確認", *self.chosen_container_number_element)
        # 滚动条拉到顶部
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        # 检查异常
        try:
            # 点击"受入确认"按钮
            ElementUtil.click(self, driver, 15, "(zyy)受入確認后数据状态由納入指示済变更为受入確認", *self.AC_button_elelment)
            # 点击"確定"按钮
            driver.find_element(*self.sure_element).click()
        except Exception as e:
            print("发现已知bug！")
            return ("发现已知bug！")
        return DO_number, container_number

    # 检查状态由納入指示済变更为受入確認
    def check_data_status(self, driver, DO_number, container_number):
        sleep(3)
        # 在D/O NO输入得到的D/O NO
        ElementUtil.send_keys(self, driver, 15, DO_number, "(zyy)受入確認后数据状态由納入指示済变更为受入確認", *self.DO_element)
        # 在コンテナNO输入得到的コンテナNO
        ElementUtil.send_keys(self, driver, 15, container_number, "(zyy)受入確認后数据状态由納入指示済变更为受入確認", *self.container_number_element)
        # 点击ステータス（状态）选择框
        ElementUtil.click(self, driver, 15, "(zyy)受入確認后数据状态由納入指示済变更为受入確認", *self.status_element)
        # 选择受入確認済
        ElementUtil.click(self, driver, 15, "(zyy)受入確認后数据状态由納入指示済变更为受入確認", *self.acceptance_confirmation_element)
        # 点击"検索"按钮
        ElementUtil.click(self, driver, 15, "(zyy)受入確認后数据状态由納入指示済变更为受入確認", *self.search_element)
        sleep(2)
        # 滚动条拉到最右
        driver.execute_script("var q=document.documentElement.scrollLeft = 10000")
        # 取受入確認日
        AC_date_elements = driver.find_elements(*self.AC_date_element)
        AC_date_list = []
        for AC_date in AC_date_elements:
            AC_date_list.append(AC_date.text)
        today = time.strftime("%Y-%m-%d", time.localtime())
        # 断言当前日期在列表中
        TestCase().assertIn(today, AC_date_list)

    # 选择BL结束时间执行查询
    def query_by_BLend_date(self, driver):
        # 点击B/L発行日结束时间输入框
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日结束日期搜索数据，能正确搜索", *self.BLend_date_box_element)
        # 两次点击结束日期栏
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日结束日期搜索数据，能正确搜索", *self.BLend_date_element)
        sleep(3)
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日结束日期搜索数据，能正确搜索", *self.BLend_date_element)
        # 选择结束日期，时间限定在2019年
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日结束日期搜索数据，能正确搜索", *self.BLendyear_element)
        sleep(1)
        BLend_month_list = driver.find_elements(*self.BLendmonth_element)
        BLend_month = choice(BLend_month_list)
        BLend_month_text = BLend_month.text
        BLend_month.click()
        sleep(0.5)
        BLend_day_list = driver.find_elements(*self.BLendday_element)
        BLend_day = choice(BLend_day_list)
        BLend_day_text = BLend_day.text
        BLend_day.click()
        sleep(0.5)
        BLend_date = "2019-{month}-{day}".format(month=BLend_month_text[:-1], day=BLend_day_text[:-1])
        # 点击"検索"按钮
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日结束日期搜索数据，能正确搜索", *self.search_element)
        return BLend_date

    # 得到结果数据的BL日期，并作断言
    def check_bl_date_result(self, driver, BLend_date, testMethodDoc):
        BLdata_element_list = driver.find_elements(*self.actual_BL_data)
        for BLdata_element in BLdata_element_list:
            actual_date_text = BLdata_element.text
            actual_date = datetime.datetime.strptime(actual_date_text, '%Y-%m-%d')
            query_date = datetime.datetime.strptime(BLend_date, '%Y-%m-%d')
            if "B/L発行日结束日期" in testMethodDoc:
                TestCase().assertTrue(query_date >= actual_date)
            elif "B/L発行日开始日期" in testMethodDoc:
                TestCase().assertTrue(query_date <= actual_date)
            else:
                raise ValueError("_testMethodDoc值定义有误，请检查")

    # 选择BL开始时间执行查询
    def query_by_BLstart_date(self, driver):
        # 点击B/L発行日开始时间输入框
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日开始日期搜索，能正确搜索", *self.BLstart_date_box_element)
        # 两次点击开始日期栏
        sleep(1)
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日开始日期搜索，能正确搜索", *self.BLstart_date_element)
        sleep(2)
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日开始日期搜索，能正确搜索", *self.BLstart_date_element)
        # 选择开始日期，时间限定在2019年
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日开始日期搜索，能正确搜索", *self.BLstart_year_element)
        sleep(1)
        BLstart_month_list = driver.find_elements(*self.BLstart_month_element)
        BLstart_month = choice(BLstart_month_list)
        BLstart_month.click()
        BLstart_month_text = BLstart_month.text
        sleep(1)
        BLstart_day_list = driver.find_elements(*self.BLstart_day_element)
        BLstart_day = choice(BLstart_day_list)
        BLstart_day.click()
        BLstart_day_text = BLstart_day.text
        sleep(1)
        BLstart_date = "2019-{month}-{day}".format(month=BLstart_month_text[:-1], day=BLstart_day_text[:-1])
        # 点击"検索"按钮
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日开始日期搜索，能正确搜索", *self.search_element)
        return BLstart_date

    # 选择BL时间段执行查询
    def query_by_BLdate(self, driver):
        # 点击B/L発行日开始时间输入框
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日时间段搜索数据，能正确搜索", *self.BLstart_date_box_element)
        # 两次点击开始日期栏
        sleep(1)
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日时间段搜索数据，能正确搜索", *self.BLstart_date_element)
        sleep(2)
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日时间段搜索数据，能正确搜索", *self.BLstart_date_element)
        # 选择开始日期，时间限定在2019年
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日时间段搜索数据，能正确搜索", *self.BLstart_year_element)
        start_month_list = driver.find_elements(*self.BLstart_month_element)
        start_month = choice(start_month_list)
        start_month_text = start_month.text
        start_month.click()
        sleep(1)
        start_day_list = driver.find_elements(*self.BLstart_day_element)
        start_day = choice(start_day_list)
        start_day_text = start_day.text
        start_day.click()
        # 点击B/L発行日结束时间输入框
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日时间段搜索数据，能正确搜索", *self.BLend_date_box_element)
        # 两次点击结束日期栏
        sleep(1)
        driver.find_element(*self.BLend_date_element).click()
        sleep(1)
        driver.find_element(*self.BLend_date_element).click()
        # 选择结束日期，时间限定在开始日期之后
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日时间段搜索数据，能正确搜索", *self.BLendyear_element)
        end_month_list = driver.find_elements(*self.BLendmonth_element)
        end_month = choice(end_month_list)
        end_month_text = end_month.text
        end_month.click()
        sleep(1)
        end_day_list = driver.find_elements(*self.BLendday_element)
        end_day = choice(end_day_list)
        end_day_text = end_day.text
        end_day.click()
        sleep(1)
        # 点击"検索"按钮
        ElementUtil.click(self, driver, 15, "(zyy)根据B/L発行日时间段搜索数据，能正确搜索", *self.search_element)
        BLstart_date = "2019-{month}-{day}".format(month=start_month_text[:-1], day=start_day_text[:-1])
        BLend_date = "2019-{month}-{day}".format(month=end_month_text[:-1], day=end_day_text[:-1])
        return BLstart_date, BLend_date

    # 得到结果数据的BL日期，并作断言(时间段用)
    def check_bldate_result(self, driver, BLstart_date, BLend_date):
        BLdata_element_list = driver.find_elements(*self.actual_BL_data)
        for BLdata_element in BLdata_element_list:
            actual_date_text = BLdata_element.text
            actual_date = datetime.datetime.strptime(actual_date_text, '%Y-%m-%d')
            query_start_date = datetime.datetime.strptime(BLstart_date, '%Y-%m-%d')
            query_end_date = datetime.datetime.strptime(BLend_date, '%Y-%m-%d')
            TestCase().assertTrue(query_start_date <= actual_date <= query_end_date)

    # 输入D/O NO 执行查询
    def query_by_DOnumber(self, driver, DO_number):
        # 填入D/O NO
        ElementUtil.send_keys(self, driver, 15, DO_number, "(zyy)根据D/O NO搜索数据，能正确搜索", *self.DOnumber_element)
        # 点击"検索"按钮
        ElementUtil.click(self, driver, 15, "(zyy)根据D/O NO搜索数据，能正确搜索", *self.search_element)

    # 得到结果数据的D/O NO，并作断言
    def check_DOnumber_result(self, driver, DO_number):
        DOnumber_element_list = driver.find_elements(*self.actual_DO_number)
        for DOnumber_element in DOnumber_element_list:
            actual_DO_number = DOnumber_element.text
            TestCase().assertEqual(DO_number, actual_DO_number)

    # 选择ETA 结束日期执行查询
    def query_by_ETAend_date(self, driver):
        # 点击ETA结束时间输入框
        ElementUtil.click(self, driver, 15, "(zyy)根据ETA结束日期搜索数据，能正确搜索", *self.ETAend_date_box_element)
        # 两次点击ETA结束日期栏
        ElementUtil.click(self, driver, 15, "(zyy)根据ETA结束日期搜索数据，能正确搜索", *self.ETAend_date_element)
        sleep(1.15)
        ElementUtil.click(self, driver, 15, "(zyy)根据ETA结束日期搜索数据，能正确搜索", *self.ETAend_date_element)
        # 选择结束日期，时间限定在2019年
        ElementUtil.click(self, driver, 15, "(zyy)根据ETA结束日期搜索数据，能正确搜索", *self.ETAend_year_element)
        sleep(1)
        ETAend_month_list = driver.find_elements(*self.ETAend_month_element)
        ETAend_month = choice(ETAend_month_list)
        ETAend_month_text = ETAend_month.text
        ETAend_month.click()
        sleep(1)
        ETAend_day_list = driver.find_elements(*self.ETAend_day_element)
        ETAend_day = choice(ETAend_day_list)
        ETAend_day_text = ETAend_day.text
        ETAend_day.click()
        sleep(1)
        ETAend_date = "2019-{month}-{day}".format(month=ETAend_month_text[:-1], day=ETAend_day_text[:-1])
        ETAend_date = "2019-07-09"
        # 点击"検索"按钮
        ElementUtil.click(self, driver, 15, "(zyy)根据ETA结束日期搜索数据，能正确搜索", *self.search_element)
        return ETAend_date

    # 得到结果数据的BL日期，并作断言
    def check_ETA_date_result(self, driver, ETA_date):
        ETAdata_element_list = driver.find_elements(*self.actual_ETAdate_element)
        for ETAdata_element in ETAdata_element_list:
            actual_date_text = ETAdata_element.text
            actual_date = datetime.datetime.strptime(actual_date_text, '%Y-%m-%d')
            query_date = datetime.datetime.strptime(ETA_date, '%Y-%m-%d')
            TestCase().assertTrue(query_date >= actual_date)
