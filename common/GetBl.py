'''
Created on 2019年7月15日

@author: chinasoft.xp.chen
'''
import json
from common.companies.Companies import Companies
from common.confirmation import Confirmation
from common.deliveryDirector.DeliveryDirector import DeliveryDirector
from common.pl.CreateInvoice import CreateInvoice
from common.shippingAdvice.ShippingAdvice import ShippingAdvice
from util.RandomUtil import RandomUtil


class getBl():

    """
    调用接口获取BL
    演示代码
    """
    def getINV(self):
        num = RandomUtil().randoms()
        r = CreateInvoice().practical(invoiceNo=num)
        return r

    def getBL(self,invoiceNo):
        k=ShippingAdvice().practical(invoiceNo)
        return k
    
    
        
    def getDataBl(self):
        a = self.getINV()
        if(a.get("code") !=200):
            return a
        invoiceNo=a.get("invoiceNo")
        r = self.getBL(invoiceNo)
        return invoiceNo,r


