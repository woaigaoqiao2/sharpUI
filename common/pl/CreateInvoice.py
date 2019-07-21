"""
#!/usr/bin/env python
#-*- coding: utf-8 -*-
@Time    : 2019/7/4 14:09
@Author  : 二部测试-陈兴川
@File    : CreateInvoice.py
@email    :chenxingchuan@chinasoftinc.com
"""
import json,time
from common.SharpModuleCommon import SharpModuleCommon
from util.RandomUtil import RandomUtil

'''
ivn p/l登录新建有偿新规
'''

class CreateInvoice(SharpModuleCommon):

    url = "https://sharpsit.jusdaglobal.com"

    '''
    PO查询检出数据
    '''
    def po_jianchu(self):
        url = '{}/api/purchase-orders'.format(CreateInvoice.url)
        params = {
            "page":"0",
            "size":"20",
            "sort":"poNo"
        }
        return self.query(url,params)


    def practical(self,invoiceNo=None, carton_end_no=1,
                  carton_start_no=1, creationDate="2019-07-15",
                  etd="2019-06-06"):
        '''PO添加保存单
        invoiceNo：输入invoiceNo号，可默认随机生成
        carton_end_no：集装箱截止号，默认为1
        carton_start_no：集装箱开始号，默认为1
        creationDate:表单创建日，默认为"2019-07-05",
        etd：默认为"2019-06-06“
        '''
        #查询出系统中数据
        datas = self.po_jianchu()
        if datas.get("code") != 200:
            print("INV检出接口失败：code={}".format(datas.get("code")))
            return datas.get("result")
        a = datas["result"]
        a = json.loads(a)
        # 添加查询出来第1条数据
        data = a["content"][0]
        # 生成可用的invoiceNo号
        invoiceNo = self.createInvoiceNo(invoiceNo)
        r = self.checkOnly(invoiceNo)
        if r.get("code") == 200:
            datas = self.createData(data, invoiceNo, carton_end_no, carton_start_no, creationDate, etd)
        else:
            print("查询invoiceNo是否是唯一接口失败：code={}".format(r.get("code")))
            return r
        # 	return self.post(url, datas)
        url = "{}/api/commercial-invoices".format(CreateInvoice.url)
        # 保存条件的数据
        r = self.postBigData(url, datas, key=None)
        if r.get("code") == 201:
            return {
                "code": 200,
                "result": "成功",
                "invoiceNo":invoiceNo
            }
        else:
            print("INV创建有偿新规失败：code={}".format(r.get("coed")))
            return r



    def createInvoiceNo(self,invoiceNo):
        #生成InvoiceNo号
        if invoiceNo==None:
            invoiceNo =RandomUtil().randoms()
        return invoiceNo

    def inv_query(self,**params):
        #查询InvoiceNo号是否占用
        rParams = {}
        url1 ="{}/api/commercial-invoices".format(CreateInvoice.url)
        if 'invoiceNo' in params.keys() and params['invoiceNo'] != "":
            rParams['invoiceNo'] = params['invoiceNo']
            rParams['page'] = 0
            rParams['size'] = 10
            rParams['sort'] = ",asc"
        return SharpModuleCommon().query(url1, rParams)


    def checkOnly(self,invoiceNo):
        '''检查InvoiceNo号是否占用'''
        rParams = {}
        rParams['invoiceNo'] = invoiceNo
        #查询InvoiceNo号是否占用
        rs = self.inv_query(**rParams)
        if  rs.get("code") == 200:
            count = int(json.loads(rs.get("result")).get("totalElements"))
            if (count != 0):
                print("invoiceNo:{} 已存在".format(rs.get("result")["invoiceNo"]))
                return {
                    "code": 100,
                    "result": "invoiceNo:{invoiceNum} 已存在".format(invoiceNum=invoiceNo)
                }
            return {
                "code": 200,
                "result": "成功"
            }
        return rs

    def createData(self,data, invoiceNo, carton_end_no, carton_start_no, creationDate,etd):

        '''生成需要创建的数据
        invoiceNo：输入invoiceNo号，可默认随机生成
        carton_end_no：集装箱截止号，默认为1
        carton_start_no：集装箱开始号，默认为1
        creationDate:表单创建日，默认为"2019-07-05",
        etd：默认为"2019-07-06"
        '''
        print("invoiceNo：{}".format(invoiceNo))
        seq=int(time.time()*1000)
        Params = {
            "items": [{
                "partnerId":data["partnerId"],
                "partnerCode":data["partnerCode"],
                "partnerName":data["partnerName"],
                "buId":data["buId"],
                "buCode":data["buCode"],
                "buName":data["buName"],
                "departmentId":data["departmentId"],
                "departmentCode":data["departmentCode"],
                "departmentName":data["departmentName"],
                "loadingPortCode":data["loadingPortCode"],
                "loadingPortName":data["loadingPortName"],
                "dischargePortCode":data["dischargePortCode"],
                "dischargePortName":data["dischargePortName"],
                "incotermId":data["incotermId"],
                "incotermCode":data["incotermCode"],
                "transportModeId":data["transportModeId"],
                "transportModeCode":data["transportModeCode"],
                "itemClassfication":data["itemClassfication"],
                "classificationName":data["classificationName"],
                "currencyCode":data["currencyCode"],
                "currencyName":data["currencyName"],
                "skuCode":data["skuCode"],
                "skuSupplierCode":data["skuSupplierCode"],
                "skuName":data["skuName"],
                "skuSupplierName":data["skuSupplierName"],
                "nw":data["nw"],
                "gw":data["gw"],
                "m3":data["m3"],
                "innerSatCode":data["innerSatCode"],
                "innerSatName":data["innerSatName"],
                "outerSatCode":data["outerSatCode"],
                "outerSatName":data["outerSatName"],
                "productSatCode":data["productSatCode"],
                "productSatName":data["productSatName"],
                "productCode":data["productCode"],
                "productName":data["productName"],
                "scWarehouseId":data["scWarehouseId"],
                "scWarehouseCode":data["scWarehouseCode"],
                "scWarehouseName":data["scWarehouseName"],
                "warehouseSatName":data["warehouseSatName"],
                "warehouseSatCode":data["warehouseSatCode"],
                "originCountryName":data["originCountryName"],
                "originCountryCode":data["originCountryCode"],
                "unit":data["unit"],
                "id":None,  #---------1
                "poId":data["poId"],
                "poNo":data["poNo"],
                "lotNo":data["lotNo"],
                "siNo":data["siNo"],
                "orderCode":data["orderCode"],
                "orderName":data["orderName"],
                "consignorCode":data["consignorCode"],
                "consignorName":data["consignorName"],
                "qty":data["qty"], #-------1
                "unitPrice":data["unitPrice"],
                "masterStatus":data["masterStatus"],
                "finishedQty":data["finishedQty"],
                "createdInvoice":data["createdInvoice"],
                "leftInvoice":data["leftInvoice"],
                "leftSupply":data["leftSupply"],
                "status":data["status"],
                "handleStatus":data["handleStatus"],
                "countEIAJ":data["countEIAJ"],
                "paid":data["paid"],
                "handModel":data["handModel"],
                "seq":seq,#--------1
                "create_date":data["create_date"],
                "productionDate":data["productionDate"],
                "sourcePoId":data["sourcePoId"],
                "payment":data["payment"],
                "subTotal":data["subTotal"],
                "poItemId":data["poId"],#-------1
                "max":data["leftInvoice"]#--------1
            }],
            "packages": [{
                "item": {
                    "partnerId":data["partnerId"],
                    "partnerCode":data["partnerCode"],
                    "partnerName":data["partnerName"],
                    "buId":data["buId"],
                    "buCode":data["buCode"],
                    "buName":data["buName"],
                    "departmentId":data["departmentId"],
                    "departmentCode":data["departmentCode"],
                    "departmentName":data["departmentName"],
                    "loadingPortCode":data["loadingPortCode"],
                    "loadingPortName":data["loadingPortName"],
                    "dischargePortCode":data["dischargePortCode"],
                    "dischargePortName":data["dischargePortName"],
                    "incotermId":data["incotermId"],
                    "incotermCode":data["incotermCode"],
                    "transportModeId":data["transportModeId"],
                    "transportModeCode":data["transportModeCode"],
                    "itemClassfication":data["itemClassfication"],
                    "classificationName":data["classificationName"],
                    "currencyCode":data["currencyCode"],
                    "currencyName":data["currencyName"],
                    "skuCode":data["skuCode"],
                    "skuSupplierCode":data["skuSupplierCode"],
                    "skuName":data["skuName"],
                    "skuSupplierName":data["skuSupplierName"],
                    "nw":data["nw"],
                    "gw":data["gw"],
                    "m3":data["m3"],
                    "innerSatCode":data["innerSatCode"],
                    "innerSatName":data["innerSatName"],
                    "outerSatCode":data["outerSatCode"],
                    "outerSatName":data["outerSatName"],
                    "productSatCode":data["productSatCode"],
                    "productSatName":data["productSatName"],
                    "productCode":data["productCode"],
                    "productName":data["productName"],
                    "scWarehouseId":data["scWarehouseId"],
                    "scWarehouseCode":data["scWarehouseCode"],
                    "scWarehouseName":data["scWarehouseName"],
                    "warehouseSatName":data["warehouseSatName"],
                    "warehouseSatCode":data["warehouseSatCode"],
                    "originCountryName":data["originCountryName"],
                    "originCountryCode":data["originCountryCode"],
                    "unit":data["unit"],
                    "id":None, #-------1
                    "poId":data["poId"],
                    "poNo":data["poNo"],
                    "lotNo":data["lotNo"],
                    "siNo":data["siNo"],
                    "orderCode":data["orderCode"],
                    "orderName":data["orderName"],
                    "consignorCode":data["consignorCode"],
                    "consignorName":data["consignorName"],
                    "qty":carton_end_no - carton_start_no + 1,  #--------1
                    "unitPrice":data["unitPrice"],
                    "masterStatus":data["masterStatus"],
                    "finishedQty":data["finishedQty"],
                    "createdInvoice":data["createdInvoice"],
                    "leftInvoice":data["leftInvoice"],
                    "leftSupply":data["leftSupply"],
                    "status":data["status"],
                    "handleStatus":data["handleStatus"],
                    "countEIAJ":data["countEIAJ"],
                    "paid":data["paid"],
                    "handModel":data["handModel"],
                    "seq":seq, #--------1
                    "create_date":data["create_date"],
                    "productionDate":data["productionDate"],
                    "sourcePoId":data["sourcePoId"],
                    "payment":data["payment"],
                    "subTotal":data["subTotal"],
                    "poItemId":data["poId"], #-------1
                    "max":data["leftInvoice"]#-------1
                },
                "partnerId":data["partnerId"],
                "partnerCode":data["partnerCode"],
                "partnerName":data["partnerName"],
                "buId":data["buId"],
                "buCode":data["buCode"],
                "buName":data["buName"],
                "departmentId":data["departmentId"],
                "departmentCode":data["departmentCode"],
                "departmentName":data["departmentName"],
                "loadingPortCode":data["loadingPortCode"],
                "loadingPortName":data["loadingPortName"],
                "dischargePortCode":data["dischargePortCode"],
                "dischargePortName":data["dischargePortName"],
                "incotermId":data["incotermId"],
                "incotermCode":data["incotermCode"],
                "transportModeId":data["transportModeId"],
                "transportModeCode":data["transportModeCode"],
                "itemClassfication":data["itemClassfication"],
                "classificationName":data["classificationName"],
                "currencyCode":data["currencyCode"],
                "currencyName":data["currencyName"],
                "skuCode":data["skuCode"],
                "skuSupplierCode":data["skuSupplierCode"],
                "skuName":data["skuName"],
                "skuSupplierName":data["skuSupplierName"],
                "nw":data["nw"],
                "gw":data["gw"],
                "m3":data["m3"],
                "innerSatCode":data["innerSatCode"],
                "innerSatName":data["innerSatName"],
                "outerSatCode":data["outerSatCode"],
                "outerSatName":data["outerSatName"],
                "productSatCode":data["productSatCode"],
                "productSatName":data["productSatName"],
                "productCode":data["productCode"],
                "productName":data["productName"],
                "scWarehouseId":data["scWarehouseId"],
                "scWarehouseCode":data["scWarehouseCode"],
                "scWarehouseName":data["scWarehouseName"],
                "warehouseSatName":data["warehouseSatName"],
                "warehouseSatCode":data["warehouseSatCode"],
                "originCountryName":data["originCountryName"],
                "originCountryCode":data["originCountryCode"],
                "id":None,  #-------1
                "poId":data["poId"],
                "poNo":data["poNo"],
                "lotNo":data["lotNo"],
                "siNo":data["siNo"],
                "orderCode":data["orderCode"],
                "orderName":data["orderName"],
                "consignorCode":data["consignorCode"],
                "consignorName":data["consignorName"],
                "qty":data["qty"],
                "unitPrice":data["unitPrice"],
                "masterStatus":data["masterStatus"],
                "finishedQty":data["finishedQty"],
                "createdInvoice":data["createdInvoice"],
                "leftInvoice":data["leftInvoice"],
                "leftSupply":data["leftSupply"],
                "status":data["status"],
                "handleStatus":data["handleStatus"],
                "countEIAJ":data["countEIAJ"],
                "paid":data["paid"],
                "handModel":data["handModel"],
                "seq":seq,
                "create_date":data["create_date"],
                "productionDate":data["productionDate"],
                "sourcePoId":data["sourcePoId"],
                "payment":data["payment"],
                "subTotal":data["subTotal"],
                "poItemId":data["poId"],
                "max":data["leftInvoice"],
                "itemSeq":seq,
                "totalQty":carton_end_no - carton_start_no + 1,
                "flag":"1",
                "cartonStartNo":carton_start_no,
                "cartonEndNo":carton_end_no,
                "perCartonQty":"1",
                "netWeight":"1",
                "grossWeight":"1",
                "volume":"1"
            }],
            "invoiceNo":invoiceNo,
            "partnerId":data["partnerId"],
            "loadingPortCode":data["loadingPortCode"],
            "incotermId":data["incotermId"],
            "dischargePortCode":data["dischargePortCode"],
            "currencyCode":data["currencyCode"],
            "transportModeId":data["transportModeId"],
            "creationDate":creationDate,
            "etd":etd
        }
        return Params