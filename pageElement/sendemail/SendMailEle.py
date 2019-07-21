'''
Created on 2019年5月22日

@author: chinasoft.xp.chen
'''

from selenium.webdriver.common.by import By

class SendMailEle():
    #納入指示メール配信
    Send_element=[By.XPATH,'//main//div[@class="flex nav xs6"][2]//div[2]//div[@class="name"]'] 
    #納入指示者
    Delivery=[By.XPATH,'(//div[@id="app"]//div[20]//form//input)[1]']
    #D/O no
    dono_element=[By.XPATH,'(//div[@id="app"]//div[20]//form//input)[2]']
    #B/L NO
    blno_element=[By.XPATH,'(//div[@id="app"]//div[20]//form//input)[3]']
    #检索
    Search_element=[By.XPATH,'//main//button[contains(@class,"btn-search")]/div']
    #只有一个结果的B/L 詳細
    bldetails_element=[By.XPATH,'//main//table//button']
    #选择cxp006的B/L
    bl_cxp006=[By.XPATH,'//td[text()="cxp006"]/..//div[@class="v-btn__content"]']
    bl_test22026=[By.XPATH,'//td[text()="test22026"]/..//div[@class="v-btn__content"]']
    bl_test06462=[By.XPATH,'//td[text()="test06462"]/..//div[@class="v-btn__content"]']
    bl_test001=[By.XPATH,'//td[text()="test001"]/..//div[@class="v-btn__content"]']
    bl_test004=[By.XPATH,'//td[text()="test004"]/..//div[@class="v-btn__content"]']
    bl_test022=[By.XPATH,'//td[text()="test022"]/..//div[@class="v-btn__content"]']
    bl_test005=[By.XPATH,'//td[text()="test005"]/..//div[@class="v-btn__content"]']
    #选择cxp007的B/L
    bl_cxp007=[By.XPATH,'//td[text()="cxp007"]/..//div[@class="v-btn__content"]']
    #納入指示者１
    Deliveryone_element=[By.XPATH,'(//input[@role="combobox"])[1]']   
    #納入指示者2
    Deliverytwo_element=[By.XPATH,'(//input[@role="combobox"])[2]']
    #納入指示者3
    Deliverythree_element=[By.XPATH,'(//input[@role="combobox"])[3]']
    #納入指示者4
    Deliveryfour_element=[By.XPATH,'(//input[@role="combobox"])[4]']
    #納入指示者5
    Deliveryfive_element=[By.XPATH,'(//input[@role="combobox"])[5]']
    #CC
    cc_element=[By.XPATH,'(//input[@role="combobox"])[6]']
    #cxp
    element_cxp=[By.XPATH,'//div[contains(@class,"menuable__content__active")]//span[text()="{}"]'.format('cxp')]
    #chen
    element_chen=[By.XPATH,'//div[contains(@class,"menuable__content__active")]//span[text()="{}"]'.format('chen')]
    #xian
    element_xian=[By.XPATH,'//div[contains(@class,"menuable__content__active")]//span[text()="{}"]'.format('xian')]
    #cxp5
    element_cxp5=[By.XPATH,'//div[contains(@class,"menuable__content__active")]//span[text()="{}"]'.format('cxp5')]
    #cxp6
    element_cxp6=[By.XPATH,'//div[contains(@class,"menuable__content__active")]//span[text()="{}"]'.format('cxp6')]
    #cxp7
    element_cxp7=[By.XPATH,'//div[contains(@class,"menuable__content__active")]//span[text()="{}"]'.format('cxp7')]
    #ping
    element_ping=[By.XPATH,'//div[contains(@class,"menuable__content__active")]//span[text()="{}"]'.format('ping')]
    #cxp1
    element_cxp1=[By.XPATH,'//div[contains(@class,"menuable__content__active")]//span[text()="{}"]'.format('cxp1')]
    #cxp2
    element_cxp2=[By.XPATH,'//div[contains(@class,"menuable__content__active")]//span[text()="{}"]'.format('cxp2')]
    #cxp3
    element_cxp3=[By.XPATH,'//div[contains(@class,"menuable__content__active")]//span[text()="{}"]'.format('cxp3')]
    #cxp4
    element_cxp4=[By.XPATH,'//div[contains(@class,"menuable__content__active")]//span[text()="{}"]'.format('cxp4')] 
    #NAOMI
    element_NAOMI=[By.XPATH,'//span[@class="v-list__tile__mask" and text()="NAOM"]'] 
    element_Daniel=[By.XPATH,'//span[@class="v-list__tile__mask" and text()="Danie"]'] 
    element_Daniel1=[By.XPATH,'//div[@class="v-list__tile__title" and text()="Daniel"]'] 
    #选择收件人
    choice_receiver=[By.XPATH,'//span[@class="v-list__tile__mask"]'] 
    #清除纳入指示者
    clear_elements=[By.XPATH,'//div[contains(@class,"v-select__slot")]//i[text()="clear"]'] 
    #勾选框
    Option_element=[By.XPATH,'//main//table/tbody/tr/td[1]']
    #勾选cxp006
    option_cxp006=[By.XPATH,'//td[text()="cxp006"]//..//div[@class="v-input__control"]']
    option_test001=[By.XPATH,'//div[@id="app"]//main//tbody/tr[2]/td[1]/div']
    option_test004=[By.XPATH,'//div[@id="app"]//main//tbody/tr[3]/td[1]/div']
    option_test022=[By.XPATH,'(//td[text()="test022"]//..//div[@class="v-input__control"])[2]']
    option_cxp007=[By.XPATH,'//td[text()="cxp007"]//..//div[@class="v-input__control"]']
    option_cxp002=[By.XPATH,'//td[text()="cxp002"]//..//div[@class="v-input__control"]']
    option_cxp004=[By.XPATH,'//td[text()="cxp004"]//..//div[@class="v-input__control"]']
    option_test22026=[By.XPATH,'//td[text()="test22026"]//..//div[@class="v-input__control"]']
    option_test06462=[By.XPATH,'//td[text()="test06462"]//..//div[@class="v-input__control"]']
    option_sendemail=[By.XPATH,'//td[text()="指示Mail送信済"]//..//div[@class="v-input__control"]']
    #勾选可以进行送信的勾选框
    option_1=[By.XPATH,'//td[text()="SA登録済"]//..//div[@class="v-input__control"]']
    option_2=[By.XPATH,'//td[text()="指示Mail送信解除"]//..//div[@class="v-input__control"]']
    next_page_element=[By.XPATH,'//i[contains(@class,"material-icons") and text()="chevron_right"]']
    #纳入指示者保存
    #获取可以送信的DO
    DO1=[By.XPATH,'//td[text()="SA登録済"]//..//td[2]']
    DONO=[By.XPATH,'(//table[@class="v-datatable v-table v-datatable--select-all theme--light"])[2]//td[2]']
    DO2=[By.XPATH,'//td[text()="指示Mail送信解除"]//..//td[2]']
    BL1=[By.XPATH,'//td[text()="SA登録済"]//..//td[3]']
    BL2=[By.XPATH,'//td[text()="指示Mail送信解除"]//..//td[3]']
    preserve_alex=[By.XPATH,'//div[contains(text(),"保存")]/..']
    #关闭返回
    return_elements=[By.XPATH,'//div[text()="戻る"]']
    #送信
    Sendmail_element=[By.XPATH,'//div[text()="送信"]']
    #点击确定
    sure_element=[By.XPATH,'(//div[@class = "v-btn__content" and text()="確定" ])[3]']    
    #送信解除
    relieve_element=[By.XPATH,'//div[starts-with(text(),"送信解除")]']
    #显示的页数和总数
    num_element=[By.XPATH,'//main//div[@class="v-datatable__actions__pagination"]']
    #获取D/O num
    do_num=[By.XPATH,'//div[@class="inline-edit"]//td[2]']
    #获取B/L num
    bl_num=[By.XPATH,'//div[@class="inline-edit"]//td[3]']
    #获取实际的时间
    date_actual=[By.XPATH,'//div[@class="inline-edit"]//td[8]']
    #获取送信状态
    actual_sendingstate=[By.XPATH,'//div[@class="inline-edit"]//td[4]']
    #没有有效数据
    no_data=[By.XPATH,'//main//table[contains(@class,"v-datatable--select-all")]/tbody/tr/td']
    #获取送信状态cxp002
    sendresult_test22026=[By.XPATH,'//td[text()="test22026"]/../td[4]']
    sendresult_test06462=[By.XPATH,'//td[text()="test06462"]/../td[4]']
    sendresult_002=[By.XPATH,'//td[text()="cxp002"]/../td[4]']
    sendresult_test001=[By.XPATH,'//td[text()="test001"]/../td[4]']
    sendresult_test004=[By.XPATH,'//td[text()="test004"]/../td[4]']
    sendresult_test022=[By.XPATH,'//td[text()="test022"]/../td[4]']
    sendresult_006=[By.XPATH,'//td[text()="cxp006"]/../td[4]']
    sendresult_007=[By.XPATH,'//td[text()="cxp007"]/../td[4]']
    #获取送信状态cxp004
    sendresult_004=[By.XPATH,'//td[text()="cxp004"]/../td[4]']
    tip2=[By.XPATH,'//div[text()="納入指示者を設定ください。"]']
    remove_text=[By.XPATH,'(//span[@class="headline"])[3]']
    tip3=[By.XPATH,'//span[text()="指示Mail送信解除"]']
    
    
    