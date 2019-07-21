"""
INV P/L登録模块中的无償新規
新建订单
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

from business.Login import Login
from common.Wait import Wait
from pageElement.pllogin.FreeNew import FreeNew
from util.createIVNum import create_IVnum
from util.ElementUtil import ElementUtil


class FreeNewOrders(FreeNew):
    """在无償新規中新建订单"""

    def __init__(self):
        """初始化"""
        self.e = ElementUtil()
        No = str(create_IVnum())
        self.PONum = "1"  # 商品数量
        self.ConNo = "M" + No  # 集装箱编号
        self.IVNo = "M" + No  # invoiceNo

    def checkPOAddOne(self, driver):
        """
        无償新規的 选择1条P/O记录进行P/L登录，Package List显示对应的记录
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录无償新規 test01CheckPOAddOne"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.Free_element)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.POAdd_element)
        sleep(4)
        # 点击 検索
        # self.e.click(driver,5,explain,*self.POSearch_element)
        # 点击任意一条数据
        # kk = driver.find_element(*self.POChoiseOne_element)
        # driver.execute_script("arguments[0].click();", kk)
        # self.e.click(driver,5,*self.POChoiseOne_element)
        driver.find_element(*self.POChoiseOne_element).send_keys(Keys.SPACE)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写商品数量
        # self.e.clear(driver,5,*self.PONum1st_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum1st_element)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        sleep(1)
        """查看Package List详情是否显示与INVOICE 详细对应记录"""
        # Package List详情 的社内品番
        acCoNum = self.e.getText(driver, 15, explain, *self.PLConNo1st_element)
        # Package List详情 的数量
        PLNum = Wait(driver, 10).until(
            lambda the_driver: the_driver.find_element(*self.PLNum1st_element).get_attribute("value"))
        return acCoNum, PLNum, self.PONum

    def checkPOAddTwo(self, driver):
        """
        无償新規的 不选择选择P/O记录进行P/L登录，Package List不显示对应的记录
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录无償新規 test02CheckPOAddTwo"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.Free_element)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.POAdd_element)
        sleep(4)
        # 点击 検索
        # self.e.click(driver,5,explain,*self.POSearch_element)
        # 点击任意一条数据
        # kk = driver.find_element(*self.POChoiseOne_element)
        # driver.execute_script("arguments[0].click();", kk)
        # self.e.click(driver,5,*self.POChoiseOne_element)
        driver.find_element(*self.POChoiseOne_element).send_keys(Keys.SPACE)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum1st_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum1st_element)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        """查看Package List详情是否显示与INVOICE 详细对应记录"""
        # Package List详情显示 No data available
        acNoData = self.e.getText(driver, 15, explain, *self.PLNoData_element)
        return acNoData

    def checkPOAddThree(self, driver):
        """
        无償新規的 选择2条P/O记录进行P/L登录，Package List显示对应的记录
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录无償新規 test03CheckPOAddThree"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.Free_element)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.POAdd_element)
        sleep(4)
        # 点击 検索
        # self.e.click(driver,5,explain,*self.POSearch_element)
        # 点击任意两条数据
        # kk1 = driver.find_element(*self.POChoise1st_element)
        # driver.execute_script("arguments[0].click();", kk1)
        # kk2 = driver.find_element(*self.POChoise2nd_element)
        # driver.execute_script("arguments[0].click();", kk2)
        # self.e.click(driver, 15, *self.POChoise1st_element)
        # self.e.click(driver, 15, *self.POChoise2nd_element)
        driver.find_element(*self.POChoise1st_element).send_keys(Keys.SPACE)
        driver.find_element(*self.POChoise2nd_element).send_keys(Keys.SPACE)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum1st_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum1st_element)
        self.e.clear(driver, 15, explain, *self.PONum2nd_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum2nd_element)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        sleep(4)
        """查看Package List详情是否显示与INVOICE 详细对应记录"""
        # Package List详情 第一条的社内品番
        acCoNum1st = self.e.getText(driver, 15, explain, *self.POCoNum1st_element)
        # Package List详情 第二条的社内品番
        acCoNum2nd = self.e.getText(driver, 15, explain, *self.POCoNum2nd_element)
        return acCoNum1st, acCoNum2nd

    def checkPLInput(self, driver):
        """
        无償新規的 选择P/O进行P/L登录，填写数量、N/W、G/W、M3
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录无償新規 test04CheckPLInput"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.Free_element)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.POAdd_element)
        sleep(4)
        # 点击 検索
        # self.e.click(driver,5,explain,*self.POSearch_element)
        # 点击任意一条数据
        # kk = driver.find_element(*self.POChoiseOne_element)
        # driver.execute_script("arguments[0].click();", kk)
        # self.e.click(driver, 15, explain,*self.POChoiseOne_element)
        driver.find_element(*self.POChoiseOne_element).send_keys(Keys.SPACE)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB単価
        self.e.clear(driver, 15, explain, *self.FOBPrice_element)
        self.e.send_keys(driver, 15, "12", explain, *self.FOBPrice_element)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum1st_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum1st_element)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        """填写Package List详情的数量、N/W、G/W、M3"""
        # 填写集装箱编号
        self.e.send_keys(driver, 15, self.ConNo, explain, *self.ConNo_element)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, "1", explain, *self.ConSt_element)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, "1", explain, *self.ConEd_element)
        # 填写净重
        self.e.send_keys(driver, 15, "1", explain, *self.ConNW_element)
        # 填写毛重
        self.e.send_keys(driver, 15, "1", explain, *self.ConGW_element)
        # 填写体积
        self.e.send_keys(driver, 15, "1", explain, *self.ConM3_element)
        return "OK"

    def notSelPODel(self, driver):
        """
        无償新規的 选择P/O进行P/L登录，在INVOCIE详情中不选择P/O记录执行删除操作
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录无償新規 test05NotSelPODel"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.Free_element)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.POAdd_element)
        sleep(4)
        # 点击 検索
        # self.e.click(driver,5,explain,*self.POSearch_element)
        # 点击任意一条数据
        # kk = driver.find_element(*self.POChoiseOne_element)
        # driver.execute_script("arguments[0].click();", kk)
        # self.e.click(driver, 15, *self.POChoiseOne_element)
        driver.find_element(*self.POChoiseOne_element).send_keys(Keys.SPACE)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB単価
        self.e.clear(driver, 15, explain, *self.FOBPrice_element)
        self.e.send_keys(driver, 15, "12", explain, *self.FOBPrice_element)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum1st_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum1st_element)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        """在INVOICE详细中不勾选P/O记录，点击删除"""
        # 判断 削除 按钮是否启用(启用返回TRUE,未启用FALSE)
        res = self.e.is_enabled(driver, 15, explain, *self.PODelDis_element)
        if res == False:
            return "OK"

    def notSelPLDel(self, driver):
        """
        无償新規的 选择P/O进行P/L登录，在Package List详细中不选择P/O记录执行删除操作
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录无償新規 test06NotSelPLDel"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.Free_element)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.POAdd_element)
        sleep(4)
        # 点击 検索
        # self.e.click(driver,5,explain,*self.POSearch_element)
        # 点击任意一条数据
        # kk = driver.find_element(*self.POChoiseOne_element)
        # driver.execute_script("arguments[0].click();", kk)
        # self.e.click(driver, 15, explain,*self.POChoiseOne_element)
        driver.find_element(*self.POChoiseOne_element).send_keys(Keys.SPACE)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB単価
        self.e.clear(driver, 15, explain, *self.FOBPrice_element)
        self.e.send_keys(driver, 15, "12", explain, *self.FOBPrice_element)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum1st_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum1st_element)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        """在Package List详细中不勾选P/O记录，点击删除"""
        # 判断 削除 按钮是否启用(启用返回TRUE,未启用FALSE)
        res = self.e.is_enabled(driver, 15, explain, *self.PODelDis_element)
        if res == False:
            return "OK"

    def transSea(self, driver):
        """
        无償新規的 运输形态选择SEA保存
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录无償新規 运输形态选择SEA保存"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.Free_element)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.POAdd_element)
        sleep(4)
        # 点击 検索
        # self.e.click(driver,5,explain,*self.POSearch_element)
        # 点击任意一条数据
        # kk = driver.find_element(*self.POChoiseOne_element)
        # driver.execute_script("arguments[0].click();", kk)
        # self.e.click(driver, 15, explain,*self.POChoiseOne_element)
        driver.find_element(*self.POChoiseOne_element).send_keys(Keys.SPACE)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum1st_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum1st_element)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        """填写Package List详情的数量、N/W、G/W、M3"""
        # 填写集装箱编号
        self.e.send_keys(driver, 15, self.ConNo, explain, *self.ConNo_element)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, "6", explain, *self.ConSt_element)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, "6", explain, *self.ConEd_element)
        # 填写净重
        self.e.send_keys(driver, 15, "6", explain, *self.ConNW_element)
        # 填写毛重
        self.e.send_keys(driver, 15, "6", explain, *self.ConGW_element)
        # 填写体积
        self.e.send_keys(driver, 15, "6", explain, *self.ConM3_element)
        # 将滚动条移动到页面的顶部
        js = "var q=document.documentElement.scrollTop=0"
        driver.execute_script(js)
        """填写INVOICE 基本情報并保存"""
        # 选择海外取引先
        self.e.click(driver, 15, explain, *self.OverseasCus_element)
        sleep(1)
        # 点击第一条
        self.e.click(driver, 15, explain, *self.Select1st_element)
        # 填写I/V No
        self.e.send_keys(driver, 15, self.IVNo, explain, *self.IVNo_element)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.IVCraDateChoose_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.IVCraDay_element)
        # 选择積出港
        self.e.click(driver, 15, explain, *self.DeliveryPort_element)
        sleep(1)
        # 点击第一个
        self.e.click(driver, 15, explain, *self.Select1st_element)
        # 选择輸送形態中 Sea海运
        self.e.click(driver, 15, explain, *self.TransForm_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.TransSea_element)
        # 选择建値中 FCA货交承运人
        self.e.click(driver, 15, explain, *self.Market_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.FCA_element)
        # 选择陸揚港
        self.e.click(driver, 15, explain, *self.UnloadPort_element)
        sleep(1)
        # 点击第二个
        self.e.click(driver, 15, explain, *self.Select2nd_element)
        # 选择通貨
        self.e.send_keys(driver, 15, "USD", explain, *self.Currency_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.SendTip_element)
        # 选择ETD预计到港日期
        self.e.click(driver, 15, explain, *self.ETD_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.ETDChooseDay_element)
        # 点击保存
        self.e.click(driver, 15, explain, *self.FreeSave_element)
        # 点击确定
        self.e.click(driver, 15, explain, *self.FreeSaveSuc_element)
        sleep(4)
        # 点击保存后弹框的提示信息(保存が完了しました。)
        acRes = self.e.getText(driver, 15, explain, *self.FreeCompletedSave_element)
        print(acRes)
        return acRes

    def freeNewSuc(self, driver):
        """
        INV P/L登录无偿新规，验证无偿新规新增成功
        :param driver:
        :return:
        """
        explain = "INV P/L登录无償新規 test07FreeNewSuc"
        # 新建一条无償新規的运输形态选择SEA的订单
        self.transSea(driver)
        # 返回INV P/L登録页面
        driver.back()
        driver.back()
        # 在检索条件中输入I/V NO
        self.e.send_keys(driver, 15, self.IVNo, explain, *self.SearchIV_element)
        # 点击检索按钮
        self.e.click(driver, 15, explain, *self.Search_element)
        sleep(4)
        # 获取检索结果的I/V NO
        SearchIV = self.e.getText(driver, 15, explain, *self.ResIV_element)
        print(SearchIV)
        return SearchIV, self.IVNo

    def notInputIV(self, driver):
        """
        无償新規的 I/V NO不输入保存
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录无償新規 test08NotInputIV"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.Free_element)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.POAdd_element)
        sleep(4)
        # 点击 検索
        # self.e.click(driver,5,explain,*self.POSearch_element)
        # 点击任意一条数据
        # kk = driver.find_element(*self.POChoiseOne_element)
        # driver.execute_script("arguments[0].click();", kk)
        # self.e.click(driver, 15, explain,*self.POChoiseOne_element)
        driver.find_element(*self.POChoiseOne_element).send_keys(Keys.SPACE)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum1st_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum1st_element)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        """填写Package List详情的数量、N/W、G/W、M3"""
        # 填写集装箱编号
        self.e.send_keys(driver, 15, self.ConNo, explain, *self.ConNo_element)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, "5", explain, *self.ConSt_element)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, "5", explain, *self.ConEd_element)
        # 填写净重
        self.e.send_keys(driver, 15, "5", explain, *self.ConNW_element)
        # 填写毛重
        self.e.send_keys(driver, 15, "5", explain, *self.ConGW_element)
        # 填写体积
        self.e.send_keys(driver, 15, "5", explain, *self.ConM3_element)
        # 将滚动条移动到页面的顶部
        js = "var q=document.documentElement.scrollTop=0"
        driver.execute_script(js)
        """填写INVOICE 基本情報并保存"""
        # 选择海外取引先
        self.e.click(driver, 15, explain, *self.OverseasCus_element)
        sleep(1)
        # 点击第一条
        self.e.click(driver, 15, explain, *self.Select1st_element)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.IVCraDateChoose_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.IVCraDay_element)
        # 选择積出港
        self.e.click(driver, 15, explain, *self.DeliveryPort_element)
        sleep(1)
        # 点击第一个
        self.e.click(driver, 15, explain, *self.Select1st_element)
        # 选择輸送形態中 Sea海运
        self.e.click(driver, 15, explain, *self.TransForm_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.TransSea_element)
        # 选择建値中 FOB船上交货价
        self.e.click(driver, 15, explain, *self.Market_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.FOB_element)
        # 选择陸揚港
        self.e.click(driver, 15, explain, *self.UnloadPort_element)
        sleep(1)
        # 点击第二个
        self.e.click(driver, 15, explain, *self.Select2nd_element)
        # 选择通貨
        self.e.send_keys(driver, 15, "USD", explain, *self.Currency_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.SendTip_element)
        # 选择ETD预计到港日期
        self.e.click(driver, 15, explain, *self.ETD_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.ETDChooseDay_element)
        # 点击保存
        self.e.click(driver, 15, explain, *self.FreeSave_element)
        try:
            # 点击确定
            self.e.click(driver, 15, explain, *self.FreeSaveSuc_element)
            sleep(4)
            # 点击保存后弹框的提示信息
            acRes = self.e.getText(driver, 15, explain, *self.FreeCompletedSave_element)
            print(acRes)
            return acRes
        except Exception as e:
            # print(e)
            pass

    def IVExceedLimit(self, driver):
        """
        无償新規的 IV/NO订单号长度超过7个字符
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录无償新規 test09IVExceedLimit"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.Free_element)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.POAdd_element)
        sleep(4)
        # 点击 検索
        # self.e.click(driver,5,explain,*self.POSearch_element)
        # 点击任意一条数据
        # kk = driver.find_element(*self.POChoiseOne_element)
        # driver.execute_script("arguments[0].click();", kk)
        # self.e.click(driver, 15, explain,*self.POChoiseOne_element)
        driver.find_element(*self.POChoise2nd_element).send_keys(Keys.SPACE)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum1st_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum1st_element)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        """填写Package List详情的数量、N/W、G/W、M3"""
        # 填写集装箱编号
        self.e.send_keys(driver, 15, self.ConNo, explain, *self.ConNo_element)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, "5", explain, *self.ConSt_element)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, "5", explain, *self.ConEd_element)
        # 填写净重
        self.e.send_keys(driver, 15, "5", explain, *self.ConNW_element)
        # 填写毛重
        self.e.send_keys(driver, 15, "5", explain, *self.ConGW_element)
        # 填写体积
        self.e.send_keys(driver, 15, "5", explain, *self.ConM3_element)
        # 将滚动条移动到页面的顶部
        js = "var q=document.documentElement.scrollTop=0"
        driver.execute_script(js)
        """填写INVOICE 基本情報并保存"""
        # 选择海外取引先
        self.e.click(driver, 15, explain, *self.OverseasCus_element)
        sleep(1)
        # 点击第一条
        self.e.click(driver, 15, explain, *self.Select1st_element)
        # 填写I/V No
        self.e.send_keys(driver, 15, "IV20199_CS", explain, *self.IVNo_element)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.IVCraDateChoose_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.IVCraDay_element)
        # 选择積出港
        self.e.click(driver, 15, explain, *self.DeliveryPort_element)
        sleep(1)
        # 点击第一个
        self.e.click(driver, 15, explain, *self.Select1st_element)
        # 选择輸送形態中 Sea海运
        self.e.click(driver, 15, explain, *self.TransForm_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.TransSea_element)
        # 选择建値中 FCA货交承运人
        self.e.click(driver, 15, explain, *self.Market_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.FCA_element)
        # 选择陸揚港
        self.e.click(driver, 15, explain, *self.UnloadPort_element)
        sleep(1)
        # 点击第二个
        self.e.click(driver, 15, explain, *self.Select2nd_element)
        # 选择通貨
        self.e.send_keys(driver, 15, "CNY", explain, *self.Currency_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.SendTip_element)
        # 选择ETD预计到港日期
        self.e.click(driver, 15, explain, *self.ETD_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.ETDChooseDay_element)
        # I/V No.超过7位的提示信息(INV.Noは7桁以内でご記入ください。)
        acRes = self.e.getText(driver, 15, explain, *self.IVExceedTips_element)
        print(acRes)
        return acRes


if __name__ == '__main__':
    # driver = webdriver.Chrome()
    from selenium.webdriver.chrome.options import Options

    option = Options()
    option.add_argument('----headless')
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(15)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)
    driver.maximize_window()
    url = "https://sharpsit.jusdaglobal.com"
    driver.get(url)
    login = Login()
    free = FreeNewOrders()
    # 登录
    login.test_click_login_btn(driver)
    sleep(4)
    # res = free.checkPOAddOne(driver)
    # res = free.checkPOAddTwo(driver)
    # res = free.checkPOAddThree(driver)
    # res = free.checkPLInput(driver)
    # res = free.notSelPODel(driver)
    # res = free.notSelPLDel(driver)
    # res = free.transSea(driver)
    res = free.freeNewSuc(driver)
    # res = free.notInputIV(driver)
    # res = free.IVExceedLimit(driver)
    sleep(4)
    print(res)
    driver.quit()
