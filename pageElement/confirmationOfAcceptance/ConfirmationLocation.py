import datetime
from selenium.webdriver.common.by import By
import random
class Location(object):
    #受入确认
    ShouRuQueRen = [By.XPATH,"//div[@class='flex nav xs6'][2]/div[3]"]

    #检索
    JianSuo = [By.XPATH,"//div[text()='検索']"]
    #受入确认解除
    JieChu = [By.XPATH,"//div[text()='受入確認解除']/.."]
    #パターン設定
    MoShiSheDing = [By.XPATH,"//div[text()='パターン設定']/.."]
    #结果
    JieGuo = [By.XPATH,"//div[@class='v-content__wrap']//tbody"]
    #test1
    ZhuangTai = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='layout row wrap']/div[13]//input/.."]
    ZhuangTaiXuanZe = [By.XPATH,"//div[@class='v-menu__content theme--light menuable__content__active']//div[text()='納入指示済']"]

    #test2
    LuYangGang = [By.XPATH,"//input[@aria-label='陸揚港']"]
    ChaXunJieGuo2 = [By.XPATH,"//div[@class='v-table__overflow']/table/tbody/tr/td[10]"]

    #test3
    NaRuChangSuo = [By.XPATH,"//div[@class='application theme--light']//div[@class='mt-2 v-card theme--light']//input[@aria-label='納入場所']"]
    NaRuChangSuoXuanZe = [By.XPATH,"//span[text()='栃木物流センター（３２－００）']/.."]
    ChaXunJieGuo3 = [By.XPATH,"//div[@class='v-table__overflow']/table/tbody/tr/td[22]"]

    #test4
    JieShuRi = [By.XPATH,"//div[@label='納入指示日']/../../div[2]//div[@class='v-input__slot']"]
    time = datetime.datetime.now().timetuple()
    Endtoday = time.tm_mday
    EndRiQi = [By.XPATH,'//div[text()="{}日"]'.format(Endtoday)]

    #test5
    KaiShiRi = [By.XPATH,"//div[@label='納入指示日']/../../div[1]//div[@class='v-input__slot']"]
    time = datetime.datetime.now().timetuple()
    Starttoday = time.tm_mday
    StartRiQi = [By.XPATH,'//div[text()="{}日"]'.format(Starttoday)]

    #test6
    OpenEndCalendar = [By.XPATH,"//div[@label='納入指示日']/../../div[2]//div[@class='v-input__slot']"]
    OpenStartCalendar = [By.XPATH, "//div[@label='納入指示日']/../../div[1]//div[@class='v-input__slot']"]
    time = datetime.datetime.now().timetuple()
    EndDate = time.tm_mday
    EndDate1 = [By.XPATH,'//div[text()="{}日"]'.format(EndDate)]

    time = datetime.datetime.now().timetuple()
    StartDate = time.tm_mday
    StartDate1 = [By.XPATH, '//div[text()="{}日"]'.format(StartDate)]

    #test7
    ShuSongXinTai = [By.XPATH,"//input[@aria-label='運送形態']/.."]
    ShuSongXinTaiXuanZe = [By.XPATH,"//div[text()='SEA']"]

    #test8
    #状态下拉框
    ZhuangTaiXiaLaXuanZe = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='layout row wrap']/div[13]//input/.."]
    XuanZeZhuangTai = [By.XPATH,"//div[@class='v-menu__content theme--light menuable__content__active']//div[text()='受入確認済']"]
    rom = random.randint(1,10)
    ShuJuXuanZe = [By.XPATH,"//div[@class='v-table__overflow']/table/tbody/tr[{}]//div[@class='v-input__slot']".format(rom)]
    QueRenJieChu = [By.XPATH,"//div[@class='v-content__wrap']//div/button[5]/div"]
    QueRen = [By.XPATH,"//div[@class='v-dialog v-dialog--active']//button[1]"]

    #test9
    NaRuZhiShiJi = [By.XPATH,"//main//input[@aria-label='ステータス']/../.."]
    XuanZeNaRuZhiShiJi = [By.XPATH,"//div[@class='v-menu__content theme--light menuable__content__active']//div[text()='納入指示済']/.."]
    c = random.randint(1,2)
    ShuJuXuanZe1 = [By.XPATH,"//div[@class='v-table__overflow']/table/tbody/tr[{}]//div[@class='v-input__slot']".format(c)]
    MoShiSheDing = [By.XPATH,"//main//div[text()='パターン設定']/.."]
    GitPatternElement = [By.XPATH,"//main//form//div[@class='v-card__title']//span[7]"]
    PeiSongMoShi = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='v-card__title']/button"]
    ShuRuMoShi = [By.XPATH,"//input[@aria-label='配送パターン']/.."]
    XuanZeShuRuMoShi = [By.XPATH,"//div[contains(@class,'menuable__content__active')]/div[1]/div[1]/div[1]//div[@class='v-list__tile__title']"]
    MoShiBaoCun = [By.XPATH,"//div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions'][1]//div[text()='保存']/.."]
    BaoCun = [By.XPATH,"//div[@class='v-content__wrap']//button[2]"]
    QueRenBaoCunJi = [By.XPATH,"//div[@class='v-dialog v-dialog--active']//button/div"]
    ChoiceDeliveryPatternElement = [By.XPATH,"//div[contains(@class,'menuable__content__active')]/div[1]/div[1]/div[1]//div[@class='v-list__tile__title']"]


