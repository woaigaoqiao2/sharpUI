'''
Created on 2019年5月20日

@author: chinasoft.cjp
SA登查询面元素对象
'''


from selenium.webdriver.common.by import By

class SaSearch():
    # S/A登录
    SA_button_element = [By.XPATH, '//main//div[contains(text(),"S/A登録")]/..']
    # 検索
    search_element = [By.XPATH, '//div[text()="検索"]/..']
    # 新規
    newlyBuilt_element = [By.XPATH, '//a[@class="ml-2 v-btn v-btn--router theme--light"]']
    # 编集
    edit_element = [By.XPATH, '//div[text()="編集"]/..']
    # 参照新規作成
    reference_new_building = [By.XPATH, '//div[text()="参照新規作成"]/..']

    # ETD开始日
    ETD_start_date_element = [By.XPATH, '//input[@aria-label="ETD"]']
    # ETD结束日
    ETD_end_date_element = [By.XPATH, '//div[@label="ETD"]/../..//input[@aria-label="~"]']

    # 依赖日开始
    Yai_start_date_element = [By.XPATH, '//input[@aria-label="依頼日"]']
    # 依赖日结束
    Yai_end_date_element = [By.XPATH, '//div[@label="依頼日"]/../..//input[@aria-label="~"]']



    # invoiceNo
    InvoiceNo = [By.XPATH, '//input[@aria-label="Invoice No"]']
    #Vol NO
    VolNO=[By.XPATH, '//input[@aria-label="Vol NO"]']
    # 本船名
    benchuan = [By.XPATH, '//input[@aria-label="本船名"]']
    # 船社
    ShippingShe = [By.XPATH, '//input[@aria-label="船社・航空会社"]']


    # 海外取引先下拉框
    haiwaiquyinxian_element = (By.XPATH, '//input[@aria-label="海外取引先" and @type="text"]')

    # 责出港
    ZheChu_element=(By.XPATH, '//input[@aria-label="積出港" and @type="text"]')

    # 陸揚港
    LuYang_element = (By.XPATH, '//input[@aria-label="陸揚港" and @type="text"]')

    xingtai_element = (By.XPATH, '//input[@aria-label="輸送形態" and @type="text"]//..')

    # 形态值 SEA
    sea_element = (By.XPATH, '//div[@class="v-list__tile__title" and contains(text(),"SEA")]')

    # 搜索结果
    SA_jieGuo = [By.XPATH, '//main//div[@class="v-table__overflow"]//tbody']
    # 参照新規作成
    reference_new_building_element = [By.XPATH,'//div[text()="参照新規作成"]/..']
    # 海外取引先
    overseas_customers_element = [By.XPATH,'//input[@aria-label="海外取引先"]']
    # B/L NO
    BL_NO_element = [By.XPATH,'//input[@aria-label="B/L NO"]']
    # 当前页面数据的B/L NO获取
    BL_NO_elements = [By.XPATH,'//main//table/tbody/tr/td[5]']
    # B/L发行开始日
    BL_issuance_start_date_element = [By.XPATH,'//input[@aria-label="B/L発行日"]']
    # B/L发行结束日
    BL_issuance_end_date_element = [By.XPATH,'//main//div[@label="B/L発行日"]/../..//input[@aria-label="~"]']
    # 开始日期按钮
    start_date_element = [By.XPATH,'//div[contains(@class,"active")]//div[text()="1日"]/..']
    # 结束日期按钮
    end_date_element = [By.XPATH,'//div[contains(@class,"active")]//div[text()="2日"]/..']
    # 当前页面数据的B/L发行日获取
    BL_Issuance_Date_elements = [By.XPATH,'//main//table/tbody/tr/td[10]']
    # ETA开始日
    ETA_start_date_element = [By.XPATH,'//input[@aria-label="ETA"]']
    # ETA结束日
    ETA_end_date_element = [By.XPATH,'//div[@label="ETA"]/../..//input[@aria-label="~"]']


