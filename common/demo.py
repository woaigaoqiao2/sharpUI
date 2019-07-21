from common.companies.Companies import Companies
from common.confirmation import Confirmation
from common.deliveryDirector.DeliveryDirector import DeliveryDirector
from common.pl.CreateInvoice import CreateInvoice
from common.shippingAdvice.ShippingAdvice import ShippingAdvice
from util.RandomUtil import RandomUtil

class demo():

    """
    演示代码
    """
    def test(self):
        #这个参数为：do\bl\invoiceNo
        #1.创建invoiceNo
        num = RandomUtil().randoms()
        r = CreateInvoice().practical(invoiceNo=num)
        if(r.get("code")!=200):
            return r
        return r


if __name__ == '__main__':
    d = demo()
    r = d.test().get('invoiceNo')
    print(r)
