"""
pl登录模块
下拉框：v-select__selections
"""
from selenium.webdriver.common.by import By

class PlLogin(object):

    #首页登录按钮
    plbuttong_element = [By.XPATH,'//*[@id="app"]/div[10]/main/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]']
    #有偿新规按钮
    youchang_element = (By.XPATH,'// *[ @ id = "app"] / div[18] / main / div / div[1] / div[1] / div[2] / button[2] / div')
    #po检出按钮
    pojianchu_element = (By.XPATH,'//*[@id="app"]/div[18]/main/div/div[1]/div[3]/div[2]/button[1]/div')
    #点击div弹窗
    div_alert_element=(By.XPATH,'//*[@id="app"]/div[4]/div')
    # 双击检索按钮
    jiansuobt_element=('//*[@id="app"]/div[4]/div/div/div[2]/button[1]/div')  # 双击按钮用,双击按钮需要传一个xpath地址，所以没有by.xpath
    # 勾选第一条值
    pofirstvalue_element=(By.XPATH,'//*[@id="app"]/div[4]/div/div/div[3]/div[1]/table/tbody/tr[1]/td[1]/div/div/div/div/div')
    # 点击使用
    pouse_element=(By.XPATH,'//*[@id="app"]/div[4]/div/div/div[2]/button[2]/div')
    # 责出港下拉框
    zhechuang_element=(By.XPATH,'//*[@id="app"]/div[19]/main/div/div[1]/div[2]/form/div/div/div[4]/div/div/div[1]/div[1]')
    #点击第一条记录
    zhechuangfirst_element = (By.XPATH, '// *[ @ id = "app"] / div[9] / div / div / div[1] / a / div / div')
    # 陆杨港下拉框
    luyang_element = (By.XPATH,'//*[@id="app"]/div[19]/main/div/div[1]/div[2]/form/div/div/div[7]/div/div/div[1]/div[1]')
    # 点击第一个下拉框
    luyangfirst_element = (By.XPATH, '//*[@id="app"]/div[6]/div/div/div[1]/a/div/div')
    # 运输形态下拉框
    xingtai_element=(By.XPATH,'//*[@id="app"]/div[20]/main/div/div[1]/div[2]/form/div/div/div[5]/div/div/div[1]/div[1]/div[1]')
    # 点击第一条记录
    xingtaifirst_element=(By.XPATH,'//div[@class="v-menu__content theme--light menuable__content__active"]/div/div/div[1]/a')
    # 建值下拉框
    jianzhi_element=(By.CSS_SELECTOR,'#app > div.application--wrap > main > div > div.container.fluid > div:nth-child(2) > form > div > div > div:nth-child(6) > div > div > div.v-input__slot > div.v-select__slot > input[type=text]')
    # 建值第一条记录
    jianzhifirst_element=(By.CSS_SELECTOR,'#app > div.v-menu__content.theme--light.menuable__content__active.v-autocomplete__content > div > div > div:nth-child(1) > a > div > div')
    # 通货下拉框
    tonghuo_element = (By.CSS_SELECTOR,'#app > div.application--wrap > main > div > div.container.fluid > div:nth-child(2) > form > div > div > div:nth-child(8) > div > div > div.v-input__slot > div.v-select__slot > input[type=text]')
    # 通货第一条记录
    tonghuofirst_element = (By.CSS_SELECTOR,'#app > div.v-menu__content.theme--light.menuable__content__active.v-autocomplete__content > div > div > div:nth-child(1) > a > div > div')
    #选择I/V工作日
    ivdate_element=(By.XPATH, '//input[@aria-label="I/V作成日"]')
    # 随机选择一个I/V日期
    ivdatevalue_element=(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[4]/td[5]/button/div')
    # 选择ETD日期
    etddate_element =(By.XPATH, '//input[@aria-label="ETD"]')
    # 随机选择一个ETD日期
    etddatevalue_element=(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[4]/td[6]/button/div')
    # 输入IVO NO
    ivono_element=(By.XPATH,'//input[@aria-label="I/V NO"]')
    # 点击P/L登录按钮
    pl_denglu_element=(By.XPATH,'//*[@id="app"]/div[21]/main/div/div[1]/div[3]/div[2]/button[2]/div')
    # 点击plNO勾选按钮
    plgouxuan_element=(By.XPATH,'//*[@id="app"]/div[21]/main/div/div[1]/div[3]/div[3]/div[1]/table/tbody/tr/td[1]/div/div/div/div/div')
    #点击list详情勾选按钮
    listdetail_element=(By.XPATH,'//*[@id="app"]/div[21]/main/div/div[1]/div[4]/div[3]/div[1]/table/thead/tr[1]/th[1]/div/div/div/div/div')
    # M3输入值
    m3input_element = (By.XPATH, '//input[@placeholder="M3"]')
    # G/W
    gwinput_element = (By.XPATH, '//input[@placeholder="G/W"]')
    # N/W
    nwinput_element = (By.XPATH, '//input[@placeholder="N/W"]')
    # Carton End No
    cartonendinput_element = (By.XPATH, '//input[@placeholder="Carton End No"]')
    # Carton Start No
    cartonstartinput_element = (By.XPATH, '//input[@placeholder="Carton Start No"]')
    # 識別番号
    shibiefanhaoinput_element = (By.XPATH, '//input[@placeholder="識別番号"]')
    # 顶部保存按钮
    topsaveinput_element = (By.XPATH, '//*[@id="app"]/div[21]/main/div/div[1]/div[1]/div[2]/button[1]/div')
    #点击确认按钮
    confirmbuton_element = [By.XPATH,'//div[@class="v-dialog__content v-dialog__content--active"]//button[1]']  # 分两次点击确认按钮
    # 获取最后确认页面的值
    confirmvalue_element= (By.XPATH, '//*[@id="app"]/div[19]/div/div/div[2]')
    # 最后点击确认按钮
    lastconfirbutton_element=(By.XPATH,'//*[@id="app"]/div[19]/div/div/div[3]/button/div')
