from time import sleep
# from jusda.sharpUIauto_cxp.pageElement.login import LoginElement
from pageElement.pllogin.login import LoginElement


class Login(LoginElement):

    def __init__(self):
        self.username='alex'
        self.password='alex'
    
    def test_click_login_btn(self,driver):
        #清空账号输入框
        driver.find_element(*self.userName_element).clear()
        #输入账号
        driver.find_element(*self.userName_element).send_keys(self.username)
        sleep(1)
        #清空密码输入框
        driver.find_element(*self.passWord_element).clear()
        #输入密码
        driver.find_element(*self.passWord_element).send_keys(self.password)
        sleep(1)
        #点击登录
        driver.find_element(*self.loginBtn_element).click()
        sleep(2)
