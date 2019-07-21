'''
Created on 2019年6月21日

@author: chinasoft.l.yu
'''
import datetime

from common.SharpModuleCommon import SharpModuleCommon
import json


"""
纳入指示

"""
httpUrl = "https://sharpsit.jusdaglobal.com/api"
class Companies():
    """
       纳入指示查询功能
    :params doNo    doNo
    :params blNo    blNo
    :params operateDirectorId    纳入指示者
    :params partnerId    海外取引先
    :params showStatus   纳入指示status
    """
    def queryDeliveryOrders(self,**params):
        rParams = {}
        url = "{urls}/delivery-orders".format(urls = httpUrl)
        if  'doNo' in params.keys() and params['doNo'] != "":
            rParams['doNo'] = params['doNo']
        if 'blNo' in params.keys() and params['blNo'] != "":
            rParams['blNo'] = params['blNo']
        if 'operateDirectorId' in params.keys() and params['operateDirectorId'] !="" :
            rParams['operateDirectorId'] = params['operateDirectorId']
        if 'partnerId' in params.keys() and params['partnerId'] !="" :
            rParams['partnerId'] = params['partnerId']
        if 'showStatus' in params.keys() and params['showStatus'] !="" :
            rParams['showStatus'] = params['showStatus']
        rParams['moduleCode'] = "F600"
        rParams['page'] = 0
        rParams['size'] = 10
        rParams['sort'] = "blNo,asc"
        return SharpModuleCommon.query(self, url, rParams)

    """
    纳入场所制定
    :params doNo    doNo
    :params finallyWarehouseId    最终纳入场所
    :params forecastDeliveryDate    纳入予定日
    :params forecastDeliveryTime    时间
    """
    def updateInfo(self,**params):
        rParams = {}
        if  'blNo' in params.keys() and params['blNo'] != "":
            rParams['blNo'] = params['blNo']
            r = Companies.queryDeliveryOrders(self, **rParams)
            if(r.get("code")!=200):
                return r
            r = json.loads(r.get("result")).get("content")
            if len(r) > 0:
                doN = r[0].get("id")
                url = "{urls}/delivery-orders/{doNos}/updateInfo".format(
                    urls = httpUrl,doNos = doN)
                r = SharpModuleCommon.queryWarehouses(self)
                if(r.get("code")!=200):
                    return r
                finallyWarehouseId = json.loads(r.get("result"))[0].get("value")
                rParams['finallyWarehouseId'] = finallyWarehouseId
                rParams['forecastDeliveryDate'] = str(datetime.date.today())
                rParams["forecastDeliveryTime"] = "10:00:00"
                return SharpModuleCommon.put(self, url, rParams)
            return {
                "code" :500,
                "result" :"doNo:{doNos},未查询到数据信息".format(doNos = params['doNo'])
            }


    def sendEmail(self,blNo):
        rParams = {}
        if  blNo != "":
            rParams['blNo'] = blNo
            data = Companies.queryDeliveryOrders(self, **rParams)
            r = json.loads(data.get("result")).get("content")
            if len(r) > 0:
                doN = r[0].get("id")
                url = "{urls}/delivery-orders/{doNos}/send-email-date".format(
                    urls = httpUrl,doNos = doN)
                params = {
                }
                return SharpModuleCommon.put(self, url, params)
            return {
                "code" :500,
                "result" :"doNo:{doNos},未查询到数据信息".format(doNos = blNo)
            }


    """
    操作数据状态为
    納入指示済状态
    :param blNo
    """
    def practical(self,**req):
        r = Companies.updateInfo(self,**req)
        if(r.get("code")!=200):
            return r
        r = Companies.sendEmail(self,req.get("blNo"))
        return r