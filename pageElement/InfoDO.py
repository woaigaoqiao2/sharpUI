'''
Created on 2019年5月23日

@author: chinasoft.jl.ma
再次确认配送信息
'''
from selenium.webdriver.common.by import By
class InfoDO():
    
    #DO确定
    doElement = [By.XPATH,'//*[@id="app"]/div[10]/main/div/div[1]/div/div[2]/div/div/div/div[2]/div[4]']
    #检索
    searchElement = [By.XPATH,'//*[@id="app"]/div[22]/main/div/div[1]/div[1]/div[2]/button[1]/div']
    #选择数据 打勾框
    seldataElement = [By.XPATH,'//*[@id="app"]/div[22]/main/div/div[1]/div[1]/div[3]/div[1]/table/tbody/tr[3]/td[1]/div/div/div/div/input']
    #配送再确认
    conOfdisElement = [By.XPATH,'//*[@id="app"]/div[22]/main/div/div[1]/div[1]/div[2]/button[2]/div']                         
    #保存
    preserveElement = [By.XPATH,'//*[@id="app"]/div[27]/main/div/div[1]/div[1]/div[2]/button[1]/div']
    #返回
    returnElement = [By.XPATH,'//*[@id="app"]/div[27]/main/div/div[1]/div[1]/div[2]/button[3]/div/font/font']
    #确定
    OKelement = [By.XPATH,'//*[@id="app"]/div[22]/div/div/div[3]/button/div']