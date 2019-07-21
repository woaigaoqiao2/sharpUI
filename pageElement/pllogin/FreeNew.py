"""
INV P/L登録模块中的无償新規
页面元素定位
"""
import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import random


class FreeNew(object):
    """
    INV P/L登録页面
    """
    # 工作台右侧第一步 INV P/L登録
    INVPL_element = [By.XPATH, '//div[@class="flex nav xs6"][1]/div[1]']
    # INV P/L登録页面导航栏 無償新規
    Free_element = [By.XPATH, '//div[@class="v-content__wrap"]//div[@class="v-card theme--light"]//button[3]']
    # INV P/L登録页面导航栏 検索
    Search_element = [By.XPATH, '//button[@class="btn-search v-btn theme--light"]']
    # 搜索条件的 I/V No
    SearchIV_element = [By.XPATH, '//input[@aria-label="I/V NO"]']
    # 搜索结果的 I/V No
    ResIV_element = [By.XPATH, '//div[contains(@class,"v-table__overflow")]//td[4]']

    """
    無償新規页面
    """
    """INVOICE 详细"""
    # INVOICE详细下的 無償商品登録行追加
    POAdd_element = [By.XPATH, '//div[@class="mt-2 v-card theme--light"][2]//button[1]']
    POSearch_element = [By.XPATH, '//div[@class="v-dialog v-dialog--active"]//div[@class="v-card__actions"]/button[1]']
    # 随机选择一个無償商品
    i = random.randint(1, 5)
    # POChoiseOne_element = [By.XPATH, '//div[contains(@class,"content--active")]//tbody//tr[{}]//i/../div'.format(i)]
    POChoiseOne_element = [By.XPATH, '//div[contains(@class,"content--active")]//tbody//tr[{}]//input'.format(i)]
    # 随机选择二个無償商品
    i = random.sample(range(1, 6), 2)
    First = i[0]
    second = i[1]
    # POChoise1st_element = [By.XPATH, '//div[contains(@class,"content--active")]//tbody//tr[{}]//i/../div'.format(First)]
    POChoise1st_element = [By.XPATH, '//div[contains(@class,"content--active")]//tbody//tr[{}]//input'.format(First)]
    # POChoise2nd_element = [By.XPATH, '//div[contains(@class,"content--active")]//tbody//tr[{}]//i/../div'.format(second)]
    POChoise2nd_element = [By.XPATH, '//div[contains(@class,"content--active")]//tbody//tr[{}]//input'.format(second)]
    # 無償商品登録行追加的 使用
    POUse_element = [By.XPATH, '//div[contains(@class,"content--active")]//div[text()="使用"]']
    # INVOICE 详细 全选勾选框
    POAll_element = [By.XPATH, '//main//div[contains(@class,"mb-2 inline-edit")]//thead//i/..']
    # INVOICE 详细的 P/L登録
    PLReg_element = [By.XPATH, '//div[@class="mt-2 v-card theme--light"][2]//div[@class="v-card__actions"]/button[2]']
    # INVOICE 详细的 FOB単価
    FOBPrice_element = [By.XPATH, '//tbody/tr[1]//input[@placeholder="FOB単価"]']
    # INVOICE 详细的 社内品番(公司编号) 第一条
    POCoNum1st_element = [By.XPATH, '//div[contains(@class,"mb-2 inline-edit")]//tbody/tr[1]/td[4]']
    # INVOICE 详细的 品種 第一条
    POKind1st_element = [By.XPATH, '//div[contains(@class,"mb-2 inline-edit")]//tbody/tr[1]/td[5]']
    # INVOICE 详细的 数量 第一条
    PONum1st_element = [By.XPATH, '//tbody/tr[1]//input[@placeholder="商品の数"]']
    # INVOICE 详细的 社内品番(公司编号) 第二条
    POCoNum2nd_element = [By.XPATH, '//div[contains(@class,"mb-2 inline-edit")]//tbody/tr[2]/td[4]']
    # INVOICE 详细的 品種 第二条
    POKind2nd_element = [By.XPATH, '//div[contains(@class,"mb-2 inline-edit")]//tbody/tr[2]/td[5]']
    # INVOICE 详细的 数量 第二条
    PONum2nd_element = [By.XPATH, '//tbody/tr[2]//input[@placeholder="商品の数"]']
    # INVOICE 详细的 隐藏的削除
    PODelDis_element = [By.XPATH, '//span[(text()="INVOICE 详细")]/../..//div[text()="削除"]/..']

    """Package List详细"""
    # Package List详细的 全选勾选框
    PLAll_element = [By.XPATH, '//main//div[contains(@class,"pb-2 inline-edit")]//thead//i/..']
    # Package List详细的 社内品番(公司编号) 第一条
    PLConNo1st_element = [By.XPATH, '//main//div[@class="elevation-1 pb-2 inline-edit"]//tbody/tr[1]/td[3]']
    # Package List详细的 品種 第一条
    PLKind1st_element = [By.XPATH, '//main//div[contains(@class,"pb-2 inline-edit")]//tbody/tr[1]/td[4]']
    # Package List详细的 数量 第一条
    PLNum1st_element = [By.XPATH, '//tbody/tr[1]//input[@placeholder="数量"]']
    # Package List详细的 社内品番(公司编号) 第二条
    PLConNo2nd_element = [By.XPATH, '//main//div[contains(@class,"pb-2 inline-edit")]//tbody/tr[2]/td[3]']
    # Package List详细的 品種 第二条
    PLKind2nd_element = [By.XPATH, '//main//div[contains(@class,"pb-2 inline-edit")]//tbody/tr[2]/td[4]']
    # Package List详细的 数量 第二条
    PLNum2nd_element = [By.XPATH, '//tbody/tr[2]//input[@placeholder="数量"]']
    # Package List详细的 No data available
    PLNoData_element = [By.XPATH, '//main//td[text()="No data available"]']
    # Package List详细的 識別番号(集装箱号)
    ConNo_element = [By.XPATH, '//input[@placeholder="識別番号"]']
    # Package List详细的 Carton Start No
    ConSt_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[6]//input']
    # Package List详细的 Carton End No
    ConEd_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[7]//input']
    # Package List详细的 入り数
    OneConNum_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[8]//input']
    # Package List详细的 N/W
    ConNW_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[10]//input']
    # Package List详细的 G/W
    ConGW_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[11]//input']
    # Package List详细的 M3
    ConM3_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[12]//input']
    # Package List详细的 隐藏的削除
    PLDelDis_element = [By.XPATH, '//span[(text()="Package List详细")]/../..//div[text()="削除"]/..']

    """INVOICE 基本情報"""
    # INVOICE 基本情報的 海外取引先(海外客户)
    OverseasCus_element = [By.XPATH, '//label[text()="海外取引先"]/..//div[contains(@class,"icon--append")]']
    # 下拉框第一条
    Select1st_element = [By.XPATH,
                         '//div[contains(@class,"content__active")]//div[(@class="v-list theme--light")]/div[1]']
    # 下拉框第二条
    Select2nd_element = [By.XPATH,
                         '//div[contains(@class,"content__active")]//div[(@class="v-list theme--light")]/div[2]']
    # 下拉框输入后的提示
    SendTip_element = [By.XPATH, '//div[contains(@class,"menuable__content__active")]//a/div']
    # INVOICE 基本情報的 I/V No
    IVNo_element = [By.XPATH, '//label[text()="I/V NO"]/../input']
    # INVOICE 基本情報的 I/V No. 超过7位的提示信息
    IVExceedTips_element = [By.XPATH, '//div[text()="INV.Noは7桁以内でご記入ください。"]']
    # 当前日期 "日"
    time = datetime.datetime.now().timetuple()
    today = time.tm_mday
    # INVOICE 基本情報的 I/V作成日选择
    IVCraDateChoose_element = [By.XPATH, '//label[text()="I/V作成日"]/../input']
    # INVOICE 基本情報的 I/V作成日 具体时间
    IVCraDay_element = [By.XPATH, '//div[text()="{}日"]'.format(today)]
    # INVOICE 基本情報的 ETD(预计到港时间)选择
    ETD_element = [By.XPATH, '//label[text()="ETD"]/../input']
    # INVOICE 基本情報的 ETD 具体时间
    ETDChooseDay_element = [By.XPATH, '//div[text()="{}日"]'.format(today)]
    # INVOICE 基本情報的 積出港
    DeliveryPort_element = [By.XPATH, '//label[text()="積出港"]/../input']
    # INVOICE 基本情報的 陸揚港
    UnloadPort_element = [By.XPATH, '//label[text()="陸揚港"]/../input']
    # INVOICE 基本情報的 輸送形態
    TransForm_element = [By.XPATH, '//label[text()="輸送形態"]/..//div[contains(@class,"icon--append")]']
    # INVOICE 基本情報的 輸送形態中 Sea海运
    TransSea_element = [By.XPATH, '//div[text()="SEA"]/..']
    # INVOICE 基本情報的 輸送形態中 Air空运
    TransAir_element = [By.XPATH, '//div[text()="AIR"]/..']
    # INVOICE 基本情報的 建値
    Market_element = [By.XPATH, '//label[text()="建値"]/..//div[contains(@class,"icon--append")]']
    # INVOICE 基本情報的 建値中 FCA货交承运人(适用于任何运输方式)
    FCA_element = [By.XPATH, '//div[text()="FCA"]/..']
    # INVOICE 基本情報的 建値中 FOB船上交货价(仅适用内河和海洋运输)
    FOB_element = [By.XPATH, '//div[text()="FOB"]/..']
    # INVOICE 基本情報的 通貨
    Currency_element = [By.XPATH, '//label[text()="通貨"]/../input']

    """P/L登録"""
    # P/L登録的 保存
    FreeSave_element = [By.XPATH, '//main//div[text()="保存"]']
    # 隐藏的保存
    FreeSaveDis_element = [By.XPATH, '//main//div[text()="保存"]/../../button[@disabled="disabled"]']

    """有償新規订单保存成功"""
    # 保存成功 確定
    FreeSaveSuc_element = [By.XPATH, '//div[text()="確定"]']
    # 保存成功 返回信息 保存が完了しました。
    FreeCompletedSave_element = [By.XPATH, '//div[contains(@class,"justify")]/../div[contains(@class,"text-xs")]']


if __name__ == '__main__':
    # today = time.strftime("%d")
    # print(f'//div[text()="{today}日"]')
    # print(today)
    # print(random.sample(range(1, 6), 2))
    # print(random.randint(1, 5))
    pass
