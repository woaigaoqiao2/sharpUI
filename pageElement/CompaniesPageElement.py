"""
Created on 2019年6月24日

页面元素操作类
@author: chinasoft.l.yu

"""

from selenium.webdriver.common.by import By

class CompaniesPageElement():
    
    #   纳入指示首页菜单
    companiesStartElement = [By.XPATH,'//div[@class="seq" and text()="5"]/..']
    #   “正在处理”元素
    dealing = [By.XPATH,'//div[@class="v-dialog v-dialog--persistent"]']
    #   查询相关元素信息
    #   検索
    queryButton = [By.XPATH,'//div[@class="v-btn__content" and text()="検索"]/..']
    #   查询条件：D/O
    #   查询条件：B/L
    queryDOInput = [By.XPATH,'//input[@aria-label="D/O NO"]']
    queryBLInput = [By.XPATH,'//input[@aria-label="B/L NO"]']
    # 一页数据
    onepagedata = [By.XPATH,'//div[@class="v-input--selection-controls__input"]']
    #   查询条件：纳入指示者
    queryOperateDirectorId = [By.XPATH,'//input[@aria-label="納入指示者"]']
    queryOperateDirectorList = [By.XPATH,'//*[@class="v-list__tile__title" and text()="小山　敬市"]']
    #   整个下拉框的定位
    EntireScroll = [By.XPATH,'//*[@class="v-menu__content theme--light menuable__content__active v-autocomplete__content" ]']
    #   查询条件：海外取引先
    queryPartnerId = [By.XPATH,'//input[@aria-label="海外取引先"]/..']
    queryPartnerList = [By.XPATH,'//div[@class="v-list__tile__title" and text()="70007:WUXI SHARP ELECTRONIC COMPONENTS CO"]']
    #   查询条件：纳入指示status
    queryShowStatus = [By.XPATH,'//input[@aria-label = "納入指示Status"]/..']
    queryShowStatusList = [By.XPATH,'//div[@class="v-list__tile__title" and text()="指示Mail送信済"]']
    queryShowStatusListn = [By.XPATH,'//div[@class="v-list__tile__title" and text()="納入指示済"]']

    #   列表相关元素信息
    #   列表无数据时
    tableNoData = [By.XPATH,'//td[@class="text-xs-center" and @colspan="20" and text()="No data available"]']
    ###  数据展示条数
    tableCountNumb = [By.XPATH,'//div[@class="v-datatable__actions__range-controls" ]/div']
    ###  列表选择数据框  返回的数据是多条
    # tableCheckData = [By.XPATH,'//div[@class="v-input--selection-controls__ripple" ]']
    tableCheckData = [By.XPATH,'//th[@aria-label = "D/O NO: Not sorted."]/..//input/..']
    ### 选择第一条数据
    tableFristData = [By.XPATH,'//div[@class="inline-edit"]//tbody//tr[1]//input/..']
    ##   选择第十条数据
    table10data = [By.XPATH,'//div[@class="inline-edit"]//tbody//tr[10]//input/..']
    ###  详细按钮
    tableDetail = [By.XPATH,'//div[@class = "v-btn__content" and text()="B/L 詳細"]']
    ###  详细页面保存按钮
    detailSave = [By.XPATH,'//button[@class="v-btn theme--light"]//div[text()="保存"]']
    ###  详细页面保存按钮
    detailSaven = [By.XPATH,'//button[@class="v-btn v-btn--disabled theme--light"]//div[text()="保存"]']
    ###  详细页面关闭按钮
    detailClose = [By.XPATH,'//div[@class="pb-4 v-card theme--light"]//div[text()="戻る"]/..']
    ###  描述输入框
    detailInput = [By.XPATH,'//div[@class="flex md3 sm6 xs12"]//input[@aria-label="コメント"]']
    
    ###  保存成功
    detailSuccess = [By.XPATH,'//div[@class="v-btn__content" and text()="確定"]/..']
    

    #######################################送信相关元素信息####################################
    ###    送信入口按钮
    sendEail = [By.XPATH,'//div[@class="v-btn__content" and text()="送信"]/..']
    #   纳入指示剂下，点击送信报错信息
    sendEailError1 = [By.XPATH,'//div[@class="v-card__text text-xs-center" and text()="既に送信済み"]']
    #   指示Mail送信済下，必填信息为空点击送信报错信息
    sendEailError2 = [By.XPATH,'//div[@class="v-card__text text-xs-center" and text()="最終納入場所が設定されていないので、送信できません。"]']
    #   指示Mail送信済下，纳入预定时间为空
    sendEailError3 = [By.XPATH,'//*[@class="v-card__text text-xs-center" and text()="納入予定日は入力必須項目です"]  ']
    #   送信成功提示
    sendEailSuccess = [By.XPATH,'//div[@class="v-card__text text-xs-center" and text()="納入指示済"]']


    #######################################纳入场所一括登录相关元素信息####################################
    ###    纳入场所一括登录入口按钮
    deliveryOrdersStar = [By.XPATH,'//div[@class="v-btn__content" and text()="納入場所一括登録"]/..']
    #   追加按钮
    deliveryOrderszj = [By.XPATH,'//div[@class="v-btn__content" and text()="追加"]/..']
    #   关闭按钮
    deliveryOrdersClose = [By.XPATH,'//div[@class="v-dialog v-dialog--active"]//div[@class="v-btn__content" and text()="戻る"]']
    #   纳入场所
    deliveryOrdersnrcs = [By.XPATH,'//div[@class="v-dialog v-dialog--active"]//form/div/div/div[1]/div/div/div[1]/div[1]']
    #  下拉框定位
    deliveryOrdersnrcsSelect = [By.XPATH,'//div[@class="v-menu__content theme--light menuable__content__active v-autocomplete__content"]']
    #   下拉框选值
    deliveryOrdersnrcsInput = [By.XPATH,'//div[@class="v-list__tile__title" and text()="031059:品質保証部（冷蔵）"] ']
    #   纳入予定日
    deliveryOrdersnrydr = [By.XPATH,'//*[@id="app"]/div[5]/div/div/form/div/div/div[2]/div/div[1]/div/div/div[1]/div[1]/input']
    #   时间选择
    deliveryOrdersTimeList = [By.XPATH,'//div[@class="v-btn__content" and text()="26日"]']
    #   时间
    deliveryOrdersTime = [By.XPATH,'//input[@aria-label="時間"]']
    #描述头名
    deliveryOrdersTDesc = [By.XPATH,'//input[@aria-label="コメント"]/..']
    #   描述
    deliveryOrdersDesc = [By.XPATH,'//div[@class="v-text-field__slot"]/input[@aria-label="コメント"]']




    #######################################納入場所指定相关元素信息####################################
    ###  納入場所指定按钮
    companiesAddButtonElement = [By.XPATH,'//div[@class="v-btn__content" and text()="納入場所指定"]/..']

    ###  最终纳入场所文本框
    companieCustoms = [By.XPATH,'//input[@aria-label="最终納入場所"]/..']
    companieCustomsInput = [By.XPATH,'//input[@aria-label="最终納入場所"]']
    companieCustomsList = [By.XPATH,'//*[@id="app"]/div[1]/div/div/div[12]/a/div/div']
    ###  納入予定日文本框
    companieTime = [By.XPATH,'//input[@aria-label="納入予定日"]/..']
    companieTimeInput = [By.XPATH,'//div[@label="納入予定日"]//div[@class="v-input__icon v-input__icon--"]']
    companieTimeList = [By.XPATH,'//div[@class="v-btn__content" and text()="25日"]']
    ###  时间文本框
    companieDate = [By.XPATH,'//input[@aria-label="時間"]/..']
    companieDateInput = [By.XPATH,'//input[@aria-label="時間"]']
    ###  保存按钮
    saveButton = [By.XPATH,'//div[@class="v-btn__content" and text()="保存"]/..']
    ###  关闭按钮
    colseButton = [By.XPATH,'//div[@class="v-content__wrap"]//button[2]']
    ###  保存后校验信息
    saveTips = [By.XPATH,'//div[text()="保存が完了でした。"]']
    saveTipssaveButton = [By.XPATH,'//div[@class="v-btn__content" and text()="確定"]']



    #######################################纳入指示变更相关元素信息####################################
    #   纳入指示变更按钮
    nrzsbgButton = [By.XPATH,'//div[@class="v-btn__content" and text()="納入指示変更"]/..']
    #   变更按钮
    updateButton = [By.XPATH,'//div[@class="v-btn__content" and text()="変更"]/..']
    #   关闭按钮
    closeButton = [By.XPATH,'//div[@class="v-btn__content" and text()="変更"]/../..//div[text()="戻る"]']
    #   纳入场所input
    nrcsInput = [By.XPATH,'//div[@class="v-input v-text-field v-select v-autocomplete v-input--is-focused theme--light primary--text"]//input[@aria-label="納入場所"]']
    #   纳入场所下拉框
    nrcsDiv = [By.XPATH,'//div[@class="v-input v-text-field v-select v-autocomplete v-input--is-label-active v-input--is-dirty theme--light"]//input[@aria-label="納入場所"]/..']
    #   纳入场所赋值
    nrcsDivValues = [By.XPATH,'//div[@class="v-menu__content theme--light menuable__content__active v-autocomplete__content"]//div[@class="v-list__tile__title" and text()="017004:栃木ＤＰ情家）国内事第一技術部"]']
    #   纳入予定日
    timeInput = [By.XPATH,'//input[@aria-label="納入予定日"]']
    timeInputDiv = [By.XPATH,'//input[@aria-label="納入予定日"]/..']
    #   纳入予定日
    timeValues = [By.XPATH,'//div[@class="v-btn__content" and text()="28日"]/..']
    #   受入予定时间
    DateInput = [By.XPATH,'//input[@aria-label="受入予定时间"]']

    siteSelectInput = [By.XPATH,'//div[@class="v-input v-text-field v-select v-autocomplete v-input--is-label-active v-input--is-dirty theme--light"]//div[@class="v-input__icon v-input__icon--clear"]']
    timeSelectInput = [By.XPATH,'//div[@class="v-input v-text-field v-input--is-label-active v-input--is-dirty v-input--is-readonly theme--light"]//div[@class="v-input__icon v-input__icon--clear"]']
#######################################D/O分け与D/O合併相关元素信息####################################
    #  D/O分け
    DOfenButton = [By.XPATH,'//*[@class="v-card theme--light"]/div[2]/button[4]']
    #  D/O合併
    DOheButton = [By.XPATH,'//*[@class="v-card theme--light"]/div[2]/button[5]']
    #  头名详细情报
    Headlinexq = [By.XPATH,'//*[@class="headline mb-0"]']
    #  详细情报页保存按钮
    SaveButton = [By.XPATH,'//*[@class="v-card theme--light"]/div[2]/button[1]']
    #  详细情报页split按钮
    SplitButton = [By.XPATH,'//*[@class="v-card theme--light"]/div[2]/button[3]']
    #  详细情报页，未选择数据时点击split，提示
    # NoChosePrompt = [By.XPATH,'//*[@class="v-card__text text-xs-center" and text()="少なくとも1つの項目を選んでください"]']
    NoChosePrompt = [By.XPATH,'//div[@class="v-dialog v-dialog--active"]//div[@class="v-card__text text-xs-center"]']
    #  详细情报页，列表数据全选
    XQchackBoxData = [By.XPATH,'//*[@class="v-input--selection-controls__input"]']
    XQchackFirstData = [By.XPATH, '//*[@class="v-datatable v-table v-datatable--select-all theme--light"]/tbody//input//..']
    #  退出键元素
    QuitButton=[By.XPATH,'//*[@class="v-card theme--light"]/div[2]/button[2]']
    #  退出后 纳入指示标题
    QXNRTittle=[By.XPATH, '//*[@class="headline mb-0" and text()="納入指示"]']
    #  点击split后的削除DO枝番
    SplitXC=[By.XPATH,'//*[@class="v-btn__content" and text()="削除DO枝番"]']
    #  保存
    XQsave=[By.XPATH,'//*[@class="v-btn__content" and text()="保存"]']
    #  保存成功提示
    XQsaveCG=[By.XPATH,'//*[@class="v-card__text text-xs-center" and text()="保存が完了しました。"]']
    #  D/O合併后成功提示
    DOheCG = [By.XPATH,'//*[@class="v-card__text text-xs-center" and text()="合併に成功する"]']




