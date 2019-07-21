'''
Created on 2019年7月9日
ShippingAdvice 功能
接口API
@author: chinasoft.l.yu
'''
import json
import time

from common.SharpModuleCommon import SharpModuleCommon


class ShippingAdvice():

    httpUrl = "https://sharpsit.jusdaglobal.com/api/"

    """
    查询
    :param invoiceNo
    """
    def queryInvoiceNo(self,invoiceNo):
        url = "{httpUrl}commercial-invoices/unused-invoice".format(
            httpUrl = ShippingAdvice.httpUrl)
        rParams = {}
        rParams['invoiceNo'] = invoiceNo
        rParams['page'] = 0
        rParams['size'] = 5
        rParams['sort'] = "invoiceNo,asc"
        return SharpModuleCommon.query(self, url, rParams)


    def queryInvoice(self,invoiceNo):
        r = ShippingAdvice.queryInvoiceNo(self,invoiceNo)
        if(r.get("code") != 200):
            return r

        r = json.loads(r.get("result"))
        if(len(r)<=0):
            return r

        id = r.get("content")[0].get("id")
        url = "{httpUrl}commercial-invoices/{ids}".format(
            httpUrl = ShippingAdvice.httpUrl,ids = id)
        rParams = {}
        return SharpModuleCommon.query(self, url, rParams)


    def queryInvoiceInfo(self,invoiceNo):
        url = "{httpUrl}/shipping-advices".format(
            httpUrl = ShippingAdvice.httpUrl)
        rParams = {}
        rParams['view'] = "B0400"
        rParams['blNo'] = invoiceNo
        rParams['page'] = 0
        rParams['size'] = 5
        rParams['sort'] = ",asc"
        return SharpModuleCommon.query(self, url, rParams)

    """
    操作数据状态为
    SA登録済状态
    :param invoiceNo
    """
    def practical(self,invoiceNo):
        # 查询
        req = ShippingAdvice.queryInvoice(self,invoiceNo)
        if(req.get("code") != 200):
            return req

        #上传文件
        r = SharpModuleCommon.upload(self,invoiceNo)
        if(r.get("code") != 200):
            return r

        #保存
        result = json.loads(req.get("result"))
        if(len(result)<=0):
            return req

        req = result.get("packages")
        req = ShippingAdvice.createReq(self,invoiceNo,req)
        url = "{httpUrl}shipping-advices".format(
            httpUrl = ShippingAdvice.httpUrl)
        querystring = {"view":"B0401"}
        r = SharpModuleCommon.postBigData(self,url,req,querystring)
        if(r.get("code") != 201):
            return r

        #查询数据
        r = ShippingAdvice.queryInvoiceInfo(self,invoiceNo)
        if(r.get("code") != 200):
            return r
        r = json.loads(r.get("result")).get("content")
        if(len(r)<=0):
            return r
        ids = r[0].get("id")
        url = "{httpUrl}shipping-advices/{ids}".format(
            httpUrl = ShippingAdvice.httpUrl,ids = ids)
        r = SharpModuleCommon.query(self, url, None)
        if(r.get("code") != 200):
            return r

        #修改数据
        req = json.loads(r.get("result"))
        querystring = {"view":"B0401"}
        r = SharpModuleCommon.putBigData(self, url, req,querystring)
        if(r.get("code") != 200):
            return r
        #送信
        url = "{httpUrl}shipping-advices/{ids}/shipping-advice-send".format(
            httpUrl = ShippingAdvice.httpUrl,ids = ids)
        r = SharpModuleCommon.put(self, url, None)
        if(r.get("code") !=200):
            return r
        #绑定BL\DO关系
        r = SharpModuleCommon.setDo(self,invoiceNo,invoiceNo)
        return r



    def createReq(self,invoiceNo,req):
        r = {}
        r["packages"] = req
        r['packages'][0]["containerNo"] = invoiceNo
        r['packages'][0]["containerTypeId"] = "CONTAINER_TYPE-20F"
        r['packages'][0]["shippedCarton"] = 1
        r['packages'][0]["seq"] = time.time()

        r["shipmentType"] = "SA"
        r["stackTypeId"] = "STACK_TYPE-FCL"  #暂时写死
        r["transportModeId"] = req[0].get("transportModeId")
        r["dischargePortCode"] = req[0].get("dischargePortCode")
        r["loadingPortCode"] = req[0].get("loadingPortCode")
        r["partnerId"] = req[0].get("partnerId")
        r["etd"] = req[0].get("etd")
        r["currencyCode"] = req[0].get("currencyCode")
        r["siNo"] = invoiceNo
        r["customsDirectorId"] = "8f44e2ae-2b7d-471d-ba2c-cc957e207a17" #暂时写死
        r["masterBlNo"] = invoiceNo
        r["houseBlNo"] = invoiceNo
        r["requestDate"] = "2019-07-08"
        r["blIssueDate"] = "2019-07-08"
        r["eta"] = "2019-07-08"
        r["volNo"] = invoiceNo
        r["shipName"] = invoiceNo
        r["commodityTypeId"] = "COMMODITY_TYPE-SMART_PHONE"
        r["forwarderId"] = "c2c81b72-b86a-4ce5-b916-7a9615a0c805"
        r["blNo"] = invoiceNo
        return r