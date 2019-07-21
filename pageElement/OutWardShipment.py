'''
Created on 2019年5月22日
@author: chinasoft.jl.ma
运赁外货登录
'''
from selenium.webdriver.common.by import By

class OutWardShipment(object):
    #首页 运凭外货按钮
    outWardElement = [By.XPATH,'//*[@id="app"]/div[10]/main/div/div[1]/div/div[2]/div/div/div/div[1]/div[4]/div[2]']
    #BL提单号
    BLNoEelement = [By.XPATH,'//input[@aria-label="B/L NO"]']                    
    #检索按钮
    searchElement = [By.XPATH,'//*[@id="app"]/div[15]/main/div/div[1]/div[1]/div[2]/button[1]/div']
    #选择数据打勾框
    selDataElement = [By.XPATH,'//*[@id="app"]/div[15]/main/div/div[1]/div[2]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/input']
    #海上，航空运凭计算按钮
    transportationElement = [By.XPATH,'//*[@id="app"]/div[15]/main/div/div[1]/div[1]/div[2]/button[4]/div']
    #FEE金额,先清空费用再进行修改
    FEEElement = [By.XPATH,'//*[@id="app"]/div[30]/main/div/div[1]/div[5]/div[2]/div/div/table/tbody/tr[1]/td[2]/div/div/div[1]/div/input']
    #保存
    preserveElement = [By.XPATH,'//*[@id="app"]/div[30]/main/div/div[1]/div[1]/div[2]/button[2]']
    #找到此按钮  发送TAB 保存按钮可见
    toPreserveElement = [By.XPATH,'//*[@id="app"]/div[30]/nav/div/div[3]/div[4]/div/button/div/div/div[3]']
