
"""
Created on 2019年7月5日
sharp 受入確認调用接口API
@author: chinasoft.l.yu
"""
import json

from common.SharpModuleCommon import SharpModuleCommon


class Confirmation():

    httpUrl = "https://sharpsit.jusdaglobal.com/api/delivery-orders"

    """
    查询
    :param blNo
    :param status
    """
    def query(self,**req):
        url = Confirmation.httpUrl
        req['moduleCode'] = "F700"
        req['page'] = 0
        req['size'] = 10
        req['sort'] = ",asc"
        r = SharpModuleCommon.query(self, url, req)
        return r

    """
    操作数据状态为
    受入確認状态
    :param blNo
    """
    def practical(self,**req):
        r = Confirmation.query(self,**req)
        if(r.get("code")!=200):
            return r
        r = json.loads(r.get("result"))
        if(len(r)>0):
            ids = r.get("content")[0].get("id")
            url = "{httpUrl}/{ids}/acceptance-confirm".format(
                httpUrl = Confirmation.httpUrl,ids = ids)
            r = SharpModuleCommon.put(self, url, req)
            return r
        else:
            return {
                "code" :500,
                "result" :"doNo:{doNos},未查询到数据信息".format(
                    doNos = req.get("blNo"))
            }