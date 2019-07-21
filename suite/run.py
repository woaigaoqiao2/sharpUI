import  unittest,os
from BeautifulReport import BeautifulReport
import datetime
import sys
sys.path.append('E:\sharpUI')

date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#获取项目路径
path=os.path.dirname(os.getcwd())
#获取case路径
casePath=path+'\\case'
#获取report路径
reprotPath = path + '\\report'

#收集测试用例
testCase = unittest.defaultTestLoader.discover(start_dir=casePath, pattern='TestFreePay.py')
print(testCase.countTestCases())
#执行测试用例
runner = BeautifulReport(testCase)
#生成测试报告
runner.report(description='sharpUI测试', filename='sharpUI' + date + '.html', log_path=reprotPath)



'''
#构造测试集
suit = unittest.TestSuite()
suit.addTest(TestInfoDO("testInfoDO"))#把这个类中需要执行的测试用例加进去，有多条再加即可
suit.addTest(TestSendMail("testSendMail"))#从上到下先后顺序
runner = unittest.TextTestRunner()
runner.run(suit)#运行测试用例
'''
