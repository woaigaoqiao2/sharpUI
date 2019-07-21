'''
Created on 2019年6月21日

@author: chinasoft.l.yu
'''

from common.SharpModuleCommon import SharpModuleCommon
import json


"""
纳入指示

"""
httpUrl = "https://sharpsit.jusdaglobal.com/api"
class CompaniesRequest():
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
        if  'doNo' in params.keys() and params['doNo'] != "":
            rParams['doNo'] = params['doNo']
        data = CompaniesRequest.queryDeliveryOrders(self, **rParams)
        r = json.loads(data.get("result")).get("content")
        if len(r) > 0:
            doN = r[0].get("id")
            url = "{urls}/delivery-orders/{doNos}/updateInfo".format(urls = httpUrl,doNos = doN)
            if  'finallyWarehouseId' in params.keys() and params['finallyWarehouseId'] != "":
                rParams['finallyWarehouseId'] = params['finallyWarehouseId']
            if  'forecastDeliveryDate' in params.keys() and params['forecastDeliveryDate'] != "":
                rParams['forecastDeliveryDate'] = params['forecastDeliveryDate']
            if  'forecastDeliveryTime' in params.keys() and params['forecastDeliveryTime'] != "":
                rParams['forecastDeliveryTime'] = params['forecastDeliveryTime']
            rParams["finallyWarehouseId"] = "12f7914e-531e-41f6-be7c-e89186d39125" ##该值当前版本写死
            return SharpModuleCommon.post(self, url, rParams)
        return {
            "code" :500,
            "result" :"doNo:{doNos},未查询到数据信息".format(doNos = params['doNo'])
        }
        
    
    def sendEmail(self,doNo):
        rParams = {}
        if  doNo != "":
            rParams['doNo'] = doNo

        data = CompaniesRequest.queryDeliveryOrders(self, **rParams)
        r = json.loads(data.get("result")).get("content")
        if len(r) > 0:
            doN = r[0].get("id")
            url = "{urls}/delivery-orders/{doNos}/send-email-date".format(urls = httpUrl,doNos = doN)
            params = {
            }
            return SharpModuleCommon.post(self, url, params)
        return {
            "code" :500,
            "result" :"doNo:{doNos},未查询到数据信息".format(doNos = doNo)
        }
    
    
    
# aa = CompaniesRequest()
# r = {}
# r['doNo'] = "do2601"
# r['finallyWarehouseId'] = '12f7914e-531e-41f6-be7c-e89186d39125'
# r['forecastDeliveryDate'] = "2019-6-22"
# r['forecastDeliveryTime'] = "14:00:00"
#
# print(aa.updateInfo(**r))
# print(aa.sendEmail(r['doNo']))
