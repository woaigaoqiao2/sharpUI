from time import sleep
from pageElement.confirmationOfAcceptance.ConfirmationLocation import Location
from common.Wait import Wait
from util.ElementUtil import ElementUtil

class Logic(Location):


    def __init__(self):
        self.test2LuYangGang = "OSK:大阪港"
        self.NaRuChangSuo1 = "栃木物流センター（３２－００）"


    def test1(self,driver):
        eu = ElementUtil()
        #受入确认
        eu.click(driver,15, '受入确认', *self.ShouRuQueRen)
        #状态下拉框
        eu.click(driver, 15, '受入确认',  *self.ZhuangTai)
        #状态选择
        eu.click(driver, 15, '受入确认',  *self.ZhuangTaiXuanZe)
        #检索
        eu.click(driver, 15, '受入确认',  *self.JianSuo)
        sleep(3)
        success_text = driver.find_element(*self.JieGuo).text
        return success_text


    def test2(self, driver):
        eu = ElementUtil()
        #受入确认
        eu.click(driver, 15, '受入确认',  *self.ShouRuQueRen)
        #陆扬港
        eu.send_keys(driver, 15, self.test2LuYangGang, '受入确认',  *self.LuYangGang)
        eu.click(driver, 15, '受入确认',  *self.LuYangGang)
        # 检索
        eu.click(driver, 15, '受入确认',  *self.JianSuo)
        success_text = driver.find_element(*self.JieGuo).text
        return success_text


    def test3(self, driver):
        eu = ElementUtil()
        #受入确认
        eu.click(driver, 15, '受入确认',  *self.ShouRuQueRen)
        #纳入场所
        Wait(driver, 10, 2).elementwait(lambda the_driver: the_driver.find_element(*self.NaRuChangSuo))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.NaRuChangSuo).send_keys(self.NaRuChangSuo1))
        driver.find_element(*self.NaRuChangSuoXuanZe).click()
        # 检索
        driver.find_element(*self.JianSuo).click()


    def test4(self, driver):
        eu = ElementUtil()
        #受入确认
        eu.click(driver, 15, '受入确认',  *self.ShouRuQueRen)
        #纳入指示日
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.JieShuRi))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.JieShuRi).click())
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.EndRiQi))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.EndRiQi).click())
        #检索
        eu.click(driver, 15, '受入确认',  *self.JianSuo)
        sleep(6)
        success_text = driver.find_element(*self.JieGuo).text;
        return success_text

    def test5(self, driver):
        eu = ElementUtil()
        # 受入确认
        eu.click(driver, 15, '受入确认',  *self.ShouRuQueRen)
        #纳入指示日
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.KaiShiRi))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.KaiShiRi).click())
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.StartRiQi))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.StartRiQi).click())
        #检索
        eu.click(driver, 15, '受入确认',  *self.JianSuo)
        sleep(6)
        success_text = driver.find_element(*self.JieGuo).text;
        return success_text


    def test6 (self,driver):
        eu = ElementUtil()
        # 受入确认
        eu.click(driver, 15, '受入确认',  *self.ShouRuQueRen)
        #纳入指示结束日
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.OpenEndCalendar))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.OpenEndCalendar).click())
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.EndDate1))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.EndDate1).click())
        #纳入指示开始日
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.OpenStartCalendar))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.OpenStartCalendar).click())
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.StartDate1))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.StartDate1).click())
        # 检索
        eu.click(driver, 15, '受入确认',  *self.JianSuo)
        sleep(6)
        success_text = driver.find_element(*self.JieGuo).text

        return success_text

    def test7(self, driver):
        eu = ElementUtil()
        # 受入确认
        eu.click(driver, 15, '受入确认',  *self.ShouRuQueRen)
        #输送形态
        Wait(driver, 10, 2).elementwait(lambda the_driver: the_driver.find_element(*self.ShuSongXinTai))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ShuSongXinTai).click())
        Wait(driver, 10, 2).elementwait(lambda the_driver: the_driver.find_element(*self.ShuSongXinTaiXuanZe))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ShuSongXinTaiXuanZe).click())
        # 检索
        eu.click(driver, 15, '受入确认',  *self.JianSuo)
        sleep(6)
        success_text = driver.find_element(*self.JieGuo).text

        return success_text


    def test8(self, driver):
        eu = ElementUtil()
        # 受入确认
        eu.click(driver, 15, '受入确认',  *self.ShouRuQueRen)
        sleep(3)
        # 选择状态
        eu.click(driver, 15, '受入确认', *self.ZhuangTaiXiaLaXuanZe)
        eu.click(driver, 15, '受入确认', *self.XuanZeZhuangTai)
        # 检索
        eu.click(driver, 15, '受入确认',  *self.JianSuo)
        sleep(5)
        #数据选择
        eu.click(driver, 15, '受入确认', *self.ShuJuXuanZe)
        #受入确认解除
        eu.click(driver, 15, '受入确认', *self.QueRenJieChu)
        sleep(3)
        #确认
        eu.click(driver, 15, '受入确认', *self.QueRen)
        sleep(3)
        success_text = 'OK'

        return success_text


    def test9(self, driver):
        eu = ElementUtil()
        # 受入确认
        eu.click(driver,15 ,'受入确认', *self.ShouRuQueRen)
        sleep(3)
        # 状态下拉框
        eu.click(driver, 15, '受入确认', *self.ZhuangTai)
        # 状态选择
        eu.click(driver, 15, '受入确认', *self.ZhuangTaiXuanZe)
        #检索
        eu.click(driver, 15, '受入确认',  *self.JianSuo)
        #数据选择

        Wait(driver, 10, 3).elementwait(lambda the_driver: the_driver.find_element(*self.ShuJuXuanZe1))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ShuJuXuanZe1).click())
        #拖动滚动条到最顶部  10000为底部
        scro="document.documentElement.scrollTop=0"
        driver.execute_script(scro)
        #パターン設定
        eu.click(driver, 15, '受入确认', *self.MoShiSheDing)
        sleep(3)
        #点击配送パターン
        eu.click(driver, 15, '受入确认', *self.PeiSongMoShi)
        sleep(3)
        #配送模式
        eu.click(driver, 15, '受入确认', *self.ShuRuMoShi)
        eu.click(driver, 15, '受入确认', *self.XuanZeShuRuMoShi)
        #模式保存
        eu.click(driver, 15, '受入确认', *self.MoShiBaoCun)
        sleep(3)
        #保存
        eu.click(driver,15, '受入确认', *self.BaoCun)
        sleep(6)
        #确认
        eu.click(driver,15,'受入确认', *self.QueRenBaoCunJi)




















