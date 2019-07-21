#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 9:51
# @Author  : 二部测试-陈兴川
# @File    : acceptverify.py
#@email    :chenxingchuan@chinasoftinc.com

from selenium.webdriver.common.by import By

#受入确认
class Accept_Verify:
    #ETA启始时间
    eta_start=(By.XPATH,'//main//input[@aria-label="ETA"]')
    # ETA结束时间
    eta_end=(By.XPATH,'//main//input[@aria-label="ETA"]/ancestor::div[@class="flex md6 pr-2"]/following-sibling::div//div[@class="v-text-field__slot"]/input')
    #検索按钮
    search_buttom=(By.XPATH,'//div[text()="検索"]')
    #ETD启始时间
    etd_start=(By.XPATH,'//main//input[@aria-label="ETD"]')
    #ETD结束时间
    etd_end=(By.XPATH,'//main//input[@aria-label="ETD"]/ancestor::div[@class="flex md6 pr-2"]/following-sibling::div//div[@class="v-text-field__slot"]/input')
    #集装箱号输入栏
    container_no=(By.XPATH,'//input[@aria-label= "コンテナNO"]')
    #查询结果数量
    select_result = (By.XPATH, '//table[contains(@class,"v-datatable")]')
    #ETA开始时间框年月显示处
    select_year=(By.XPATH,'//strong[contains(text(),"年")]')
    # 时间框年月显示处左方向
    time_left=(By.XPATH,'//button[contains(@class,"v-btn v-btn--icon")]//i[text()="chevron_left"]')
    # 时间框年月显示处右方向
    time_r=(By.XPATH,'//button[contains(@class,"v-btn v-btn--icon")]//i[text()="chevron_right"]')
    #时间框中选择1号
    time_day=(By.XPATH,'//div[text()="{}日"]')
    #ETA结束时间框年月显示处
    s_year=(By.XPATH,'//div[contains(@class,"content__active")]//strong[contains(text(),"年")]')
    # ETA结束时间框左方向
    te_left=(By.XPATH,'//div[contains(@class,"menuable__content__active")]//i[text()="chevron_left"]')
    # ETA结束时间框右方向
    te_r = (By.XPATH, '//div[contains(@class,"menuable__content__active")]//i[text()="chevron_right"]')
    #ETA结束时间框中选择1号
    te_day = (By.XPATH, '//button[contains(@class,"flat")]//div[text()="{}日"]')
    # etd开始时间框年月显示处
    e_syear=(By.XPATH,'//div[contains(@class,"active")]//strong[contains(text(),"年")]')
    # etd时间框年月显示处左方向
    etime_left = (By.XPATH, '//div[contains(@class,"active")]//i[text()="chevron_left"]')
    # etd时间框年月显示处右方向
    etime_r = (By.XPATH, '//div[contains(@class,"active")]//i[text()="chevron_right"]')
    # etd时间框中选择1号
    etime_day = (By.XPATH, '//div[contains(@class,"active")]//div[text()="{}日"]')

    # etd结束时间框年月显示处
    ee_syear = (By.XPATH, '//div[contains(@class,"active")]//strong[contains(text(),"年")]')
    # etd结束时间框年月显示处左方向
    eetime_left = (By.XPATH, '//div[contains(@class,"active")]//i[text()="chevron_left"]')
    # etd结束时间框年月显示处右方向
    eetime_r = (By.XPATH, '//div[contains(@class,"active")]//i[text()="chevron_right"]')
    # etd结束时间框中选择1号
    eetime_day = (By.XPATH, '//strong[contains(text(),"年")]/parent::div/parent::div/following-sibling::div//div[text()="{}日"]')
    #查询结果向下翻页按钮
    result_down=(By.XPATH,'//button[@aria-label="Next page"]')
    #等待框
    wait=(By.XPATH,'//div[contains(text(),"只今")]/ancestor::div[contains(@class,"persistent")]')
