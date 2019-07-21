'''
Created on 2019年6月18日
sharp 公用模块
接口API
@author: chinasoft.l.yu
'''
import json
from time import sleep
from selenium import webdriver
from business.Login import Login
from pageElement.index.LoginElement import LoginElement
from util.RequestsUtil import requestsUtil
import requests

token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb3VudHJ5X2NvZGUiOiJKUCIsImxvY2FsZV9jb2RlIjoiZW5fVVMiLCJ1c2VyX25hbWUiOiJhbGV4Iiwic2NvcGUiOlsiZm9vIiwicmVhZCIsIndyaXRlIl0sImFwcGxpY2F0aW9uX2NvZGUiOiJJREVBUyIsImV4cCI6MTU2MzY3ODA2OSwidXNlcmFjY291bnRfaWQiOiJVQUNfMTAwNDczIiwianRpIjoiNmY1ZGVlZmItY2U4OC00NDczLWExYTktNzIzNjQ0ZTViMWZiIiwiY2xpZW50X2lkIjoiY2xpZW50IiwidGVuYW50X2NvZGUiOiJTSEFSUCJ9.lYQ0trO-SvWB0hziVQR69H6CT8W_eNTnZRZrep3269tYjQLuWmMGB6ns921VGiogbeAZcx5cNAR6aX_t1EvcAALV9NoP6R05-GMApogPJeer7no55_ceeA-HR5ahOIcAn15ssSr5C74nnxhgfEgWIGpwZdEoPv0RaPf_zU9-WlaN44WuxcdoJ6cOr-UfvjsIO9zz0uAXqlIE_eSiGJhzp_qMV5bnzVBpy_873wPRCCj6BUnHtrSnySiOTZfxRx1zv-POsGZqYEWcZX_6hyITk4p3m9Tvoz0B9iHz5oXfscQd-Lqq5H1QD5StjPqW7-Iuv0v8KAO6DUDYLYsuvO1spg"

class SharpModuleCommon():


    """
    登录模块
    """
    def login(self):
        global token
        if token == "":
            num = 5
            while num >0:
                str = SharpModuleCommon.getToken(self)
                print("-------------token------------:",str)
                if str != "":
                    token = str
                    break
                sleep(1)
        return token




    def getToken(self):
        access_token = ""
        url = "https://sharpsit.jusdaglobal.com/api/login"
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"grant_type\"\r\n\r\npassword\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nalex\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n534b44a19bf18d20b71ecc4eb77c572f\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"tenant_code\"\r\n\r\nSHARP\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Content-Type': "application/json",
            'Authorization': "Basic Y2xpZW50OjYyNjA4ZTA4YWRjMjlhOGQ2ZGJjOTc1NGU2NTlmMTI1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        if response.status_code == 200:
            r = json.loads(response.text)
            access_token = r.get("token_type")+" "+r.get("access_token")
        return access_token

        # print("--------------------开始获取token------------------:",token)
        # if not token:
        #     opt = webdriver.ChromeOptions()
        #     opt.add_argument('--headless')  # 不提供可视化界面
        #     opt.add_argument('--disable-gpu')  # 需要加这个属性规避bug
        #     opt.add_argument('--no-sandbox')
        #     opt.add_argument("blink-settings=imagesEnabled=false")
        #     drivera = webdriver.Chrome(chrome_options=opt)
        #     # drivera = webdriver.Chrome()
        #     url = "https://sharpsit.jusdaglobal.com"
        #     drivera.get(url)
        #     r = drivera.execute_script('return window.localStorage.access_token;')
        #     if r != None:
        #         token = "bearer "+ r
        #         return token
        #     num = 5
        #     while num:
        #         login = Login()
        #         test = LoginElement()
        #
        #         #清空账号输入框
        #         drivera.find_element(*test.userName_element).clear()
        #         #输入账号
        #         drivera.find_element(*test.userName_element).send_keys("alex")
        #         #清空密码输入框
        #         drivera.find_element(*test.passWord_element).clear()
        #         #输入密码
        #         drivera.find_element(*test.passWord_element).send_keys("alex")
        #         #点击登录
        #         drivera.find_element(*test.loginBtn_element).click()
        #         str = drivera.execute_script('return window.localStorage.access_token;')
        #         if str != None:
        #             token = "bearer "+ str
        #             print("--------------------等待获取结束获取token------------------:", token)
        #             return token
        #         sleep(0.2)
        #         num = num -1
        #     # driver.quit()
        # print("--------------------结束获取token------------------:",token)




    """
    查询
    公用方法
    """
    def query(self,url,params):
        headers = {
            'authorization': SharpModuleCommon.login(self)
        }
        return requestsUtil.getRequest(self, url, params, headers)

    """
    put提交数据
    公用方法
    """
    def put(self,url,params):
        headers = {
            "content-type": "application/json;charset=UTF-8",
            'authorization': SharpModuleCommon.login(self)
        }
        return requestsUtil.putRequest(self, url, params, headers)

    """
    post提交数据
    公用方法
    """
    def post(self,url,params):
        headers = {
            "content-type": "application/json;charset=UTF-8",
            'authorization': SharpModuleCommon.login(self)
        }
        return requestsUtil.postRequest(self, url, params, headers)


    """
    查询
    纳入场所
    """
    def queryWarehouses(self):
        url = "https://sharpsit.jusdaglobal.com/api/warehouses/sjl-kv"
        r = SharpModuleCommon.query(self,url,None)
        return r


    """
    文件上传
    :param invoice
    """
    def upload(self,invoice):
        url = "https://sharpsit.jusdaglobal.com/api/files/bls/{invoice}/files".format(
            invoice = invoice)
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\"demo1.png\"\r\nContent-Type: image/png\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"category\"\r\n\r\ninvoice\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            "authorization": SharpModuleCommon.login(self),
            "category":"invoice",
            "content-type": "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
        }
        r = requests.request("POST", url, data=payload, headers=headers)
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\"demo2.png\"\r\nContent-Type: image/png\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"category\"\r\n\r\nbl\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        if(r.status_code != 200):
            return {
                "code":r.status_code,
                "result":r.text
            }
        headers["category"] = "bl"
        r = requests.request("POST", url, data=payload, headers=headers)
        return {
            "code":r.status_code,
            "result":r.text
        }



    def postBigData(self,url,params,key):
        headers = {
            "authorization": SharpModuleCommon.login(self),
            'Content-Type': "application/json",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "sharpsit.jusdaglobal.com",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        return requestsUtil.postBigDataRequest(self, url, params, headers,key)


    def putBigData(self,url,params,key):
        headers = {
            "authorization": SharpModuleCommon.login(self),
            'Content-Type': "application/json",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "sharpsit.jusdaglobal.com",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        return requestsUtil.putBigDataRequest(self, url, params, headers,key)



    def setDo(self,bl,do):
        url = "https://sharpsit.jusdaglobal.com/api/shipping-advices/setDo"
        headers = {
            "authorization": SharpModuleCommon.login(self),
            'Content-Type': "application/json",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "sharpsit.jusdaglobal.com",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        params = {
            "doNo":do,
            "blNo":bl
        }
        return requestsUtil.putRequest(self, url, params, headers)

if __name__ == '__main__':
    test = SharpModuleCommon()
    a = test.setDo("334df","3df")
    # print(a)
