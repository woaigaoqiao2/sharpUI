
from common.deliveryDirector.DeliveryDirector import DeliveryDirector
from common.pl.CreateInvoice import CreateInvoice
from common.shippingAdvice.ShippingAdvice import ShippingAdvice
from util.RandomUtil import RandomUtil

class Jiekou():
    def getDONO(self):
        #这个参数为：do\bl\invoiceNo
        #1.创建invoiceNo
        num = RandomUtil().randoms()
        r = CreateInvoice().practical(invoiceNo=num)
        if(r.get("code")!=200):
            return r

        k = ShippingAdvice.practical(self, num)
        if (k.get("code") != 200):
            return k

        j = DeliveryDirector.practical(self,blNo=num)

        return j






# if __name__ == '__main__':
#     # d = demo()
#     # r = d.test().get('invoiceNo')
#     # print(r)
#     d = Jiekou()
#     r = d.getDONO()
#     if(r.get("code")!=200):
#         return r
#     print(r)