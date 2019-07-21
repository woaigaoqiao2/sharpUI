from selenium.webdriver.common.by import By

class Location(object):
    # 公用XPATH

    Loading=[By.XPATH, "//div[@class='v-dialog v-dialog--persistent']"]

    # 点击INV P/L登録
    BL_dianJi=[By.XPATH, "// main // div[contains(text(), 'INV P/L登録')]"]
    #BL_dianJi = [By.XPATH, "//div[@class='flex nav xs6'][1]/div[1]"];
    #点击有償新規
    BL_youChang = [By.XPATH, "//button[@class='v-btn v-btn--small theme--light'][1]"];
    # INVOICE 详细-P/O で検出
    POjianChu = [By.XPATH, "//div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[1]"];
    #P/O で検出-検索
    BL_jianShuo = [By.XPATH, "//div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]"];
    # P/O で検出-选择第一条数据
    BL_xuanZheShuJu = [By.XPATH,"//div[@class='v-dialog v-dialog--active']//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    # P/O で検出-点击使用
    BL_shiYong = [By.XPATH, "//div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[2]"];
    # INVOICE 详细-选择第一条数据
    BL_xuanInvoiceZheShuJu = [By.XPATH,"//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]//div[contains(@class,'selection-controls__ripple')]"];
    # INVOICE 详细-P/L登録
    BL_dianJiPlDengLu = [By.XPATH,"//div[@class='mt-2 v-card theme--light'][2]//div[@class='v-card__actions']/button[2]"];


    #test1
    test1BL_jieGuo = [By.XPATH, "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody"];

    # test2
    test2poNO_element = [By.XPATH,"//div[@class='v-dialog v-dialog--active']//input[@aria-label='P/O NO']"];

    jiansuopo=[By.XPATH,"//input[@aria-label='P/O NO']"]

    test2BL_jieGuo = [By.XPATH, "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody"];

    # test3
    test3poNO_element = [By.XPATH, "//div[@class='v-dialog v-dialog--active']//input[@aria-label='P/O NO']"];

    test3BL_jieGuo = [By.XPATH, "//div[@class='v-dialog v-dialog--active']//tbody"];

    # test4
    test4poNO_element = [By.XPATH, "//div[@class='v-dialog v-dialog--active']//input[@aria-label='事業本部']"];
    test4BL_jieGuo = [By.XPATH, "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody"];

    # test5
    test5lotNO_element = [By.XPATH, "//div[@class='v-dialog v-dialog--active']//input[@aria-label='Lot NO']"];
    test5BL_jieGuo = [By.XPATH, "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody"];

    # test6
    test6seNiePinFan_element = [By.XPATH, "//div[@class='v-dialog v-dialog--active']//input[@aria-label='社内品番']"];
    test6BL_jieGuo = [By.XPATH, "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody"];

    # test7
    test7seWaiPinFan_element = [By.XPATH,
                                "//div[@class='v-dialog v-dialog--active']//input[@aria-label='社外品番']"];
    test7BL_jieGuo = [By.XPATH,
                      "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody"];

    # test8
    test8siNO_element = [By.XPATH, "//div[@class='v-dialog v-dialog--active']//input[@aria-label='SI.NO']"];
    test8BL_jieGuo = [By.XPATH, "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody"];

    # test9
    test9poNO_element = [By.XPATH, "//div[@class='v-dialog v-dialog--active']//input[@aria-label='P/O NO']"];
    test9siNO_element = [By.XPATH, "//div[@class='v-dialog v-dialog--active']//input[@aria-label='SI.NO']"];
    test9BL_jieGuo = [By.XPATH, "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody"];

    # test10
    test10BL_fanHui = [By.XPATH,"//div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[3]"];
    test10BL_jieGuo = [By.XPATH, "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody"];

    # test11
    test11BL_jieGuo = [By.XPATH, "//div[@class='mt-2 v-card theme--light'][3]//tbody"];

    # test12
    test12BL_xuanZheShuJuEr = [By.XPATH,
                             "//div[@class='v-dialog v-dialog--active']//tbody/tr[2]//div[@class='v-input--selection-controls__ripple']"];
    test12BL_xuanInvoiceZheShuJuEr = [By.XPATH,
                                    "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[2]//div[contains(@class,'selection-controls__ripple')]"];
    test12BL_jieGuo = [By.XPATH, "//div[@class='mt-2 v-card theme--light'][3]//tbody"]

    test12BL_confirm_alert=[By.XPATH, "//div[@class='v-btn__content' and contains(text(),'はい')]"]

    # test13
    test13shuLiangQingChu_element = [By.XPATH,
                              "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[9]//i[@class='v-icon v-icon--link material-icons theme--light']"];
    test13shuLiang_element = [By.XPATH,
                                    "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[9]//input[@placeholder='商品の数']"];
    test13BL_jieGuo = [By.XPATH,
                       "//div[@class='mt-2 v-card theme--light'][3]//tbody"];

    # test14
    test14yuanChanGuoQingChu_element = [By.XPATH,
                                     "//i[@class='v-icon v-icon--link material-icons theme--light'and contains(text(),'clear') ]"];
    test14yuanChanGuo_element = [By.XPATH,
                              "//tbody/tr[1]/td[11]//input[@placeholder='原産国']"];
    test14dianJiYuanChanGuo_element = [By.XPATH,
                                 "//a[@class='v-list__tile v-list__tile--link theme--light v-list__tile--highlighted']"];
    test14BL_jieGuo = [By.XPATH,
                       "//div[@class='mt-2 v-card theme--light'][3]//tbody"];

    # test15
    test15BL_shiBeiFanHao = [By.XPATH,
                               "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[5]//input[@placeholder='識別番号']"];
    test15BL_xuanZhePackageList = [By.XPATH,
                               "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test15BL_zongLiangDengLu = [By.XPATH,
                               "//div[@class='mt-2 v-card theme--light'][3]//button[3]"];
    test15BL_queDing = [By.XPATH,
                        "//div[contains(text(),'確定') and @class='v-btn__content']/.."];
    test15BL_jieGuo = [By.XPATH,
                       "//div[@class='mt-2 v-card theme--light'][3]//tbody"];



    # test16
    test16BL_cartonStartNo = [By.XPATH,
                             "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[6]//input"];
    test16BL_cartonEndNo = [By.XPATH,
                             "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[7]//input"];
    test16BL_xuanZhePackageList = [By.XPATH,
                                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test16BL_zongLiangDengLu = [By.XPATH,
                                "//div[@class='mt-2 v-card theme--light'][3]//button[3]"];
    test16BL_queDing = [By.XPATH,
                        "//div[contains(text(),'確定') and @class='v-btn__content']/.."];
    test16BL_jieGuo = [By.XPATH,
                       "//div[@class='mt-2 v-card theme--light'][3]//tbody"];

    # test17
    test17BL_NW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input"];
    test17BL_GW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input"];
    test17BL_M3 = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input"];
    test17BL_xuanZhePackageList = [By.XPATH,
                                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test17BL_zongLiangDengLu = [By.XPATH,
                                "//div[@class='mt-2 v-card theme--light'][3]//button[3]"];
    test17BL_queDing = [By.XPATH,
                        "//div[contains(text(),'確定') and @class='v-btn__content']/.."];
    test17BL_jieGuo = [By.XPATH,
                       "//div[@class='mt-2 v-card theme--light'][3]//tbody//td[10]//input"];

    # test18
    test18BL_xuanZhePackageList = [By.XPATH,
                                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test18BL_xiaoChu = [By.XPATH,
                                "//div[@class='mt-2 v-card theme--light'][3]//button[2]"];
    test18BL_queDing = [By.XPATH,
                        "//div[contains(text(),'削除してよろしいでしょうか？')]/..//button[1]"];
    test18BL_xiaoChuJiQueDing = [By.XPATH,
                        "//div[contains(text(), '削除成功しました。')]/..//button"];
    test18BL_jieGuo = [By.XPATH,
                       "//div[@class='mt-2 v-card theme--light'][3]//tbody"];

    # test19;
    test19BL_xuanZhePackageList = [By.XPATH,
                                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test19BL_xiaoChu = [By.XPATH,
                        "//div[@class='mt-2 v-card theme--light'][3]//button[2]"];
    test19BL_quXiao = [By.XPATH,
                        "//div[contains(text(), '削除してよろしいでしょうか？')]/..//button[2]"];
    test19BL_jieGuo = [By.XPATH,
                       "//div[@class='mt-2 v-card theme--light'][3]//tbody"];

    # test20
    test20BL_xuanZhePackageList = [By.XPATH,
                                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test20BL_PLhangFen = [By.XPATH,
                        "//div[@class='mt-2 v-card theme--light'][3]//button[1]"];
    test20BL_jieGuo = [By.XPATH,
                       "//div[@class='mt-2 v-card theme--light'][3]//tbody"];

    # test21
    test21shuLiangQingChu_element = [By.XPATH,
                                     "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[8]//i[@class='v-icon v-icon--link material-icons theme--light']"];
    test21shuLiang_element = [By.XPATH,
                              "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[8]//input[@placeholder='商品の数']"];
    test21BL_shiBeiFanHao = [By.XPATH,
                             "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[5]//input[@placeholder='識別番号']"];
    test21BL_cartonStartNo = [By.XPATH,
                              "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[6]//input"];
    test21BL_cartonEndNo = [By.XPATH,
                            "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[7]//input"];
    # test21BL_packageListShuLiang = [By.XPATH,
    #                                 "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[9]//input"];
    test21BL_NW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input"];
    test21BL_GW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input"];
    test21BL_M3 = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input"];
    test21BL_xuanZhePackageList = [By.XPATH,
                                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test21BL_zongLiangDengLu = [By.XPATH,
                                "//div[@class='mt-2 v-card theme--light'][3]//button[3]"];
    test21BL_queDing = [By.XPATH,
                        "//div[contains(text(),'確定') and @class='v-btn__content']/.."];
    test21BL_ivNO = [By.XPATH,
                     "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V NO']"];
    test21BL_dianJiIvNORiQiShuRuKuang = [By.XPATH,
                                         "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V作成日']"];
    test21BL_dianJiIvNORiQi = [By.XPATH,
                               "//div[@class='v-picker__body theme--light']//tbody//div[contains(text(), '17日')]/.."];

    test21BL_shuSongXinTai = [By.XPATH,
                              "//label[text()='輸送形態']/..//input"];
    test21BL_dianshuSongXinTai = [By.XPATH,
                                  "//div[contains(@class,'menuable__content__active')]//a/div"];
    test21BL_jianZhi = [By.XPATH,
                        "//label[text()='建値']/..//input"];
    test21BL_dianJianZhi = [By.XPATH,
                            "//div[contains(@class,'menuable__content__active')]//a/div"];
    test21BL_tongHuo = [By.XPATH,
                        "//label[text()='通貨']/..//input"];
    test21BL_dianTongHuo = [By.XPATH,
                            "//div[contains(@class,'menuable__content__active')]//a/div"];


    test21BL_dianJiEtdShuRuKuang = [By.XPATH,
                                    "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']"];
    test21BL_dianJiEtdRiQi = [By.XPATH,
                              "//div[@class='v-picker__body theme--light']//tbody//div[contains(text(), '20日')]/.."];
    test21BL_dianJiBaoCun = [By.XPATH,
                             "//a[contains(text(), 'SYTC I/V Upload template')]/../button[1]"];
    test21BL_jieGuo = [By.XPATH,
                       "//div[contains(text(), '保存が完了しました。')]"];
    test21BL_dianJiQueDing = [By.XPATH,
                              "//div[contains(text(), '確定') and @class='v-btn__content']/.."];

    # test22
    test22shuLiangQingChu_element = [By.XPATH,
                        "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[8]//i[@class='v-icon v-icon--link material-icons theme--light']"];
    test22shuLiang_element = [By.XPATH,
                        "//div[@class='elevation-1 mt-2 mb-2 inline-edit']//tbody/tr[1]/td[8]//input[@placeholder='商品の数']"];
    test22BL_shiBeiFanHao = [By.XPATH,
                             "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[5]//input[@placeholder='識別番号']"];
    test22BL_cartonStartNo = [By.XPATH,
                              "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[6]//input"];
    test22BL_cartonEndNo = [By.XPATH,
                            "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[7]//input"];
    test22BL_packageListShuLiang = [By.XPATH,
                            "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[9]//input"];
    test22BL_NW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input"];
    test22BL_GW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input"];
    test22BL_M3 = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input"];
    test22BL_xuanZhePackageList = [By.XPATH,
                                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test22BL_zongLiangDengLu = [By.XPATH,
                                "//div[@class='mt-2 v-card theme--light'][3]//button[3]"];
    test22BL_queDing = [By.XPATH,
                        "//div[contains(text(),'確定') and @class='v-btn__content']/.."];
    test22BL_ivNO = [By.XPATH,
                     "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V NO']"];
    test22BL_dianJiIvNORiQiShuRuKuang = [By.XPATH,
                                         "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V作成日']"];
    test22BL_dianJiIvNORiQi = [By.XPATH,
                               "//div[@class='v-picker__body theme--light']//tbody//div[contains(text(), '17日')]/.."];
    test22BL_shuSongXinTai = [By.XPATH,
                              "//label[text()='輸送形態']/..//input"];
    test22BL_dianshuSongXinTai = [By.XPATH,
                                  "//div[contains(@class,'menuable__content__active')]//a/div"];
    test22BL_jianZhi = [By.XPATH,
                        "//label[text()='建値']/..//input"];
    test22BL_dianJianZhi = [By.XPATH,
                            "//div[contains(@class,'menuable__content__active')]//a/div"];
    test22BL_tongHuo = [By.XPATH,
                        "//label[text()='通貨']/..//input"];
    test22BL_dianTongHuo = [By.XPATH,
                            "//div[contains(@class,'menuable__content__active')]//a/div"];


    test22BL_dianJiEtdShuRuKuang = [By.XPATH,
                                    "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']"];
    test22BL_dianJiEtdRiQi = [By.XPATH,
                              "//div[@class='v-picker__body theme--light']//tbody//div[contains(text(), '20日')]/.."];
    test22BL_dianJiBaoCun = [By.XPATH,
                             "//a[contains(text(), 'SYTC I/V Upload template')]/../button[1]"];
    test22BL_jieGuo = [By.XPATH,
                       "//div[contains(text(), 'PO出荷数量とPOのPackingList数量が不一致のため、保存できません。')]"];
    test22BL_dianJiQueDing = [By.XPATH,
                              "//div[contains(text(), '確定') and @class='v-btn__content']/.."];


    # test23
    test23BL_shiBeiFanHao = [By.XPATH,
                             "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[5]//input[@placeholder='識別番号']"];
    test23BL_cartonStartNo = [By.XPATH,
                              "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[6]//input"];
    test23BL_cartonEndNo = [By.XPATH,
                            "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[7]//input"];
    test23BL_NW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input"];
    test23BL_GW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input"];
    test23BL_M3 = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input"];
    test23BL_xuanZhePackageList = [By.XPATH,
                                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test23BL_zongLiangDengLu = [By.XPATH,
                                "//div[@class='mt-2 v-card theme--light'][3]//button[3]"];
    test23BL_queDing = [By.XPATH,
                        "//div[contains(text(),'確定') and @class='v-btn__content']/.."];
    test23BL_jieGuo = [By.XPATH,
                       "//div[@class='mt-2 v-card theme--light'][3]//tbody//input[@placeholder='識別番号']"];

    # test24
    test24BL_shiBeiFanHao = [By.XPATH,
                             "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[5]//input[@placeholder='識別番号']"];
    test24BL_cartonStartNo = [By.XPATH,
                              "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[6]//input"];
    test24BL_cartonEndNo = [By.XPATH,
                            "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[7]//input"];
    test24BL_NW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input"];
    test24BL_GW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input"];
    test24BL_M3 = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input"];
    test24BL_xuanZhePackageList = [By.XPATH,
                                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test24BL_zongLiangDengLu = [By.XPATH,
                                "//div[@class='mt-2 v-card theme--light'][3]//button[3]"];
    test24BL_queDing = [By.XPATH,
                        "//div[contains(text(),'確定') and @class='v-btn__content']/.."];
    test24BL_ivNO = [By.XPATH,
                     "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V NO']"];
    test24BL_dianJiIvNORiQiShuRuKuang = [By.XPATH,
                                         "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V作成日']"];
    test24BL_dianJiIvNORiQi = [By.XPATH,
                               "//div[@class='v-picker__body theme--light']//tbody//div[contains(text(), '17日')]/.."];

    test24BL_shuSongXinTai = [By.XPATH,
                              "//label[text()='輸送形態']/..//input"];
    test24BL_dianshuSongXinTai = [By.XPATH,
                                  "//div[contains(@class,'menuable__content__active')]//a/div"];
    test24BL_jianZhi = [By.XPATH,
                        "//label[text()='建値']/..//input"];
    test24BL_dianJianZhi = [By.XPATH,
                            "//div[contains(@class,'menuable__content__active')]//a/div"];
    test24BL_tongHuo = [By.XPATH,
                        "//label[text()='通貨']/..//input"];
    test24BL_dianTongHuo = [By.XPATH,
                            "//div[contains(@class,'menuable__content__active')]//a/div"];

    test24BL_dianJiEtdShuRuKuang = [By.XPATH,
                                    "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']"];
    test24BL_dianJiEtdRiQi = [By.XPATH,
                              "//div[@class='v-picker__body theme--light']//tbody//div[contains(text(), '20日')]/.."];
    test24BL_dianJiBaoCun = [By.XPATH,
                             "//a[contains(text(), 'SYTC I/V Upload template')]/../button[1]"];
    test24BL_jieGuo = [By.XPATH,
                       "//div[contains(text(), 'INV番号はすでに存在しています。')]"];
    test24BL_dianJiQueDing = [By.XPATH,
                              "//div[contains(text(), '確定') and @class='v-btn__content']/.."];

    # test25
    test25BL_shiBeiFanHao = [By.XPATH,
                             "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[5]//input[@placeholder='識別番号']"];
    test25BL_cartonStartNo = [By.XPATH,
                              "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[6]//input"];
    test25BL_cartonEndNo = [By.XPATH,
                            "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[7]//input"];
    test25BL_NW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input"];
    test25BL_GW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input"];
    test25BL_M3 = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input"];
    test25BL_xuanZhePackageList = [By.XPATH,
                                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test25BL_zongLiangDengLu = [By.XPATH,
                                "//div[@class='mt-2 v-card theme--light'][3]//button[3]"];
    test25BL_queDing = [By.XPATH,
                        "//div[contains(text(),'確定') and @class='v-btn__content']/.."];
    test25BL_ivNO = [By.XPATH,
                        "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V NO']"];
    test25BL_dianJiIvNORiQiShuRuKuang = [By.XPATH,
                        "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='I/V作成日']"];
    test25BL_dianJiIvNORiQi = [By.XPATH,
                        "//div[@class='v-picker__body theme--light']//tbody//div[contains(text(), '17日')]/.."];\


    test25BL_shuSongXinTai = [By.XPATH,
                               "//label[text()='輸送形態']/..//input"];
    test25BL_dianshuSongXinTai = [By.XPATH,
                               "//div[contains(@class,'menuable__content__active')]//a/div"];
    test25BL_jianZhi = [By.XPATH,
                        "//label[text()='建値']/..//input"];
    test25BL_dianJianZhi = [By.XPATH,
                        "//div[contains(@class,'menuable__content__active')]//a/div"];
    test25BL_tongHuo = [By.XPATH,
                        "//label[text()='通貨']/..//input"];
    test25BL_dianTongHuo = [By.XPATH,
                        "//div[contains(@class,'menuable__content__active')]//a/div"];


    test25BL_dianJiEtdShuRuKuang = [By.XPATH,
                        "//div[@class='mt-2 v-card theme--light'][1]//input[@aria-label='ETD']"];
    test25BL_dianJiEtdRiQi = [By.XPATH,
                        "//div[@class='v-picker__body theme--light']//tbody//div[contains(text(), '20日')]/.."];
    test25BL_dianJiBaoCun = [By.XPATH,
                              "//a[contains(text(), 'SYTC I/V Upload template')]/../button[1]"];
    test25BL_jieGuo = [By.XPATH,
                       "//div[contains(text(), '保存が完了しました。')]"];
    test25BL_dianJiQueDing = [By.XPATH,
                             "//div[contains(text(), '確定') and @class='v-btn__content']/.."];

    # test26
    test26BL_NW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input"];
    test26BL_GW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input"];
    test26BL_M3 = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input"];
    test26BL_xuanZhePackageList = [By.XPATH,
                                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test26BL_zongLiangDengLu = [By.XPATH,
                                "//div[@class='mt-2 v-card theme--light'][3]//button[3]"];
    test26BL_queDing = [By.XPATH,
                        "//div[contains(text(),'確定') and @class='v-btn__content']/.."];
    test26BL_jieGuo = [By.XPATH,
                       "//div[@class='mt-2 v-card theme--light'][3]//tbody//td[11]//input"];

    # test27
    test27BL_NW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[10]//input"];
    test27BL_GW = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[11]//input"];
    test27BL_M3 = [By.XPATH,
                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]/td[12]//input"];
    test27BL_xuanZhePackageList = [By.XPATH,
                                   "//div[@class='mt-2 v-card theme--light'][3]//tbody/tr[1]//div[@class='v-input--selection-controls__ripple']"];
    test27BL_zongLiangDengLu = [By.XPATH,
                                "//div[@class='mt-2 v-card theme--light'][3]//button[3]"];
    test27BL_queDing = [By.XPATH,
                        "//div[contains(text(),'確定') and @class='v-btn__content']/.."];
    test27BL_jieGuo = [By.XPATH,
                       "//div[@class='mt-2 v-card theme--light'][3]//tbody//td[12]//input"];





