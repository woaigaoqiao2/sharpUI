from selenium.webdriver.common.by import By

class Location(object):
    # 公用XPATH
    # 点击INV P/L登録
    BL_dianJi = [By.XPATH, "//div[@class='flex nav xs6'][1]/div[1]"];
    # 检索
    BL_JianShuo = [By.XPATH, "//button[@class='btn-search v-btn theme--light']"];
    # 搜索结果
    BL_jieGuo = [By.XPATH, '//tbody'];
    #I/V NO输入框
    ivNo_element = [By.XPATH, "//input[@aria-label='I/V NO']"];
    # P/O NO输入框
    poNo_element = [By.XPATH, "//input[@aria-label='P/O NO']"]




    #test1
    # test2
    # test3
    test3haiWai_element = [By.XPATH,"//input[@aria-label='海外取引先']"];
    test3BL_dianji = [By.XPATH, "//span[@class='v-list__tile__mask']"];
    # test4
    # test5
    # test6
    # test7
    test7BL_jiChuGang = [By.XPATH,"//input[@aria-label='積出港']"];
    test7BL_dianji = [By.XPATH, "//span[@class='v-list__tile__mask']"];

    # test8
    test8BL_yunShuXinTai = [By.XPATH, "//input[@aria-label='輸送形態']"];
    test8BL_dianji = [By.XPATH, "//div[contains(@class,'menuable__content__active')]//a/div"];


    # test9
    test9BL_naRuChangSuo = [By.XPATH,"//input[@aria-label='最終納入場所']"];
    test9BL_dianji = [By.XPATH, "//span[@class='v-list__tile__mask']"];

    # test10
    test10BL_luYangGang = [By.XPATH,"//input[@aria-label='陸揚港']"];
    test10BL_dianJiLuYangGang = [By.XPATH, "//span[@class='v-list__tile__mask']"];

    # test11
    test11BL_luRuDanDangZe = [By.XPATH, "//input[@aria-label='納入場所担当者']"];
    test11BL_dianJiLuRuDanDangZe = [By.XPATH, "//span[@class='v-list__tile__mask']"];

    # test12
    test12BL_jianzhi = [By.XPATH, "//input[@aria-label='建値']"];
    test12BL_dianJiJianzhi = [By.XPATH, "//span[@class='v-list__tile__mask']"];

    # test13
    test13BL_tongHuo = [By.XPATH, "//input[@aria-label='通貨']"];
    test13BL_dianJiJianzhi = [By.XPATH, "//span[@class='v-list__tile__mask']"];

    # test14
    test14BL_haiWai = [By.XPATH, "//input[@aria-label='海外取引先']"];
    test14BL_dianJihaiWai = [By.XPATH, "//span[@class='v-list__tile__mask']"];
    test14BL_jianzhi = [By.XPATH, "//input[@aria-label='建値']"];
    test14BL_dianJijianzhi = [By.XPATH, "//span[@class='v-list__tile__mask']"];
    test14BL_tongHuo = [By.XPATH, "//input[@aria-label='通貨']"];
    test14BL_dianJiJianzhi = [By.XPATH, "//span[@class='v-list__tile__mask']"];

    # test15
    test15lotNo_element = [By.XPATH, "//input[@aria-label='Lot NO']"];

    # test16
    test16dianJiKaiShiSiJian_element = [By.XPATH, "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']"];
    test16xuanZheKaiShiSiJian_element = [By.XPATH, "//div[@class='v-picker__body theme--light']//tbody//div[contains(text(), '11日')]/.."];

    # test17
    test17dianJiIVKaiShiSiJian_element = [By.XPATH,
                                        "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V作成日']"];
    test17xuanZheIVKaiShiSiJian_element = [By.XPATH,
                                         "//div[@class='v-picker__body theme--light']//tbody//div[contains(text(), '12日')]/.."];

    # test18
    test18dianJiKaiShiSiJian_element = [By.XPATH,
                                        "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']"];
    test18xuanZheKaiShiSiJian_element = [By.XPATH,
                                         "//div[@class='v-picker__body theme--light']//tbody//div[contains(text(), '11日')]/.."];
    test18dianJiIVKaiShiSiJian_element = [By.XPATH,
                                        "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V作成日']"];
    test18xuanZheIVKaiShiSiJian_element = [By.XPATH,
                                         "//div[@class='v-picker__body theme--light']//tbody//div[contains(text(), '25日')]/.."];

