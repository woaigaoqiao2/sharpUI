import time
from pageElement.PlLogin import PlLogin
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from selenium.webdriver.support.select import Select
import os
path=os.path.dirname(os.getcwd())

class PlLogin(PlLogin):

    def __init__(self, driver):
        self.driver = driver
        self.ivonovalue=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.listbill=datetime.datetime.now().strftime("%Y%m%d")
        self.js1 = "document.documentElement.scrollTop=10000"  # 滚动条滚动到底部js脚本
        self.js2 = "document.documentElement.scrollTop=0"  # 滚动条滚动到底部js脚本
        self.js3 = "document.getElementsByTagName('button')[5].click()"  #  点击弹窗第一个按钮

    def testPlLogin(self):

            time.sleep(2)
            self.driver.find_element(*self.plbuttong_element).click()  # 首页登录按钮
            self.driver.implicitly_wait(3)
            time.sleep(2)
            self.driver.find_element(*self.youchang_element).click()  # 有偿新规按钮
            self.driver.implicitly_wait(3)
            time.sleep(3)
            self.driver.find_element(*self.pojianchu_element).click()  # po检出按钮
            time.sleep(2)
            self.driver.implicitly_wait(4)
            implement = self.driver.find_element_by_xpath(self.jiansuobt_element)  # 点击检索按钮
            chain = ActionChains(self.driver)
            chain.double_click(implement).perform()
            self.driver.implicitly_wait(3)
            self.driver.find_element(*self.pofirstvalue_element).click()  # 点击第一条记录
            self.driver.implicitly_wait(3)
            self.driver.find_element(*self.pouse_element).click()  # 点击使用按钮
            self.driver.implicitly_wait(3)
            self.driver.find_element(*self.zhechuang_element).click()  # 点击责出港下拉框
            self.driver.implicitly_wait(3)
            self.driver.find_element(*self.zhechuangfirst_element).click()  # 选择责出刚第一条记录
            self.driver.implicitly_wait(3)
            self.driver.find_element(*self.luyang_element).click()  # 点击陆杨港下拉框
            self.driver.implicitly_wait(3)
            self.driver.find_element(*self.luyangfirst_element).click()  # 选择陆洋刚第一条记录
            self.driver.implicitly_wait(3)
            time.sleep(2)
            self.driver.find_element(*self.ivdate_element).click()  # 点击iv日期选择框
            self.driver.implicitly_wait(3)
            time.sleep(2)
            self.driver.find_element(*self.ivdatevalue_element).click()  # 随机选择一个日期
            self.driver.implicitly_wait(3)
            time.sleep(2)
            self.driver.find_element(*self.xingtai_element).click()  # 点击形态下拉框
            time.sleep(2)
            self.driver.implicitly_wait(3)
            self.driver.find_element(*self.xingtaifirst_element).click()  # 点击形态下拉框第一个值
            time.sleep(2)
            self.driver.find_element(*self.jianzhi_element).click()  # 点击建值下拉框
            time.sleep(2)
            self.driver.implicitly_wait(3)
            self.driver.find_element(*self.jianzhifirst_element).click()  # 点击建值第一个值
            time.sleep(2)
            self.driver.find_element(*self.tonghuo_element).click()  # 点击通货下拉框
            time.sleep(2)
            self.driver.implicitly_wait(3)
            self.driver.find_element(*self.tonghuofirst_element).click()  # 点击通货第一个值
            time.sleep(2)
            self.driver.find_element(*self.etddate_element).click()  # 选择etd日期
            self.driver.implicitly_wait(3)
            time.sleep(2)
            self.driver.find_element(*self.etddatevalue_element).click()  # 随机选择一个ETD日期
            time.sleep(2)
            self.driver.implicitly_wait(3)
            self.driver.implicitly_wait(3)
            self.driver.find_element(*self.ivono_element).send_keys(self.ivonovalue)  # ivoNO输入一个时间随机数
            self.driver.implicitly_wait(3)
            self.driver.execute_script(self.js1)  # 滚动条滚动到底部
            self.driver.implicitly_wait(3)
            self.driver.find_element(*self.plgouxuan_element).click()  # 第一次点击pl勾选按钮
            self.driver.implicitly_wait(3)
            self.driver.find_element(*self.pl_denglu_element).click()  # 点击登出按钮
            time.sleep(1)
            self.driver.find_element(*self.plgouxuan_element).click()  # pl勾选按钮
            time.sleep(1)
            self.driver.find_element(*self.listdetail_element).click()  # list详情勾选按钮
            time.sleep(1)
            self.driver.find_element(*self.m3input_element).send_keys(self.listbill)  # 详情订单输入M3
            time.sleep(1)
            self.driver.find_element(*self.gwinput_element).send_keys(self.listbill)  # 详情订单输入gw
            time.sleep(1)
            self.driver.find_element(*self.nwinput_element).send_keys(self.listbill)  # 详情订单输入nw
            time.sleep(1)
            self.driver.find_element(*self.cartonendinput_element).send_keys(self.listbill)  # 详情订单输入cartonEnd号
            time.sleep(1)
            self.driver.find_element(*self.cartonstartinput_element).send_keys(self.listbill)  # 详情订单输入cartonStart号
            time.sleep(1)
            self.driver.find_element(*self.shibiefanhaoinput_element).send_keys(self.listbill)  # 详情订单输入cartonStart号
            time.sleep(1)
            self.driver.execute_script(self.js2)  # 滚动条滚动到顶部
            time.sleep(3)
            self.driver.find_element(*self.topsaveinput_element).click()  # 点击顶部保存按钮
            self.driver.implicitly_wait(3)
            time.sleep(3)
            self.driver.find_element(*self.confirmbuton_element).click()  # 点击确认按钮
            time.sleep(3)
            self.returnvalue=self.driver.find_element(*self.confirmvalue_element).text  # 获取确认页面的值
            return self.returnvalue  # 返回实际值给测试页面做断言
            time.sleep(1)
            self.driver.find_element(*self.lastconfirbutton_element).click() #  点击最后确认按钮
            time.sleep(1)

