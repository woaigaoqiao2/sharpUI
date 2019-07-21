'''
Created on 2019年5月23日

@author: chinasoft.jl.ma
追加费用
'''
from selenium.webdriver.common.by import By
class AddCost():
    #DO确定
    doElement = [By.XPATH,'//*[@id="app"]/div[10]/main/div/div[1]/div/div[2]/div/div/div/div[2]/div[4]']
    #检索
    searchElement = [By.XPATH,'//*[@id="app"]/div[22]/main/div/div[1]/div[1]/div[2]/button[1]/div']
    #选择数据 打勾框
    seldataElement = [By.XPATH,'//*[@id="app"]/div[22]/main/div/div[1]/div[1]/div[3]/div[1]/table/tbody/tr[7]/td[1]/div/div/div/div/input']
    #追加费用
    addCostElement = [By.XPATH,'//*[@id="app"]/div[22]/main/div/div[1]/div[1]/div[2]/button[3]/div']
    #选择通关料区分
    selMaterials = [By.XPATH,'//*[@id="app"]/div[36]/main/div/div[1]/div[2]/form/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div']
    #选择7栏以上
    selMaterials7 = [By.XPATH,'//*[@id="app"]/div[27]/div/div/div[6]/a/div/div']
    #费用计算
    calCostElement = [By.XPATH,'//*[@id="app"]/div[36]/main/div/div[1]/div[1]/div[2]/button[3]/div']
    #确定
    OKElement = [By.XPATH,'//div[@class="v-card__actions justify-center"]/button']
    #保存
    preserveElement = [By.XPATH,'//*[@id="app"]/div[36]/main/div/div[1]/div[1]/div[2]/button[1]/div']
    
