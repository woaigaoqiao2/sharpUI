from time import sleep
from pageElement.confirmationOfAcceptance.ConfirmationLocation import Location
from common.Wait import Wait

class Logic(Location):
    
    
    def __init__(self):
        self.test2LuYangGang = "OSK:大阪港";
        self.NaRuChangSuo1 = "栃木物流センター（３２－００）";
        
        
    def test1(self,driver):
        #受入确认
        Wait(driver, 10, 2).elementwait(lambda the_driver: the_driver.find_element(*self.ShouRuQueRen))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ShouRuQueRen).click())
        #状态下拉框
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.ZhuangTai))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ZhuangTai).click())
        #状态选择
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.ZhuangTaiXuanZe))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ZhuangTaiXuanZe).click())
        #检索
        driver.find_element(*self.JianSuo).click()
        sleep(5)
        success_text = driver.find_element(*self.JieGuo).text
        return success_text
    
    
    def test2 (self,driver):
        #受入确认
        driver.find_element(*self.ShouRuQueRen).click()
        #陆扬港
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.LuYangGang))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.LuYangGang).send_keys(self.test2LuYangGang))
        # 检索
        driver.find_element(*self.JianSuo).click()
        sleep(5)
        success_text = driver.find_element(*self.JieGuo).text
        success_text = driver.find_element(*self.JieGuo).text
        return success_text
    
    
    def test3 (self,driver):
        #受入确认
        driver.find_element(*self.ShouRuQueRen).click();
        #纳入场所
        Wait(driver, 10, 2).elementwait(lambda the_driver: the_driver.find_element(*self.NaRuChangSuo))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.NaRuChangSuo).send_keys(self.NaRuChangSuo1))
        driver.find_element(*self.NaRuChangSuoXuanZe).click()
        # 检索
        driver.find_element(*self.JianSuo).click()
        sleep(1)
        Result3 = driver.find_element(*self.ChaXunJieGuo3).text
        return Result3,self.NaRuChangSuo1
    
    
    def test4 (self,driver):
        #受入确认
        driver.find_element(*self.ShouRuQueRen).click();
        #纳入指示日
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.JieShuRi))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.JieShuRi).click())
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.EndRiQi))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.EndRiQi).click())
        #检索
        driver.find_element(*self.JianSuo).click();
        sleep(5)
        success_text = driver.find_element(*self.JieGuo).text;
        return success_text
    
    def test5 (self,driver):
        #受入确认
        driver.find_element(*self.ShouRuQueRen).click();
        #纳入指示日
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.KaiShiRi))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.KaiShiRi).click())
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.StartRiQi))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.StartRiQi).click())
        #检索
        driver.find_element(*self.JianSuo).click();
        sleep(1)
        success_text = driver.find_element(*self.JieGuo).text;
        return success_text
    
    
    def test6 (self,driver):
        #受入确认
        driver.find_element(*self.ShouRuQueRen).click();
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
        #检索
        driver.find_element(*self.JianSuo).click();
        sleep(5)
        success_text = driver.find_element(*self.JieGuo).text;
        return success_text
    def test7 (self,driver):
        #受入确认
        driver.find_element(*self.ShouRuQueRen).click()
        #输送形态
        Wait(driver, 10, 2).elementwait(lambda the_driver: the_driver.find_element(*self.ShuSongXinTai))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ShuSongXinTai).click())
        Wait(driver, 10, 2).elementwait(lambda the_driver: the_driver.find_element(*self.ShuSongXinTaiXuanZe))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ShuSongXinTaiXuanZe).click())
        #检索
        driver.find_element(*self.JianSuo).click()
        sleep(5)
        success_text = driver.find_element(*self.JieGuo).text
        return success_text
    
    
    def test8 (self,driver):
        #受入确认
        Wait(driver, 10, 2).elementwait(lambda the_driver: the_driver.find_element(*self.ShouRuQueRen))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ShouRuQueRen).click())
        # 选择状态
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.ZhuangTaiXiaLaXuanZe))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ZhuangTaiXiaLaXuanZe).click())
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.XuanZeZhuangTai))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.XuanZeZhuangTai).click())
        #检索
        driver.find_element(*self.JianSuo).click();
        sleep(2)
        #数据选择
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.ShuJuXuanZe))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ShuJuXuanZe).click())
        #受入确认解除
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.QueRenJieChu))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.QueRenJieChu).click())
        #确认
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.QueRen))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.QueRen).click())
        sleep(5)
        success_text = 'OK';
        return success_text
    
    
    def test9 (self,driver):
        # 受入确认
        Wait(driver, 10, 2).elementwait(lambda the_driver: the_driver.find_element(*self.ShouRuQueRen))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ShouRuQueRen).click())
        sleep(3)
        #检索状态为納入指示済的数据
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.ZhuangTaiXiaLaXuanZe))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ZhuangTaiXiaLaXuanZe).click())
        Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.XuanZeZhuangTai))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.XuanZeZhuangTai).click())
        driver.find_element(*self.JianSuo).click()
        sleep(5)
        #数据选择
        Wait(driver, 10, 3).elementwait(lambda the_driver: the_driver.find_element(*self.ShuJuXuanZe1))
        Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.ShuJuXuanZe1).click())
        # #拖动滚动条到最顶部  10000为底部
        # scro="document.documentElement.scrollTop=0"
        # driver.execute_script(scro)
        # #パターン設定
        # Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.MoShiSheDing))
        # Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.MoShiSheDing).click())
        # sleep(5)
        # #点击配送パターン
        # Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.PeiSongMoShi))
        # Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.PeiSongMoShi).click())
        # sleep(5)
        # #配送模式
        # driver.find_element(*self.ShuRuMoShi).click()
        # driver.find_element(*self.XuanZeShuRuMoShi).click()
        # #模式保存
        # driver.find_element(*self.MoShiBaoCun).click()
        # #保存
        # Wait(driver, 10, 1).elementwait(lambda the_driver: the_driver.find_element(*self.BaoCun))
        # Wait(driver, 10).until(lambda the_driver: the_driver.find_element(*self.BaoCun).click())
        # sleep(5)
        # #确认
        # driver.find_element(*self.QueRenBaoCunJi).click()
        # sleep(2)




















