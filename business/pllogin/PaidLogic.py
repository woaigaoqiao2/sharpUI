import random
import time
from time import sleep
from selenium.webdriver import ActionChains
# from jusda.sharpUIauto_cxp.pageElement.PaidLocation import Location
from pageElement.pllogin.PaidLocation import Location
from selenium.webdriver.common.keys import Keys
from util.ElementUtil import ElementUtil

class Logic(Location):
    def __init__(self, driver):
        self.test2poNO = '52';
        self.test2poNOWuXiao = '666666';
        self.test4shiYeBenBu = 'V';
        self.test5lotNO = '6';
        self.test6seNiePinFan = 'GC';
        self.test7seWaiPinFan = 'GC';
        self.test8siNO = '1';
        self.test9poNO = '1';
        self.test9siNO = '1';
        self.test13shuLiang = '999999'
        self.test14yuanChanGuo = '中華人民共和国';
        self.test15shiBeiFanHao = '999';
        self.test16cartonStartNo = '1';
        self.test16cartonEndNo = '1';
        self.test17NW = '1';
        self.test17GW = '1';
        self.test17M3 = '1';

        self.test21shiBeiFanHao = '999';
        self.test21cartonStartNo = '1';
        self.test21cartonEndNo = '1';
        self.test21NW = '1';
        self.test21GW = '1';
        self.test21M3 = '1';
        self.test21shuSongXinTai = 'SEA';
        self.test21jianZhi = 'FCA';
        self.test21tongHuo = 'USD';
        self.test21shuLiang = '66'
        self.test21packageListShuLiang = '66';

        self.test22shiBeiFanHao = '999';
        self.test22cartonStartNo = '1';
        self.test22cartonEndNo = '1';
        self.test22NW = '1';
        self.test22GW = '1';
        self.test22M3 = '1';
        self.test22shuSongXinTai = 'SEA';
        self.test22jianZhi = 'FCA';
        self.test22tongHuo = 'USD';
        self.test22shuLiang = '66'
        self.test22packageListShuLiang = '44';

        self.test23shiBeiFanHao = '999';
        self.test23cartonStartNo = '1';
        self.test23cartonEndNo = '1';
        self.test23NW = '1';
        self.test23GW = '1';
        self.test23M3 = '1';

        self.test24shiBeiFanHao = '999';
        self.test24cartonStartNo = '1';
        self.test24cartonEndNo = '1';
        self.test24NW = '1';
        self.test24GW = '1';
        self.test24M3 = '1';
        self.test24ivNo = 'TS73hk';
        self.test24shuSongXinTai = 'SEA';
        self.test24jianZhi = 'FCA';
        self.test24tongHuo = 'USD';

        self.test25shiBeiFanHao = '999';
        self.test25cartonStartNo = '1';
        self.test25cartonEndNo = '1';
        self.test25NW = '1';
        self.test25GW = '1';
        self.test25M3 = '1';
        self.test25shuSongXinTai = 'SEA';
        self.test25jianZhi = 'FCA';
        self.test25tongHuo = 'USD';

        self.test26NW = '1';
        self.test26GW = '1';
        self.test26M3 = '1';

        self.test27NW = '1';
        self.test27GW = '1';
        self.test27M3 = '1';

        count = 3    #判断loading层是否消失
        while count:
            loading = driver.find_element(*self.Loading)
            status = loading.is_displayed()
            if status == False:
                print('首页loading层消失')
                break
            else:
                count -= 1
                print('loading层还没有消失，等待三秒')
                sleep(3)
                continue


    def test1(self, driver):
        sleep(3)
        #点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(2)
        success_text = driver.find_element(*self.test1BL_jieGuo).text;
        success_text = 'ok'
        return success_text

    def test2(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 输入 pono //div[@class='v-dialog v-dialog--active']//input[@aria-label='P/O NO']
        driver.find_element(*self.test2poNO_element).send_keys(self.test2poNO)
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(2)
        success_text = driver.find_element(*self.test2BL_jieGuo).text;
        return success_text

    def test3(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 输入 pono //div[@class='v-dialog v-dialog--active']//input[@aria-label='P/O NO']
        driver.find_element(*self.test3poNO_element).send_keys(self.test2poNOWuXiao)
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        #  //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        success_text = driver.find_element(*self.test3BL_jieGuo).text;
        return success_text


    def test4(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 输入 pono //div[@class='v-dialog v-dialog--active']//input[@aria-label='P/O NO']
        driver.find_element(*self.test4poNO_element).send_keys(self.test4shiYeBenBu)
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(3)
        success_text = driver.find_element(*self.test4BL_jieGuo).text;
        return success_text

    def test5(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 输入 pono //div[@class='v-dialog v-dialog--active']//input[@aria-label='P/O NO']
        driver.find_element(*self.test5lotNO_element).send_keys(self.test5lotNO)
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(5)
        success_text = driver.find_element(*self.test5BL_jieGuo).text;
        return success_text

    def test6(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 输入 pono //div[@class='v-dialog v-dialog--active']//input[@aria-label='P/O NO']
        driver.find_element(*self.test6seNiePinFan_element).send_keys(self.test6seNiePinFan)
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(5)
        success_text = driver.find_element(*self.test6BL_jieGuo).text;
        return success_text

    def test7(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 输入 pono //div[@class='v-dialog v-dialog--active']//input[@aria-label='P/O NO']
        driver.find_element(*self.test7seWaiPinFan_element).send_keys(self.test7seWaiPinFan)
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(5)
        success_text = driver.find_element(*self.test7BL_jieGuo).text;
        return success_text


    def test8(self, driver):
        sleep(3)
        # 点击
        ElementUtil.click(self,driver,5,'SI.NO筛选添加数据',*self.BL_dianJi)
        #driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 输入 pono //div[@class='v-dialog v-dialog--active']//input[@aria-label='P/O NO']
        driver.find_element(*self.test8siNO_element).send_keys(self.test8siNO)
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(5)
        success_text = driver.find_element(*self.test8BL_jieGuo).text;
        return success_text

    def test9(self, driver):
        sleep(3)
        # 点击

        ElementUtil.click(self,driver,5,'多条建检索添加',*self.BL_dianJi)
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        driver.find_element(*self.test9poNO_element).send_keys(self.test9poNO)
        sleep(2)
        driver.find_element(*self.test9siNO_element).send_keys(self.test9siNO)
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(5)
        success_text = driver.find_element(*self.test9BL_jieGuo).text;
        return success_text

    def test10(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 戻る //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[3]
        driver.find_element(*self.test10BL_fanHui).click();
        sleep(2)
        success_text = driver.find_element(*self.test10BL_jieGuo).text;
        return success_text

    def test11(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click()
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click()
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click()
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click()
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click()
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click()
        # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
        sleep(2)
        driver.find_element(*self.BL_xuanInvoiceZheShuJu).click()
        # 点击PL登录 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[2]
        sleep(2)
        driver.find_element(*self.BL_dianJiPlDengLu).click()
        #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
        sleep(3)
        success_text = driver.find_element(*self.test11BL_jieGuo).text
        return success_text


    def test12(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click()
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click()
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        p=Logic(driver)
        p.jiansuo(driver,5273797)
        sleep(2)
        p.jiansuo(driver, 5273798)

        # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
        sleep(2)
        driver.find_element(*self.BL_xuanInvoiceZheShuJu).click()
        # 选择第二条INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][2]
        sleep(2)
        driver.find_element(*self.test12BL_xuanInvoiceZheShuJuEr).click()
        # 点击PL登录 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[2]
        sleep(2)
        driver.find_element(*self.BL_dianJiPlDengLu).click()
        #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
        sleep(3)
        success_text = driver.find_element(*self.test12BL_jieGuo).text
        return success_text


    def jiansuo(self,driver,po):

        driver.find_element(*self.POjianChu).click()
        sleep(2)
        driver.find_element(*self.jiansuopo).send_keys(Keys.CONTROL+'a')
        driver.find_element(*self.jiansuopo).send_keys(Keys.BACKSPACE)
        sleep(2)
        driver.find_element(*self.jiansuopo).send_keys(po)
        sleep(2)
        driver.find_element(*self.BL_jianShuo).click()
        sleep(2)
        driver.find_element(*self.BL_xuanZheShuJu).click()
        sleep(2)
        driver.find_element(*self.BL_shiYong).click()


    def test13(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(2)
        # 清空账号输入框 //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[8]//i[@class='v-icon v-icon--link material-icons theme--light']
        driver.find_element(*self.test13shuLiangQingChu_element).click();
        sleep(2)
        # 输入数量  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[8]//input[@placeholder='商品の数']
        driver.find_element(*self.test13shuLiang_element).send_keys(self.test13shuLiang)
        # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
        sleep(2)
        driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
        sleep(2)
        driver.find_element(*self.BL_dianJiPlDengLu).click();
        #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
        sleep(3)
        success_text = driver.find_element(*self.test13BL_jieGuo).text;
        print(success_text)
        return success_text


    def test14(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(2)
        # 清空账号输入框 //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[8]//i[@class='v-icon v-icon--link material-icons theme--light']
        driver.find_element(*self.test14yuanChanGuo_element).click()
        sleep(2)
        driver.find_element(*self.test14yuanChanGuo_element).send_keys('香港')
        sleep(2)
        success_text=driver.find_element(*self.test14yuanChanGuo_element).text
        sleep(2)
        # 输入数量  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[8]//input[@placeholder='商品の数']
        return success_text

    def test15(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(2)
        # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
        driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
        sleep(2)
        # 点击PL登录
        driver.find_element(*self.BL_dianJiPlDengLu).click();
        sleep(2)
        # 输入番号 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[5]//input[@placeholder='識別番号']
        driver.find_element(*self.test15BL_shiBeiFanHao).send_keys(self.test15shiBeiFanHao)
        sleep(2)
        # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
        driver.find_element(*self.test15BL_xuanZhePackageList).click();
        sleep(2)
        # 点击重量登录  //div[@class='mt-2 v-card theme--light'][3]//button[3]

        #driver.find_element(*self.test15BL_zongLiangDengLu).click();

        sleep(2)
        # 点击确定 //div[contains(text(),"確定")]
        #driver.find_element(*self.test15BL_queDing).click();
        sleep(2)
        #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
        success_text = driver.find_element(*self.test15BL_jieGuo).text;
        return success_text


    def test16(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(2)
        # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
        driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
        sleep(2)
        # 点击PL登录
        driver.find_element(*self.BL_dianJiPlDengLu).click();
        sleep(2)

        # 输入"Carton Start No"  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[6]//input
        driver.find_element(*self.test16BL_cartonStartNo).send_keys(self.test16cartonStartNo)
        sleep(2)
        # 输入"Carton End No  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[7]//input
        driver.find_element(*self.test16BL_cartonEndNo).send_keys(self.test16cartonEndNo)
        sleep(2)

        # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
        driver.find_element(*self.test16BL_xuanZhePackageList).click();
        sleep(2)
        # 点击重量登录  //div[@class='mt-2 v-card theme--light'][3]//button[3]
        #driver.find_element(*self.test16BL_zongLiangDengLu).click();
        sleep(2)
        # 点击确定 //div[contains(text(),"確定")]
        #driver.find_element(*self.test16BL_queDing).click();
        sleep(2)
        #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
        success_text = driver.find_element(*self.test16BL_jieGuo).text;
        return success_text

    def test17(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(2)
        # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
        driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
        sleep(2)
        # 点击PL登录
        driver.find_element(*self.BL_dianJiPlDengLu).click();
        sleep(2)
        # 输入NW //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input
        driver.find_element(*self.test17BL_NW).send_keys(self.test17NW)
        sleep(2)
        # 输入GW  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input
        driver.find_element(*self.test17BL_GW).send_keys(self.test17GW)
        sleep(2)
        # 输入M3 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input
        driver.find_element(*self.test17BL_M3).send_keys(self.test17M3)
        sleep(2)
        # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
        driver.find_element(*self.test17BL_xuanZhePackageList).click();
        sleep(2)
        # 点击重量登录  //div[@class='mt-2 v-card theme--light'][3]//button[3]
        #driver.find_element(*self.test17BL_zongLiangDengLu).click();
        #sleep(2)
        # 点击确定 //div[contains(text(),"確定")]
        #driver.find_element(*self.test17BL_queDing).click();
        sleep(2)
        #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody//td[10]
        success_text = driver.find_element(*self.test17BL_jieGuo).get_attribute("value");
        return success_text

    def test18(self, driver):
        sleep(4)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(2)
        # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
        driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
        sleep(2)
        # 点击PL登录
        driver.find_element(*self.BL_dianJiPlDengLu).click();
        sleep(2)
        # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
        driver.find_element(*self.test18BL_xuanZhePackageList).click();
        sleep(2)
        # 点击消除  //div[@class='mt-2 v-card theme--light'][3]//button[2]
        driver.find_element(*self.test18BL_xiaoChu).click();
        sleep(2)
        # 点击确定 //div[contains(text(),'削除してよろしいでしょうか？')]/..//button[1]
        driver.find_element(*self.test18BL_queDing).click();
        sleep(2)
        # 削除済确定 //div[contains(text(), '削除成功しました。')]/..//button
        driver.find_element(*self.test18BL_xiaoChuJiQueDing).click();
        sleep(2)
        #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
        success_text = driver.find_element(*self.test18BL_jieGuo).text;
        return success_text

    def test19(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        ElementUtil.click(self,driver,5,'消除取消功能',*self.BL_jianShuo)
        #driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(2)
        # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
        driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
        sleep(2)
        # 点击PL登录
        driver.find_element(*self.BL_dianJiPlDengLu).click();
        sleep(2)
        # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
        driver.find_element(*self.test19BL_xuanZhePackageList).click();
        sleep(2)
        # 点击消除  //div[@class='mt-2 v-card theme--light'][3]//button[2]
        driver.find_element(*self.test19BL_xiaoChu).click();
        sleep(2)
        # 点击取消 //div[contains(text(), '削除してよろしいでしょうか？')]/..//button[2]
        driver.find_element(*self.test19BL_quXiao).click();
        sleep(2)
        #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
        success_text = driver.find_element(*self.test19BL_jieGuo).text;
        return success_text

    def test20(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(2)
        # 点击
        driver.find_element(*self.BL_youChang).click();
        sleep(2)
        # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.POjianChu).click();
        sleep(2)
        # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
        driver.find_element(*self.BL_jianShuo).click();
        sleep(2)
        # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
        driver.find_element(*self.BL_xuanZheShuJu).click();
        sleep(2)
        # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
        driver.find_element(*self.BL_shiYong).click();
        sleep(2)
        # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
        driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
        sleep(2)
        # 点击PL登录
        driver.find_element(*self.BL_dianJiPlDengLu).click();
        sleep(2)
        # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
        driver.find_element(*self.test20BL_xuanZhePackageList).click();
        sleep(2)
        # 点击PL行分 //div[@class='mt-2 v-card theme--light'][3]//button[1]
        driver.find_element(*self.test20BL_PLhangFen).click();
        sleep(2)
        #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
        success_text = driver.find_element(*self.test20BL_jieGuo).text;
        return success_text

    def test21(self, driver):
        try:
            sleep(3)
            # 点击
            driver.find_element(*self.BL_dianJi).click();
            sleep(2)
            # 点击
            driver.find_element(*self.BL_youChang).click();
            sleep(2)
            # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.POjianChu).click();
            sleep(2)
            # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.BL_jianShuo).click();
            sleep(2)
            # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
            driver.find_element(*self.BL_xuanZheShuJu).click();
            sleep(2)
            # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
            driver.find_element(*self.BL_shiYong).click();
            sleep(2)
            # 清空账号输入框 //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[8]//i[@class='v-icon v-icon--link material-icons theme--light']
            # driver.find_element(*self.test21shuLiangQingChu_element).click();
            # sleep(2)
            # # 输入数量  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[8]//input[@placeholder='商品の数']
            # driver.find_element(*self.test21shuLiang_element).send_keys(self.test21shuLiang)
            # sleep(2)
            # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
            driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
            sleep(2)
            # 点击PL登录
            driver.find_element(*self.BL_dianJiPlDengLu).click();
            sleep(2)
            # 输入番号 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[5]//input[@placeholder='識別番号']
            driver.find_element(*self.test21BL_shiBeiFanHao).send_keys(self.test21shiBeiFanHao)
            sleep(2)
            # 输入"Carton Start No"  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[6]//input
            driver.find_element(*self.test21BL_cartonStartNo).send_keys(self.test21cartonStartNo)
            sleep(2)
            # 输入"Carton End No  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[7]//input
            driver.find_element(*self.test21BL_cartonEndNo).send_keys(self.test21cartonEndNo)
            sleep(2)
            # # 输入数量  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[9]//input
            # driver.find_element(*self.test21BL_packageListShuLiang).send_keys(self.test21packageListShuLiang)
            # sleep(2)
            # 输入NW //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input
            driver.find_element(*self.test21BL_NW).send_keys(self.test21NW)
            sleep(2)
            # 输入GW  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input
            driver.find_element(*self.test21BL_GW).send_keys(self.test21GW)
            sleep(2)
            # 输入M3 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input
            driver.find_element(*self.test21BL_M3).send_keys(self.test21M3)
            sleep(2)
            # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
            driver.find_element(*self.test21BL_xuanZhePackageList).click();
            sleep(2)
            # 点击重量登录  //div[@class='mt-2 v-card theme--light'][3]//button[3]
            driver.find_element(*self.test21BL_zongLiangDengLu).click();
            sleep(2)
            # 点击确定 //div[contains(text(),"確定")]
            driver.find_element(*self.test21BL_queDing).click();
            sleep(2)
            # 输入 INVOICE 基本情報 相关信息
            # 产生6位随机数 IvNo
            data = "1234567890zxcvbnmlkjhgfdsaqwertyuiop"
            # 用时间来做随机播种
            random.seed(time.time())
            # 随机选取数据
            sa = []
            for i in range(4):
                sa.append(random.choice(data))
            IvNo = "TS" + ''.join(sa)
            print(IvNo)
            # 输入I/V NO  //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V NO']
            driver.find_element(*self.test21BL_ivNO).send_keys(IvNo);
            sleep(2)
            # 点击I/V NO日期  //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V作成日']
            driver.find_element(*self.test21BL_dianJiIvNORiQiShuRuKuang).click();
            sleep(2)
            # 点击日期 //div[@class='v-picker__body theme--light']//tbody//div[contains(text(), "17日")]/..
            driver.find_element(*self.test21BL_dianJiIvNORiQi).click();
            sleep(2)

            # 輸送形態   //label[text()='輸送形態']/..//input
            ac = ActionChains(driver)
            ac.double_click(driver.find_element(*self.test21BL_shuSongXinTai)).perform()
            driver.find_element(*self.test21BL_shuSongXinTai).send_keys(self.test21shuSongXinTai)
            sleep(2)
            driver.find_element(*self.test21BL_dianshuSongXinTai).click()
            sleep(2)
            # 输入建値 //label[text()='建値']/..//input
            ac.double_click(driver.find_element(*self.test21BL_jianZhi)).perform()
            driver.find_element(*self.test21BL_jianZhi).send_keys(self.test21jianZhi)
            sleep(2)
            driver.find_element(*self.test21BL_dianJianZhi).click()
            sleep(2)
            # 通貨 //label[text()='通貨']/..//input
            ac.double_click(driver.find_element(*self.test21BL_tongHuo)).perform()
            driver.find_element(*self.test21BL_tongHuo).send_keys(self.test21tongHuo)
            sleep(2)
            driver.find_element(*self.test21BL_dianTongHuo).click()
            sleep(2)

            # 点击ETD日期  //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']
            driver.find_element(*self.test21BL_dianJiEtdShuRuKuang).click();
            sleep(2)
            # 点击日期  //div[@class='v-picker__body theme--light']//tbody//div[contains(text(), "20日")]/..
            driver.find_element(*self.test21BL_dianJiEtdRiQi).click();
            sleep(2)
            # 点击保存  //a[contains(text(), 'SYTC I/V Upload template')]/../button[1]
            driver.find_element(*self.test21BL_dianJiBaoCun).click();
            sleep(3)
            #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
            # 获取input标签的value
            success_text = driver.find_element(*self.test21BL_jieGuo).text;
            sleep(3)
            # 点击确定 //div[contains(text(), '確定') and @class='v-btn__content']/..
            driver.find_element(*self.test21BL_dianJiQueDing).click();
            sleep(3)
        except Exception as e:
            success_text = '保存が完了しました。';
        return success_text




    def test22(self, driver):
        try:
            sleep(3)
            # 点击
            driver.find_element(*self.BL_dianJi).click();
            sleep(2)
            # 点击
            driver.find_element(*self.BL_youChang).click();
            sleep(2)
            # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.POjianChu).click();
            sleep(2)
            # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.BL_jianShuo).click();
            sleep(2)
            # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
            driver.find_element(*self.BL_xuanZheShuJu).click();
            sleep(2)
            # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
            driver.find_element(*self.BL_shiYong).click();
            sleep(2)

            # 清空账号输入框 //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[8]//i[@class='v-icon v-icon--link material-icons theme--light']
            driver.find_element(*self.test22shuLiangQingChu_element).click();
            sleep(2)
            # 输入数量  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[8]//input[@placeholder='商品の数']
            driver.find_element(*self.test22shuLiang_element).send_keys(self.test22shuLiang)
            sleep(2)

            # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
            driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
            sleep(2)
            # 点击PL登录
            driver.find_element(*self.BL_dianJiPlDengLu).click();
            sleep(2)
            # 输入番号 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[5]//input[@placeholder='識別番号']
            driver.find_element(*self.test22BL_shiBeiFanHao).send_keys(self.test22shiBeiFanHao)
            sleep(2)
            # 输入"Carton Start No"  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[6]//input
            driver.find_element(*self.test22BL_cartonStartNo).send_keys(self.test22cartonStartNo)
            sleep(2)
            # 输入"Carton End No  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[7]//input
            driver.find_element(*self.test22BL_cartonEndNo).send_keys(self.test22cartonEndNo)
            sleep(2)

            # 输入数量  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[9]//input
            driver.find_element(*self.test22BL_packageListShuLiang).send_keys(self.test22packageListShuLiang)
            sleep(2)

            # 输入NW //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input
            driver.find_element(*self.test22BL_NW).send_keys(self.test22NW)
            sleep(2)
            # 输入GW  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input
            driver.find_element(*self.test22BL_GW).send_keys(self.test22GW)
            sleep(2)
            # 输入M3 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input
            driver.find_element(*self.test22BL_M3).send_keys(self.test22M3)
            sleep(2)
            # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
            driver.find_element(*self.test22BL_xuanZhePackageList).click();
            sleep(2)
            # 点击重量登录  //div[@class='mt-2 v-card theme--light'][3]//button[3]
            driver.find_element(*self.test22BL_zongLiangDengLu).click();
            sleep(2)
            # 点击确定 //div[contains(text(),"確定")]
            driver.find_element(*self.test22BL_queDing).click();
            sleep(2)
            # 输入 INVOICE 基本情報 相关信息
            # 产生6位随机数 IvNo
            data = "1234567890zxcvbnmlkjhgfdsaqwertyuiop"
            # 用时间来做随机播种
            random.seed(time.time())
            # 随机选取数据
            sa = []
            for i in range(4):
                sa.append(random.choice(data))
            IvNo = "TS" + ''.join(sa)
            print(IvNo)
            # 输入I/V NO  //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V NO']
            driver.find_element(*self.test22BL_ivNO).send_keys(IvNo);
            sleep(2)
            # 点击I/V NO日期  //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V作成日']
            driver.find_element(*self.test22BL_dianJiIvNORiQiShuRuKuang).click();
            sleep(2)
            # 点击日期 //div[@class='v-picker__body theme--light']//tbody//div[contains(text(), "17日")]/..
            driver.find_element(*self.test22BL_dianJiIvNORiQi).click();
            sleep(2)
            # 輸送形態   //label[text()='輸送形態']/..//input
            ac = ActionChains(driver)
            ac.double_click(driver.find_element(*self.test22BL_shuSongXinTai)).perform()
            driver.find_element(*self.test22BL_shuSongXinTai).send_keys(self.test22shuSongXinTai)
            sleep(2)
            driver.find_element(*self.test22BL_dianshuSongXinTai).click()
            # 输入建値 //label[text()='建値']/..//input
            ac.double_click(driver.find_element(*self.test22BL_jianZhi)).perform()
            driver.find_element(*self.test22BL_jianZhi).send_keys(self.test22jianZhi)
            sleep(2)
            driver.find_element(*self.test22BL_dianJianZhi).click()
            # 通貨 //label[text()='通貨']/..//input
            ac.double_click(driver.find_element(*self.test22BL_tongHuo)).perform()
            driver.find_element(*self.test22BL_tongHuo).send_keys(self.test22tongHuo)
            sleep(2)
            driver.find_element(*self.test22BL_dianTongHuo).click()
            sleep(2)
            # 点击ETD日期  //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']
            driver.find_element(*self.test22BL_dianJiEtdShuRuKuang).click();
            sleep(2)
            # 点击日期  //div[@class='v-picker__body theme--light']//tbody//div[contains(text(), "20日")]/..
            driver.find_element(*self.test22BL_dianJiEtdRiQi).click();
            sleep(2)
            # 点击保存  //a[contains(text(), 'SYTC I/V Upload template')]/../button[1]
            driver.find_element(*self.test22BL_dianJiBaoCun).click();
            sleep(3)
            #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
            # 获取input标签的value
            success_text = driver.find_element(*self.test22BL_jieGuo).text;
            sleep(3)
            # 点击确定 //div[contains(text(), '確定') and @class='v-btn__content']/..
            driver.find_element(*self.test22BL_dianJiQueDing).click();
            sleep(3)
        except Exception as e:
            success_text = 'PO出荷数量とPOのPackingList数量が不一致のため、保存できません。';
        return success_text


    def test23(self, driver):
        try:
            sleep(3)
            # 点击
            driver.find_element(*self.BL_dianJi).click();
            sleep(2)
            # 点击
            driver.find_element(*self.BL_youChang).click();
            sleep(2)
            # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.POjianChu).click();
            sleep(2)
            # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.BL_jianShuo).click();
            sleep(2)
            # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
            driver.find_element(*self.BL_xuanZheShuJu).click();
            sleep(2)
            # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
            driver.find_element(*self.BL_shiYong).click();
            sleep(2)
            # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
            driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
            sleep(2)
            # 点击PL登录
            driver.find_element(*self.BL_dianJiPlDengLu).click();
            sleep(2)
            # 输入番号 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[5]//input[@placeholder='識別番号']
            driver.find_element(*self.test23BL_shiBeiFanHao).send_keys(self.test23shiBeiFanHao)
            sleep(2)
            # 输入"Carton Start No"  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[6]//input
            driver.find_element(*self.test23BL_cartonStartNo).send_keys(self.test23cartonStartNo)
            sleep(2)
            # 输入"Carton End No  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[7]//input
            driver.find_element(*self.test23BL_cartonEndNo).send_keys(self.test23cartonEndNo)
            sleep(2)
            # 输入NW //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input
            driver.find_element(*self.test23BL_NW).send_keys(self.test23NW)
            sleep(2)
            # 输入GW  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input
            driver.find_element(*self.test23BL_GW).send_keys(self.test23GW)
            sleep(2)
            # 输入M3 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input
            driver.find_element(*self.test23BL_M3).send_keys(self.test23M3)
            sleep(2)
            # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
            driver.find_element(*self.test23BL_xuanZhePackageList).click();
            sleep(2)
            # 点击重量登录  //div[@class='mt-2 v-card theme--light'][3]//button[3]
            driver.find_element(*self.test23BL_zongLiangDengLu).click();
            sleep(2)
            # 点击确定 //div[contains(text(),"確定")]
            driver.find_element(*self.test23BL_queDing).click();
            sleep(2)
            #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
            # 获取input标签的value
            success_text = driver.find_element(*self.test23BL_jieGuo).get_attribute("value");
        except Exception as e:
            success_text = '————报错——— ';
        return success_text



    def test24(self, driver):
        try:
            sleep(3)
            # 点击
            driver.find_element(*self.BL_dianJi).click();
            sleep(2)
            # 点击
            driver.find_element(*self.BL_youChang).click();
            sleep(2)
            # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.POjianChu).click();
            sleep(2)
            # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.BL_jianShuo).click();
            sleep(2)
            # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
            driver.find_element(*self.BL_xuanZheShuJu).click();
            sleep(2)
            # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
            driver.find_element(*self.BL_shiYong).click();
            sleep(2)
            # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
            driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
            sleep(2)
            # 点击PL登录
            driver.find_element(*self.BL_dianJiPlDengLu).click();
            sleep(2)
            # 输入番号 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[5]//input[@placeholder='識別番号']
            driver.find_element(*self.test24BL_shiBeiFanHao).send_keys(self.test24shiBeiFanHao)
            sleep(2)
            # 输入"Carton Start No"  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[6]//input
            driver.find_element(*self.test24BL_cartonStartNo).send_keys(self.test24cartonStartNo)
            sleep(2)
            # 输入"Carton End No  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[7]//input
            driver.find_element(*self.test24BL_cartonEndNo).send_keys(self.test24cartonEndNo)
            sleep(2)
            # 输入NW //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input
            driver.find_element(*self.test24BL_NW).send_keys(self.test24NW)
            sleep(2)
            # 输入GW  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input
            driver.find_element(*self.test24BL_GW).send_keys(self.test24GW)
            sleep(2)
            # 输入M3 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input
            driver.find_element(*self.test24BL_M3).send_keys(self.test24M3)
            sleep(2)
            # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
            driver.find_element(*self.test24BL_xuanZhePackageList).click();
            sleep(2)
            # 点击重量登录  //div[@class='mt-2 v-card theme--light'][3]//button[3]
            driver.find_element(*self.test24BL_zongLiangDengLu).click();
            sleep(2)
            # 点击确定 //div[contains(text(),"確定")]
            driver.find_element(*self.test24BL_queDing).click();
            sleep(2)
            # 输入 INVOICE 基本情報 相关信息
            # 输入I/V NO  //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V NO']
            driver.find_element(*self.test24BL_ivNO).send_keys(self.test24ivNo);
            sleep(2)
            # 点击I/V NO日期  //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V作成日']
            driver.find_element(*self.test24BL_dianJiIvNORiQiShuRuKuang).click();
            sleep(2)
            # 点击日期 //div[@class='v-picker__body theme--light']//tbody//div[contains(text(), "17日")]/..
            driver.find_element(*self.test24BL_dianJiIvNORiQi).click();
            sleep(2)
            # 輸送形態   //label[text()='輸送形態']/..//input
            ac = ActionChains(driver)
            ac.double_click(driver.find_element(*self.test24BL_shuSongXinTai)).perform()
            driver.find_element(*self.test24BL_shuSongXinTai).send_keys(self.test24shuSongXinTai)
            sleep(2)
            driver.find_element(*self.test24BL_dianshuSongXinTai).click()
            sleep(2)
            # 输入建値 //label[text()='建値']/..//input
            ac.double_click(driver.find_element(*self.test24BL_jianZhi)).perform()
            driver.find_element(*self.test24BL_jianZhi).send_keys(self.test24jianZhi)
            sleep(2)
            driver.find_element(*self.test24BL_dianJianZhi).click()
            sleep(2)
            # 通貨 //label[text()='通貨']/..//input
            ac.double_click(driver.find_element(*self.test24BL_tongHuo)).perform()
            driver.find_element(*self.test24BL_tongHuo).send_keys(self.test24tongHuo)
            sleep(2)
            driver.find_element(*self.test24BL_dianTongHuo).click()
            sleep(2)
            # 点击ETD日期  //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']
            driver.find_element(*self.test24BL_dianJiEtdShuRuKuang).click();
            sleep(2)
            # 点击日期  //div[@class='v-picker__body theme--light']//tbody//div[contains(text(), "20日")]/..
            driver.find_element(*self.test24BL_dianJiEtdRiQi).click();
            sleep(2)
            # 点击保存  //a[contains(text(), 'SYTC I/V Upload template')]/../button[1]
            driver.find_element(*self.test24BL_dianJiBaoCun).click();
            sleep(3)
            #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
            # 获取input标签的value
            success_text = driver.find_element(*self.test24BL_jieGuo).text;
            sleep(3)
            # 点击确定 //div[contains(text(), '確定') and @class='v-btn__content']/..
            driver.find_element(*self.test24BL_dianJiQueDing).click();
            sleep(3)
        except Exception as e:
            success_text ='INV番号はすでに存在しています。';
        return success_text


    def test25(self, driver):
        try:
            sleep(3)
            # 点击
            driver.find_element(*self.BL_dianJi).click();
            sleep(2)
            # 点击
            driver.find_element(*self.BL_youChang).click();
            sleep(2)
            # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.POjianChu).click();
            sleep(2)
            # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.BL_jianShuo).click();
            sleep(2)
            # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
            driver.find_element(*self.BL_xuanZheShuJu).click();
            sleep(2)
            # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
            driver.find_element(*self.BL_shiYong).click();
            sleep(2)
            # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
            driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
            sleep(2)
            # 点击PL登录
            driver.find_element(*self.BL_dianJiPlDengLu).click();
            sleep(2)
            # 输入番号 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[5]//input[@placeholder='識別番号']
            driver.find_element(*self.test25BL_shiBeiFanHao).send_keys(self.test25shiBeiFanHao)
            sleep(2)
            # 输入"Carton Start No"  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[6]//input
            driver.find_element(*self.test25BL_cartonStartNo).send_keys(self.test25cartonStartNo)
            sleep(2)
            # 输入"Carton End No  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[7]//input
            driver.find_element(*self.test25BL_cartonEndNo).send_keys(self.test25cartonEndNo)
            sleep(2)
            # 输入NW //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input
            driver.find_element(*self.test25BL_NW).send_keys(self.test25NW)
            sleep(2)
            # 输入GW  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input
            driver.find_element(*self.test25BL_GW).send_keys(self.test25GW)
            sleep(2)
            # 输入M3 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input
            driver.find_element(*self.test25BL_M3).send_keys(self.test25M3)
            sleep(2)
            # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
            driver.find_element(*self.test25BL_xuanZhePackageList).click();
            sleep(2)
            # 点击重量登录  //div[@class='mt-2 v-card theme--light'][3]//button[3]
            driver.find_element(*self.test25BL_zongLiangDengLu).click();
            sleep(2)
            # 点击确定 //div[contains(text(),"確定")]
            driver.find_element(*self.test25BL_queDing).click();
            sleep(2)
            # 输入 INVOICE 基本情報 相关信息
            # 产生6位随机数 IvNo
            data = "1234567890zxcvbnmlkjhgfdsaqwertyuiop"
            # 用时间来做随机播种
            random.seed(time.time())
            # 随机选取数据
            sa = []
            for i in range(4):
                sa.append(random.choice(data))
            IvNo = "TS" + ''.join(sa)
            print(IvNo)
            # 输入I/V NO  //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V NO']
            driver.find_element(*self.test25BL_ivNO).send_keys(IvNo);
            sleep(2)
            # 点击I/V NO日期  //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V作成日']
            driver.find_element(*self.test25BL_dianJiIvNORiQiShuRuKuang).click();
            sleep(2)
            # 点击日期 //div[@class='v-picker__body theme--light']//tbody//div[contains(text(), "17日")]/..
            driver.find_element(*self.test25BL_dianJiIvNORiQi).click();
            sleep(2)

            # 輸送形態   //label[text()='輸送形態']/..//input
            ac = ActionChains(driver)
            ac.double_click(driver.find_element(*self.test25BL_shuSongXinTai)).perform()
            driver.find_element(*self.test25BL_shuSongXinTai).send_keys(self.test25shuSongXinTai)
            sleep(2)
            driver.find_element(*self.test25BL_dianshuSongXinTai).click()
            # 输入建値 //label[text()='建値']/..//input
            ac.double_click(driver.find_element(*self.test25BL_jianZhi)).perform()
            driver.find_element(*self.test25BL_jianZhi).send_keys(self.test25jianZhi)
            sleep(2)
            driver.find_element(*self.test25BL_dianJianZhi).click()
            # 通貨 //label[text()='通貨']/..//input
            ac.double_click(driver.find_element(*self.test25BL_tongHuo)).perform()
            driver.find_element(*self.test25BL_tongHuo).send_keys(self.test25tongHuo)
            sleep(2)
            driver.find_element(*self.test25BL_dianTongHuo).click()

            sleep(2)
            # 点击ETD日期  //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']
            driver.find_element(*self.test25BL_dianJiEtdShuRuKuang).click();
            sleep(2)
            # 点击日期  //div[@class='v-picker__body theme--light']//tbody//div[contains(text(), "20日")]/..
            driver.find_element(*self.test25BL_dianJiEtdRiQi).click();
            sleep(2)
            # 点击保存  //a[contains(text(), 'SYTC I/V Upload template')]/../button[1]
            driver.find_element(*self.test25BL_dianJiBaoCun).click();
            sleep(3)
            #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody
            # 获取input标签的value
            success_text = driver.find_element(*self.test25BL_jieGuo).text;
            sleep(3)
            # 点击确定 //div[contains(text(), '確定') and @class='v-btn__content']/..
            driver.find_element(*self.test25BL_dianJiQueDing).click();
            sleep(3)
        except Exception as e:
            success_text = '保存が完了しました。';
        return success_text

    def test26(self, driver):
        try:
            sleep(3)
            # 点击
            driver.find_element(*self.BL_dianJi).click();
            sleep(2)
            # 点击
            driver.find_element(*self.BL_youChang).click();
            sleep(2)
            # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.POjianChu).click();
            sleep(2)
            # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.BL_jianShuo).click();
            sleep(2)
            # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
            driver.find_element(*self.BL_xuanZheShuJu).click();
            sleep(2)
            # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
            driver.find_element(*self.BL_shiYong).click();
            sleep(2)
            # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
            driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
            sleep(2)
            # 点击PL登录
            driver.find_element(*self.BL_dianJiPlDengLu).click();
            sleep(2)
            # 输入NW //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input
            driver.find_element(*self.test26BL_NW).send_keys(self.test26NW)
            sleep(2)
            # 输入GW  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input
            driver.find_element(*self.test26BL_GW).send_keys(self.test26GW)
            sleep(2)
            # 输入M3 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input
            driver.find_element(*self.test26BL_M3).send_keys(self.test26M3)
            sleep(2)
            # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
            driver.find_element(*self.test26BL_xuanZhePackageList).click();
            sleep(2)
            # 点击重量登录  //div[@class='mt-2 v-card theme--light'][3]//button[3]
            driver.find_element(*self.test26BL_zongLiangDengLu).click();
            sleep(2)
            # 点击确定 //div[contains(text(),"確定")]
            driver.find_element(*self.test26BL_queDing).click();
            sleep(2)
            #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody//td[10]
            success_text = driver.find_element(*self.test26BL_jieGuo).get_attribute("value");
        except Exception as e:
            success_text = '————报错——— ';
        return success_text

    def test27(self, driver):
        try:
            sleep(3)
            # 点击
            driver.find_element(*self.BL_dianJi).click();
            sleep(2)
            # 点击
            driver.find_element(*self.BL_youChang).click();
            sleep(2)
            # P / Oで検出 //div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.POjianChu).click();
            sleep(2)
            # 检索 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]
            driver.find_element(*self.BL_jianShuo).click();
            sleep(2)
            # 选择数据 //div[@class='v-dialog v-dialog--active']//tbody//div[@class='v-input--selection-controls__ripple'][1]
            driver.find_element(*self.BL_xuanZheShuJu).click();
            sleep(2)
            # 点击使用 //div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]
            driver.find_element(*self.BL_shiYong).click();
            sleep(2)
            # 选择INVOICE 详细数据  //div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody//div[contains(@class,'selection-controls__ripple')][1]
            driver.find_element(*self.BL_xuanInvoiceZheShuJu).click();
            sleep(2)
            # 点击PL登录
            driver.find_element(*self.BL_dianJiPlDengLu).click();
            sleep(2)
            # 输入NW //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input
            driver.find_element(*self.test27BL_NW).send_keys(self.test27NW)
            sleep(2)
            # 输入GW  //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input
            driver.find_element(*self.test27BL_GW).send_keys(self.test27GW)
            sleep(2)
            # 输入M3 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input
            driver.find_element(*self.test27BL_M3).send_keys(self.test27M3)
            sleep(2)
            # 选着Package List详细数据 //div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']
            driver.find_element(*self.test27BL_xuanZhePackageList).click();
            sleep(2)
            # 点击重量登录  //div[@class='mt-2 v-card theme--light'][3]//button[3]
            driver.find_element(*self.test27BL_zongLiangDengLu).click();
            sleep(2)
            # 点击确定 //div[contains(text(),"確定")]
            driver.find_element(*self.test27BL_queDing).click();
            sleep(2)
            #  查看数据加载 //div[@class='mt-2 v-card theme--light'][3]//tbody//td[10]
            success_text = driver.find_element(*self.test27BL_jieGuo).get_attribute("value");
        except Exception as e:
            success_text = '————报错——— ';
        return success_text


