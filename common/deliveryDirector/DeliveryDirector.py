"""

Created on 2019年7月4日

sharp 納入指示メール送信调用接口API

@author: chinasoft.l.yu

"""
import json
from time import sleep

from common.SharpModuleCommon import SharpModuleCommon


class DeliveryDirector():

    #请求url
    httpUrl = "https://sharpsit.jusdaglobal.com/api"

    """
    查询接口
    r 查询条件
    """
    def query(self,**r):
        url = "{urls}/shipping-advices/".format(urls = DeliveryDirector.httpUrl)
        rParams = {}
        if 'blNo' in r.keys() and r['blNo'] != "":
            rParams['blNo'] = r['blNo']
        rParams['view'] = "B0500"
        rParams['moduleCode'] = "F500"
        rParams['page'] = 0
        rParams['size'] = 10
        rParams['sort'] = ",asc"
        return SharpModuleCommon.query(self, url, rParams)



    """
    设置接收人
    """
    def setDeliveryDirector(self,blNo):
        req = {
            "blNo":blNo
        }
        r = DeliveryDirector.query(self,**req)
        if(r.get("code") != 200):
            return r
        result = json.loads(r.get("result"))
        if(len(result)>0):
            id = result.get("content")[0].get("id")
            url = "{urls}/shipping-advices/".format(urls = DeliveryDirector.httpUrl)+id
            r = {}
            r = SharpModuleCommon.query(self, url, r)
            if(r.get("code") != 200):
                return r
            url = "{urls}/shipping-advices/{ids}/set-delivery-director".format(
                urls = DeliveryDirector.httpUrl,ids = id)
            req = json.loads(r.get("result"))
            req['deliveryDirectorEmail1'] = "1111@qq.com"
            req['deliveryDirectorId1'] = "ea65e9c6-71e2-4a76-ac0c-a39dcdc1ef56"
            req['deliveryDirectorName1'] = "Daniel"
            return SharpModuleCommon.put(self,url,req)
        else:
            return {
                "code" :500,
                "result" :"doNo:{doNos},未查询到数据信息".format(
                    doNos = blNo)
            }





    """
    送信
    """
    def sendEail(self,blNo):
        req = {
            "blNo":blNo
        }
        r = DeliveryDirector.query(self,**req)
        if(r.get("code") != 200):
            return r
        result = json.loads(r.get("result"))
        if(len(result)>0):
            id = result.get("content")[0].get("id")
            url = "{urls}/delivery-orders/create-do".format(urls = DeliveryDirector.httpUrl)
            rParams = {
                "said":id
            }
            return SharpModuleCommon.postBigData(self, url, None,rParams)
        else:
            return {
                "code" :500,
                "result" :"doNo:{doNos},未查询到数据信息".format(
                    doNos = blNo)
            }


    """
    操作数据状态为
    指示Mail送信済状态
    :param blNo
    """
    def practical(self,**r):
        blNo = r.get("blNo")
        #设置收信人
        r = DeliveryDirector.setDeliveryDirector(self,blNo)
        if(r.get("code") != 200):
            return r
        #送信
        r = DeliveryDirector.sendEail(self,blNo)
        if(r.get("code") !=201):
            return r
        else:
            return {
                "result":blNo,
                "code":200,
                "msg":"成功!"
            }

if __name__ == '__main__':
    ss = DeliveryDirector()
    r = {
        "blNo":"pPoC14Y"
    }
    test = ss.practical(**r)
    print(test.get("code"))
    print(test.get("result"))