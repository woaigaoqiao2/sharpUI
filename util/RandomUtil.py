
'''
Created on 2019年6月18日
工具类
@author: chinasoft.l.yu
'''


import random
import string

"""
生成随机数
"""
class RandomUtil():
    
    """
    生成7位唯一随机字符串
    包含字母（大小写）+数字
    """
    def randoms(self):
        str = ''.join(random.sample(string.ascii_letters + string.digits, 7))
        return str
        
    