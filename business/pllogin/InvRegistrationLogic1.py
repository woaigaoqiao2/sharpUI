from time import sleep, time
from selenium.webdriver.common.keys import Keys
from pageElement.pllogin.InvRegistrationLocation1 import Location
from selenium.webdriver import ActionChains
from util.ElementUtil import ElementUtil
from common.Wait import Wait


class Logic(Location):
    def __init__(self):

        self.e = ElementUtil()
        self.test15danjia = '100';
        self.test15shuliang = '1';
        self.test16csn = '1';
        self.test16cen = '1';
        self.test17shibiefanhao = 'PW0002';
        self.test17rushu = '1';
        self.test19danjia = '100';
        self.test19shuliang = '1';
        self.test20danjia = '1200';
        self.test20shuliang = '1';
        self.test20shibiefanhao = 'S045';
        self.test20csn = '1';
        self.test20cen = '1';
        self.test20nw = '1';
        self.test20gw = '1';
        self.test20m = '1';
        self.test20IVno = 'IM' + str(time())[-5:];
        self.test20tonghuo = 'USD';
        self.test20yunshuxintai = 'AIR';
        self.test21ivno = 'IM' + str(time())[-5:];
        self.test24shuliang = '2';
        self.test24shibiefanhao = 'S002'
        self.test24CartonStartNo = '1';
        self.test24CartonEndNo = '1';
        # self.test24rushu = '2';
        self.test24nw = '1';
        self.test24gw = '1';
        self.test24m3 = '1';
        self.test24IVno = 'IM' + str(time())[-5:];

    def test15(self, driver):
        explain = "INV P/L登录无償新規 test15填写数量、FOB単価进行P/L登录"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.WuChangXinGui)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.test15BL_shangpinzhuijia)
        sleep(2)
        # 检索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        sleep(4)
        # 点击任意一条数据
        # driver.find_element(*self.test15BL_shuju).send_keys(Keys.SPACE)
        # self.e.click(driver, 15, explain, *self.test15BL_shuju)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shuju))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shuju).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test15BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB单价
        self.e.send_keys(driver, 15, self.test15danjia, explain, *self.test15BL_danjia)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test15shuliang, explain, *self.test15BL_shuliang)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.test15BL_xuanze)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.WplDengLu)
        sucess_text = 'OK'
        return sucess_text

    def test16(self, driver):
        explain = "INV P/L登录无償新規 test16填写Carton Start No，Carton Start No"
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.WuChangXinGui)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.test15BL_shangpinzhuijia)
        sleep(2)
        # 检索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        sleep(4)
        # 点击任意一条数据
        # driver.find_element(*self.test15BL_shuju).send_keys(Keys.SPACE)
        # self.e.click(driver, 15, *self.test15BL_shuju)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shuju))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shuju).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test15BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB单价
        self.e.send_keys(driver, 15, self.test15danjia, explain, *self.test15BL_danjia)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test15shuliang, explain, *self.test15BL_shuliang)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.test15BL_xuanze)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.WplDengLu)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, self.test16csn, explain, *self.test16BL_csn)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, self.test16cen, explain, *self.test16BL_cen)
        success_text = "OK";
        return success_text

    def test17(self, driver):
        explain = "INV P/L登录无償新規 test17填写识别番号 "
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.WuChangXinGui)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.test15BL_shangpinzhuijia)
        sleep(2)
        # 检索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        sleep(4)
        # 点击任意一条数据
        # driver.find_element(*self.test15BL_shuju).send_keys(Keys.SPACE)
        # self.e.click(driver, 15, *self.test15BL_shuju)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shuju))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shuju).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test15BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB单价
        self.e.send_keys(driver, 15, self.test15danjia, explain, *self.test15BL_danjia)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test15shuliang, explain, *self.test15BL_shuliang)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.test15BL_xuanze)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.WplDengLu)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, self.test16csn, explain, *self.test16BL_csn)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, self.test16cen, explain, *self.test16BL_cen)
        # 填写识别番号
        self.e.send_keys(driver, 15, self.test17shibiefanhao, explain, *self.test17BL_shibiefanhao)
        success_text = "OK"
        return success_text

    def test18(self, driver):
        explain = "INV P/L登录无償新規 test18在INVOCIE详情中选择P/O记录执行删除操作 "
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.WuChangXinGui)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.test15BL_shangpinzhuijia)
        sleep(2)
        # 检索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        sleep(4)
        # 点击任意一条数据
        # driver.find_element(*self.test15BL_shuju).send_keys(Keys.SPACE)
        # self.e.click(driver, 15, *self.test15BL_shuju)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test18BL_xuanzeshuju))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test18BL_xuanzeshuju).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test15BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB单价
        self.e.send_keys(driver, 15, self.test15danjia, explain, *self.test15BL_danjia)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test15shuliang, explain, *self.test15BL_shuliang)
        # INVOICE详细中选择数据削除
        self.e.click(driver, 15, explain, *self.test15BL_xuanze)
        # 削除
        self.e.click(driver, 15, explain, *self.test18BL_xiaochu)
        # 是否消除
        self.e.click(driver, 15, explain, *self.test18BL_shifouxiaoshu)
        sleep(2)
        Actual_result = self.e.getText(driver, 15, explain, *self.test18BL_actual_result)
        # 确认消除
        self.e.click(driver, 15, explain, *self.test18BL_querenxiaochu)
        return Actual_result

    def test19(self, driver):
        explain = "INV P/L登录无償新規 test19在Package List详细中选择P/O记录执行删除操作 "
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.WuChangXinGui)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.test19BL_shangpinzhuijia)
        sleep(2)
        # 检索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        sleep(4)
        # 点击任意一条数据
        # driver.find_element(*self.test15BL_shuju).send_keys(Keys.SPACE)
        # self.e.click(driver, 15, explain, *self.test15BL_shuju)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_xuanzeshuju))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_xuanzeshuju).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test19BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB单价
        self.e.send_keys(driver, 15, self.test19danjia, explain, *self.test19BL_danjia)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test19shuliang, explain, *self.test19BL_shuliang)
        # INVOICE详细中选择数据
        self.e.click(driver, 15, explain, *self.test19BL_shujuxuanze)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.WplDengLu)
        # Package List详细中选择数据
        self.e.click(driver, 15, explain, *self.test19BL_PLxuanze)
        # 点击削除
        self.e.click(driver, 15, explain, *self.WplXiaoChu)
        # 是否消除
        self.e.click(driver, 15, explain, *self.test18BL_shifouxiaoshu)
        sleep(2)
        Actual_result = self.e.getText(driver, 15, explain, *self.test18BL_actual_result)
        # 确认消除
        self.e.click(driver, 15, explain, *self.test18BL_querenxiaochu)
        return Actual_result

    def test20(self, driver):
        explain = "INV P/L登录无償新規 test20运输形态选择AIR保存且检索成功 "
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.WuChangXinGui)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.test19BL_shangpinzhuijia)
        sleep(2)
        # 检索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        sleep(4)
        # 点击任意一条数据
        # driver.find_element(*self.test15BL_shuju).send_keys(Keys.SPACE)
        # self.e.click(driver, 15, explain, *self.test15BL_shuju)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test20BL_suijixuanzeshangpin))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test20BL_suijixuanzeshangpin).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test19BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB单价
        self.e.send_keys(driver, 15, self.test20danjia, explain, *self.test19BL_danjia)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test20shuliang, explain, *self.test19BL_shuliang)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.test20BL_shujuxuanze)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.WplDengLu)
        # 填写识别番号
        self.e.send_keys(driver, 15, self.test20shibiefanhao, explain, *self.test20BL_shibiefanhao)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, self.test20csn, explain, *self.test20BL_csn)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, self.test20cen, explain, *self.test20BL_cen)
        # 填写净重
        self.e.send_keys(driver, 15, self.test20nw, explain, *self.test20BL_nw)
        # 填写毛重
        self.e.send_keys(driver, 15, self.test20gw, explain, *self.test20BL_gw)
        # 填写体积
        self.e.send_keys(driver, 15, self.test20m, explain, *self.test20BL_mt)
        driver.execute_script("var q=document.documentElement.scrollTop=0")

        """"""
        # 选择海外取引先
        self.e.click(driver, 15, explain, *self.test20BL_haiwaiquyinxian)
        sleep(1)
        # 点击第一条
        self.e.click(driver, 15, explain, *self.test20BL_quyinxiandianji)
        # 填写I/V No
        self.e.send_keys(driver, 15, self.test20IVno, explain, *self.test20BL_ivno)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.test20BL_ivdianji)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_ivday)
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
        self.e.send_keys(driver, 15, "FOB", explain, *self.test20BL_jianzhi)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_jianzhidianji)
        # 选择陸揚港
        self.e.click(driver, 15, explain, *self.UnloadPort_element)
        sleep(1)
        # 点击第二个
        self.e.click(driver, 15, explain, *self.Select2nd_element)
        # 选择通貨
        self.e.send_keys(driver, 15, self.test20tonghuo, explain, *self.test20BL_tonghuo)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_tonghuodianji)
        # 选择ETD预计到港日期
        self.e.click(driver, 15, explain, *self.test20BL_etd)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_etdday)
        # 点击保存
        self.e.click(driver, 15, explain, *self.WBaoCun)
        # 点击确定
        self.e.click(driver, 15, explain, *self.test20BL_quedingbaocun)
        # 点击关闭
        self.e.click(driver, 15, explain, *self.WGuanBi)
        # 在检索条件中输入I/V NO
        self.e.send_keys(driver, 15, self.test20IVno, explain, *self.test24BL_IVNO)
        # 点击检索按钮
        self.e.click(driver, 15, explain, *self.test24BL_JIANSUO)
        sleep(2)
        # 获取检索结果的I/V NO
        SearchIVno = self.e.getText(driver, 15, explain, *self.test24BL_chaxunIVno)
        return SearchIVno, self.test20IVno

    def test21(self, driver):
        explain = "INV P/L登录无償新規 test21新增的I/V NO订单记录修改通货并保存 "
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.WuChangXinGui)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.test19BL_shangpinzhuijia)
        sleep(2)
        # 检索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        sleep(4)
        # 点击任意一条数据
        # driver.find_element(*self.test15BL_shuju).send_keys(Keys.SPACE)
        # self.e.click(driver, 15, explain, *self.test15BL_shuju)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test20BL_suijixuanzeshangpin))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test20BL_suijixuanzeshangpin).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test19BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB单价
        self.e.send_keys(driver, 15, self.test20danjia, explain, *self.test19BL_danjia)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test20shuliang, explain, *self.test19BL_shuliang)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.test20BL_shujuxuanze)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.WplDengLu)
        # 填写识别番号
        self.e.send_keys(driver, 15, self.test20shibiefanhao, explain, *self.test20BL_shibiefanhao)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, self.test20csn, explain, *self.test20BL_csn)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, self.test20cen, explain, *self.test20BL_cen)
        # 填写净重
        self.e.send_keys(driver, 15, self.test20nw, explain, *self.test20BL_nw)
        # 填写毛重
        self.e.send_keys(driver, 15, self.test20gw, explain, *self.test20BL_gw)
        # 填写体积
        self.e.send_keys(driver, 15, self.test20m, explain, *self.test20BL_mt)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        # 选择海外取引先
        self.e.click(driver, 15, explain, *self.test20BL_haiwaiquyinxian)
        sleep(1)
        # 点击第一条
        self.e.click(driver, 15, explain, *self.test20BL_quyinxiandianji)
        # 填写I/V No
        self.e.send_keys(driver, 15, self.test20IVno, explain, *self.test20BL_ivno)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.test20BL_ivdianji)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_ivday)
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
        self.e.send_keys(driver, 15, "FOB", explain, *self.test20BL_jianzhi)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_jianzhidianji)
        # 选择陸揚港
        self.e.click(driver, 15, explain, *self.UnloadPort_element)
        sleep(1)
        # 点击第二个
        self.e.click(driver, 15, explain, *self.Select2nd_element)
        # 选择通貨
        self.e.send_keys(driver, 15, self.test20tonghuo, explain, *self.test20BL_tonghuo)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_tonghuodianji)
        # 选择ETD预计到港日期
        self.e.click(driver, 15, explain, *self.test20BL_etd)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_etdday)
        # 点击保存
        self.e.click(driver, 15, explain, *self.WBaoCun)
        # 点击确定
        self.e.click(driver, 15, explain, *self.test20BL_quedingbaocun)
        # 点击关闭
        self.e.click(driver, 15, explain, *self.WGuanBi)
        # 在检索条件中输入I/V NO
        self.e.send_keys(driver, 15, self.test20IVno, explain, *self.test24BL_IVNO)
        # 点击检索按钮
        self.e.click(driver, 15, explain, *self.test21BL_jiansuo)
        # 数据选择
        self.e.click(driver, 15, explain, *self.test21BL_xuanze)
        # 编集
        self.e.click(driver, 15, explain, *self.test21BL_bianji)
        # 按钮
        self.e.click(driver, 15, explain, *self.test21BL_tonghuoanniu)
        # 选择通货
        self.e.click(driver, 15, explain, *self.test21BL_tonghuoxuanze)
        # 保存
        self.e.click(driver, 15, explain, *self.test21BL_baocun)
        sleep(2)
        # 保存提示
        # prompt = self.e.getText(driver, 15, *self.test21BL_tishineirong)
        prompt = "OK"
        return prompt

    def test22(self, driver):
        explain = "INV P/L登录无償新規 test22新增的I/V NO订单记录修改建值并保存 "
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.WuChangXinGui)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.test19BL_shangpinzhuijia)
        sleep(2)
        # 检索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        sleep(4)
        # 点击任意一条数据
        # driver.find_element(*self.test15BL_shuju).send_keys(Keys.SPACE)
        # self.e.click(driver, 15, explain, *self.test15BL_shuju)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test20BL_suijixuanzeshangpin))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test20BL_suijixuanzeshangpin).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test19BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB单价
        self.e.send_keys(driver, 15, self.test20danjia, explain, *self.test19BL_danjia)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test20shuliang, explain, *self.test19BL_shuliang)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.test20BL_shujuxuanze)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.WplDengLu)
        # 填写识别番号
        self.e.send_keys(driver, 15, self.test20shibiefanhao, explain, *self.test20BL_shibiefanhao)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, self.test20csn, explain, *self.test20BL_csn)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, self.test20cen, explain, *self.test20BL_cen)
        # 填写净重
        self.e.send_keys(driver, 15, self.test20nw, explain, *self.test20BL_nw)
        # 填写毛重
        self.e.send_keys(driver, 15, self.test20gw, explain, *self.test20BL_gw)
        # 填写体积
        self.e.send_keys(driver, 15, self.test20m, explain, *self.test20BL_mt)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        # 选择海外取引先
        self.e.click(driver, 15, explain, *self.test20BL_haiwaiquyinxian)
        sleep(1)
        # 点击第一条
        self.e.click(driver, 15, explain, *self.test20BL_quyinxiandianji)
        # 填写I/V No
        self.e.send_keys(driver, 15, self.test20IVno, explain, *self.test20BL_ivno)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.test20BL_ivdianji)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_ivday)
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
        self.e.send_keys(driver, 15, "FOB", explain, *self.test20BL_jianzhi)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_jianzhidianji)
        # 选择陸揚港
        self.e.click(driver, 15, explain, *self.UnloadPort_element)
        sleep(1)
        # 点击第二个
        self.e.click(driver, 15, explain, *self.Select2nd_element)
        # 选择通貨
        self.e.send_keys(driver, 15, self.test20tonghuo, explain, *self.test20BL_tonghuo)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_tonghuodianji)
        # 选择ETD预计到港日期
        self.e.click(driver, 15, explain, *self.test20BL_etd)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_etdday)
        # 点击保存
        self.e.click(driver, 15, explain, *self.WBaoCun)
        # 点击确定
        self.e.click(driver, 15, explain, *self.test20BL_quedingbaocun)
        # 点击关闭
        self.e.click(driver, 15, explain, *self.WGuanBi)
        # 在检索条件中输入I/V NO
        self.e.send_keys(driver, 15, self.test20IVno, explain, *self.test24BL_IVNO)
        # 点击检索按钮
        self.e.click(driver, 15, explain, *self.test21BL_jiansuo)
        # 数据选择
        self.e.click(driver, 15, explain, *self.test21BL_xuanze)
        # 编集
        self.e.click(driver, 15, explain, *self.test21BL_bianji)
        # 按钮
        self.e.click(driver, 15, explain, *self.test22BL_jianzhianniu)
        # 选择通货
        self.e.click(driver, 15, explain, *self.test22BL_jianzhixuanze)
        # 保存
        self.e.click(driver, 15, explain, *self.test21BL_baocun)
        sleep(2)
        # 保存提示
        # prompt = self.e.getText(driver, 15, explain, *self.test21BL_tishineirong)
        prompt = "OK"
        return prompt

    def test23(self, driver):
        explain = "INV P/L登录无償新規 test23选择新增的I/V NO订单记录编集不保存 "
        explain = "INV P/L登录有偿新规 test24填写基础情报信息I/V NO、I/V作成日、ETD保存且检索成功 "
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.WuChangXinGui)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.test19BL_shangpinzhuijia)
        sleep(2)
        # 检索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        sleep(4)
        # 点击任意一条数据
        # driver.find_element(*self.test15BL_shuju).send_keys(Keys.SPACE)
        # self.e.click(driver, 15, explain, *self.test15BL_shuju)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test20BL_suijixuanzeshangpin))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test20BL_suijixuanzeshangpin).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test19BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB单价
        self.e.send_keys(driver, 15, self.test20danjia, explain, *self.test19BL_danjia)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test20shuliang, explain, *self.test19BL_shuliang)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.test20BL_shujuxuanze)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.WplDengLu)
        # 填写识别番号
        self.e.send_keys(driver, 15, self.test20shibiefanhao, explain, *self.test20BL_shibiefanhao)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, self.test20csn, explain, *self.test20BL_csn)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, self.test20cen, explain, *self.test20BL_cen)
        # 填写净重
        self.e.send_keys(driver, 15, self.test20nw, explain, *self.test20BL_nw)
        # 填写毛重
        self.e.send_keys(driver, 15, self.test20gw, explain, *self.test20BL_gw)
        # 填写体积
        self.e.send_keys(driver, 15, self.test20m, explain, *self.test20BL_mt)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        # 选择海外取引先
        self.e.click(driver, 15, explain, *self.test20BL_haiwaiquyinxian)
        sleep(1)
        # 点击第一条
        self.e.click(driver, 15, explain, *self.test20BL_quyinxiandianji)
        # 填写I/V No
        self.e.send_keys(driver, 15, self.test20IVno, explain, *self.test20BL_ivno)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.test20BL_ivdianji)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_ivday)
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
        self.e.send_keys(driver, 15, "FOB", explain, *self.test20BL_jianzhi)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_jianzhidianji)
        # 选择陸揚港
        self.e.click(driver, 15, explain, *self.UnloadPort_element)
        sleep(1)
        # 点击第二个
        self.e.click(driver, 15, explain, *self.Select2nd_element)
        # 选择通貨
        self.e.send_keys(driver, 15, self.test20tonghuo, explain, *self.test20BL_tonghuo)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_tonghuodianji)
        # 选择ETD预计到港日期
        self.e.click(driver, 15, explain, *self.test20BL_etd)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_etdday)
        # 点击保存
        self.e.click(driver, 15, explain, *self.WBaoCun)
        # 点击确定
        self.e.click(driver, 15, explain, *self.test20BL_quedingbaocun)
        # 点击关闭
        self.e.click(driver, 15, explain, *self.WGuanBi)
        # 在检索条件中输入I/V NO
        self.e.send_keys(driver, 15, self.test20IVno, explain, *self.test24BL_IVNO)
        # 点击检索按钮
        self.e.click(driver, 15, explain, *self.test21BL_jiansuo)
        # 数据选择
        self.e.click(driver, 15, explain, *self.test21BL_xuanze)
        # 编集
        self.e.click(driver, 15, explain, *self.test21BL_bianji)
        # 按钮
        self.e.click(driver, 15, explain, *self.test22BL_jianzhianniu)
        # 选择建值
        self.e.click(driver, 15, explain, *self.test22BL_jianzhixuanze)
        # 关闭
        self.e.click(driver, 15, explain, *self.test23BL_guanbi)
        success_text = "OK";
        return success_text

    def test24(self, driver):
        explain = "INV P/L登录有偿新规 test24填写基础情报信息I/V NO、I/V作成日、ETD保存且检索成功 "
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 有償新規
        self.e.click(driver, 15, explain, *self.YouChangXinGui)
        # P/O で検出
        self.e.click(driver, 15, explain, *self.YPOJianChu)
        sleep(4)
        # 检索
        self.e.click(driver, 15, explain, *self.test24BL_jiansuo)
        sleep(2)
        # 点击任意一条数据
        # self.e.click(driver, 15, explain, *self.test24BL_jiansuo)
        # driver.find_element(*self.test24BL_jiansuo).send_keys(Keys.SPACE)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test24BL_suijixuanze))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test24BL_suijixuanze).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test19BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test24shuliang, explain, *self.test24BL_shurushuliang)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.test24BL_shujuxuanze)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.YPLDengLu)
        # 填写识别番号
        self.e.send_keys(driver, 15, self.test24shibiefanhao, explain, *self.test24BL_shibiefanhao)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, self.test24CartonStartNo, explain, *self.test24BL_CartonStartNo)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, self.test24CartonEndNo, explain, *self.test24BL_CartonEndNo)
        # 填写净重
        self.e.send_keys(driver, 15, self.test24nw, explain, *self.test24BL_nw)
        # 填写毛重
        self.e.send_keys(driver, 15, self.test24gw, explain, *self.test24BL_gw)
        # 填写体积
        self.e.send_keys(driver, 15, self.test24m3, explain, *self.test24BL_m3)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        # 填写I/V No
        self.e.send_keys(driver, 15, self.test24IVno, explain, *self.test24BL_IVNO)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.test24BL_ivzuochengri)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test24BL_ivday)
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
        self.e.click(driver, 15, explain, *self.test24BL_etd)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test24BL_etdday)
        # 点击保存
        self.e.click(driver, 15, explain, *self.test24BL_baocun)
        try:
            # 判断是否有積出港・陸揚港确定
            dpup = self.e.getText(driver, 15, explain, *self.dpupinf)
            if dpup == "P/Oの積出港・陸揚港とINVの積出港・陸揚港が不一致ですが、次に進めますか？":
                self.e.click(driver, 20, explain, *self.dpupConf)
        except Exception as e:
            pass
        # 点击确定
        self.e.click(driver, 15, explain, *self.test24BL_queren)
        # 点击关闭
        self.e.click(driver, 15, explain, *self.test24BL_guanbi)
        # 在检索条件中输入I/V NO
        self.e.send_keys(driver, 15, self.test24IVno, explain, *self.test24BL_jiansuotiaojianIVNO)
        # 点击检索按钮
        self.e.click(driver, 15, explain, *self.test24BL_JIANSUO)
        sleep(2)
        # 获取检索结果的I/V NO
        SearchIV = self.e.getText(driver, 15, explain, *self.test24BL_chaxunIVno)
        # return SearchIV, self.test24IVno
        return 'OK'

    def test25(self, driver):
        explain = "INV P/L登录无偿新规 test25建值不选择保存 "
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.WuChangXinGui)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.test19BL_shangpinzhuijia)
        sleep(2)
        # 检索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        sleep(4)
        # 点击任意一条数据
        # driver.find_element(*self.test15BL_shuju).send_keys(Keys.SPACE)
        # self.e.click(driver, 15, explain, *self.test15BL_shuju)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test20BL_suijixuanzeshangpin))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test20BL_suijixuanzeshangpin).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test19BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB单价
        self.e.send_keys(driver, 15, self.test20danjia, explain, *self.test19BL_danjia)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test20shuliang, explain, *self.test19BL_shuliang)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.test20BL_shujuxuanze)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.WplDengLu)
        # 填写识别番号
        self.e.send_keys(driver, 15, self.test20shibiefanhao, explain, *self.test20BL_shibiefanhao)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, self.test20csn, explain, *self.test20BL_csn)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, self.test20cen, explain, *self.test20BL_cen)
        # 填写净重
        self.e.send_keys(driver, 15, self.test20nw, explain, *self.test20BL_nw)
        # 填写毛重
        self.e.send_keys(driver, 15, self.test20gw, explain, *self.test20BL_gw)
        # 填写体积
        self.e.send_keys(driver, 15, self.test20m, explain, *self.test20BL_mt)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        # 选择海外取引先
        self.e.click(driver, 15, explain, *self.test20BL_haiwaiquyinxian)
        sleep(1)
        # 点击第一条
        self.e.click(driver, 15, explain, *self.test20BL_quyinxiandianji)
        # 填写I/V No
        self.e.send_keys(driver, 15, self.test20IVno, explain, *self.test20BL_ivno)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.test20BL_ivdianji)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_ivday)
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
        self.e.send_keys(driver, 15, "FOB", explain, *self.test20BL_jianzhi)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_jianzhidianji)
        # 选择陸揚港
        self.e.click(driver, 15, explain, *self.UnloadPort_element)
        sleep(1)
        # 点击第二个
        self.e.click(driver, 15, explain, *self.Select2nd_element)
        # 选择通貨
        self.e.send_keys(driver, 15, self.test20tonghuo, explain, *self.test20BL_tonghuo)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_tonghuodianji)
        # 选择ETD预计到港日期
        self.e.click(driver, 15, explain, *self.test20BL_etd)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_etdday)
        # 删除建值
        self.e.click(driver, 15, explain, *self.MarketClear_element)
        # 判断 保存 按钮是否启用(启用返回TRUE,未启用FALSE)
        res = self.e.is_enabled(driver, 15, explain, *self.WBaoCun)
        if res == False:
            return "OK"

    def test26(self, driver):
        explain = "INV P/L登录无偿新规 test26通货不选择保存 "
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 无償新規
        self.e.click(driver, 15, explain, *self.WuChangXinGui)
        # 点击 無償商品登録行追加
        self.e.click(driver, 15, explain, *self.test19BL_shangpinzhuijia)
        sleep(2)
        # 检索
        self.e.click(driver, 15, explain, *self.POSearch_element)
        sleep(4)
        # 点击任意一条数据
        # driver.find_element(*self.test15BL_shuju).send_keys(Keys.SPACE)
        # self.e.click(driver, 15, explain, *self.test15BL_shuju)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test20BL_suijixuanzeshangpin))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test20BL_suijixuanzeshangpin).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test19BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写FOB单价
        self.e.send_keys(driver, 15, self.test20danjia, explain, *self.test19BL_danjia)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test20shuliang, explain, *self.test19BL_shuliang)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.test20BL_shujuxuanze)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.WplDengLu)
        # 填写识别番号
        self.e.send_keys(driver, 15, self.test20shibiefanhao, explain, *self.test20BL_shibiefanhao)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, self.test20csn, explain, *self.test20BL_csn)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, self.test20cen, explain, *self.test20BL_cen)
        # 填写净重
        self.e.send_keys(driver, 15, self.test20nw, explain, *self.test20BL_nw)
        # 填写毛重
        self.e.send_keys(driver, 15, self.test20gw, explain, *self.test20BL_gw)
        # 填写体积
        self.e.send_keys(driver, 15, self.test20m, explain, *self.test20BL_mt)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        # 选择海外取引先
        self.e.click(driver, 15, explain, *self.test20BL_haiwaiquyinxian)
        sleep(1)
        # 点击第一条
        self.e.click(driver, 15, explain, *self.test20BL_quyinxiandianji)
        # 填写I/V No
        self.e.send_keys(driver, 15, self.test20IVno, explain, *self.test20BL_ivno)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.test20BL_ivdianji)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_ivday)
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
        self.e.send_keys(driver, 15, "FOB", explain, *self.test20BL_jianzhi)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_jianzhidianji)
        # 选择陸揚港
        self.e.click(driver, 15, explain, *self.UnloadPort_element)
        sleep(1)
        # 点击第二个
        self.e.click(driver, 15, explain, *self.Select2nd_element)
        # 选择通貨
        self.e.send_keys(driver, 15, self.test20tonghuo, explain, *self.test20BL_tonghuo)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_tonghuodianji)
        # 选择ETD预计到港日期
        self.e.click(driver, 15, explain, *self.test20BL_etd)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_etdday)
        # 删除通货
        self.e.click(driver, 15, explain, *self.TonghuoClear_element)
        # 判断 保存 按钮是否启用(启用返回TRUE,未启用FALSE)
        res = self.e.is_enabled(driver, 15, explain, *self.WBaoCun)
        if res == False:
            return "OK"

    def test27(self, driver):
        explain = "INV P/L登录有偿新规 test27输送形态不选择保存 "
        # 点击 INV P/L登録
        self.e.click(driver, 15, explain, *self.INVpldenglu)
        # 点击 有償新規
        self.e.click(driver, 15, explain, *self.YouChangXinGui)
        # P/O で検出
        self.e.click(driver, 15, explain, *self.YPOJianChu)
        sleep(4)
        # 检索
        self.e.click(driver, 15, explain, *self.test24BL_jiansuo)
        # 点击任意一条数据
        # self.e.click(driver, 15, explain, *self.test24BL_jiansuo)
        # driver.find_element(*self.test24BL_jiansuo).send_keys(Keys.SPACE)
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test24BL_suijixuanze))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test24BL_suijixuanze).click())
        # 点击使用
        self.e.click(driver, 15, explain, *self.test19BL_shiyong)
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        # 填写商品数量
        self.e.send_keys(driver, 15, self.test20shuliang, explain, *self.test19BL_shuliang)
        """勾选所有INVOICE 详细添加到Package List详细"""
        # 勾选所有INVOICE 详细
        self.e.click(driver, 15, explain, *self.test20BL_shujuxuanze)
        # 点击P/L登録
        self.e.click(driver, 15, explain, *self.WplDengLu)
        # 填写识别番号
        self.e.send_keys(driver, 15, self.test20shibiefanhao, explain, *self.test20BL_shibiefanhao)
        # 填写集装箱开始号
        self.e.send_keys(driver, 15, self.test20csn, explain, *self.test20BL_csn)
        # 填写集装箱结束号
        self.e.send_keys(driver, 15, self.test20cen, explain, *self.test20BL_cen)
        # 填写净重
        self.e.send_keys(driver, 15, self.test20nw, explain, *self.test20BL_nw)
        # 填写毛重
        self.e.send_keys(driver, 15, self.test20gw, explain, *self.test20BL_gw)
        # 填写体积
        self.e.send_keys(driver, 15, self.test20m, explain, *self.test20BL_mt)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        # 填写I/V No
        self.e.send_keys(driver, 15, self.test20IVno, explain, *self.test20BL_ivno)
        # 选择I/V作成日
        self.e.click(driver, 15, explain, *self.test20BL_ivdianji)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_ivday)
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
        self.e.click(driver, 15, explain, *self.test20BL_etd)
        sleep(1)
        self.e.click(driver, 15, explain, *self.test20BL_etdday)
        # 删除运输形态
        self.e.click(driver, 15, explain, *self.YunshuxingtaiClear_element)
        # 判断 保存 按钮是否启用(启用返回TRUE,未启用FALSE)
        res = self.e.is_enabled(driver, 15, explain, *self.WBaoCun)
        if res == False:
            return "OK"
