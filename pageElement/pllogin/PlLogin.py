"""
pl登录模块
下拉框：v-select__selections
"""
from selenium.webdriver.common.by import By

class PlLogin(object):
    # 海外取引先下拉框
    haiwaiquyinxian_element=(By.XPATH,'//input[@aria-label="海外取引先" and @type="text"]')
    # I/V no
    ivnonumber_element = (By.XPATH, '//input[@aria-label="I/V NO" and @type="text"]')
    # I/V作成日
    ivzuocheng_element=(By.XPATH,'//input[@aria-label="I/V作成日" and @type="text"]')
    # 责出港下拉框
    zhechugang_element=(By.XPATH,'//input[@aria-label="積出港" and @type="text"]')
    # 输送形态
    xingtai_element=(By.XPATH,'//input[@aria-label="輸送形態" and @type="text"]//..')
    # 形态值 SEA
    sea_element=(By.XPATH,'//div[@class="v-list__tile__title" and contains(text(),"SEA")]')
    # 建值
    jianzhi_element=(By.XPATH,'//input[@aria-label="建値" and @type="text"]')
    # 陆杨港
    luyanggang_element=(By.XPATH,'//input[@aria-label="陸揚港" and @type="text"]')
    # 通货
    tonghuo_element=(By.XPATH,'//input[@aria-label="通貨" and @type="text"]')
    # ETD
    ETD_element=(By.XPATH,'//input[@aria-label="ETD" and @type="text"]')
    # 无偿登录保存按钮
    wuchagnbaocun_element=(By.XPATH,'//div[@class="v-btn__content" and contains(text(),"保存")]')
    # 首页点击第一个模块
    plbuttong_element=(By.XPATH,'//main//div[contains(text(),"INV P/L登録")]')
    # 页面无偿新规按钮
    wuchangbutton_element=(By.XPATH,'//div[@class="v-content__wrap"]//div[@class="v-card theme--light"]//button[3]')
    # 无偿新规追加
    wuchangzuijia_element=(By.XPATH,'//div[@class="mt-2 v-card theme--light"][2]//button[1]')
    # 无偿新规追加下一页按钮
    wuchangzuijianext_element=(By.XPATH,'//*[@id="app"]/div[3]/div/div/div[3]/div[2]/div/div/button[2]/div/i')
    # 无偿追加页面社外品番输入框
    wuchangshewaiinsert_element=(By.XPATH,'//input[@aria-label="社外品番"]')
    # 无偿追加页面社内品番输入框
    wuchangsheneiinsert_element = (By.XPATH, '//input[@aria-label="社内品番"]')
    # 点击检索按钮
    wuchangzuijiajainsuo_element=(By.XPATH,'//div[@class="v-btn__content" and contains(text(),"検索")]')
    # 点击使用按钮
    wuchangzuijiashiyong_element = (By.XPATH, '//div[@class="v-btn__content" and contains(text(),"使用")]')
    # 无偿商品追加结果值
    wuchangzuijiavalue_element=(By.XPATH,'//div[@class="elevation-0"][1]//td[2]')
    # 无偿商品追加标题
    wuchangzuijiatite_element=(By.XPATH,'//span[@class="headline" and contains(text(),"無償商品登録行追加")]')
    # 无偿追加搜索不到商品显示nodata
    wuchangzuijianodata_element=(By.XPATH,'//td[@class="text-xs-center"]')
    # INVOICE无偿商品登录行追加检索出第一个值追加
    wuchangzuijiavaluefirstgouxuan_element=(By.XPATH,'//div[@class="v-input--selection-controls__input"]')
    # INVOICE 详细页面无偿商品勾选
    invoicejilugouxuan_element=(By.XPATH,'//input[@role="checkbox"]')
    # INVOICE 详细页面点击PL/登录按钮
    invoicepldenglubutton_element=(By.XPATH,'//div[@class="v-btn__content" and contains(text(),"P/L登録")]')
    # INVOICE 详细-数量
    invoicenumber_element=(By.XPATH,'//div[@class="elevation-1 mt-2 mb-2 inline-edit"]//td[8]')
    # INVOICE 详细-小计价格
    invoicexiaoji_element = (By.XPATH, '//div[@class="elevation-1 mt-2 mb-2 inline-edit"]//td[10]')

    # INVOICE 详细 商品の数input(数量)
    invoiceshuliang_element=(By.XPATH,'//input[@type="text" and @placeholder="商品の数"]')
    # INVOICE 详细 FOB単価
    invoicefob_element = (By.XPATH, '//input[@type="text" and @placeholder="FOB単価"]')
    # INVOICE 原产国input标签
    invoiceguojia_element=(By.XPATH,'//input[@type="text" and @placeholder="原産国"]')
    # INVOICE 原产国input标签下拉框日本
    invoiceguojiariben_element = (By.XPATH, '//div[@class="v-list__tile__title" and contains(text(),"日本")]')
    # Package List详细-数量
    packagelistshuliang_element=(By.XPATH,'//input[@type="text" and @placeholder="数量"]')
    # Package List详细-人数
    packagelistrenshu_element = (By.XPATH, '//input[@type="text" and @placeholder="入り数"]')
    # Package List-社内品番
    packagelistshenei_element = (By.XPATH, '//div[@class="elevation-1 pb-2 inline-edit"]//td[3]')
    # Package List详情标签
    packagelistlable_element=(By.XPATH,'//span[@class="headline mb-0" and contains(text(),"Package List详细")]')
    # Package List详情识别番号
    packagelistshibie_element = (By.XPATH, '//input[@type="text" and @placeholder="識別番号"]')
    # Package List第一条记录
    packagelistfirstvalue_element = (By.XPATH, '//div[@class="elevation-1 pb-2 inline-edit"]//td//input')
    # Package List-Carton Start No
    packageliststartno_element = (By.XPATH, '//div[@class="elevation-1 pb-2 inline-edit"]//td[6]//input')
    # Package List-Carton end no
    packagelistendno_element = (By.XPATH, '//div[@class="elevation-1 pb-2 inline-edit"]//td[7]//input')
    # Package List-NW
    packagelistnw_element = (By.XPATH, '//div[@class="elevation-1 pb-2 inline-edit"]//td[10]//input')
    # Package List-GW
    packagelistgw_element = (By.XPATH, '//div[@class="elevation-1 pb-2 inline-edit"]//td[11]//input')
    # Package List-M3
    packagelistm3_element = (By.XPATH, '//div[@class="elevation-1 pb-2 inline-edit"]//td[12]//input')
    # 无偿新规界面删除按钮
    wuchangxinguishanchu_element=(By.XPATH,'//div[@class="v-btn__content" and contains(text(),"削除")]')
    # packagelist删除记录确认按钮
    wuchangxinguishanchuqueren_element=(By.XPATH,'//div[@class="v-btn__content" and contains(text(),"はい")]')
    # packagelist删除记录取消确认按钮
    wuchangxinguishanchuquxiaoqueren_element = (By.XPATH, '//div[@class="v-btn__content" and contains(text(),"戻る")]')
    # packagelist-PL分行按钮
    wuchangxinguipackagelistfenhang_element = (By.XPATH, '//div[@class="v-btn__content" and contains(text(),"P/L 行分け")]')
    # packagelist-页面分页数量显示2
    wuchangxinguipackagelistfenyeshutwo_element = (By.XPATH, '//div[@class="v-datatable__actions__pagination" and contains(text(),"1-2 of 2")]')
    # packagelist-页面分页数量显示1
    wuchangxinguipackagelistfenyeshuone_element = (By.XPATH, '//div[@class="v-datatable__actions__pagination" and contains(text(),"1-1 of 1")]')
    # packagelist删除成功返回消息
    wuchangxinguishanchufanhui_element = (By.XPATH, '//div[@class="v-card__text text-xs-center" and contains(text(),"削除成功しました。")]')
    # 添加成功弹出对话框
    successmessage_element=(By.XPATH,'//div[@class="v-card__text text-xs-center" and contains(text(),"保存が完了しました。")]')
    # 数量不一致提示信息
    unsamemessage_element=(By.XPATH,'//div[@class="v-card__text text-xs-center" and contains(text(),"PO出荷数量とPOのPackingList数量が不一致のため、保存できません。")]')
    # 无偿IVO订单已重复记录
    wuchangivosame_element=(By.XPATH,'//div[@class="v-card__text text-xs-center" and contains(text(),"INV番号はすでに存在しています。")]' )
    # packagelist 重量登录按钮
    zhongliangdenglu_element=(By.XPATH,'//div["v-btn__content" and contains(text(),"重量登録")]')
    # 重量登录按钮确认按钮
    zhongliangdengluconfirm_element=(By.XPATH,'//div["v-card__text text-xs-center" and contains(text(),"保存が完了しました。")]')