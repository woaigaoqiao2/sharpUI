'''
Created on 2019年6月18日

http请求接口API

@author: chinasoft.l.yu
'''
#coding=utf-8
import requests,json

from util.logs import logs


class requestsUtil():
    
    def getRequest(self,url,params,headers):
        """
        get请求
        :params url    请求url
        :params params 请求参数
        :params headers 请求头
        """
        num = 5
        result = None
        while num > 0:
            num = num - 1
            try:
                result = requests.get(url,params=params,headers=headers)
                result.encoding = 'UTF-8'
                if result.status_code == 200 or result.status_code == 201:
                    break
                if num == 0:
                    msg = "\n调用接口："+url+" \n返回结果code："+ str(result.status_code) +" \n返回结果："+ result.text
                    logs("Interface").info_log(msg)
            except Exception as e:
                msg = "调用接口："+url+" 异常!"
                logs("Interface").error_log(msg)
                logs("Interface").error_log(e)
                return {
                    "code": 500,
                    "result": 'get请求出错，出错原因:%s'%e
                }
        return {
            "code":result.status_code,
            "result":result.text
        }
        
    def postRequest(self, url, params,headers):
        """
        post请求
        :params url    请求url
        :params params 请求参数
        :params headers 请求头
        """    
        data = json.dumps(params)
        num = 5
        r = ""
        while num >0:
            num = num - 1
            try:
                r = requests.post(url,params=data,headers=headers)
                r.encoding = 'UTF-8'
                if r.status_code == 200 or r.status_code == 201:
                    break
                if num == 0:
                    msg = "\n调用接口："+url+" \n返回结果code："+ str(r.status_code) +" \n返回结果："+ r.text
                    logs("Interface").info_log(msg)
            except Exception as e:
                msg = "调用接口："+ url +" 异常!"
                logs("Interface").error_log(msg)
                logs("Interface").error_log(e)
                return {
                    "code": 500,
                    "result": 'post请求出错，出错原因:%s' % e
                }

        return {
            "code":r.status_code,
            "result":r.text
        }
    def putRequest(self,url,params,headers):
        """
        put请求
        :params url    请求url
        :params params 请求参数
        :params headers 请求头
        """
        r = ""
        num = 5
        while num > 0:
            num = num - 1
            try:
                data = json.dumps(params)
                r = requests.put(url,data,headers=headers)
                r.encoding = 'UTF-8'
                if r.status_code == 200 or r.status_code == 201:
                    break
                if num == 0:
                    msg = "\n调用接口："+url+" \n返回结果code："+ str(r.status_code) +" \n返回结果："+ r.text
                    logs("Interface").info_log(msg)
            except Exception as e:
                msg = "调用接口："+url+" 异常!"
                logs("Interface").error_log(msg)
                logs("Interface").error_log(e)
                return {
                    "code": 500,
                    "result": 'put请求出错，出错原因:%s' % e
                }
        return {
            "code":r.status_code,
            "result":r.text
        }

    def putBigDataRequest(self,url,params,headers,key):
        """
        put请求
        :params url    请求url
        :params params 请求参数
        :params headers 请求头
        """
        num = 5
        r = ""
        while num > 0:
            num = num - 1
            try:
                data = json.dumps(params)
                r = requests.request("PUT", url, data=data.encode(), headers=headers,params=key)
                r.encoding = 'UTF-8'
                if r.status_code == 200 or r.status_code == 201:
                    break
                if num == 0:
                    msg = "\n调用接口："+url+" \n返回结果code："+ str(r.status_code) +" \n返回结果："+ r.text
                    logs("Interface").info_log(msg)
            except Exception as e:
                msg = "调用接口："+url+" 异常!"
                logs("Interface").error_log(msg)
                logs("Interface").error_log(e)
                return {
                    "code": 500,
                    "result": 'put请求出错，出错原因:%s' % e
                }
        return {
            "code":r.status_code,
            "result":r.text
        }

    def postBigDataRequest(self, url, params,headers,key):
        """
        post请求
        :params url    请求url
        :params params 请求参数
        :params headers 请求头
        """
        r = ""
        num = 5
        while num > 0:
            num = num - 1
            data = json.dumps(params,ensure_ascii=False)
            try:
                r = requests.request("POST", url, data=data.encode(), headers=headers,params=key)
                r.encoding = 'UTF-8'
                if r.status_code == 200 or r.status_code == 201:
                    break
                if num == 0:
                    msg = "\n调用接口："+url+" \n返回结果code："+ str(r.status_code) +" \n返回结果："+ r.text
                    logs("Interface").info_log(msg)
            except Exception as e:
                msg = "调用接口："+url+" 异常!"
                logs("Interface").error_log(msg)
                logs("Interface").error_log(e)
                return {
                    "code": 500,
                    "result": 'post请求出错，出错原因:%s' % e
                }
        return {
            "code":r.status_code,
            "result":r.text
        }