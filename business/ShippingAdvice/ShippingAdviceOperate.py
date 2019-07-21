'''
Created on 2019年7月4日

@author: chinasoft.yy.zhang
'''

from time import sleep
from business.Login import Login
from random import choice
from selenium import webdriver
from unittest.case import TestCase
from pageElement.ShippingAdvice.ShippingAdviceEle import ShippingAdviceEle
import datetime
from util.ElementUtil import ElementUtil


class ShippingAdviceOperate(ShippingAdviceEle, ElementUtil):
    #登录并点击“S/A登録”
    def Login_and_ShippingAdvice(self,driver):
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击“S/A登録”
        ElementUtil.click(self, driver, 15, "S/A登録", *self.SA_element)

    #选择依頼日时间段执行查询
    def query_by_rely_date(self, driver):
        #点击依頼日开始时间输入框
        ElementUtil.click(self, driver, 15, "(zyy)根据依賴日时间段搜索数据，能正确搜索", *self.rely_start_date_box_element)
        #两次点击开始日期栏
        ElementUtil.click(self, driver, 15, "(zyy)根据依賴日时间段搜索数据，能正确搜索", *self.rely_start_date_element)
        sleep(3)
        ElementUtil.click(self, driver, 15, "(zyy)根据依賴日时间段搜索数据，能正确搜索", *self.rely_start_date_element)
        #选择开始日期，时间限定在2019年
        sleep(3)
        ElementUtil.click(self, driver, 15, "(zyy)根据依賴日时间段搜索数据，能正确搜索", *self.rely_start_year_element)
        sleep(1)
        start_month_list = driver.find_elements(*self.rely_start_month_element)
        start_month = choice(start_month_list)
        start_month_text =start_month.text
        start_month.click()
        sleep(1)
        start_day_list = driver.find_elements(*self.rely_start_day_element)
        start_day = choice(start_day_list)
        start_day_text = start_day.text
        start_day.click()
        #点击依頼日结束时间输入框
        ElementUtil.click(self, driver, 15, "(zyy)根据依賴日时间段搜索数据，能正确搜索", *self.rely_end_date_box_element)
        #两次点击结束日期栏
        sleep(1)
        driver.find_element(*self.rely_end_date_element).click()
        sleep(3)
        driver.find_element(*self.rely_end_date_element).click()
        # 选择结束日期，时间限定在开始日期之后
        sleep(3)
        ElementUtil.click(self, driver, 15, "(zyy)根据依賴日时间段搜索数据，能正确搜索", *self.rely_endyear_element)
        sleep(1)
        end_month_list = driver.find_elements(*self.rely_endmonth_element)
        end_month = choice(end_month_list)
        end_month_text = end_month.text
        end_month.click()
        sleep(1)
        end_day_list = driver.find_elements(*self.rely_endday_element)
        end_day = choice(end_day_list)
        end_day_text = end_day.text
        end_day.click()
        #点击"検索"按钮
        ElementUtil.click(self, driver, 15, "(zyy)根据依賴日时间段搜索数据，能正确搜索", *self.search_element)
        rely_start_date = "2019-{month}-{day}".format(month=start_month_text[:-1], day=start_day_text[:-1])
        rely_end_date = "2019-{month}-{day}".format(month=end_month_text[:-1], day=end_day_text[:-1])
        return rely_start_date, rely_end_date

    #得到结果数据的依頼日，并作断言
    def check_rely_date_result(self, driver, rely_start_date, rely_end_date):
        rely_date_element_list = driver.find_elements(*self.actual_rely_data)
        for rely_date_element in rely_date_element_list:
            actual_date_text = rely_date_element.text
            actual_date = datetime.datetime.strptime(actual_date_text, '%Y-%m-%d')
            query_start_date = datetime.datetime.strptime(rely_start_date, '%Y-%m-%d')
            query_end_date = datetime.datetime.strptime(rely_end_date, '%Y-%m-%d')
            TestCase().assertTrue(query_start_date<=actual_date<=query_end_date)

    #追加情报(随机选择)
    def random_add_information(self, driver):
        #点击新規按钮
        ElementUtil.click(self, driver, 15, "(zyy)ETA时间在ETD之前不能新建Shipping Advice数据", *self.new_rule_element)
        #点击追加按钮
        ElementUtil.click(self, driver, 15, "(zyy)ETA时间在ETD之前不能新建Shipping Advice数据", *self.add_element)
        #点击I/V List検索按钮
        ElementUtil.click(self, driver, 15, "(zyy)ETA时间在ETD之前不能新建Shipping Advice数据", *self.IVlist_search_element)
        sleep(1.15)
        #随机勾选I/V List数据
        checkbox_list = driver.find_elements(*self.IVlist_checkbox_list_element)[1:]
        choice(checkbox_list).click()
        #点击I/V List追加按钮
        ElementUtil.click(self, driver, 15, "(zyy)根据依賴日时间段搜索数据，能正确搜索", *self.IVlist_add_element)
        sleep(2)
        
    #得到ETD日期的前一天作为预期ETA日期
    def get_etddate(self, driver):
        #找到ETD元素
        ETD_element = driver.find_element(*self.ETD_element)
        #取文本
        ETD_date = ETD_element.get_attribute("value")
        s = ETD_date.split("-")
        ETA_year = s[0]+"年"
        ETA_month = s[1]+"月"
        ETA_day = str(int(s[2])-1)+"日"
        if ETA_month[0]=="0":
            ETA_month=ETA_month[1:]
        if ETA_day[0]=="0":
            ETA_day=ETA_day[1:]
        return ETA_year, ETA_month, ETA_day
    
    #判断ETA日期不可点击
    def check_ETAdate_status(self, driver):
        ETA_date = self.get_etddate(driver)
        ETA_year = ETA_date[0]
        ETA_month = ETA_date[1]
        ETA_day = ETA_date[2]
        #点击ETA日期输入框
        ElementUtil.click(self, driver, 15, "(zyy)ETA时间在ETD之前不能新建Shipping Advice数据", *self.ETA_box_element)
        #两次点击ETA日期栏
        sleep(2)
        driver.find_element(*self.ETA_date_element).click()
        sleep(3)
        driver.find_element(*self.ETA_date_element).click()
        #找到ETA日期
        ElementUtil.click(self, driver, 15, "(zyy)ETA时间在ETD之前不能新建Shipping Advice数据", self.ETA_year_element[0],self.ETA_year_element[1]%ETA_year)
        ElementUtil.click(self, driver, 15, "(zyy)ETA时间在ETD之前不能新建Shipping Advice数据", self.ETA_month_element[0],self.ETA_month_element[1]%ETA_month)
        actual_ETAdate = driver.find_element(self.ETAend_day_element[0], self.ETAend_day_element[1]%ETA_day)
        #查看ETA日期状态
        actual_ETAdate_status = actual_ETAdate.get_attribute("class")
        #判断ETA日期不可点击
        TestCase().assertIn("disabled", actual_ETAdate_status)

    #追加情报(不同積出港)
    def add_info_by_diff_delivery_port(self, driver):
        #点击新規按钮
        ElementUtil.click(self, driver, 15, "(zyy)新建Shipping Advice，添加2个積出港不同的数据，追加失败", *self.new_rule_element)
        #点击追加按钮
        ElementUtil.click(self, driver, 15, "(zyy)新建Shipping Advice，添加2个積出港不同的数据，追加失败", *self.add_element)
        #点击I/V List検索按钮
        ElementUtil.click(self, driver, 15, "(zyy)新建Shipping Advice，添加2个積出港不同的数据，追加失败", *self.IVlist_search_element)
        sleep(1)
        #勾选两条陸揚港相同，積出港不同的数据
        def get_different_delivery_port():
            sleep(1)
            trs = driver.find_elements(*self.tr_element)
            value = []
            #取勾选框，積出港，陸揚港
            for tr in trs:
                tds = tr.find_elements_by_tag_name('td')
                value.append([tds[0], tds[2].text, tds[3].text])
            #以陸揚港为key,積出港为value，构建字典
            d = {}
            for e, v, k in value:
                if k not in d:
                    d[k] = {v}
                else:
                    d[k].add(v)
            return d, value
        try:
            tag = 0
            d, value = get_different_delivery_port()
            # 检查有没有不同的（数量大于1），没有则翻页再来一次
            while not list(filter(lambda x: len(x) > 1, d.values())):
                driver.find_element(*self.next_page_element).click()
                d, value = get_different_delivery_port()
            #找出字典中value值大于1的key，即陸揚港相同，積出港不同
            for k in d:
                c = 0
                if len(d[k]) > 1:
                    is_click = set()
                    for i in value:
                        if i[2] == k and (i[1] not in is_click):
                            i[0].click()
                            is_click.add(i[1])
                            c += 1
                            if c == 2:
                                tag = 1
                                break
            if tag == 0:
                raise ValueError("没有符合条件的数据！")
        except BaseException as e:
            raise e
        else:
            #点击I/V List追加按钮
            ElementUtil.click(self, driver, 15, "(zyy)新建Shipping Advice，添加2个積出港不同的数据，追加失败", *self.IVlist_add_element)

    #追加情报(不同陸揚港)
    def add_info_by_diff_unloading_port(self, driver):
        #点击新規按钮
        ElementUtil.click(self, driver, 15, "(zyy)新建Shipping Advice，添加2个陸揚港不同的数据，追加失败", *self.new_rule_element)
        #点击追加按钮
        ElementUtil.click(self, driver, 15, "(zyy)新建Shipping Advice，添加2个陸揚港不同的数据，追加失败", *self.add_element)
        #点击I/V List検索按钮
        ElementUtil.click(self, driver, 15, "(zyy)新建Shipping Advice，添加2个陸揚港不同的数据，追加失败", *self.IVlist_search_element)
        sleep(1)
        #勾选两条積出港相同，陸揚港不同的数据
        def get_different_unloading_port():
            sleep(1)
            trs = driver.find_elements(*self.tr_element)
            value = []
            #取勾选框，陸揚港，積出港
            for tr in trs:
                tds = tr.find_elements_by_tag_name('td')
                value.append([tds[0], tds[2].text, tds[3].text])
            #以積出港为key,陸揚港为value，构建字典
            d = {}
            for e, v, k in value:
                if k not in d:
                    d[k] = {v}
                else:
                    d[k].add(v)
            return d, value
        try:
            tag = 0
            d, value = get_different_unloading_port()
            # 检查有没有不同的（数量大于1），没有则翻页再来一次
            while not list(filter(lambda x: len(x) > 1, d.values())):
                driver.find_element(*self.next_page_element).click()
                d, value = get_different_unloading_port()
            #找出字典中value值大于1的key，即積出港相同，陸揚港不同
            for k in d:
                c = 0
                is_click = set()
                for i in value:
                    if i[2] == k and (i[1] not in is_click):
                        i[0].click()
                        is_click.add(i[1])
                        c += 1
                        if c == 2:
                            tag = 1
                            break
            if tag == 0:
                raise ValueError("没有符合条件的数据！")
        except BaseException as e:
            raise e

        else:
            #点击I/V List追加按钮
            ElementUtil.click(self, driver, 15, "(zyy)新建Shipping Advice，添加2个陸揚港不同的数据，追加失败", *self.IVlist_add_element)
            sleep(1)

    #检查错误提示    
    def check_failed_tip(self, driver):
        expect_tip = "S/Aの積出港・陸揚港とINVの積出港・陸揚港が不一致のため、再度確認してください"
        #取文本
        actual_tip = ElementUtil.getText(self, driver, 15, "(zyy)新建Shipping Advice，添加2个積出港不同的数据，追加失败", *self.failed_tip_element)
        #断言
        TestCase().assertEqual(actual_tip, expect_tip)
        
    #点击行分け按钮，验证数据增加一条
    def check_PL_number(self, driver):
        #得到当前INV P/L情報数量
        before_PL_list = driver.find_elements(*self.PL_list_elelment)
        before_PLnumber = len(before_PL_list)
        expect_PLnumber = before_PLnumber + 1
        #随机勾选一条数据
        PLcheck_box_list_elelment = driver.find_elements(*self.PLcheck_box_list_elelment)
        choice(PLcheck_box_list_elelment).click()
        #点击行分け按钮
        ElementUtil.click(self, driver, 15, "(zyy)新建时选择货物拆分，用多个集装箱装货，可以成功保存", *self.sorting_button_element)
        #检查INV P/L情報数量增加一条
        later_PL_list = driver.find_elements(*self.PL_list_elelment)
        later_PLnumber = len(later_PL_list)
        TestCase().assertEqual(later_PLnumber, expect_PLnumber)

    #保存運送情報,检查成功提示
    def save_transport_info(self, driver, BLnumber):
        #填写Master B/L NO
        ElementUtil.send_keys(self, driver, 15, BLnumber, "(zyy)新建时选择货物拆分，用多个集装箱装货，可以成功保存", *self.Master_BLnumber_elelment)
        #填写House B/L NO
        ElementUtil.send_keys(self, driver, 15, BLnumber, "(zyy)新建时选择货物拆分，用多个集装箱装货，可以成功保存", *self.House_BLnumber_elelment)
        #判断輸送形態
        shipping_type = driver.find_element(*self.shipping_type_element).text
        if shipping_type == "SEA":
        #选择積み方
            ElementUtil.click(self, driver, 15, "(zyy)新建时选择货物拆分，用多个集装箱装货，可以成功保存", *self.loading_box_element)
            loading_list = driver.find_elements(*self.loading_element)
            choice(loading_list).click()
        # 滚动条拉到顶部
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        #点击一時保存
        ElementUtil.click(self, driver, 15, "(zyy)新建时选择货物拆分，用多个集装箱装货，可以成功保存", *self.save_button_element)
        #检查提示文本
        expect_tip = "完了しました"
        actual_tip = ElementUtil.getText(self, driver, 15, "(zyy)新建时选择货物拆分，用多个集装箱装货，可以成功保存", *self.tip_element)
        TestCase().assertEqual(expect_tip, actual_tip)
        #点击確定按钮
        ElementUtil.click(self, driver, 15, "(zyy)新建时选择货物拆分，用多个集装箱装货，可以成功保存", *self.sure_button_element)

    #检查状态变为SA一時保存
    def check_status(self, driver, BLnumber):
        #点击戻る(返回)按钮
        ElementUtil.click(self, driver, 15, "(zyy)新建时选择货物拆分，用多个集装箱装货，可以成功保存", *self.back_elemnet)
        #输入B/L NO
        ElementUtil.send_keys(self, driver, 15, BLnumber, "(zyy)新建时选择货物拆分，用多个集装箱装货，可以成功保存", *self.BLnumber_box_element)
        #点击"検索"按钮
        ElementUtil.click(self, driver, 15, "(zyy)新建时选择货物拆分，用多个集装箱装货，可以成功保存", *self.search_element)
        #状態显示栏
        sleep(1)
        expect_status = "SA一時保存"
        actual_status = ElementUtil.getText(self, driver, 15, "(zyy)新建时选择货物拆分，用多个集装箱装货，可以成功保存", *self.status_element)
        TestCase().assertEqual(expect_status, actual_status)

    #点击參照新規作成
    def reference_create(self, driver):
        #点击"検索"按钮
        ElementUtil.click(self, driver, 15, "(zyy)延用以前的数据信息创建一条積出港和陸揚港相同的海关数据，能成功创建", *self.search_element)
        sleep(1)
        #随机勾选数据
        check_box_list = driver.find_elements(*self.check_box_list_element)
        choice(check_box_list).click()
        sleep(1)
        # 滚动条拉到顶部
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        #点击參照新規作成按钮
        ElementUtil.click(self, driver, 15, "(zyy)延用以前的数据信息创建一条積出港和陸揚港相同的海关数据，能成功创建", *self.ref_create_button_element)
        sleep(2)

    #清除積出港陸揚港默认值
    def clear_port__data(self,driver):
        # 清除積出港默认值
        delivery_port_box_element = driver.find_element(*self.delivery_port_box_element)
        delivery_clear_element = driver.find_element(*self.delivery_clear_element)
        action = webdriver.ActionChains(driver)
        action.move_to_element(delivery_port_box_element).click(delivery_clear_element).perform()
        # 清除陸揚港默认值
        unloading_port_box_element = driver.find_element(*self.unloading_port_box_element)
        unloading_clear_element = driver.find_element(*self.unloading_clear_element)
        action = webdriver.ActionChains(driver)
        action.move_to_element(unloading_port_box_element).click(unloading_clear_element).perform()

    #追加情报(相同積出港相同陸揚港)
    def add_info_by_same_port(self, driver, BLnumber):
        #点击追加按钮
        ElementUtil.click(self, driver, 15, "(zyy)延用以前的数据信息创建一条積出港和陸揚港相同的海关数据，能成功创建", *self.add_element)
        # 点击I/V List検索按钮
        ElementUtil.click(self, driver, 15, "(zyy)延用以前的数据信息创建一条積出港和陸揚港相同的海关数据，能成功创建", *self.IVlist_search_element)
        #勾选两条積出港相同，陸揚港相同的数据
        def get_the_same_port():
            sleep(1)
            trs = driver.find_elements(*self.tr_element)
            value = []
            #取勾选框，積出港，陸揚港
            for tr in trs:
                tds = tr.find_elements_by_tag_name('td')
                value.append([tds[0], tds[3].text, tds[2].text])
            # 以陸揚港为 key，積出港为 value 构建一个字典
            # value 为集合 set 也就是不会重复，如果集合数量大于一，说明有不相同的
            d = {}
            c = 0
            for e, v, k in value:
                if k not in d:
                    d[k] = {v}
                else:
                    d[k].add(v)
                    c += 1
                if c >0 and len(d[k]) == 1:
                    return k, value

        def click_same_port():
                k, value = get_the_same_port()
                try:
                    while not k:
                        ElementUtil.click(self, driver, 15, "(zyy)延用以前的数据信息创建一条積出港和陸揚港相同的海关数据，能成功创建", *self.next_page_element)
                        k, value = get_the_same_port()
                    c = 0
                    for i in value:
                        if i[2] == k:
                            i[0].click()
                            c += 1
                        if c == 2:
                            break
                    if not click_same_port():
                        raise ValueError("没有符合条件的数据！")
                except BaseException as e:
                    raise e

                else:
                    #点击I/V List追加按钮
                    driver.find_element(*self.IVlist_add_element).click()
                    sleep(2)
                    # 填写Master B/L NO
                    ElementUtil.send_keys(self, driver, 15, BLnumber, "(zyy)延用以前的数据信息创建一条積出港和陸揚港相同的海关数据，能成功创建", *self.Master_BLnumber_elelment)
                    # 填写House B/L NO
                    ElementUtil.send_keys(self, driver, 15, BLnumber, "(zyy)延用以前的数据信息创建一条積出港和陸揚港相同的海关数据，能成功创建", *self.House_BLnumber_elelment)
                    #点击一時保存
                    ElementUtil.click(self, driver, 15, "(zyy)延用以前的数据信息创建一条積出港和陸揚港相同的海关数据，能成功创建", *self.save_button_element)
                    sleep(2)
                    # 检查提示文本
                    expect_tip = "完了しました"
                    actual_tip = ElementUtil.getText(self, driver, 15, "(zyy)延用以前的数据信息创建一条積出港和陸揚港相同的海关数据，能成功创建", *self.tip_element)
                    TestCase().assertEqual(expect_tip, actual_tip)
                    # 点击確定按钮
                    ElementUtil.click(self, driver, 15, "(zyy)延用以前的数据信息创建一条積出港和陸揚港相同的海关数据，能成功创建", *self.sure_button_element)

    #点击編集
    def click_edit_button(self, driver):
        #点击"検索"按钮
        ElementUtil.click(self, driver, 15, "(zyy)编辑时选择货物拆分，用多个集装箱装货，可以成功保存", *self.search_element)
        #随机勾选数据
        check_box_list = driver.find_elements(*self.check_box_list_element)
        choice(check_box_list).click()
        # 滚动条拉到顶部
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        #点击編集按钮
        ElementUtil.click(self, driver, 15, "(zyy)编辑时选择货物拆分，用多个集装箱装货，可以成功保存", *self.edit_button_element)

    #点击行分け按钮
    def click_sorting_button(self, driver):
        sleep(3)
        #随机勾选一条数据
        PLcheck_box_list_elelment = driver.find_elements(*self.PLcheck_box_list_elelment)
        choice(PLcheck_box_list_elelment).click()
        sleep(1)
        #点击行分け按钮
        ElementUtil.click(self, driver, 15, "(zyy)编辑时选择货物拆分，用多个集装箱装货，可以成功保存", *self.sorting_button_element)
