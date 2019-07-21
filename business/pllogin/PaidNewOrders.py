"""
INV P/L登録模块中的有償新規
新建订单
"""
from time import sleep
from selenium import webdriver
from business.Login import Login
from common.Wait import Wait
from pageElement.pllogin.PaidNew import PaidNew
from util.ElementUtil import ElementUtil
from util.createIVNum import create_IVnum


class PaidNewOrders(PaidNew):
    """在有償新規中新建订单"""

    def __init__(self):
        """初始化"""
        self.e = ElementUtil()
        No = str(create_IVnum())
        self.PONum = "1"  # 商品数量
        self.ConNo = "X" + No  # 集装箱编号
        self.IVNo = "M" + No  # invoiceNo

    def transSea(self, driver):
        """
        有償新規的 运输形态选择SEA保存
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录有償新規 运输形态选择SEA保存"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 有償新規
        self.e.click(driver, 15, explain, *self.Paid_element)
        # 点击 P/O で検出
        self.e.click(driver, 15, explain, *self.PODetection_element)
        # 点击 検索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        # 点击任意一条数据
        self.e.click(driver, 15, explain, *self.POChoise_element)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum_element)
        """勾选所有INVOICE 详细添加到Package List详细并填写相关信息"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        # 填写集装箱编号
        self.e.send_keys(driver, 15, self.ConNo, explain, *self.ConNo_element)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, 5, explain, *self.ConSt_element)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, 5, explain, *self.ConEd_element)
        # 填写净重
        self.e.send_keys(driver, 15, 5, explain, *self.ConNW_element)
        # 填写毛重
        self.e.send_keys(driver, 15, 5, explain, *self.ConGW_element)
        # 填写体积
        self.e.send_keys(driver, 15, 5, explain, *self.ConM3_element)
        """填写INVOICE 基本情報并保存"""
        # 将滚动条移动到页面的顶部
        js = "var q=document.documentElement.scrollTop=0"
        driver.execute_script(js)
        # 填写I/V No
        self.e.clear(driver, 15, explain, *self.IVNo_element)
        self.e.send_keys(driver, 15, self.IVNo, explain, *self.IVNo_element)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.IVCraDateChoose_element)
        sleep(2)
        self.e.click(driver, 15, explain, *self.IVCraDay_element)
        # 选择積出港(判断是否自动带出)
        dp = Wait(driver, 10).until(
            lambda the_driver: the_driver.find_element(*self.DeliveryPort_element).get_attribute("value"))
        if dp == None:
            # 点击第一个
            self.e.click(driver, 15, explain, *self.DeliveryPort_element)
            sleep(1)
            self.e.click(driver, 15, explain, *self.Select1st_element)
        # 选择輸送形態中 Sea海运
        self.e.click(driver, 15, explain, *self.TransForm_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.TransSea_element)
        # 选择建値中 FCA货交承运人
        mk = Wait(driver, 10).until(
            lambda the_driver: the_driver.find_element(*self.Market_element).get_attribute("value"))
        if mk == None:
            self.e.click(driver, 15, explain, *self.Market_element)
            sleep(1)
            self.e.click(driver, 15, explain, *self.FCA_element)
        # 选择陸揚港
        up = Wait(driver, 10).until(
            lambda the_driver: the_driver.find_element(*self.UnloadPort_element).get_attribute("value"))
        if up == None:
            # 点击第二个
            self.e.click(driver, 15, explain, *self.UnloadPort_element)
            sleep(1)
            self.e.click(driver, 15, explain, *self.Select2nd_element)
        # 选择通貨
        cu = Wait(driver, 10).until(
            lambda the_driver: the_driver.find_element(*self.Currency_element).get_attribute("value"))
        if cu == None:
            self.e.clear(driver, 15, explain, *self.Currency_element)
            self.e.send_keys(driver, 15, "USD", explain, *self.Currency_element)
            sleep(1)
            self.e.click(driver, 15, explain, *self.SendCur_element)
        # 选择ETD预计到港日期
        self.e.click(driver, 15, explain, *self.ETD_element)
        sleep(2)
        self.e.click(driver, 15, explain, *self.ETDChooseDay_element)
        sleep(2)

    def saveOrder(self, driver):
        """
        正常保存订单
        :param driver:
        :return:
        """
        explain = "INV P/L登录有償新規 正常保存订单"
        # 点击保存
        self.e.click(driver, 15, explain, *self.PaidSave_element)
        try:
            # 判断是否有積出港・陸揚港确定
            dpup = self.e.getText(driver, 15, explain, *self.dpupinf)
            if dpup == "P/Oの積出港・陸揚港とINVの積出港・陸揚港が不一致ですが、次に進めますか？":
                self.e.click(driver, 20, explain, *self.dpupConf)
        except Exception as e:
            pass
        # 点击确定
        self.e.click(driver, 10, explain, *self.PaidSaveSuc_element)
        # 点击保存后弹框的提示信息(保存が完了しました。)
        sleep(2)
        acRes = self.e.getText(driver, 15, explain, *self.PaidCompletedSave_element)
        print(acRes)
        print(self.IVNo)
        return acRes

    def notFillIV(self, driver):
        """
        有偿新规的 I/V NO不填保存
        :param driver:
        :return:
        """
        explain = "INV P/L登录有償新規 test02NotFillIV"
        # 填写订单信息
        self.transSea(driver)
        # 删除I/V NO
        self.e.click(driver, 15, explain, *self.IVClear_element)
        # 点击保存
        self.e.click(driver, 15, explain, *self.PaidSave_element)
        try:
            # 判断是否有積出港・陸揚港确定
            dpup = self.e.getText(driver, 15, explain, *self.dpupinf)
            if dpup == "P/Oの積出港・陸揚港とINVの積出港・陸揚港が不一致ですが、次に進めますか？":
                self.e.click(driver, 15, explain, *self.dpupConf)
            # 点击确定
            self.e.click(driver, 15, explain, *self.PaidSaveSuc_element)
            # 点击保存后弹框的提示信息
            acRes = self.e.getText(driver, 15, explain, *self.PaidCompletedSave_element)
            print(acRes)
            return acRes
        except Exception as e:
            # print(e)
            pass

    def noMarket(self, driver):
        """
        有偿新规的 建值不选择保存
        :param driver:
        :return:
        """
        explain = "INV P/L登录有償新規 test03NoMarket"
        # 填写订单信息
        self.transSea(driver)
        # 删除建值
        self.e.click(driver, 15, explain, *self.MarketClear_element)
        # 判断 保存 按钮是否启用(启用返回TRUE,未启用FALSE)
        res = self.e.is_enabled(driver, 15, explain, *self.PaidSaveDis_element)
        if res == False:
            return "OK"

    def paidNewSuc(self, driver):
        """
        验证有偿新规新增成功
        :param driver:
        :return:
        """
        explain = "INV P/L登录有償新規 test01PaidNewSuc"
        # 填写订单信息
        self.transSea(driver)
        # 保存订单成功
        self.saveOrder(driver)
        # 返回INV P/L登録页面
        driver.back()
        driver.back()
        # 在检索条件中输入I/V NO
        self.e.clear(driver, 15, explain, *self.SearchIV_element)
        self.e.send_keys(driver, 10, self.IVNo, explain, *self.SearchIV_element)
        # 点击检索按钮
        self.e.click(driver, 10, explain, *self.Search_element)
        sleep(2)
        # 获取检索结果的I/V NO
        SearchIV = self.e.getText(driver, 10, explain, *self.ResIV_element)
        print(SearchIV)
        return SearchIV, self.IVNo

    def checkPOAdd(self, driver):
        """
        有偿新规的 选择商品进行P/L登录，Package List详细中数据同步
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录有償新規 test04CheckPOAdd"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 有償新規
        self.e.click(driver, 15, explain, *self.Paid_element)
        # 点击 P/O で検出
        self.e.click(driver, 15, explain, *self.PODetection_element)
        # 点击 検索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        # 点击任意一条数据
        self.e.click(driver, 15, explain, *self.POChoise_element)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum_element)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        """查看Package List详情是否显示与INVOICE 详细对应记录"""
        # Package List详情 的P/O NO、社内品番、品種
        acPONO = self.e.getText(driver, 15, explain, *self.PLPONo1st_element)
        acCoNum = self.e.getText(driver, 15, explain, *self.PLConNo1st_element)
        acKind = self.e.getText(driver, 15, explain, *self.PLKind1st_element)
        return acPONO, acCoNum, acKind

    def changeTrans(self, driver):
        """
        选择新增的运输形态为Sea的I/V NO记录,修改运输形态为Air
        :param driver:
        :return:
        """
        explain = "INV P/L登录有償新規 test05ChangeTrans"
        # 填写订单信息
        self.transSea(driver)
        # 保存订单成功
        self.saveOrder(driver)
        # 返回INV P/L登録页面
        driver.back()
        driver.back()
        # 在检索条件中输入I/V NO
        self.e.clear(driver, 15, explain, *self.SearchIV_element)
        self.e.send_keys(driver, 15, self.IVNo, explain, *self.SearchIV_element)
        # 点击检索按钮
        self.e.click(driver, 15, explain, *self.Search_element)
        # 勾选检索出的P/O记录的勾选框
        self.e.click(driver, 15, explain, *self.ResSel_element)
        # 点击編集
        self.e.click(driver, 15, explain, *self.Edit_element)
        # 选择輸送形態中 Air空运
        self.e.click(driver, 15, explain, *self.TransForm_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.TransAir_element)
        try:
            # 点击保存
            kk = driver.find_element(*self.PaidSave_element)
            driver.execute_script("arguments[0].click();", kk)
            # self.e.click(driver,3,*self.PaidSave_element)
            # 点击确定
            self.e.click(driver, 15, explain, *self.PaidSaveSuc_element)
            # 点击保存后弹框的提示信息(保存が完了しました。)
            acRes = self.e.getText(driver, 15, explain, *self.PaidCompletedSave_element)
            print(acRes)
            return acRes
        except Exception as e:
            # print(e)
            pass

    def paidDfaultSuc(self, driver):
        """
        INV P/L登录有偿新规，有偿新规默认新增成功"
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录有償新規 test06PaidDfaultSuc"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 有償新規
        self.e.click(driver, 15, explain, *self.Paid_element)
        # 点击 P/O で検出
        self.e.click(driver, 15, explain, *self.PODetection_element)
        # 点击 検索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        # 点击任意一条数据
        self.e.click(driver, 15, explain, *self.POChoise_element)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum_element)
        """勾选所有INVOICE 详细添加到Package List详细并填写相关信息"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
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
        """填写INVOICE 基本情報并保存"""
        # 将滚动条移动到页面的顶部
        js = "var q=document.documentElement.scrollTop=0"
        driver.execute_script(js)
        # 填写I/V No
        self.e.clear(driver, 15, explain, *self.IVNo_element)
        self.e.send_keys(driver, 15, self.IVNo, explain, *self.IVNo_element)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.IVCraDateChoose_element)
        sleep(2)
        self.e.click(driver, 15, explain, *self.IVCraDay_element)
        # 选择積出港(判断是否自动带出)
        dp = Wait(driver, 10).until(
            lambda the_driver: the_driver.find_element(*self.DeliveryPort_element).get_attribute("value"))
        if dp == None:
            # 点击第一个
            self.e.click(driver, 15, explain, *self.DeliveryPort_element)
            sleep(1)
            self.e.click(driver, 15, explain, *self.Select1st_element)
        # 选择輸送形態中 Sea海运
        tf = Wait(driver, 10).until(
            lambda the_driver: the_driver.find_element(*self.TransForm_element).get_attribute("value"))
        if tf == None:
            self.e.click(driver, 15, explain, *self.TransForm_element)
            sleep(1)
            self.e.click(driver, 15, explain, *self.TransSea_element)
        # 选择建値中 FCA货交承运人
        mk = Wait(driver, 10).until(
            lambda the_driver: the_driver.find_element(*self.Market_element).get_attribute("value"))
        if mk == None:
            self.e.click(driver, 15, explain, *self.Market_element)
            sleep(1)
            self.e.click(driver, 15, explain, *self.FCA_element)
        # 选择陸揚港
        up = Wait(driver, 10).until(
            lambda the_driver: the_driver.find_element(*self.UnloadPort_element).get_attribute("value"))
        if up == None:
            # 点击第二个
            self.e.click(driver, 15, explain, *self.UnloadPort_element)
            sleep(1)
            self.e.click(driver, 15, explain, *self.Select2nd_element)
        # 选择通貨
        cu = Wait(driver, 10).until(
            lambda the_driver: the_driver.find_element(*self.Currency_element).get_attribute("value"))
        if cu == None:
            self.e.clear(driver, 15, explain, *self.Currency_element)
            self.e.send_keys(driver, 15, "USD", explain, *self.Currency_element)
            sleep(1)
            self.e.click(driver, 15, explain, self.SendCur_element)
        # 选择ETD预计到港日期
        self.e.click(driver, 15, explain, *self.ETD_element)
        sleep(1)
        self.e.click(driver, 15, explain, *self.ETDChooseDay_element)
        # 保存订单成功
        self.saveOrder(driver)
        # 返回INV P/L登録页面
        driver.back()
        driver.back()
        # 在检索条件中输入I/V NO
        self.e.clear(driver, 15, explain, *self.SearchIV_element)
        self.e.send_keys(driver, 15, self.IVNo, explain, *self.SearchIV_element)
        # 点击检索按钮
        self.e.click(driver, 15, explain, *self.Search_element)
        sleep(2)
        # 获取检索结果的I/V NO
        SearchIV = self.e.getText(driver, 15, explain, *self.ResIV_element)
        print(SearchIV)
        return SearchIV, self.IVNo

    def checkPOAddNoNum(self, driver):
        """
        有偿新规的 选择商品不修改数量进行P/L登录，Package List详细中数据同步
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录有償新規 test04CheckPOAdd"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 有償新規
        self.e.click(driver, 15, explain, *self.Paid_element)
        # 点击 P/O で検出
        self.e.click(driver, 15, explain, *self.PODetection_element)
        # 点击 検索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        # 点击任意一条数据
        self.e.click(driver, 15, explain, *self.POChoise_element)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 填写商品数量
        # self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum_element)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        """查看Package List详情是否显示与INVOICE 详细对应记录"""
        # Package List详情 的P/O NO、社内品番、品種
        acPONO = self.e.getText(driver, 15, explain, *self.PLPONo1st_element)
        acCoNum = self.e.getText(driver, 15, explain, *self.PLConNo1st_element)
        acKind = self.e.getText(driver, 15, explain, *self.PLKind1st_element)
        return acPONO, acCoNum, acKind

    def addConNo(self, driver):
        """
        有償新規的 P/L登录后,填写识别番号
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录有償新規P/L登录后,填写识别番号"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 有償新規
        self.e.click(driver, 15, explain, *self.Paid_element)
        # 点击 P/O で検出
        self.e.click(driver, 15, explain, *self.PODetection_element)
        # 点击 検索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        # 点击任意一条数据
        self.e.click(driver, 15, explain, *self.POChoise_element)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum_element)
        """勾选所有INVOICE 详细添加到Package List详细并填写相关信息"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        # 填写集装箱编号
        self.e.send_keys(driver, 15, self.ConNo, explain, *self.ConNo_element)
        return "OK"

    def addConSt(self, driver):
        """
        有償新規的 P/L登录后,填写集装箱开始号
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录有償新規P/L登录后,填写集装箱开始号"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 有償新規
        self.e.click(driver, 15, explain, *self.Paid_element)
        # 点击 P/O で検出
        self.e.click(driver, 15, explain, *self.PODetection_element)
        # 点击 検索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        # 点击任意一条数据
        self.e.click(driver, 15, explain, *self.POChoise_element)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum_element)
        """勾选所有INVOICE 详细添加到Package List详细并填写相关信息"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        # 填写集装箱编号
        self.e.send_keys(driver, 15, self.ConNo, explain, *self.ConNo_element)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, 5, explain, *self.ConSt_element)
        return "OK"

    def addConEd(self, driver):
        """
        有償新規的 P/L登录后,填写集装箱结束号
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录有償新規P/L登录后,填写集装箱结束号"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 有償新規
        self.e.click(driver, 15, explain, *self.Paid_element)
        # 点击 P/O で検出
        self.e.click(driver, 15, explain, *self.PODetection_element)
        # 点击 検索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        # 点击任意一条数据
        self.e.click(driver, 15, explain, *self.POChoise_element)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum_element)
        """勾选所有INVOICE 详细添加到Package List详细并填写相关信息"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        # 填写集装箱编号
        self.e.send_keys(driver, 15, self.ConNo, explain, *self.ConNo_element)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, 5, explain, *self.ConSt_element)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, 5, explain, *self.ConEd_element)
        return "OK"

    def addConNW(self, driver):
        """
        有償新規的 P/L登录后,填写净重
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录有償新規P/L登录后,填写净重"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 有償新規
        self.e.click(driver, 15, explain, *self.Paid_element)
        # 点击 P/O で検出
        self.e.click(driver, 15, explain, *self.PODetection_element)
        # 点击 検索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        # 点击任意一条数据
        self.e.click(driver, 15, explain, *self.POChoise_element)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum_element)
        """勾选所有INVOICE 详细添加到Package List详细并填写相关信息"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        # 填写集装箱编号
        self.e.send_keys(driver, 15, self.ConNo, explain, *self.ConNo_element)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, 5, explain, *self.ConSt_element)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, 5, explain, *self.ConEd_element)
        # 填写净重
        self.e.send_keys(driver, 15, "5", explain, *self.ConNW_element)
        return "OK"

    def addConGW(self, driver):
        """
        有償新規的 P/L登录后,填写毛重
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录有償新規P/L登录后,填写毛重"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 有償新規
        self.e.click(driver, 15, explain, *self.Paid_element)
        # 点击 P/O で検出
        self.e.click(driver, 15, explain, *self.PODetection_element)
        # 点击 検索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        # 点击任意一条数据
        self.e.click(driver, 15, explain, *self.POChoise_element)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum_element)
        """勾选所有INVOICE 详细添加到Package List详细并填写相关信息"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        # 填写集装箱编号
        self.e.send_keys(driver, 15, self.ConNo, explain, *self.ConNo_element)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, 5, explain, *self.ConSt_element)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, 5, explain, *self.ConEd_element)
        # 填写净重
        self.e.send_keys(driver, 15, "5", explain, *self.ConNW_element)
        # 填写毛重
        self.e.send_keys(driver, 15, "5", explain, *self.ConGW_element)
        return "OK"

    def addConM3(self, driver):
        """
        有償新規的 P/L登录后,填写体积
        :param driver:
        :return:
        """
        """检索P/L使用到INVOICE 详细"""
        explain = "INV P/L登录有償新規P/L登录后,填写体积"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVPL_element)
        # 点击 有償新規
        self.e.click(driver, 15, explain, *self.Paid_element)
        # 点击 P/O で検出
        self.e.click(driver, 15, explain, *self.PODetection_element)
        # 点击 検索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        # 点击任意一条数据
        self.e.click(driver, 15, explain, *self.POChoise_element)
        # 点击使用
        self.e.click(driver, 15, explain, *self.POUse_element)
        # 填写商品数量
        self.e.clear(driver, 15, explain, *self.PONum_element)
        self.e.send_keys(driver, 15, self.PONum, explain, *self.PONum_element)
        """勾选所有INVOICE 详细添加到Package List详细并填写相关信息"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.POAll_element)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.PLReg_element)
        # 填写集装箱编号
        self.e.send_keys(driver, 15, self.ConNo, explain, *self.ConNo_element)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, 5, explain, *self.ConSt_element)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, 5, explain, *self.ConEd_element)
        # 填写净重
        self.e.send_keys(driver, 15, "5", explain, *self.ConNW_element)
        # 填写毛重
        self.e.send_keys(driver, 15, "5", explain, *self.ConGW_element)
        # 填写体积
        self.e.send_keys(driver, 15, "5", explain, *self.ConM3_element)
        return "OK"


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
    paid = PaidNewOrders()
    # 登录
    login.test_click_login_btn(driver)
    sleep(2)
    # res = paid.transSea(driver)
    # res = paid.notFillIV(driver)
    # res = paid.noMarket(driver)
    # res = paid.paidNewSuc(driver)
    # res = paid.checkPOAdd(driver)
    res = paid.changeTrans(driver)
    print(res)
    driver.quit()
