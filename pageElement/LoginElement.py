'''
Created on 2019年5月20日

@author: chinasoft.jl.ma
登录页面元素对象
'''

from selenium.webdriver.common.by import By

class LoginElement(object):
   
    #用户名
    userName_element = [By.XPATH,'//*[@type="text"]']
    #密码
    passWord_element = [By.XPATH,'//*[@aria-label="パスワード"]']
    #登录按钮
    loginBtn_element = [By.XPATH,'//div[@class="v-btn__content" and text()="ログイン"]']
