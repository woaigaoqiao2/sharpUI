from common.companies.Companies import Companies
from common.confirmation.Confirmation import Confirmation
from common.deliveryDirector.DeliveryDirector import DeliveryDirector
from common.pl.CreateInvoice import CreateInvoice
from common.shippingAdvice.ShippingAdvice import ShippingAdvice
from util.RandomUtil import RandomUtil
import json


class GetBLNO():
    """
    演示代码
    """

    def test(self):
        # 这个参数为：do\bl\invoiceNo
        # 1.创建invoiceNo
        num = RandomUtil().randoms()
        r = CreateInvoice().practical(invoiceNo=num)

        if (r.get("code") != 200):
            return r

        r = ShippingAdvice.practical(self, num)
        if (r.get("code") != 200):
            return r
        print('第二步结果', r)

        r = DeliveryDirector().practical(blNo=num)
        if (r.get("code") != 200):
            return r


        r = Companies.practical(self, blNo=num)
        if (r.get("code") != 200):
            return r

        resultF = r.get('result')
        aa = json.loads(resultF)
        bl = {}
        bl['blNo'] = aa.get('blNo')

        if bl.get('blNo') == "":
            print('接口调用失败')

        r = Confirmation.practical(self, **bl)


        return bl.get('blNo')



# if __name__ == '__main__':
#     d = GetBLNO()
#     r = d.test()

