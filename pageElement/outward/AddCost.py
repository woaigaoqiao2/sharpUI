'''
增加费用的页面元素对象
'''
from selenium.webdriver.common.by import By
class AddCost():
    
    
    #首页 做成
    outWardElement = (By.XPATH,'//div[@class="seq" and text()="7"]')
    #BL提单号
    BLNoEelement = (By.XPATH,'//input[@aria-label="B/L NO"]')
    #检索
    selElement = (By.XPATH,'//main//button')
    #选择要修改得数据
    selDateElement = (By.XPATH,'//tbody/tr[1]/td/div[1]')
    #编辑
    editElement = (By.XPATH,'//div[text()="編集"]')
    
    #DOC FEE的金额
    DOCFEElement = (By.XPATH,'//div[@class="container fluid"]/div[4]//tbody/tr[1]/td[2]//input')
    #DOC tax的金额
    DOCtaxElement = (By.XPATH,'//div[@class="container fluid"]/div[4]//tbody/tr[2]/td[2]//input')
    #other charge的金额
    otherElement = (By.XPATH,'//div[@class="container fluid"]/div[4]//tbody/tr[3]/td[2]//input')
    #20F的金额
    twoFElement = (By.XPATH,'//div[@class="container fluid"]/div[4]//tbody/tr[4]/td[2]//input')
    #40F的金额
    fourFElement = (By.XPATH,'//div[@class="container fluid"]/div[4]//tbody/tr[5]/td[2]//input')
    #海上航空凭运计算
    costCalElement = (By.XPATH,'//div[text()="海上・航空運賃計算"]')
    #确定
    doElement = (By.XPATH,'//div[text()="確定"]')
    #保存
    saveElement = (By.XPATH,'//div[text()="保存"]')