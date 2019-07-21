from selenium.webdriver.common.by import By


class HomePageElement(object):
    
    
    # S/A登录
    # SA_button_element = [By.XPATH,'//main//div[text()="S/A登録"]']
    SA_button_element = [By.XPATH,'//div[text()="S/A 確定待ち"]/../../..']
    # 検索
    search_element = [By.XPATH,'//div[text()="検索"]/..']
    # 新規
    newlyBuilt_element = [By.XPATH,'//div[text()="新規"]']
    # 编集
    edit_element = [By.XPATH,'//div[text()="編集"]/..']
    # 参照新規作成
    reference_new_building_element = [By.XPATH,'//div[text()="参照新規作成"]/..']
    # 海外取引先
    overseas_customers_element = [By.XPATH,'//input[@aria-label="海外取引先"]']
    # B/L NO
    BL_NO_element = [By.XPATH,'//input[@aria-label="B/L NO"]']
    # 当前页面数据的B/L NO获取
    BL_NO_elements = [By.XPATH,'//main//tbody//td[5]']
    # B/L发行开始日
    BL_issuance_start_date_element = [By.XPATH,'//input[@aria-label="B/L発行日"]']
    # B/L发行结束日
    BL_issuance_end_date_element = [By.XPATH,'//main//div[@label="B/L発行日"]/../..//input[@aria-label="~"]']
    # B/L発行日上个月按钮
    BL_last_month_element = [By.XPATH,'//div[@label="B/L発行日"]//i[text()="chevron_left"]/../..']
    # B/L発行日上个月按钮
    BL_last_month_element2 = [By.XPATH,'//div[@label="~"]//i[text()="chevron_left"]/../..']
    # B/L発行日下个月按钮
    BL_next_month_element = [By.XPATH,'//div[@label="B/L発行日"]//i[text()="chevron_right"]/../..']
    # 开始日期按钮
    start_date_element = [By.XPATH,'//div[contains(@class,"active")]//div[text()="1日"]/..']
    # 结束日期按钮
    end_date_element = [By.XPATH,'//div[contains(@class,"active")]//div[text()="2日"]/..']
    # 当前页面数据的B/L发行日获取
    BL_Issuance_Date_elements = [By.XPATH,'//main//table/tbody/tr/td[11]']
    # ETA开始日
    ETA_start_date_element = [By.XPATH,'//input[@aria-label="ETA"]']
    # ETA结束日
    ETA_end_date_element = [By.XPATH,'//div[@label="ETA"]/../..//input[@aria-label="~"]']
    # ETA上个月按钮
    ETA_last_month_element = [By.XPATH,'//div[contains(@class,"active")]//i[text()="chevron_left"]/../..']
    # ETA下个月按钮
    ETA_next_month_element = [By.XPATH,'//div[contains(@class,"active")]//i[text()="chevron_right"]/../..']
    # 当前页面的ETA数据获取
    ETA_date_elements = [By.XPATH,'//main//table/tbody/tr/td[16]']
    # SA一時保存状态的数据
    temporary_preservation_elements = [By.XPATH,'//td[text()="SA一時保存"]/..//input']
    # SA登録済状态的数据
    registered_elements = [By.XPATH,'//td[text()="SA登録済"]/..//input']
    # 指示Mail送信済状态的数据
    instruction_sent_elements = [By.XPATH,'//td[text()="指示Mail送信済"]/..//input']
    # 翻页按钮
    next_page_element = [By.XPATH,'//main//button[@aria-label="Next page"]']


    #首页S/A登录
    SAElement = (By.XPATH,'//main[@class="v-content"]//div[text()="S/A登録"]')

    #BL提单号
    BLNoElement = (By.XPATH,'//input[@aria-label="B/L NO"]')

    #搜索按钮
    searchElement = (By.XPATH, '//main//div[@class="v-card theme--light"]//button[1]')

    #新規
    newRuleElement = (By.XPATH, '//div[text()="新規"]')

    #表头
    headElement = (By.XPATH,'//main//thead')

    #表内容
    contentElement =  (By.XPATH,'//main//tbody')

    #Carton Start No
    startNoElement = (By.XPATH,'//main//tbody//td[10]//input')

    #Carton end No
    endNoElement = (By.XPATH,'//main//tbody//td[11]//input')

    #Shipped Carton
    ShippedCartonElement = (By.XPATH,'//main//tbody//td[12]//input')

    #编辑按钮
    editElement = (By.XPATH, '//div[text()="編集"]')

    #一時保存按钮
    tempSaveElement = (By.XPATH, '//main//div[@class="v-card theme--light"]//button[1]')

    # 临时保存 确定按钮
    tempEnsureElement = (By.XPATH, '//div[@class="v-dialog v-dialog--active"]//button[1]')

    # 保存按钮
    saveElement = (By.XPATH, '//main//div[@class="v-card theme--light"]//button[2]')
    #确定保存
    ensureSaveElement = (By.XPATH, '//div[@class="v-dialog v-dialog--active"]//button[1]')
    #取消保存
    cancelSaveElement =(By.XPATH, '//div[@class="v-dialog v-dialog--active"]//button[2]')

    #取消按钮
    cancelElement = (By.XPATH, '//main//div[@class="v-card theme--light"]//button[4]')

    #确定送信按钮
    ensureLettersElement = (By.XPATH,'//main//div[@class="v-card theme--light"]//button[5]')

    #确定送信 确认发送按钮
    ensureSendElement = (By.XPATH,'//div[@class="v-dialog__content v-dialog__content--active"]//button')

    #如果没有有偿INV，我们就无法创造SA 弹框
    noINVElement = (By.XPATH,'//div[@class="v-dialog__content v-dialog__content--active"]//button')

    #运输信息 装运港清除键 其他运输信息div位置即可
    loadPortClearElement = (By.XPATH,'//main//div[@class="layout row wrap"]/div[6]//i')

    #运输信息 装运港清除键 其他运输信息div位置即可
    toPortClearElement = (By.XPATH,'//main//div[@class="layout row wrap"]/div[11]//i')


    #文件上传
    fileUploadElement = (By.XPATH,'//main//div[@class="v-card theme--light"]//button[6]')

    #文件上传INV P/L单选按钮
    INVPLradioElement = (By.XPATH,'//div[@role="radiogroup"]/div[1]//input')

    #文件上传B/L单选按钮
    BLradioElement = (By.XPATH,'//div[@role="radiogroup"]/div[2]//input')

    #文件上传S/A单选按钮
    SAradioElement = (By.XPATH, '//div[@role="radiogroup"]/div[3]//input')

    # 文件上传A/N单选按钮
    ANradioElement = (By.XPATH, '//div[@role="radiogroup"]/div[4]//input')

    #文件上传 按钮,input标签
    uploadElement = (By.XPATH,'//div[@class="v-card theme--light"]//div[@class="v-card__actions"]//input')

    #文件上传取消按钮
    uploadCancelElement = (By.XPATH,'//div[@class="v-dialog__content v-dialog__content--active"]//button')

    #文件上传完毕 关闭按钮
    closeBtnElement = (By.XPATH,'//div[@tabindex="-1"]//button[@class="v-btn v-btn--flat theme--light"]')



    # 打钩按钮
    checkElement = (By.XPATH, '//main//div[@class="v-input--selection-controls__ripple"]')

    #表第一条复选框
    fistCheckElement=(By.XPATH,'//main//tbody//tr[1]//div[@class="v-input--selection-controls__ripple"]')

    #INV P/L信息 第一条复选框
    INVFistCheckElement = (By.XPATH,'//main//tbody//tr[1]//div[@class="v-input--selection-controls__ripple"]')

    #INV P/L信息 P/O NO
    INVFistPoElement = (By.XPATH,'//main//tbody//tr[1]/td[5]')

    #INV PL 表 定位行
    tableTbodyElement = (By.XPATH,'//main//tbody')
    #INV PL表 定位列
    tableTheadElement = (By.XPATH,'//main//thead')
    #INV P表复选框 用for循环tr
    tableCheckboxElemet='//main//tbody//tr[]//input[@type="checkbox"]'

    #INV PL表勾选第一条数据
    fistINVDataElement = (By.XPATH,'//main//thead/tr[1]/th[1]//input')

    #分类按钮
    classifyElement = (By.XPATH,'//div[(text()="行分け")]')

    #取消行政分工
    cancelAdminElement = (By.XPATH,'//div[text()="行分け取り消し"]')

    #追加按钮
    addElement = (By.XPATH, '//main[@class="v-content"]//div[text()="追加"]')

    #对话框搜索按钮
    dialogSearchElement = (By.XPATH, '//div[@class="v-dialog v-dialog--active"]//div[text()="検索"]')

    #对话框追加
    dialogAddElement = (By.XPATH, '//div[@class="v-dialog v-dialog--active"]//div[text()="追加"]')

    #对话框表头
    dialogHeadElement = (By.XPATH,'//table/thead')

    #对话框表内容
    dialogContentElement = (By.XPATH,'//table/tbody')

    #对话框表的第一行数据
    firstDataElement = (By.XPATH,'//table/tbody/tr/td')


    #弹框提示装运港和陆卸港不一致
    inconformityElement = (By.XPATH,'//div[text()="S/Aの積出港・陸揚港とINVの積出港・陸揚港が不一致のため、再度確認してください"]')

    #弹框确定按钮
    enterElement = (By.XPATH,'//div[@class="v-dialog v-dialog--active"]//div[text()="確定"]')

    # 对话框下一页按钮
    dialogNextpageElement = (By.XPATH, '//div[@class="elevation-0"]//button[2]')

    # 输送形态
    conveyElement = (By.XPATH, '//main//div[@class="layout row wrap"]/div[9]//div[@class="v-select__selections"]')
    # SEA
    seaElement = (By.XPATH, '//div[@class="v-menu__content theme--light menuable__content__active"]//div[text()="SEA"]')
    # 有償INVが無いと、SAを作成できません。
    repet_element = [By.XPATH, '//div[text()="有償INVが無いと、SAを作成できません。"]']
    # 送信成功
    successElement = [By.XPATH, '//div[text()="SA送信成功しました。"]']

    # 资料填写不完整
    incompleteElement = [By.XPATH, '//div[text()="コンテナ情報が不完全です"]']
    # 确定
    sureElement = [By.XPATH, '//div[@class="v-dialog v-dialog--active"]//button[@class="v-btn theme--light"]']

    #inv资料填写不完整
    inv_incomplete_element = [By.XPATH,'//div[contains(text(),"INV P/L情報が不整備です、ご確認お願いします。")]']
        #确定按钮
    inv_sure_element = [By.XPATH,'//div[@class="v-dialog v-dialog--active"]//button']

    #INV PL 行定位
    inv_rows_element = [By.XPATH,'//main//table[@class="v-datatable v-table v-datatable--select-all theme--light"]/tbody']
    inv_col_element = [By.XPATH,'//main//table[@class="v-datatable v-table v-datatable--select-all theme--light"]/thead']
    #INV PL 具体单元格定位 tr代表行 td列
    INV_cell_element = [By.XPATH,'//table[@class="v-datatable v-table theme--light"]/tbody/tr[]/td[]']

    #datatable
    datatable_cell_element=[By.XPATH,'//table[@class="v-datatable v-table v-datatable--select-all theme--light"]/tbody/tr[]/td[]']


    #I/V NO
    IVNoElement = (By.XPATH,'//input[@aria-label="I/V NO"]')

    # 有償INVが無いと、SAを作成できません。
    error1_element = [By.XPATH, '//div[text()="有償INVが無いと、SAを作成できません。"]']


    # #资料填写不完整
    # incompleteElement = [By.XPATH,'//div[text()="コンテナ情報が不完全です"]']
    # #确定
    # sureElement = [By.XPATH, '//div[@class="v-dialog v-dialog--active"]//button[@class="v-btn theme--light"]']
    #首页 masterNO
    master_no_element = [By.XPATH,'//input[@aria-label="Master B/L No"]']

    #首页 HouseNo
    house_no_element = [By.XPATH,'//input[@aria-label="House B/L No"]']




    def locate_status(self, params):
        # 根据B/L NO定位状态
        status_element = [By.XPATH,'//td[text()="{}"]/../td[7]'.format(params)]
        print(status_element)
        return status_element
    
    
    
    
    