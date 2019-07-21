from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

# from jusda.sharpUIauto_cxp.pageElement.InvRegistrationLocation import Location
from pageElement.pllogin.InvRegistrationLocation import Location


class Logic(Location):
    def __init__(self):
        self.test2ivNo = '5024040';
        self.test3haiWai = '77512:FIH(HONG KONG)LIMITED';
        self.test4ivNo = '666666';
        self.test5poNo = '5271811';
        self.test6poNo = '666666';
        self.test7jiChuGang = 'SHA:ＳＨＡＮＧＨＡＩ';
        self.test8yunShuXinTai = 'SEA';
        self.test9naRuChangSuo = 'B98:（健康環境）サービスパーツ倉庫';
        self.test10luYangGang = 'OSK:大阪港';
        self.test1lluRuDanDangZe = 'NAOMI'
        self.test12jianzhi = 'FCA';
        self.test13tongHuo = 'USD';
        self.test14haiWai = '77512:FIH(HONG KONG)LIMITED';
        self.test14jianzhi = 'FCA'
        self.test14tongHuo = 'USD'
        self.test15lotNo = '00001';


    def test1(self, driver):
        sleep(3)
        #点击
        WebDriverWait(driver, 10).until(lambda x: x.find_element(*self.BL_dianJi)).click();
        # 点击
        WebDriverWait(driver, 10).until(lambda x: x.find_element(*self.BL_JianShuo)).click();
        sleep(1.5)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text

    def test2(self, driver):
        sleep(3)
        #点击
        driver.find_element(*self.BL_dianJi).click();
        # 输入账号  //*[@id="app"]/div[19]/main/div/div[1]/div[2]/form/div/div/div[2]/div/div/div[1]/div[1]/input
        driver.find_element(*self.ivNo_element).send_keys(self.test2ivNo)
        sleep(1.5)
        # 点击
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text

    def test3(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        # 输入账号  //input[@aria-label='海外取引先']
        driver.find_element(*self.test3haiWai_element).send_keys(self.test3haiWai)
        sleep(1.5)
        # 点击
        driver.find_element(*self.test3BL_dianji).click();
        sleep(1.5)
        # 点击
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text

    def test4(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        # 输入账号  //*[@id="app"]/div[19]/main/div/div[1]/div[2]/form/div/div/div[5]/div/div/div[1]/div[1]/input
        driver.find_element(*self.ivNo_element).send_keys(self.test4ivNo)
        sleep(1.5)
        # 点击
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text

    def test5(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        # 输入账号  //input[@aria-label='P/O NO']
        driver.find_element(*self.poNo_element).send_keys(self.test5poNo)
        sleep(1.5)
        # 点击
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text

    def test6(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        # 输入账号  //input[@aria-label='P/O NO']
        driver.find_element(*self.poNo_element).send_keys(self.test6poNo)
        sleep(1.5)
        # 点击
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text

    def test7(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        # 输入账号  //input[@aria-label='積出港']
        driver.find_element(*self.test7BL_jiChuGang).send_keys(self.test7jiChuGang)
        sleep(1.5)
        # 点击
        driver.find_element(*self.test7BL_dianji).click();
        sleep(1.5)
        # 点击
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text


    def test8(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        sleep(1.5)
        # 輸送形態   //label[text()='輸送形態']/..//input
        ac = ActionChains(driver)
        ac.double_click(driver.find_element(*self.test8BL_yunShuXinTai)).perform()
        driver.find_element(*self.test8BL_yunShuXinTai).send_keys(self.test8yunShuXinTai)
        sleep(1.5)
        driver.find_element(*self.test8BL_dianji).click()
        # 点击
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text

    def test9(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        # 输入账号  //*[@id="app"]/div[19]/main/div/div[1]/div[2]/form/div/div/div[5]/div/div/div[1]/div[1]/input
        driver.find_element(*self.test9BL_naRuChangSuo).send_keys(self.test9naRuChangSuo)
        sleep(1.5)
        # 点击
        driver.find_element(*self.test9BL_dianji).click();
        sleep(1.5)
        # 点击
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text

    def test10(self, driver):
        sleep(3)
        driver.find_element(*self.BL_dianJi).click();
        # driver.find_element_by_xpath("//input[@aria-label='陸揚港']").send_keys("AOJ:青森空港")
        driver.find_element(*self.test10BL_luYangGang).send_keys(self.test10luYangGang)
        sleep(1.5)
        # driver.find_element_by_xpath("//span[@class='v-list__tile__mask']").click();
        driver.find_element(*self.test10BL_dianJiLuYangGang).click();
        sleep(1.5)
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        # success_text = driver.find_element_by_xpath("//tbody").text;
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text


    def test11(self, driver):
        sleep(3)
        driver.find_element(*self.BL_dianJi).click();
        # driver.find_element_by_xpath("//input[@aria-label='陸揚港']").send_keys("AOJ:青森空港")
        driver.find_element(*self.test11BL_luRuDanDangZe).send_keys(self.test1lluRuDanDangZe)
        sleep(1.5)
        # driver.find_element_by_xpath("//span[@class='v-list__tile__mask']").click();
        driver.find_element(*self.test11BL_dianJiLuRuDanDangZe).click();
        sleep(1.5)
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        # success_text = driver.find_element_by_xpath("//tbody").text;
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text




    def test12(self, driver):
        sleep(3)
        driver.find_element(*self.BL_dianJi).click();
        # driver.find_element_by_xpath("//input[@aria-label='陸揚港']").send_keys("AOJ:青森空港")
        driver.find_element(*self.test12BL_jianzhi).send_keys(self.test12jianzhi)
        sleep(1.5)
        # driver.find_element_by_xpath("//span[@class='v-list__tile__mask']").click();
        driver.find_element(*self.test12BL_dianJiJianzhi).click();
        sleep(1.5)
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        # success_text = driver.find_element_by_xpath("//tbody").text;
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text

    def test13(self, driver):
        sleep(4)
        driver.find_element(*self.BL_dianJi).click();
        # driver.find_element_by_xpath("//input[@aria-label='陸揚港']").send_keys("AOJ:青森空港")
        driver.find_element(*self.test13BL_tongHuo).send_keys(self.test13tongHuo)
        sleep(1.5)
        # driver.find_element_by_xpath("//span[@class='v-list__tile__mask']").click();
        driver.find_element(*self.test13BL_dianJiJianzhi).click();
        sleep(1.5)
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        # success_text = driver.find_element_by_xpath("//tbody").text;
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text



    def test14(self, driver):
        sleep(3)
        driver.find_element(*self.BL_dianJi).click();
        # 海外引取先
        driver.find_element(*self.test14BL_haiWai).send_keys(self.test14haiWai)
        sleep(1.5)
        driver.find_element(*self.test14BL_dianJihaiWai).click();
        sleep(1.5)
        # 建值
        driver.find_element(*self.test14BL_jianzhi).send_keys(self.test14jianzhi)
        sleep(1.5)
        driver.find_element(*self.test14BL_dianJijianzhi).click();
        sleep(1.5)
        # 通货
        driver.find_element(*self.test14BL_tongHuo).send_keys(self.test14tongHuo)
        sleep(1.5)
        driver.find_element(*self.test14BL_dianJiJianzhi).click();
        sleep(1.5)
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text

    def test15(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click();
        # 输入账号  //*[@id="app"]/div[19]/main/div/div[1]/div[2]/form/div/div/div[2]/div/div/div[1]/div[1]/input
        driver.find_element(*self.test15lotNo_element).send_keys(self.test15lotNo)
        sleep(1.5)
        # 点击
        driver.find_element(*self.BL_JianShuo).click();
        sleep(1.5)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        return success_text

    def test16(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click()
        sleep(2)
        # 点击开始时间 //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']
        driver.find_element(*self.test16dianJiKaiShiSiJian_element).click()
        sleep(2)
        # 选择时间 //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']
        driver.find_element(*self.test16xuanZheKaiShiSiJian_element).click()
        sleep(2)
        # 点击
        driver.find_element(*self.BL_JianShuo).click()
        sleep(2)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        sleep(2)
        return success_text

    def test17(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click()
        sleep(2)
        # 点击开始时间 //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V作成日']
        driver.find_element(*self.test17dianJiIVKaiShiSiJian_element).click()
        sleep(2)
        # 选择时间 //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']
        driver.find_element(*self.test17xuanZheIVKaiShiSiJian_element).click()
        sleep(2)
        # 点击
        driver.find_element(*self.BL_JianShuo).click()
        sleep(2)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        sleep(2)
        return success_text


    def test18(self, driver):
        sleep(3)
        # 点击
        driver.find_element(*self.BL_dianJi).click()
        sleep(2)
        # 点击开始时间 //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']
        driver.find_element(*self.test18dianJiKaiShiSiJian_element).click()
        sleep(2)
        # 选择时间 //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']
        driver.find_element(*self.test18xuanZheKaiShiSiJian_element).click()
        sleep(2)
        # 点击开始时间 //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V作成日']
        driver.find_element(*self.test18dianJiIVKaiShiSiJian_element).click()
        sleep(2)
        # 选择时间 //div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']
        driver.find_element(*self.test18xuanZheIVKaiShiSiJian_element).click()
        sleep(2)
        # 点击
        driver.find_element(*self.BL_JianShuo).click()
        sleep(2)
        success_text = driver.find_element(*self.BL_jieGuo).text;
        sleep(2)
        return success_text











