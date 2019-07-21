import time
from pageElement.pllogin.PlLogin import PlLogin
from util.generate_random import generate_random
from selenium.webdriver.common.keys import Keys
import datetime
import os
path=os.path.dirname(os.getcwd())
import random
from util.ElementUtil import ElementUtil
from common.Wait import Wait

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException

class PlLogin(PlLogin):

    def __init__(self, driver):
        self.driver = driver
        self.el = ElementUtil()
        self.ivonovalue=datetime.datetime.now().strftime("%H%M%S")
        self.listbill=datetime.datetime.now().strftime("%Y-%m-%d") # 年月日 YYYY-MM-DD
        self.js1 = "document.documentElement.scrollTop=10000"  # 滚动条滚动到底部js脚本
        self.js2 = "document.documentElement.scrollTop=0"  # 滚动条滚动到顶部js脚本
        self.js3 = "document.getElementsByTagName('button')[5].click()"  # 点击弹窗第一个按钮
        self.str = ""
        time.sleep(5)
        d=self.driver.execute_script('return document.readyState')
        if d != 'complete':
            self.driver.execute_script("location.reload()")
            time.sleep(10)
        ElementUtil.click(self,self.driver,10,'每次登陆后点击第一个模块',*self.plbuttong_element) # 每次登陆后点击页面第一个模块
        time.sleep(2)


    def testFreePay(self):
        ElementUtil.click(self, self.driver,10,'無償商品登録行追加无条件检索功能验证',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        ElementUtil.click(self, self.driver,10,'無償商品登録行追加无条件检索功能验证',*self.wuchangzuijia_element) # 页面点击无偿新规追加按钮
        time.sleep(2)
        ElementUtil.click(self, self.driver,10,'無償商品登録行追加无条件检索功能验证',*self.wuchangzuijianext_element) # 无偿新规追加下一页按钮
        time.sleep(2)
        actualvalue=ElementUtil.getText(self,self.driver,10,'無償商品登録行追加无条件检索功能验证',*self.wuchangzuijiatite_element)
        return actualvalue


    def sheneiinsert(self):

        ElementUtil.click(self, self.driver,10,'社内品番检索功能验证',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijia_element))[0].click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangsheneiinsert_element))[1].send_keys('DUNTK9890FMW0')
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiajainsuo_element))[0].click()
        time.sleep(3)
        # 无偿追加页面点击检索按钮
        actualvalue = ElementUtil.getText(self, self.driver,10,'社内品番检索功能验证',*self.wuchangzuijiavalue_element)
        return actualvalue


    def sheneiNoData(self):
        ElementUtil.click(self, self.driver,10,'社内品番无效检索功能验证',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijia_element))[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangsheneiinsert_element))[1].send_keys("6666666666")
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiajainsuo_element))[0].click() # 无偿追加页面点击检索按钮
        time.sleep(2)
        actualvalue= WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijianodata_element))[0].text
        return actualvalue


    def shenwaiNoData(self):
        ElementUtil.click(self, self.driver,10,'社外品番检索功能验证', *self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijia_element))[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangshewaiinsert_element))[0].send_keys("6666666666")
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiajainsuo_element))[0].click()  # 无偿追加页面点击检索按钮
        time.sleep(2)
        actualvalue=WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijianodata_element))[0].text
        return actualvalue


    def shewaiinsert(self):
        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'社外品番无效检索功能验证',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("DUNTK9890FMW0")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮
        time.sleep(3)
        actualvalue=self.driver.find_element(*self.wuchangzuijiavalue_element).text
        return actualvalue
        time.sleep(3)


    def sheneiwaiinsert(self):

        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'社内品番和社外品番同时输入值验证',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijia_element))[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("MOCKUP")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangsheneiinsert_element)[1].send_keys("MOCKUP")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮
        time.sleep(3)
        actualvalue = self.driver.find_element(*self.wuchangzuijiavalue_element).text
        return actualvalue


    def PldengchuOne(self):
        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'无偿新规P/L登出功能验证',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element))[1].click()
        time.sleep(1)
        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[8].click() # 页面点击invoice详情第一个条记录
        time.sleep(2)
        self.driver.find_element(*self.invoicepldenglubutton_element).click()
        time.sleep(2)
        self.driver.execute_script(self.js1)
        time.sleep(3)
        actualvalue=self.driver.find_element(*self.wuchangxinguipackagelistfenyeshuone_element).text # pagelist分页数量
        return actualvalue


    def PlLoginTwo(self):

        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'P/L登陆-添加多条功能验证', *self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(1)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[2].click()
        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element))[8].click() # 页面点击invoice详情第一个条记录
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[9].click()  # 页面点击invoice详情第一个条记录
        time.sleep(2)
        self.driver.find_element(*self.invoicepldenglubutton_element).click()
        time.sleep(2)
        self.driver.execute_script(self.js1)
        time.sleep(3)
        actualvalue=self.driver.find_element(*self.wuchangxinguipackagelistfenyeshutwo_element).text # pagelist分页数量
        return actualvalue


    def Plliebiaoshuliang(self):

        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'列表数据数量添加功能验证',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)

        try:
            self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[4].click()  # 页面点击invoice详情第一个条记录
        except ElementNotVisibleException as e:
            time.sleep(3)
            self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[4].click()

        time.sleep(3)
        self.driver.find_element(*self.invoicepldenglubutton_element).click()
        time.sleep(3)
        self.driver.find_element(*self.invoiceshuliang_element).send_keys('10')  # vocie详情数量输入10
        time.sleep(2)
        self.driver.execute_script(self.js1)
        time.sleep(2)
        self.driver.find_element(*self.packagelistshuliang_element).click()
        time.sleep(2)
        self.driver.find_element(*self.packagelistlable_element).click()
        time.sleep(2)
        actualvalue=self.driver.find_element(*self.packagelistshuliang_element)
        time.sleep(2)
        srt = actualvalue.get_attribute("value")
        return srt


    def PLfbodanjia(self):
        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'列表数据FOB单面添加功能验证', *self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮
        time.sleep(3)

        try:
            self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        except ElementNotVisibleException as e:
            time.sleep(3)
            self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()

        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click() # 无偿追加页面使用
        time.sleep(3)

        self.driver.find_element(*self.invoicefob_element).send_keys('10')  # vocie详情数量输入10
        time.sleep(2)
        self.driver.find_element(*self.invoiceshuliang_element).send_keys('10')  # vocie详情数量输入10
        time.sleep(2)
        respectvalue=self.driver.find_element(*self.invoicexiaoji_element).text
        print(respectvalue)
        return respectvalue


    def PLyuanchanguo(self):

        time.sleep(1)
        ElementUtil.click(self, self.driver,10, '列表数据原产国添加功能验证',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)

        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click() # 无偿追加页面使用
        time.sleep(3)

        self.driver.find_element(*self.invoiceguojia_element).click()  # 点击原产国
        time.sleep(3)

        self.driver.find_element(*self.invoiceguojiariben_element).click()  # 点击日本
        time.sleep(3)

        time.sleep(2)
        self.driver.execute_script(self.js1)
        time.sleep(2)

        respectvalue=self.driver.find_element(*self.invoiceguojia_element).get_attribute("value")
        return respectvalue


    def PLshibiefanhao(self):

        time.sleep(2)
        self.driver.find_element(*self.wuchangbutton_element).click()  # 页面点击无偿新规按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[4].click()  # 页面点击invoice详情第一个条记录
        time.sleep(3)
        self.driver.find_element(*self.invoicepldenglubutton_element).click()
        time.sleep(2)
        self.driver.execute_script(self.js1)
        self.driver.find_element(*self.packagelistshibie_element).send_keys('999')
        time.sleep(3)
        respectvalue=self.driver.find_element(*self.packagelistshibie_element).get_attribute("value")
        return respectvalue


    def PLcartonno(self):

        time.sleep(1)
        self.driver.find_element(*self.wuchangbutton_element).click()  # 页面点击无偿新规按钮

        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮

        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮

        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)

        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)

        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[4].click()  # 页面点击invoice详情第一个条记录
        time.sleep(3)

        self.driver.find_element(*self.invoicepldenglubutton_element).click()
        time.sleep(2)

        self.driver.execute_script(self.js1)
        self.driver.find_element(*self.invoiceshuliang_element).send_keys('100')
        time.sleep(1)

        self.driver.find_element(*self.packageliststartno_element).send_keys('1')
        time.sleep(1)

        self.driver.find_element(*self.packagelistendno_element).send_keys('2')
        time.sleep(1)
        self.driver.find_element(*self.packagelistlable_element).click()
        time.sleep(2)
        respectvalue=self.driver.find_element(*self.packagelistrenshu_element).get_attribute("value")
        return respectvalue


    def PLNW(self):

        time.sleep(1)
        self.driver.find_element(*self.wuchangbutton_element).click()  # 页面点击无偿新规按钮

        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮

        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮

        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)

        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)

        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[4].click()  # 页面点击invoice详情第一个条记录
        time.sleep(3)

        self.driver.find_element(*self.invoicepldenglubutton_element).click()
        time.sleep(2)

        self.driver.execute_script(self.js1)
        time.sleep(2)

        self.driver.find_element(*self.packagelistnw_element).send_keys('1')
        time.sleep(2)
        respectvalue = self.driver.find_element(*self.packagelistnw_element).get_attribute("value")
        return respectvalue

    def PLGW(self):

        time.sleep(1)
        self.driver.find_element(*self.wuchangbutton_element).click()  # 页面点击无偿新规按钮

        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮

        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮

        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)

        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)

        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[4].click()  # 页面点击invoice详情第一个条记录
        time.sleep(3)

        self.driver.find_element(*self.invoicepldenglubutton_element).click()
        time.sleep(2)

        self.driver.execute_script(self.js1)
        time.sleep(2)

        self.driver.find_element(*self.packagelistgw_element).send_keys('1')
        time.sleep(2)
        respectvalue = self.driver.find_element(*self.packagelistgw_element).get_attribute("value")
        return respectvalue

    def PLM3(self):

        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'输入M3功能验证',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element))[4].click() # 页面点击invoice详情第一个条记录

        time.sleep(3)
        self.driver.find_element(*self.invoicepldenglubutton_element).click()
        time.sleep(2)
        self.driver.execute_script(self.js1)
        time.sleep(2)
        self.driver.find_element(*self.packagelistm3_element).send_keys('1')
        time.sleep(2)
        respectvalue = self.driver.find_element(*self.packagelistm3_element).get_attribute("value")
        return respectvalue


    def PLlistxiaochu(self):

        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'List消除功能验证',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element))[4].click()  # 页面点击invoice详情第一个条记录
        time.sleep(3)
        self.driver.find_element(*self.invoicepldenglubutton_element).click()
        time.sleep(2)
        self.driver.execute_script(self.js1)
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[6].click() # 页面点击packagelist详情第一个条记录
        time.sleep(2)
        self.driver.find_elements(*self.wuchangxinguishanchu_element)[1].click() #页面点击packagelist删除按钮
        time.sleep(2)
        self.driver.find_element(*self.wuchangxinguishanchuqueren_element).click() # packagelist删除记录确认按钮
        time.sleep(2)
        actualvlaue=self.driver.find_element(*self.wuchangxinguishanchufanhui_element).text
        return actualvlaue

    def PLcanclelistxiaochu(self):

        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'List消除功能验证',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element))[4].click()  # 页面点击invoice详情第一个条记录
        time.sleep(3)
        self.driver.find_element(*self.invoicepldenglubutton_element).click()
        time.sleep(2)
        self.driver.execute_script(self.js1)
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[6].click() # 页面点击packagelist详情第一个条记录
        time.sleep(2)
        self.driver.find_elements(*self.wuchangxinguishanchu_element)[1].click() #页面点击packagelist删除按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangxinguishanchuquxiaoqueren_element)[4].click() # packagelist删除记录点击取消确认
        time.sleep(2)
        actualvlaue=self.driver.find_element(*self.packagelistshenei_element).text
        return actualvlaue


    def PlPackageFenHang(self):

        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'PL行分功能',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(2)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element))[4].click()  # 页面点击invoice详情第一个条记录
        time.sleep(3)
        self.driver.find_element(*self.invoicepldenglubutton_element).click()
        time.sleep(2)
        self.driver.execute_script(self.js1)
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[6].click() # 页面点击packagelist详情第一个条记录
        time.sleep(2)
        self.driver.find_element(*self.wuchangxinguipackagelistfenhang_element).click() #页面点击packagelist分行按钮
        time.sleep(1)
        actual=self.driver.find_element(*self.wuchangxinguipackagelistfenyeshutwo_element).text
        return actual


    def testPackageListandINVOICE(self):

        time.sleep(1)
        ElementUtil.click(self, self.driver,10,'Package List详细和INVOICE 详细数量属性相同保存',*self.wuchangbutton_element)  # 页面点击无偿新规按钮
        time.sleep(1)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(1)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮
        time.sleep(1)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element))[4].click()  # 页面点击invoice详情第一个条记录
        time.sleep(3)
        self.driver.find_element(*self.invoicepldenglubutton_element).click() # 点击页面登出按钮
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element))[4].click()  # 再次点击invoice详情第一个条记录
        time.sleep(3)
        self.driver.execute_script(self.js1)
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[6].click()  # 页面点击packagelist详情第一个条记录
        time.sleep(2)
        self.driver.find_element(*self.invoicefob_element).send_keys('10')  # 页面fob价格输入
        time.sleep(1)
        self.driver.find_element(*self.invoiceshuliang_element).send_keys('100')  # voice详情数量输入
        time.sleep(1)
        self.driver.find_element(*self.packageliststartno_element).send_keys('1')
        time.sleep(1)
        self.driver.find_element(*self.packagelistendno_element).send_keys('1')
        time.sleep(1)
        self.driver.find_element(*self.packagelistnw_element).send_keys('10')
        time.sleep(1)
        self.driver.find_element(*self.packagelistgw_element).send_keys('10')
        time.sleep(1)
        self.driver.find_element(*self.packagelistm3_element).send_keys('10')
        time.sleep(1)
        self.driver.find_element(*self.haiwaiquyinxian_element).send_keys('70192:TSMC')
        time.sleep(1)
        self.driver.find_element(*self.haiwaiquyinxian_element).send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(*self.ivnonumber_element).send_keys(generate_random.generate_random_unique())
        time.sleep(1)
        d = self.driver.find_element_by_xpath('//input[@aria-label="I/V作成日" and @type="text"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)  # 清除元素属性readonly
        self.driver.find_element(*self.ivzuocheng_element).send_keys(self.listbill)
        time.sleep(1)
        self.driver.find_element(*self.zhechugang_element).send_keys('AXT:秋田空港')
        time.sleep(1)
        self.driver.find_element(*self.zhechugang_element).send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(*self.xingtai_element).click()  # 点击形态下拉框
        time.sleep(1)
        self.driver.find_element(*self.sea_element).click()
        time.sleep(1)
        self.driver.find_element(*self.jianzhi_element).send_keys('FCA')
        time.sleep(1)
        self.driver.find_element(*self.jianzhi_element).send_keys(Keys.ENTER)
        self.driver.find_element(*self.luyanggang_element).send_keys('AOJ:青森空港')
        time.sleep(1)
        self.driver.find_element(*self.luyanggang_element).send_keys(Keys.ENTER)
        self.driver.find_element(*self.tonghuo_element).send_keys('USD')
        time.sleep(1)
        self.driver.find_element(*self.tonghuo_element).send_keys(Keys.ENTER)
        d = self.driver.find_element_by_xpath('//input[@aria-label="ETD" and @type="text"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(1)
        self.driver.find_element(*self.ETD_element).send_keys(self.listbill)
        self.driver.find_element(*self.ETD_element).send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.execute_script(self.js2)
        time.sleep(1)
        self.driver.find_elements(*self.wuchagnbaocun_element)[1].click()
        time.sleep(3)
        respectvalue=self.driver.find_element(*self.successmessage_element).text
        return respectvalue

    def testPackageListandINVOICEunsame(self):

        time.sleep(1)
        self.driver.find_element(*self.wuchangbutton_element).click()  # 页面点击无偿新规按钮

        time.sleep(1)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮

        time.sleep(1)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear()
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮

        time.sleep(1)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)

        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element))[4].click()  # 页面点击invoice详情第一个条记录
        time.sleep(3)

        self.driver.find_element(*self.invoicepldenglubutton_element).click() # 点击页面登出按钮
        time.sleep(2)

        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[4].click()  # 再次点击invoice详情第一个条记录
        time.sleep(3)
        self.driver.execute_script(self.js1)
        time.sleep(2)

        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[6].click()  # 页面点击packagelist详情第一个条记录
        time.sleep(2)
        self.driver.find_element(*self.invoicefob_element).send_keys('10')  # 页面fob价格输入
        time.sleep(1)

        self.driver.find_element(*self.invoiceshuliang_element).send_keys('100')  # voice详情数量输入
        time.sleep(1)

        self.driver.find_element(*self.packageliststartno_element).send_keys('1')
        time.sleep(1)

        self.driver.find_element(*self.packagelistendno_element).send_keys('1')
        time.sleep(1)

        self.driver.find_element(*self.packagelistshuliang_element).send_keys(Keys.CONTROL,'a')
       # self.driver.find_element(*self.packagelistshuliang_element).send_keys(Keys.BACK_SPACE)

        self.driver.find_element(*self.packagelistshuliang_element).send_keys('200')
        time.sleep(1)

        self.driver.find_element(*self.packagelistnw_element).send_keys('10')
        time.sleep(1)

        self.driver.find_element(*self.packagelistgw_element).send_keys('10')
        time.sleep(1)

        self.driver.find_element(*self.packagelistm3_element).send_keys('10')
        time.sleep(1)

        self.driver.find_element(*self.haiwaiquyinxian_element).send_keys('70192:TSMC')
        time.sleep(1)

        self.driver.find_element(*self.haiwaiquyinxian_element).send_keys(Keys.ENTER)
        time.sleep(1)

        self.driver.find_element(*self.ivnonumber_element).send_keys(generate_random.generate_random_unique())
        time.sleep(1)

        d = self.driver.find_element_by_xpath('//input[@aria-label="I/V作成日" and @type="text"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)  # 清除元素属性readonly
        self.driver.find_element(*self.ivzuocheng_element).send_keys(self.listbill)
        time.sleep(1)

        self.driver.find_element(*self.zhechugang_element).send_keys('AXT:秋田空港')
        time.sleep(1)

        self.driver.find_element(*self.zhechugang_element).send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(*self.xingtai_element).click()  # 点击形态下拉框
        time.sleep(1)
        self.driver.find_element(*self.sea_element).click()
        time.sleep(1)

        self.driver.find_element(*self.jianzhi_element).send_keys('FCA')
        time.sleep(1)

        self.driver.find_element(*self.jianzhi_element).send_keys(Keys.ENTER)
        self.driver.find_element(*self.luyanggang_element).send_keys('AOJ:青森空港')
        time.sleep(1)

        self.driver.find_element(*self.luyanggang_element).send_keys(Keys.ENTER)
        self.driver.find_element(*self.tonghuo_element).send_keys('USD')
        time.sleep(1)

        self.driver.find_element(*self.tonghuo_element).send_keys(Keys.ENTER)
        d = self.driver.find_element_by_xpath('//input[@aria-label="ETD" and @type="text"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(1)

        self.driver.find_element(*self.ETD_element).send_keys(self.listbill)
        self.driver.find_element(*self.ETD_element).send_keys(Keys.ENTER)
        time.sleep(1)

        self.driver.execute_script(self.js2)
        time.sleep(1)

        self.driver.find_elements(*self.wuchagnbaocun_element)[1].click()
        time.sleep(3)

        respectvalue=self.driver.find_element(*self.unsamemessage_element).text
        return respectvalue


    def testInsertUnexistIvo(self):

        time.sleep(1)
        self.driver.find_element(*self.wuchangbutton_element).click()  # 页面点击无偿新规按钮
        time.sleep(1)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮
        time.sleep(1)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮
        time.sleep(4)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)

        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element))[4].click()  # 页面点击invoice详情第一个条记录
        time.sleep(3)

        self.driver.find_element(*self.invoicepldenglubutton_element).click()  # 点击页面登出按钮
        time.sleep(4)

        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[4].click()  # 再次点击invoice详情第一个条记录
        time.sleep(3)
        self.driver.execute_script(self.js1)
        time.sleep(4)

        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[6].click()  # 页面点击packagelist详情第一个条记录
        time.sleep(2)
        self.driver.find_element(*self.invoicefob_element).send_keys('10')  # 页面fob价格输入
        time.sleep(1)

        self.driver.find_element(*self.invoiceshuliang_element).send_keys('100')  # voice详情数量输入
        time.sleep(1)

        self.driver.find_element(*self.packageliststartno_element).send_keys('1')
        time.sleep(1)

        self.driver.find_element(*self.packagelistendno_element).send_keys('1')
        time.sleep(1)

        self.driver.find_element(*self.packagelistnw_element).send_keys('10')
        time.sleep(1)

        self.driver.find_element(*self.packagelistgw_element).send_keys('10')
        time.sleep(1)

        self.driver.find_element(*self.packagelistm3_element).send_keys('10')
        time.sleep(1)

        self.driver.find_element(*self.haiwaiquyinxian_element).send_keys('70192:TSMC')
        time.sleep(1)

        self.driver.find_element(*self.haiwaiquyinxian_element).send_keys(Keys.ENTER)
        time.sleep(1)

        self.driver.find_element(*self.ivnonumber_element).send_keys(generate_random.generate_random_unique())
        time.sleep(1)

        d = self.driver.find_element_by_xpath('//input[@aria-label="I/V作成日" and @type="text"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)  # 清除元素属性readonly
        self.driver.find_element(*self.ivzuocheng_element).send_keys(self.listbill)
        time.sleep(1)

        self.driver.find_element(*self.zhechugang_element).send_keys('AXT:秋田空港')
        time.sleep(1)

        self.driver.find_element(*self.zhechugang_element).send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(*self.xingtai_element).click()  # 点击形态下拉框
        time.sleep(1)
        self.driver.find_element(*self.sea_element).click()
        time.sleep(1)

        self.driver.find_element(*self.jianzhi_element).send_keys('FCA')
        time.sleep(1)

        self.driver.find_element(*self.jianzhi_element).send_keys(Keys.ENTER)
        self.driver.find_element(*self.luyanggang_element).send_keys('AOJ:青森空港')
        time.sleep(1)

        self.driver.find_element(*self.luyanggang_element).send_keys(Keys.ENTER)
        self.driver.find_element(*self.tonghuo_element).send_keys('USD')
        time.sleep(1)

        self.driver.find_element(*self.tonghuo_element).send_keys(Keys.ENTER)
        d = self.driver.find_element_by_xpath('//input[@aria-label="ETD" and @type="text"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(1)

        self.driver.find_element(*self.ETD_element).send_keys(self.listbill)
        self.driver.find_element(*self.ETD_element).send_keys(Keys.ENTER)
        time.sleep(1)

        self.driver.execute_script(self.js2)
        time.sleep(1)

        self.driver.find_elements(*self.wuchagnbaocun_element)[1].click()
        time.sleep(3)

        respectvalue = self.driver.find_element(*self.successmessage_element).text
        return respectvalue


    def InsertIvoNotsame(self):

        time.sleep(1)
        self.driver.find_element(*self.wuchangbutton_element).click()  # 页面点击无偿新规按钮

        time.sleep(1)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮

        time.sleep(1)
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].clear
        self.driver.find_elements(*self.wuchangshewaiinsert_element)[0].send_keys("RJ63ACL1D")
        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijiajainsuo_element)[0].click()
        # 无偿追加页面点击检索按钮

        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(3)

        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element))[4].click()  # 页面点击invoice详情第一个条记录
        time.sleep(3)

        self.driver.find_element(*self.invoicepldenglubutton_element).click()  # 点击页面登出按钮
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element))[4].click()  # 再次点击invoice详情第一个条记录
        time.sleep(3)
        self.driver.execute_script(self.js1)
        time.sleep(2)

        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[6].click()  # 页面点击packagelist详情第一个条记录
        time.sleep(2)
        self.driver.find_element(*self.invoicefob_element).send_keys('10')  # 页面fob价格输入
        time.sleep(1)

        self.driver.find_element(*self.invoiceshuliang_element).send_keys('100')  # voice详情数量输入
        time.sleep(1)

        self.driver.find_element(*self.packageliststartno_element).send_keys('1')
        time.sleep(1)

        self.driver.find_element(*self.packagelistendno_element).send_keys('1')
        time.sleep(1)

        self.driver.find_element(*self.packagelistnw_element).send_keys('10')
        time.sleep(1)

        self.driver.find_element(*self.packagelistgw_element).send_keys('10')
        time.sleep(1)

        self.driver.find_element(*self.packagelistm3_element).send_keys('10')
        time.sleep(1)

        self.driver.find_element(*self.haiwaiquyinxian_element).send_keys('70192:TSMC')
        time.sleep(1)

        self.driver.find_element(*self.haiwaiquyinxian_element).send_keys(Keys.ENTER)
        time.sleep(1)

        self.driver.find_element(*self.ivnonumber_element).send_keys('999999')
        time.sleep(1)

        d = self.driver.find_element_by_xpath('//input[@aria-label="I/V作成日" and @type="text"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)  # 清除元素属性readonly
        self.driver.find_element(*self.ivzuocheng_element).send_keys(self.listbill)
        time.sleep(1)

        self.driver.find_element(*self.zhechugang_element).send_keys('AXT:秋田空港')
        time.sleep(1)

        self.driver.find_element(*self.zhechugang_element).send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(*self.xingtai_element).click()  # 点击形态下拉框
        time.sleep(1)
        self.driver.find_element(*self.sea_element).click()
        time.sleep(1)

        self.driver.find_element(*self.jianzhi_element).send_keys('FCA')
        time.sleep(1)

        self.driver.find_element(*self.jianzhi_element).send_keys(Keys.ENTER)
        self.driver.find_element(*self.luyanggang_element).send_keys('AOJ:青森空港')
        time.sleep(1)

        self.driver.find_element(*self.luyanggang_element).send_keys(Keys.ENTER)
        self.driver.find_element(*self.tonghuo_element).send_keys('USD')
        time.sleep(1)

        self.driver.find_element(*self.tonghuo_element).send_keys(Keys.ENTER)
        d = self.driver.find_element_by_xpath('//input[@aria-label="ETD" and @type="text"]')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', d)
        time.sleep(1)

        self.driver.find_element(*self.ETD_element).send_keys(self.listbill)
        self.driver.find_element(*self.ETD_element).send_keys(Keys.ENTER)
        time.sleep(1)

        self.driver.execute_script(self.js2)
        time.sleep(1)

        self.driver.find_elements(*self.wuchagnbaocun_element)[1].click()
        time.sleep(3)

        respectvalue = self.driver.find_element(*self.wuchangivosame_element).text
        return respectvalue


    def Plzhongliagndenglu(self):

        time.sleep(1)
        self.driver.find_element(*self.wuchangbutton_element).click()  # 页面点击无偿新规按钮

        time.sleep(2)
        self.driver.find_elements(*self.wuchangzuijia_element)[0].click()  # 页面点击无偿新规追加按钮

        time.sleep(4)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[1].click()
        time.sleep(1)
        self.driver.find_elements(*self.wuchangzuijiashiyong_element)[0].click()
        time.sleep(4)

        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[8].click() # 页面点击invoice详情第一个条记录
        time.sleep(2)

        self.driver.find_element(*self.invoicepldenglubutton_element).click()
        time.sleep(2)

        self.driver.execute_script(self.js1)
        time.sleep(3)
        self.driver.find_elements(*self.wuchangzuijiavaluefirstgouxuan_element)[10].click()  # 页面点击invoice详情第一个条记录
        time.sleep(1)
        self.driver.find_element(*self.zhongliangdenglu_element).click() # 点击重量登录按钮
        time.sleep(2)
        actualvalue=self.driver.find_element(*self.zhongliangdengluconfirm_element).text # 重量登录确认信息
        time.sleep(2)

        return actualvalue