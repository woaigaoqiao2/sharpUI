"""
生成IV No.
"""
import random
import time


def create_IVnum():
    """
    生成IV No.
    :return:
    """
    data = "1234567890zxcvbnmlkjhgfdsaqwertyuiop"
    # 用时间来做随机播种
    random.seed(time.time())
    # 随机选取数据
    sa = []
    for i in range(4):
        sa.append(random.choice(data))
    IvNo = "M" + ''.join(sa)

    return IvNo


if __name__ == '__main__':
    IvNo = create_IVnum()
    print(IvNo)
