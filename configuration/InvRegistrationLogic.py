from time import sleep, time
from pageElement.confirmationOfAcceptance.InvRegistrationLocation import Location
from selenium.webdriver import ActionChains
from common.Wait import Wait

class Logic(Location):
    def __init__(self):

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
        self.test20IVno = 'IV'+str(time())[-5:];
        self.test20tonghuo = 'USD';
        self.test20yunshuxintai = 'AIR';
        self.test21ivno = 'IV'+str(time())[-5:];
        self.test24shuliang = '2';
        self.test24shibiefanhao = 'S002'
        self.test24CartonStartNo = '1';
        self.test24CartonEndNo = '1';
        # self.test24rushu = '2';
        self.test24nw = '1';
        self.test24gw = '1';
        self.test24m3 = '1';
        self.test24IVno = 'IV'+str(time())[-5:];

    def test15(self, driver):
        #INV P/L登录
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.INVpldenglu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.INVpldenglu).click())
        #无偿新规
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WuChangXinGui))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WuChangXinGui).click())
        #无偿商品登录追加
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shangpinzhuijia))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shangpinzhuijia).click())
        #选择第一条数据
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shuju))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shuju).click())
        #点击使用
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shiyong))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shiyong).click())
        #填写FOB单价
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_danjia))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_danjia).send_keys(self.test15danjia))
        #填写数量
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shuliang))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shuliang).send_keys(self.test15shuliang))
        #勾选数据
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_xuanze))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_xuanze).click())
        #P/L登录
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WplDengLu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WplDengLu).click())
        sucess_text = 'OK'
        return sucess_text

    def test16(self, driver):
        #INV 登录
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.INVpldenglu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.INVpldenglu).click())
        # 无偿新规
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WuChangXinGui))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WuChangXinGui).click())
        #无偿商品登录追加
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shangpinzhuijia))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shangpinzhuijia).click())
        #选择第一条数据
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shuju))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shuju).click())
        #点击使用
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shiyong))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shiyong).click())
        #填写FOB单价
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_danjia))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_danjia).send_keys(self.test15danjia))
        #填写数量
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shuliang))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shuliang).send_keys(self.test15shuliang))
        #勾选数据
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_xuanze))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_xuanze).click())
        #P/L登录
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WplDengLu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WplDengLu).click())
        #填写Carton Start NO
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test16BL_csn))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test16BL_csn).send_keys(self.test16csn))
        #填写Carton End NO
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test16BL_cen))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test16BL_cen).send_keys(self.test16cen))
        success_text = "OK";
        return success_text

    def test17(self, driver):
        # INV 登录
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.INVpldenglu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.INVpldenglu).click())
        # 无偿新规
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WuChangXinGui))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WuChangXinGui).click())
        # 无偿商品登录追加
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shangpinzhuijia))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shangpinzhuijia).click())
        # 选择第一条数据
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shuju))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shuju).click())
        # 点击使用
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shiyong))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shiyong).click())
        # 填写FOB单价
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_danjia))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_danjia).send_keys(self.test15danjia))
        # 填写数量
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shuliang))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shuliang).send_keys(self.test15shuliang))
        # 勾选数据
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_xuanze))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_xuanze).click())
        # P/L登录
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WplDengLu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WplDengLu).click())
        # 填写Carton Start NO
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test16BL_csn))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test16BL_csn).send_keys(self.test16csn))
        # 填写Carton End NO
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test16BL_cen))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test16BL_cen).send_keys(self.test16cen))
        #填写识别番号
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test17BL_shibiefanhao))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test17BL_shibiefanhao).send_keys(self.test17shibiefanhao))
        success_text = "OK"
        return success_text

    def test18(self, driver):
        # INV 登录
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.INVpldenglu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.INVpldenglu).click())
        # 无偿新规
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WuChangXinGui))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WuChangXinGui).click())
        # 无偿商品登录追加
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shangpinzhuijia))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shangpinzhuijia).click())
        # 选择第一条数据
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test18BL_xuanzeshuju))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test18BL_xuanzeshuju).click())
        # 点击使用
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shiyong))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shiyong).click())
        # 填写FOB单价
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_danjia))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_danjia).send_keys(self.test15danjia))
        # 填写数量
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_shuliang))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_shuliang).send_keys(self.test15shuliang))
        #INVOICE详细中选择数据削除
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test15BL_xuanze))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test15BL_xuanze).click())
        #削除
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test18BL_xiaochu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test18BL_xiaochu).click())
        #是否消除
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test18BL_shifouxiaoshu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test18BL_shifouxiaoshu).click())
        #确认消除
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test18BL_querenxiaochu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test18BL_querenxiaochu).click())
        Actual_result = driver.find_element(*self.test18BL_actual_result).text;
        return Actual_result

    def test19 (self,driver):
        # INV 登录
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.INVpldenglu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.INVpldenglu).click())
        # 无偿新规
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WuChangXinGui))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WuChangXinGui).click())
        # 点击无偿商品登录行追加
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_shangpinzhuijia))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_shangpinzhuijia).click())
        #选择商品信息表中的第一条数据
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_xuanzeshuju))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_xuanzeshuju).click())
        #点击使用
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_shiyong))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_shiyong).click())
        #INVOICE详细中填写FOB单价、数量
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_danjia))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_danjia).send_keys(self.test19danjia))
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_shuliang))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_shuliang).send_keys(self.test19shuliang))
        #点击P/L登录
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_shujuxuanze))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_shujuxuanze).click())
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WplDengLu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WplDengLu).click())
        #Package List详细中选择数据
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_PLxuanze))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_PLxuanze).click())
        #点击削除
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WplXiaoChu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WplXiaoChu).click())
        #是否消除
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test18BL_shifouxiaoshu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test18BL_shifouxiaoshu).click())
        #确认消除
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test18BL_querenxiaochu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test18BL_querenxiaochu).click())
        Actual_result = driver.find_element(*self.test18BL_actual_result).text;
        return Actual_result

    def test20(self, driver):
        # INV 登录
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.INVpldenglu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.INVpldenglu).click())
        # 无偿新规
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WuChangXinGui))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WuChangXinGui).click())
        # 点击无偿商品登录行追加
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_shangpinzhuijia))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_shangpinzhuijia).click())
        # 选择商品信息表中的第一条数据
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_xuanzeshuju))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_xuanzeshuju).click())
        # 点击使用
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_shiyong))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_shiyong).click())
        # INVOICE详细中填写FOB单价、数量
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_danjia))
        Wait(driver, 10).until(
            lambda the_driver: the_driver.find_element(*self.test19BL_danjia).send_keys(self.test19danjia))
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_shuliang))
        Wait(driver, 10).until(
            lambda the_driver: the_driver.find_element(*self.test19BL_shuliang).send_keys(self.test19shuliang))
        # 点击P/L登录
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_shujuxuanze))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_shujuxuanze).click())
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WplDengLu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WplDengLu).click())
        # Package List详细中选择数据
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test19BL_PLxuanze))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test19BL_PLxuanze).click())
        # 点击削除
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.WplXiaoChu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.WplXiaoChu).click())
        # 是否消除
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test18BL_shifouxiaoshu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test18BL_shifouxiaoshu).click())
        # 确认消除
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.test18BL_querenxiaochu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.test18BL_querenxiaochu).click())
        Actual_result = driver.find_element(*self.test18BL_actual_result).text;
        return Actual_result
    

     







    



