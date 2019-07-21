from selenium.webdriver.common.by import By
import datetime
import random

class Location(object):

    #公用
    INVpldenglu = [By.XPATH,"//div[@class='flex nav xs6'][1]/div[1]"]

    #INV P/L登録
    JianSuo = [By.XPATH,"//div[@class='application--wrap']//div[@class='v-card__actions']/button[1]"]
    YouChangXinGui = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='v-card__actions']/button[2]"]
    WuChangXinGui = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='v-card__actions']/button[3]/div"]

    #有偿新规》INVP/L登录
    YBaoCun = [By.XPATH,"//*[@id='app']/div[22]/main/div/div[1]/div[1]/div[2]/button[1]/div"]
    YGuanBi = [By.XPATH,"//div[@class='v-content__wrap']//div//div[text()='戻る']/.."]

    #有偿新规》INVOICE详细
    YPOJianChu = [By.XPATH,"//div[@class='v-content__wrap']/div/div[3]//div[@class='v-card__actions']/button[1]"]
    YPLDengLu = [By.XPATH,"//div[@class='v-content__wrap']/div/div[3]//div[@class='v-card__actions']/button[2]"]
    YINXiaoChu = [By.XPATH,"//div[@class='elevation-1 mt-2 mb-2 inline-edit']/..//div//button[3]"]

    #有偿新规》PackageList详细
    PLXiaoChu = [By.XPATH,"//div[@class='elevation-1 pb-2 inline-edit']/..//div[@class='v-card__actions']/button[2]/div"]

    #无偿新规》INVP/L登录
    WBaoCun = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='v-card theme--light']/div[2]/button[1]"]
    WGuanBi = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='v-card theme--light']/div[2]/button[3]"]

    #无偿新规》INVOICE 详细
    WuChangShangPinZhuiJia = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='v-card theme--light']/../div[3]/div[2]/button[1]"]
    WplDengLu = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='v-card theme--light']/../div[3]/div[2]/button[2]"]
    WXiaoChu = [By.XPATH,"//div[@class='elevation-1 mt-2 mb-2 inline-edit']/..//button[3]"]

    #无偿新规》PackageList详细
    WplXiaoChu = [By.XPATH,"//div[@class='elevation-1 mt-2 mb-2 inline-edit']/../../div[4]/div[2]/button[2]"]



    #test15
    test15BL_shangpinzhuijia = [By.XPATH," //*[@id='app']/div[19]/main/div/div[1]/div[3]/div[2]/button[1]/div"]
    test15BL_jiansuo = [By.XPATH,"//*[@id='app']/div[3]/div/div/div[2]/button[1]/div"]
    #选择第一条数据
    test15BL_shuju = [By.XPATH,"//div[contains(@class,'v-dialog--active')]//tbody/tr[1]//i/.."]
    test15BL_shiyong = [By.XPATH,"//div[contains(@class,'v-dialog--active')]//div/div[2]/button[2]/div[1]"]
    #添加商品后的社内品番
    test15BL_insheneipinfan = [By.XPATH,"//div[@class='elevation-1 mt-2 mb-2 inline-edit']//table/tbody/tr/td[4]"]
    #FOB单价
    test15BL_danjia = [By.XPATH,"//div[contains(@class,'v-table__overflow')]//table/tbody[1]/tr/td[7]//input"]
    test15BL_shuliang = [By.XPATH,"//div[contains(@class,'v-table__overflow')]//table/tbody[1] /tr/td[8] //input "]
    test15BL_xuanze = [By.XPATH,"//*[@id='app']/div[20]/main/div/div[1]/div[3]/div[3]/div[1]/table/tbody/tr/td[1]/div/div/div"]
    # test15BL_PLdenglu = [By.XPATH,"//div[text()='P/L登録']/.."]
    #P/L登录后的社内品番
    test15BL_sheneipinfan = [By.XPATH,"//div[@class='elevation-1 pb-2 inline-edit']//table/tbody/tr/td[3]"]

    #test16
    #Carton Start NO
    test16BL_csn = [By.XPATH,"//div[contains(@class,'v-table__overflow')]/table[1]/tbody/tr[1]/td[6]//input"]
    #Carton End No
    test16BL_cen = [By.XPATH,"//*[@id='app']/div[20]/main/div/div[1]/div[4]/div[3]/div[1]/table/tbody/tr/td[7]//div[1]/div[1]/input"]

    #test17
    #识别番号
    test17BL_shibiefanhao = [By.XPATH,"//div[contains(@class,'elevation-1 pb-2 inline-edit')]//tbody/tr/td[5]//input"]
    #入数
    test17BL_rushu = [By.XPATH,"//div[contains(@class,'elevation-1 pb-2 inline-edit')]//tbody/tr/td[8]//input"]

    #test18
    #INVOICE详细 削除
    test18BL_xiaochu = [By.XPATH,"//div[@class='elevation-1 mt-2 mb-2 inline-edit']/..//button[3]"]
    test18BL_xuanzeshuju = [By.XPATH,"//div[contains(@class,'v-dialog--active')]//tbody/tr[1]/td/div/div"]
    #是否先出
    test18BL_shifouxiaoshu = [By.XPATH,"//div[@class='v-dialog v-dialog--active']//div[text()='はい']"]
    #确认消除
    test18BL_querenxiaochu = [By.XPATH,"//div[@class='v-dialog v-dialog--active']//div[3]/button[1]"]
    #Actual_result
    test18BL_actual_result = [By.XPATH,"//div[text()='削除成功しました。']"]

    #test19
    #无偿商品登录行追加
    test19BL_shangpinzhuijia = [By.XPATH,"//*[@id='app']/div[19]/main/div/div[1]/div[3]/div[2]/button[1]/div"]
    #检索
    test19BL_jiansuo = [By.XPATH,"//*[@id='app']/div[4]/div/div/div[2]/button[1]/div"]
    #选择第一条数据
    test19BL_xuanzeshuju = [By.XPATH,"//div[contains(@class,'v-dialog v-dialog--active')]//tbody/tr[1]//i/.."]
    #使用
    test19BL_shiyong = [By.XPATH,"//div[contains(@class,'v-dialog--active')]//div/div[2]/button[2]/div[1]"]
    #FOB单价
    test19BL_danjia = [By.XPATH,"//div[contains(@class,'v-table__overflow')]//table/tbody[1]/tr/td[7]//input"]
    #数量
    test19BL_shuliang = [By.XPATH,"//div[contains(@class,'v-table__overflow')]//table/tbody[1]/tr/td[8]//input"]
    #数据选择
    test19BL_shujuxuanze = [By.XPATH,"//*[@id='app']/div[20]/main/div/div[1]/div[3]/div[3]/div[1]/table/tbody/tr/td[1]/div/div/div/div/div"]
    #P/L登录
    # test19BL_denglu = [By.XPATH,"//div[text()='P/L登録']/.."]
    #Package List详细中数据选择
    test19BL_PLxuanze = [By.XPATH,"//div[contains(@class,'elevation-1 pb-2 inline-edit')]//tbody/tr[1]//i//../div"]
    #Package Lise详细 削出
    # test19BL_xiaochu = [By.XPATH,"//div[contains(@class,'pb-2')]/..//div[text()='削除']/.."]

    #test20
    #选择一个商品
    test20BL_suijixuanzeshangpin = [By.XPATH,"//div[contains(@class,'v-dialog v-dialog--active')]//tbody/tr[1]//i/.."]
    #INVOICE详细中选择数据
    test20BL_shujuxuanze = [By.XPATH,"//*[@id='app']/div[20]/main/div/div[1]/div[3]/div[3]/div[1]/table/tbody/tr/td[1]/div/div/div/div/div"]
    #识别番号
    test20BL_shibiefanhao = [By.XPATH,"//div[@class='elevation-1 pb-2 inline-edit']//table/tbody/tr[1]/td[5]//input"]
    #Carton Start No
    test20BL_csn = [By.XPATH,"//div[contains(@class,'elevation-1 pb-2 inline-edit')]//table//tbody/tr/td[6]/div/div/div[1]/div[1]/input"]
    #Carton End NO
    test20BL_cen = [By.XPATH,"//div[contains(@class,'elevation-1 pb-2 inline-edit')]//table//tbody/tr/td[7]/div/div/div[1]/div[1]/input"]
    #NW
    test20BL_nw = [By.XPATH,"//div[contains(@class,'elevation-1 pb-2 inline-edit')]//table//tbody/tr/td[10]/div/div/div[1]/div[1]/input"]
    #GW
    test20BL_gw = [By.XPATH,"//div[contains(@class,'elevation-1 pb-2 inline-edit')]//table//tbody/tr/td[11]/div/div/div[1]/div[1]/input"]
    #M3
    test20BL_mt = [By.XPATH,"//div[contains(@class,'elevation-1 pb-2 inline-edit')]//table//tbody/tr/td[12]/div/div/div[1]/div[1]/input"]
    #海外去引先
    test20BL_haiwaiquyinxian = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='layout row wrap']//div[@class='flex xs3'][1]//input"]
    test20BL_quyinxiandianji = [By.XPATH,"//div[@class='v-menu__content theme--light menuable__content__active v-autocomplete__content']//a"]
    #I/V NO
    test20BL_ivno = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='layout row wrap']//div[@class='flex xs3'][2]//input"]
    #积出港
    test20BL_jichugang = [By.XPATH, "//div[@class='v-content__wrap']//div[@class='layout row wrap']//div[@class='flex xs3'][4]//input"]
    test20BL_jichugangdianji = [By.XPATH,'//span[@class="v-list__tile__mask"]']
    #输送形态
    test20BL_shusongxintai = [By.XPATH,"//div[@class='v-input v-text-field v-select theme--light']//input/.."]
    test20BL_shusongxintaixuanze = [By.XPATH,"//div[text()='AIR']/.."]

    #建值
    test20BL_jianzhi = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='layout row wrap']//div[@class='flex xs3'][6]//input"]
    test20BL_jianzhidianji = [By.XPATH,"//div[contains(@class,'menuable__content__active ')]//div[@class='v-list__tile__title']"]
    #陆扬港
    test20BL_luyanggang = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='layout row wrap']//div[@class='flex xs3'][7]//input"]
    test20BL_luyanggangdianji = [By.XPATH,"//*[@id='app']/div[6]/div/div/div/a/div/div"]
    #通货
    test20BL_tonghuo = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='layout row wrap']//div[@class='flex xs3'][8]//input"]
    test20BL_tonghuodianji = [By.XPATH,"//*[@id='app']/div[5]/div/div/div/a/div/div"]
    #I/V作成日
    test20BL_ivdianji = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='layout row wrap']//div[@class='flex xs3'][3]//input"]
    time = datetime.datetime.now().timetuple()
    today = time.tm_mday
    test20BL_ivday = [By.XPATH,'//div[text()="{}日"]'.format(today)]
    #ETD
    test20BL_etd = [By.XPATH,"//input[@aria-label='ETD']"]
    time = datetime.datetime.now().timetuple()
    etdday = time.tm_mday
    test20BL_etdday = [By.XPATH,'//div[text()="{}日"]'.format(etdday)]
    #保存
    # test20BL_baocun = [By.XPATH,"//div[contains(@class,'v-content__wrap')]//div[text()='保存']"]
    test20BL_quedingbaocun = [By.XPATH,"//div[contains(@class,'v-dialog__content--active')]//div[@class='v-card__actions justify-center']//button"]
    # test20BL_guanbi = [By.XPATH,"//div[@class='application--wrap']//main[@class='v-content']//div[text()='戻る']/.."]

    #test21
    #检索
    test21BL_jiansuo = [By.XPATH,"//div[@class='application--wrap']//main//div[@class='v-card__actions']/button[1]"]
    #数据选择
    test21BL_xuanze = [By.XPATH,"//div[contains(@class,'elevation-0')]//tbody/tr[1]/td[1]/div/div/div"]
    #编集
    test21BL_bianji = [By.XPATH,"//div[@class='application--wrap']//main//div[@class='v-card__actions']/button[4]"]
    #通货下拉按钮
    test21BL_tonghuoanniu = [By.XPATH,"//input[@aria-label ='通貨']/../div[2]//i"]
    #通货选择
    test21BL_tonghuoxuanze = [By.XPATH,"//div[text()='GBP']"]
    #保存
    test21BL_baocun = [By.XPATH,"//*[@id='app']/div[20]/main/div/div[1]/div[1]/div[2]/button[1]/div"]
    #保存提示框的内容
    test21BL_tishineirong = [By.XPATH,"//div[@class='v-dialog v-dialog--active']/div//div[text()='保存が完了しました。']"]

    #test22
    #建值下拉框按钮
    test22BL_jianzhianniu = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='layout row wrap']//div[@class='flex xs3'][6]//input"]
    #建值选择
    test22BL_jianzhixuanze = [By.XPATH,"//div[text()='FCA']"]

    #test23
    #戻る
    test23BL_guanbi = [By.XPATH,"//*[@id='app']/div[20]/main/div/div[1]/div[1]/div[2]/button[3]/div"]

    #test24
    #有偿新规
    # test24BL_youchangxingui = [By.XPATH,"//div[text()='有償新規']/.."]
    #P/O で検出
    # test24BL_pojianchu = [By.XPATH,"//div[text()='P/O で検出']/.."]
    #検索
    test24BL_jiansuo = [By.XPATH,"//div[@class='v-dialog v-dialog--active']//div[@class='v-card__actions']/button[1]"]
    #随机取一个商品
    a = random.randint(1,20)
    test24BL_suijixuanze = [By.XPATH,"//div[contains(@class,'v-dialog v-dialog--active')]//table/tbody/tr[{}]//div[contains(@class,'v-input__slot')]".format(a)]
    #使用
    test24BL_shiyong = [By.XPATH,"//div[@class='v-dialog__content v-dialog__content--active']//div[@class='v-card__actions']/button[2]"]
    #输入数量
    test24BL_shurushuliang = [By.XPATH,"//div[@class='v-content__wrap']//table/tbody/tr/td[8]//input"]
    #数据选择
    test24BL_shujuxuanze = [By.XPATH,"//td[@class='td-cb']//input[@aria-checked='false']/../.."]
    #P/L登录
    # test24BL_pldenglu = [By.XPATH,"//div[text()='P/L登録']/.."]
    #识别番号、Carton Start No、Carton End No、入数、N/W 、G/W 、M3
    test24BL_shibiefanhao = [By.XPATH,"//input[@placeholder='識別番号']"]
    test24BL_CartonStartNo = [By.XPATH,"//div[@class='elevation-1 pb-2 inline-edit']//table//tbody/tr/td[6]/div/div/div[1]/div[1]/input"]
    test24BL_CartonEndNo = [By.XPATH,"//div[@class='elevation-1 pb-2 inline-edit']//table//tbody/tr/td[7]/div/div/div[1]/div[1]/input"]
    test24BL_nw = [By.XPATH,"//div[@class='elevation-1 pb-2 inline-edit']//table//tbody/tr/td[10]/div/div/div[1]/div[1]/input"]
    test24BL_gw = [By.XPATH,"//div[@class='elevation-1 pb-2 inline-edit']//table//tbody/tr/td[11]/div/div/div[1]/div[1]/input"]
    test24BL_m3 = [By.XPATH,"//div[@class='elevation-1 pb-2 inline-edit']//table//tbody/tr/td[12]/div/div/div[1]/div[1]/input"]
    #IV/no
    test24BL_IVNO = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='flex xs3'][2]//input"]
    #I/V作成日
    test24BL_ivzuochengri = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='flex xs3'][3]//input"]
    time = datetime.datetime.now().timetuple()
    ivtoday = time.tm_mday
    test24BL_ivday = [By.XPATH,'//div[text()="{}日"]'.format(ivtoday)]

    #ETD
    test24BL_etd = [By.XPATH,"//div[@class='v-content__wrap']//div[@class='flex xs3'][9]//input"]
    time = datetime.datetime.now().timetuple()
    etdday = time.tm_mday
    test24BL_etdday = [By.XPATH,'//div[text()="{}日"]'.format(etdday)]
    #保存
    test24BL_baocun = [By.XPATH,"//*[@id='app']/div[22]/main/div/div[1]/div[1]/div[2]/button[1]/div"]
    #保存后点击确定
    test24BL_queren = [By.XPATH,"//div[text()='確定']/.."]
    #确定后关闭页面
    test24BL_guanbi = [By.XPATH,"//div[@class='v-content__wrap']//div//div[text()='戻る']/.."]
    #检索条件I/V NO
    test24BL_jiansuotiaojianIVNO = [By.XPATH,"//input[@aria-label='I/V NO']"]
    #检索
    test24BL_JIANSUO = [By.XPATH,"//div[text()='検索']/.."]
    #查询出的I/V NO
    test24BL_chaxunIVno = [By.XPATH,"//div[@class='v-content__wrap']//table/tbody/tr/td[4]"]

    #test25
    b=random.randint(1,5)
    test25BL_suijixuanze = [By.XPATH,"//div[contains(@class,'v-dialog v-dialog--active')]//tbody/tr[1]//i/..".format(b)]
    #test27
    test27BL_yunshuxintaiqingchu = [By.XPATH,"//label[text()='輸送形態']/../div[2]//i"]



