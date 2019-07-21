from common.pl.CreateInvoice import CreateInvoice
from util.RandomUtil import RandomUtil


class IV_NO():

    @staticmethod
    def yj_randoms():
        # 1.创建invoiceNo
        num = RandomUtil().randoms()
        r = CreateInvoice().practical(invoiceNo=num)
        if (r.get("code") != 200):
            return r
        return r


if __name__ == '__main__':
    d = IV_NO()
    # r = d.yj_randoms().get('invoiceNo')
    # print(r)
    # r = IV_NO.yj_randoms().get('invoiceNo')
    # print(r)
