'''
Created on 2019年5月20日

@author: chinasoft.jl.ma
BL確認完了送信
'''
from selenium.webdriver.common.by import By
class BlElement(object):
    #BL確認完了送信
    BL_element=[By.XPATH,'//*[@id="app"]/div[10]/main/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]']
    #検索
    Search_element=[By.XPATH,"//div[@id='app']/div[15]/main/div/div/div[2]/div/button"]
    #勾选框
    Option_element=[By.XPATH,"//td/div/div/div/div/div"]
    #確認完了通知メール
    Inform_element=[By.XPATH,'//*[@id="app"]/div[15]/main/div/div[1]/div[2]/div/button[3]/div']
    #弹窗确定
    Sure_element=[By.XPATH,'//*[@id="app"]/div[15]/div/div/div[3]/button']
    #成功的文本
    Success_element=[By.XPATH,'//*[@id="app"]/div[15]/main/div/div[1]/div[3]/div[1]/div[1]/table/tbody/tr[1]/td[5]']