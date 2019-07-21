'''
Created on 2019年5月20日
@author: chinasoft.jl.ma
登录方法
'''
from pageElement.index.LoginElement import LoginElement
from time import sleep
import os,ddt,json
#from openpyxl import load_workbook
   
class Login(LoginElement):
    
    
    def __init__(self):
#         wb = load_workbook(r'C:\eclipse-py\sharpUIauto\data\case.xlsx')
#         ws = wb.get_sheet_by_name("case")
#         cell = ws["c2"].value
#         data = json.loads(cell)
#         self.username = data.get("username")
#         self.password = data.get("pwd")
        self.username = 'alex'
        self.password = 'alex'
    
    def test_click_login_btn(self, driver):
        #清空账号输入框
        driver.find_element(*self.userName_element).clear()
        #输入账号
        driver.find_element(*self.userName_element).send_keys(self.username)
        
        #清空密码输入框
        driver.find_element(*self.passWord_element).clear()
        #输入密码
        driver.find_element(*self.passWord_element).send_keys(self.password)
        
        #点击登录
        driver.find_element(*self.loginBtn_element).click()
        sleep(5)