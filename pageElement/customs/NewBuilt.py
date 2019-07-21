from selenium.webdriver.common.by import By

class NewBuiltElement:
    # 首页S/A登录
    SAElement = (By.XPATH, '//main[@class="v-content"]//div[text()="S/A登録"]')

    # 搜索按钮
    searchElement = (By.XPATH, '//div[text()="検索"]')

    # 新規
    newRuleElement = (By.XPATH, '//div[text()="新規"]')

    #临时保存
    tempSaveElement = (By.XPATH,'//main//div[@class="v-card theme--light"]//button[1]')
    #完成确定按钮
    tempSaveFilishElement =(By.XPATH,'//*[@id="app"]/div[28]/div/div/div[3]/button')

    #取消按钮
    cancelElement = (By.XPATH,'//main//div[@class="v-card theme--light"]//button[4]')

    #确认发送
    ensureElement = (By.XPATH,'//main//div[@class="v-card theme--light"]//button[5]')

    #文件上传
    fileUploadElement = (By.XPATH,'//main//div[@class="v-card theme--light"]//button[6]')

    #新规运输信息master BLNO
    newRuleMasterElement=(By.XPATH,'//main//div[@class="layout row wrap"]/div[2]//input')
    #新規运输信息House B/L NO必填提示 其他信息修改div数字
    newRuleHouseNoFillElement = (By.XPATH,'//div[text()="House B/L NO必要である"]')
    #規运输信息House B/L NO
    newRuleHouseNoElement=(By.XPATH,'//main//div[@class="layout row wrap"]/div[3]//input')

    #装载方法下拉框必填
    stowageMethondElement = (By.XPATH,'//main//div[@class="layout row wrap"]/div[10]//div[@class="v-select__selections"]')

    stowagepullElement = (By.XPATH,'//div[@class="v-menu__content theme--light menuable__content__active"]/div/div/div[1]/a')

    #参考制作
    referMakeElement = (By.XPATH,'//div[text()="参照新規作成"]')

    #B/L NO
    BLNoElement = (By.XPATH,'//main//input[@aria-label="B/L NO"]')

    #House B/L NO
    HouseBLNoElement = (By.XPATH,'//input[@aria-label="House B/L NO"]')

    #输送形态
    conveyElement = (By.XPATH,'//main//div[@class="layout row wrap"]/div[9]//div[@class="v-select__selections"]')
    #SEA
    seaElement = (By.XPATH,'//main//div[@class="layout row wrap"]/div[9]//div[text()="SEA"]')

    # 追加按钮
    addElement = (By.XPATH, '//main[@class="v-content"]//div[text()="追加"]')

    #分类按钮
    classifyElement  = (By.XPATH,'//main//div[@class="mt-2 v-card theme--light"]//button[3]')

    #取消行政分工
    cancelAdminElement = (By.XPATH,'//main//div[@class="mt-2 v-card theme--light"]//button[4]')

    # 勾选第一条
    firstCheckElement = [By.XPATH, '//main//tbody/tr[1]//div[@class="v-input--selection-controls__ripple"]']

    # 表内容
    contentElement = (By.XPATH, '//main//tbody')

    # 对话框搜索按钮
    dialogSearchElement = (By.XPATH, '//div[@class="v-dialog v-dialog--active"]//div[text()="検索"]')

    # 对话框追加
    dialogAddElement = (By.XPATH, '//div[@class="v-dialog v-dialog--active"]//div[text()="追加"]')

    # 对话框表头
    dialogHeadElement = (By.XPATH, '//table/thead')

    # 对话框表内容
    dialogContentElement = (By.XPATH, '//table/tbody')

    # 对话框下一页按钮
    dialogNextpageElement = (By.XPATH,'//div[@class="elevation-0"]//button[2]')

    #I/V NO
    IVNoElement = (By.XPATH,'//input[@aria-label="I/V NO"]')



    #弹框提示装运港和陆卸港不一致
    inconformityElement = (By.XPATH,'//div[text()="S/Aの積出港・陸揚港とINVの積出港・陸揚港が不一致のため、再度確認してください"]')

    # 弹框确定按钮
    enterElement = (By.XPATH, '//div[@class="v-dialog v-dialog--active"]//div[text()="確定"]')

    # 对话框表的第一行数据
    firstDataElement = (By.XPATH, '//table/tbody/tr/td')


    # Carton Start No
    startNoElement = (By.XPATH, '//main//tbody/tr/td[8]//input')
    #参考新规
    refer_startNo =[By.XPATH,'//main//tbody/tr/td[10]//input']

    # Carton end No
    endNoElement = (By.XPATH, '//main//tbody//td[9]//input')

    #INV P/L信息 第一条复选框
    INVFistCheckElement = (By.XPATH,'//main//tbody//tr[1]//div[@class="v-input--selection-controls__ripple"]')

    #INV P/L信息 P/O NO
    INVFistPoElement = (By.XPATH,'//main//tbody//tr[1]/td[5]')

    # 有償INVが無いと、SAを作成できません。
    error1_element = [By.XPATH, '//div[text()="有償INVが無いと、SAを作成できません。"]']
    #送信成功
    successElement = [By.XPATH,'//div[text()="SA送信成功しました。"]']

    #资料填写不完整
    incompleteElement = [By.XPATH,'//div[text()="コンテナ情報が不完全です"]']
    #确定
    sureElement = [By.XPATH, '//div[@class="v-dialog v-dialog--active"]//button[@class="v-btn theme--light"]']
    #首页 masterNO
    master_no_element = [By.XPATH,'//input[@aria-label="Master B/L No"]']

    #首页 HouseNo
    house_no_element = [By.XPATH,'//input[@aria-label="House B/L No"]']

    # 表第一条复选框
    fistCheckElement = (By.XPATH, '//main//tbody//tr[1]//div[@class="v-input--selection-controls__ripple"]')

    # 编辑按钮
    editElement = (By.XPATH, '//div[text()="編集"]')

    # 有償INVが無いと、SAを作成できません。
    repet_element = [By.XPATH, '//div[text()="有償INVが無いと、SAを作成できません。"]']

    #存在重复的 b/l
    repet_el=[By.XPATH,'//div[contains(text(),"重複B/L No.が存在します。")]']

from selenium.webdriver.common.by import By
from time import strftime



class NewlyBuildElement():


    nowdate = strftime("%d")
    # INV P/L情报没有时
    without_INV_data_element = [By.XPATH,'//main//td[@class="text-xs-center"]']
    # INV P/L情報 追加
    INV_add_element = [By.XPATH,'//main//div[contains(text(),"追加")]/..']
    # I/V NO输入框
    IV_NO_element = [By.XPATH,'//input[@aria-label="I/V NO"]']
    # P/O NO输入框
    PO_NO_element = [By.XPATH,'//input[@aria-label="P/O NO"]']
    # 檢索
    IV_NO_search_element = [By.XPATH,'//div[text()="検索"]/..']
    # 获取I/V NO数据
    IV_NO_get_element = [By.XPATH,'//div[contains(@class,"active")]//tbody/tr/td[2]']
    # I/V list弹窗里的数据勾选框
    choose_click_element = [By.XPATH,'//div[@class="v-dialog v-dialog--active"]//tbody//input']
    # I/V list弹窗里的 追加按钮
    IV_list_add_element = [By.XPATH,'//div[@class="v-dialog v-dialog--active"]//div[contains(text(),"追加")]/..']
    # Master B/L NO输入框
    Master_BL_NO_element = [By.XPATH,'//input[@aria-label="Master B/L NO"]']
    # Master B/L NO清除
    Master_BL_NO_clear_element = [By.XPATH,'//input[@aria-label="Master B/L NO"]/../..//div[contains(@class,"clear")]']
    # House B/L NO输入框
    House_BL_NO_element = [By.XPATH,'//input[@aria-label="House B/L NO"]']
    # House B/L NO清除
    House_BL_NO_clear_element = [By.XPATH,'//input[@aria-label="House B/L NO"]/../..//div[contains(@class,"clear")]']
    # 依頼日
    trust_day_element = [By.XPATH,'//input[@aria-label="依頼日"]']
    # 依頼日翻月
    trust_day_month_element = [By.XPATH,'//div[@label="依頼日" and contains(@class,"theme--light")]//button[not(@disabled) and contains(@class,"v-btn--icon")]']
    # 依頼日日期
    trust_day_click_element = [By.XPATH,'//div[@label="依頼日" and contains(@class,"theme--light")]//button[not(@disabled) and contains(@class,"floating")]']
    # B/L発行日
    issue_date_element = [By.XPATH,'//input[@aria-label="B/L発行日"]']
    # B/L翻月按钮
    issue_month_click_element = [By.XPATH,'//div[@label="B/L発行日" and contains(@class,"theme--light")]//button[not(@disabled) and contains(@class,"v-btn--icon")]']
    # B/L発行日日期
    issue_date_click_element = [By.XPATH,'//div[@label="B/L発行日" and contains(@class,"theme--light")]//button[not(@disabled) and contains(@class,"v-btn--floating")]']
    # 積出港
    loading_port_element = [By.XPATH,'//input[@aria-label="積出港"]']
    # 積出港下拉框
    loading_port_choice_elements = [By.XPATH,'//div[contains(@class,"menuable__content__active")]//a']
    # 積出港清除按钮
    loading_port_clear_element = [By.XPATH,'//input[@aria-label="積出港"]/..//div[contains(@class,"clear")]']
    # 陸揚港清除按钮
    unloading_port_clear_element = [By.XPATH,'//input[@aria-label="陸揚港"]/..//div[contains(@class,"clear")]']
    # ETD
    ETD_element = [By.XPATH,'//form//div[@label="ETD"]//input']
    #ETD翻月
    ETD_month_clikc_element=[By.XPATH,'//div[@label="ETD" and contains(@class,"theme--light")]//button[not(@disabled) and contains(@class,"v-btn--icon")]']
    #ETD日期
    ETD_click_element = [By.XPATH,'//div[@label="ETD" and contains(@class,"theme--light")]//button[@class="v-btn v-btn--flat v-btn--floating theme--light" and not(@disabled)]']

    # ETA
    ETA_element = [By.XPATH,'//form//div[@label="ETA"]//input']
    # ETA翻月
    ETA_month_clikc_element = [By.XPATH,'//div[@label="ETA" and contains(@class,"theme--light")]//button[not(@disabled) and contains(@class,"v-btn--icon")]']
    # ETA日期
    ETA_click_element = [By.XPATH,'//div[@label="ETA" and contains(@class,"theme--light")]//button[not(@disabled) and contains(@class,"v-btn--floating")]']
    # 运输方式
    transport_mode_element = [By.XPATH,'//div[contains(@class,"v-select__selection--comma")]']
    # 積み方
    loading_method_element = [By.XPATH,'//main//input[@aria-label="積み方"]']
    # 積み方下拉框
    loading_method_choice_elements = [By.XPATH,'//div[contains(@class,"menuable__content__active")]//a']
    # 積み方获取
    loading_method_get_element = [By.XPATH,'//input[@aria-label="積み方"]/../div']
    # 輸出通関日
    export_declaration_date_element = [By.XPATH,'//input[@aria-label="輸出通関日"]']
    # 輸出通関日翻月
    export_declaration_month_click_element = [By.XPATH,'//div[@label="輸出通関日" and contains(@class,"theme--light")]//button[not(@disabled) and contains(@class,"v-btn--icon")]']
    # 輸出通関日日期
    export_declaration_date_click_element = [By.XPATH,'//div[@label="輸出通関日" and contains(@class,"theme--light")]//button[not(@disabled) and contains(@class,"v-btn--floating")]']
    # 船社・航空会社
    shipping_co_element = [By.XPATH,'//input[@aria-label="船社・航空会社"]']
    # 船社・航空会社下拉框
    shipping_co_choice_element = [By.XPATH,'//div[contains(@class,"menuable__content__active")]//a']
    # 本船名输入框
    ships_name_element = [By.XPATH,'//main//input[@aria-label="本船名"]']
    # フライトNO
    flying_No_element = [By.XPATH,'//input[@aria-label="フライトNO"]']
    # VOYAGE NO输入框
    VOYAGE_NO_element = [By.XPATH,'//main//input[@aria-label="VOYAGE NO"]']
    # S/I NO输入框
    SI_NO_element = [By.XPATH,'//input[@aria-label="S/I NO"]']
    # 通関業者
    customs_broker_element = [By.XPATH,'//input[@aria-label="通関業者"]']
    # 通関業者下拉框
    customs_broker_choice_element = [By.XPATH,'//div[contains(@class,"menuable__content__active")]//a']
    # 貨物タイプ
    cargo_type_element = [By.XPATH,'//input[@aria-label="貨物タイプ"]']
    # 貨物タイプ下拉框
    cargo_type_choice_element = [By.XPATH,'//div[contains(@class,"menuable__content__active")]//a']
    # INV数量统计
    INV_count_element = [By.XPATH,'//main//table/tbody/tr']
    # INV P/L勾选框
    INV_checklist_element = [By.XPATH,'//main//tbody/tr/td[1]//input']
    # CONTAINER NO输入框
    container_NO_element = [By.XPATH,'//input[@placeholder="CONTAINER NO"]']
    # CONTAINER SIZE
    container_size_element = [By.XPATH,'//input[@placeholder="CONTAINER SIZE"]']
    # CONTAINER SIZE下拉框
    container_size_choice_element = [By.XPATH,'//div[contains(@class,"menuable__content__active")]//a']
    # 識別番号
    PID_element = [By.XPATH,'//input[@placeholder="識別番号"]']
    # Carton start No
    Carton_start_No_element = [By.XPATH,'//main//tbody/tr/td[last()-6]//input']
    # Carton end No
    Carton_end_No_element = [By.XPATH,'//main//tbody/tr/td[last()-5]//input']
    # SHIPPED CARTON
    shipped_Carton_element = [By.XPATH,'//tbody/tr[1]//input[@placeholder="SHIPPED CARTON"]']
    # 一時保存
    temporary_saving_element = [By.XPATH,'//main//div[text()="一時保存"]/..']
    # 确认按钮
    confirm_button_element = [By.XPATH,'//div[contains(@class,"active")]//div[text()="確定"]/..']
    # 書類アップロード
    file_upload_element = [By.XPATH,'//div[text()="書類アップロード"]/..']
    # INV P/L选择
    INV_upload_element = [By.XPATH,'//input[@aria-label="INV P/L"]']
    # B/L选择
    BL_upload_element = [By.XPATH,'//label[text()="B/L"]/..//input']
    # 上传按钮
    upload_button_element = [By.XPATH,'//div[contains(text(),"Upload")]/input']
    # 关闭
    close_button_element = [By.XPATH,'//div[text()="关闭"]/..']
    # 弹窗的戻る
    popup_return_element = [By.XPATH,'//div[@class="v-dialog v-dialog--active"]//div[text()="戻る"]/..']
    # 保存
    saving_element = [By.XPATH,'//div[text()="保存"]/..']
    # 确定送信
    sending_confirmation_element = [By.XPATH,'//div[text()="確定送信"]/..']
    # 确认按钮
    sure_button_element = [By.XPATH,'//div[text()="はい"]/..']
    # 送信确定
    confirm_element = [By.XPATH,'//div[contains(@class,"active")]//div[text()="確定"]/..']
    # 戻る
    return_element = [By.XPATH,'//main//div[text()="戻る"]/..']