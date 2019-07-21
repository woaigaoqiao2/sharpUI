import datetime

from selenium.webdriver.common.by import By
import time


class CAccept():
    # 点击受入确认
    CAcceptanceElement = [By.XPATH, "//div[@class='flex nav xs6'][2]/div[3]"]
    # 点击检索
    SearchElement = [By.XPATH, "//button[contains(@class,'btn-search')]"]
    # 输入DONO
    InputDONOElement = [By.XPATH, "//main//div[@class='layout row wrap']/div[3]//input"]
    # 输入コンテナNo
    InputAcceptNoElement = [By.XPATH, "//main//div[@class='layout row wrap']/div[4]//input"]

    # 定位到ステータス下拉框
    SelectSelectionsElement = [By.XPATH, "//main//div[@class='layout row wrap']/div[13]//input//.."]
    # 选择状态为納入指示済的数据
    DeliveryElement = [By.XPATH, "//div[contains(@class,'menuable__content__active')]/div/div/div[1]"]
    # 选择状态为受入確認済的数据
    AcceptElement = [By.XPATH, "//div[contains(@class,'menuable__content__active')]/div/div/div[2]"]
    # 选择第一条数据
    ChoiceAcceptElement = [By.XPATH, "//tbody//tr[1]/td[1]//div[@class='v-input--selection-controls__input']"]
    # 获取第一条数据的コンテナNo
    GitAcceptNoElement = [By.XPATH, "//main//tbody/tr[1]/td[4]"]
    # 获取第一条数据的D/O NO
    GitDONoElement = [By.XPATH, "//main//tbody/tr[1]/td[2]"]
    # 获取第一条数据的受入予定日
    GitDeliveryDateElement = [By.XPATH, "//main//tbody/tr[1]/td[5]"]
    # 获取第一条数据的受入予定时间
    GitDeliveryTimeElement = [By.XPATH, "//main//tbody/tr[1]/td[6]"]
    # 获取无数据时table展示
    GitTableElement = [By.XPATH, "//tbody/tr/td"]

    # 点击コンテナNo更新
    ClickContainerUpElement = [By.XPATH, "//main//div[@class='v-card__actions']/button[6]"]
    # 填写コンテナNo更新
    InputContainerUpElement = [By.XPATH, "//div[contains(@class,'v-dialog--active')]//input"]
    # 点击コンテナNo更新按钮
    ClickNoUpElement = [By.XPATH, "//div[contains(@class,'v-dialog--active')]//button[1]"]
    # 点击コンテナNo戻る按钮
    ClickAcceptNoBackElement = [By.XPATH, "//div[contains(@class,'v-dialog--active')]//button[2]"]
    # 更新成功后点击确认
    ClickYesElement = [By.XPATH, "//div[@class='v-dialog v-dialog--active']//div[text()='確定']/.."]
    # 点击パターン設定
    ClickPatternElement = [By.XPATH, "//main//div[@class='v-card__actions']/button[2]"]
    # 点击配送パターン
    ClickDeliveryPatternElement = [By.XPATH, "//button[contains(@class, 'v-btn--icon')]//div"]
    # 获取配送パターン信息
    GitPatternElement = [By.XPATH, "//main//form//div[@class='v-card__title']//span[7]"]
    # 选择配送パターン
    SelectDeliveryPatternElement = [By.XPATH, '//input[@aria-label="配送パターン"]']

    # 选择第一条配送パターン数据
    ChoiceDeliveryPatternElement = [By.XPATH,'(//div[contains(@class,"menuable__content__active")]//div[@class="v-list__tile__title"])[1]']
    ChoiceDeliveryPatternElement1 = [By.XPATH, '//*[@id="app"]/div[17]/div/div/div[1]/a/div/div']

    # 点击配送パターン保存
    SaveDeliveryPatternElement = [By.XPATH, "//form//div[@class='v-card theme--light']/div[2]/button[1]"]
    # 点击配送パターン戻る
    ClickDeliveryBackElement = [By.XPATH, "//form//div[@class='v-card theme--light']/div[2]/button[4]"]
    # 点击配送パターン設定戻る
    ClickPatternBackElement = [By.XPATH, "//main//div[@class='v-card__actions']/button[3]"]

    # 点击納入情報一括変更
    ClickInformationUPElement = [By.XPATH, "//main//div[@class='v-card__actions']/button[3]"]

    # 获取当前时间
    time = datetime.datetime.now().timetuple()
    today = time.tm_mday
    # 納入予定日定位
    DeliveryDateElement = [By.XPATH, "//div[contains(@class,'v-dialog--active')]//div[@class='flex xs12'][1]//input"]
    # 填写納入予定日
    ChoiceDeliveryDateElement = [By.XPATH, '//div[text()="{}日"]'.format(today)]
    # 填写受入予定时间
    InputAcceptanceTimeElement = [By.XPATH,
                                  "//div[contains(@class,'v-dialog--active')]//div[@class='flex xs12'][2]//input"]
    # 点击追加
    ClickAdditionElement = [By.XPATH, "//div[contains(@class,'v-dialog--active')]//button[1]"]
    # 点击戻る
    ClickComplaintsBackElement = [By.XPATH, "//div[contains(@class,'v-dialog--active')]//button[2]"]






