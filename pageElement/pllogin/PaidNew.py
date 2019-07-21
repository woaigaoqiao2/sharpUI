"""
INV P/L登録模块中的有償新規
页面元素定位
"""
import datetime
from selenium.webdriver.common.by import By
import time
import random


class PaidNew(object):
    """
    INV P/L登録页面
    """
    # 工作台右侧第一步 INV P/L登録
    # INVPL_element = [By.XPATH, '//main//div[text()="INV P/L登録"]']
    INVPL_element = (By.XPATH, '//div[@class="flex nav xs6"][1]/div[1]')
    # INV P/L登録页面导航栏 有償新規
    Paid_element = [By.XPATH, '//button[@class="v-btn v-btn--small theme--light"][1]']
    # INV P/L登録页面导航栏 検索
    Search_element = [By.XPATH, '//button[@class="btn-search v-btn theme--light"]']
    # INV P/L登録页面导航栏 編集
    Edit_element = [By.XPATH, '//button[@class="v-btn v-btn--small theme--light"][3]']
    # 搜索条件的 I/V No
    SearchIV_element = [By.XPATH, '//input[@aria-label="I/V NO"]']
    # 搜索结果的 I/V No
    ResIV_element = [By.XPATH, '//div[contains(@class,"v-table__overflow")]//td[4]']
    # 搜索结果的 勾选框
    ResSel_element = [By.XPATH, '//main//div[contains(@class,"v-table__overflow")]//tbody//i/..']

    """
    有償新規页面
    """
    """INVOICE 详细"""
    # INVOICE详细下的 P/O で検出
    PODetection_element = [By.XPATH,
                           '//div[@class="mt-2 v-card theme--light"][2]//div[@class="v-card__actions"]/button[1]']
    # P/O で検出 的検索
    POSearch_element = [By.XPATH, '//div[@class="v-dialog v-dialog--active"]//div[@class="v-card__actions"]/button[1]']
    # 随机选择P/O
    i = random.randint(1, 20)
    POChoise_element = [By.XPATH, '//div[contains(@class,"t--active")]//tbody//tr[{}]//i/../div'.format(i)]
    # P/O で検出弹框的 使用
    POUse_element = [By.XPATH, '//div[@class="v-dialog v-dialog--active"]//div[@class="v-card__actions"]/button[2]']
    # INVOICE 详细的 商品数量
    PONum_element = [By.XPATH, '//input[@placeholder="商品の数"]']
    # INVOICE 详细的 商品数量删除
    PONumClear = [By.XPATH,'//div[contains(@class,"placeholder v-input")]//i']
    # INVOICE 详细 全选勾选框
    POAll_element = [By.XPATH, '//main//div[contains(@class,"mb-2 inline-edit")]//thead//i/..']
    # INVOICE 详细的 P/L登録
    PLReg_element = [By.XPATH, '//div[@class="mt-2 v-card theme--light"][2]//div[@class="v-card__actions"]/button[2]']
    # INVOICE 详细的 P/O NO 第一条
    PONO1st_element = [By.XPATH, '//div[contains(@class,"mb-2 inline-edit")]//tbody/tr[1]/td[2]']
    # INVOICE 详细的 社内品番(公司编号) 第一条
    POCoNum1st_element = [By.XPATH, '//div[contains(@class,"mb-2 inline-edit")]//tbody/tr[1]/td[4]']
    # INVOICE 详细的 品種 第一条
    POKind1st_element = [By.XPATH, '//div[contains(@class,"mb-2 inline-edit")]//tbody/tr[1]/td[5]']
    # INVOICE 详细的 数量 第一条
    PONum1st_element = [By.XPATH, '//tbody/tr[1]//input[@placeholder="商品の数"]']

    """Package List详细"""
    # Package List详细的 全选勾选框
    PLAll_element = [By.XPATH, '//main//div[contains(@class,"pb-2 inline-edit")]//thead//i']
    # Package List详细的 P/O NO 第一条
    PLPONo1st_element = [By.XPATH, '//main//div[contains(@class,"pb-2 inline-edit")]//tbody/tr[1]/td[2]']
    # Package List详细的 社内品番(公司编号) 第一条
    PLConNo1st_element = [By.XPATH, '//main//div[contains(@class,"pb-2 inline-edit")]//tbody/tr[1]/td[3]']
    # Package List详细的 品種 第一条
    PLKind1st_element = [By.XPATH, '//main//div[contains(@class,"pb-2 inline-edit")]//tbody/tr[1]/td[4]']
    # Package List详细的 数量 第一条
    PLNum1st_element = [By.XPATH, '//tbody/tr[1]//input[@placeholder="数量"]']
    # Package List详细的 識別番号(集装箱号)
    ConNo_element = [By.XPATH, '//input[@placeholder="識別番号"]']
    # Package List详细的 Carton Start No
    ConSt_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[6]//input']
    # Package List详细的 Carton End No
    ConEd_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[7]//input']
    # Package List详细的 入り数
    OneConNum_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[8]//input']
    # Package List详细的 数量
    Sum_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[9]//input']
    # Package List详细的 N/W
    ConNW_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[10]//input']
    # Package List详细的 G/W
    ConGW_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[11]//input']
    # Package List详细的 M3
    ConM3_element = [By.XPATH, '//div[contains(@class,"elevation-1 pb-2 inline-edit")]//td[12]//input']

    """INVOICE 基本情報"""
    # 下拉框第一条
    Select1st_element = [By.XPATH,
                         '//div[contains(@class,"content__active")]//div[(@class="v-list theme--light")]/div[1]']
    # 下拉框第二条
    Select2nd_element = [By.XPATH,
                         '//div[contains(@class,"content__active")]//div[(@class="v-list theme--light")]/div[2]']
    # INVOICE 基本情報的 I/V No
    IVNo_element = [By.XPATH, '//label[text()="I/V NO"]/../input']
    # 当前日期 "日"
    time = datetime.datetime.now().timetuple()
    today = time.tm_mday
    # INVOICE 基本情報的 I/V作成日选择
    IVCraDateChoose_element = [By.XPATH, '//label[text()="I/V作成日"]/../input']
    # INVOICE 基本情報的 I/V作成日 具体时间
    IVCraDay_element = [By.XPATH, '//div[text()="{}日"]'.format(today)]
    IVClear_element = [By.XPATH, '//label[text()="I/V NO"]/../..//i']
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
    # Market_element = [By.XPATH, '//label[text()="建値"]/..//div[contains(@class,"icon--append")]']
    Market_element = [By.XPATH, '//label[text()="建値"]/../input']
    MarketClear_element = [By.XPATH, '//label[text()="建値"]/..//i']
    # INVOICE 基本情報的 建値中 FCA货交承运人(适用于任何运输方式)
    FCA_element = [By.XPATH, '//div[text()="FCA"]/..']
    # INVOICE 基本情報的 建値中 FOB船上交货价(仅适用内河和海洋运输)
    FOB_element = [By.XPATH, '//div[text()="FOB"]/..']
    # INVOICE 基本情報的 通貨
    Currency_element = [By.XPATH, '//label[text()="通貨"]/../input']
    # 输入货币
    SendCur_element = [By.XPATH, '//div[contains(@class,"menuable__content__active")]//a/div']

    """P/L登録"""
    # P/L登録的 保存
    PaidSave_element = [By.XPATH, '//main//div[@class="v-btn__content" and contains(text(),"保存")]']
    # 隐藏的保存
    PaidSaveDis_element = [By.XPATH, '//main//div[text()="保存"]/..']

    """有償新規订单保存成功"""
    # 保存成功 確定
    PaidSaveSuc_element = [By.XPATH, '//div[text()="確定"]']
    # 保存成功 返回信息 保存が完了しました。
    PaidCompletedSave_element = [By.XPATH, '//div[contains(@class,"justify")]/../div[contains(@class,"text-xs")]']
    # 点击保存后的積出港・陸揚港确认信息
    dpupinf = [By.XPATH, '//div[contains(@class,"v-dialog v-dialog--active")]//div[contains(@class,"text-xs")]']
    # 積出港・陸揚港确认信息的确定键
    dpupConf = [By.XPATH, '//div[contains(@class,"v-dialog--active")]//div[@class="v-card__actions"]/button[1]']


if __name__ == '__main__':
    time = datetime.datetime.now().timetuple()
    today = time.tm_mday
    # print(f'//div[text()="{today}日"]')
