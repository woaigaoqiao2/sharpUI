'''
DO确定
'''
from pageElement.doinfo.DODetermine import DODetermine
from business.Login import Login
from util.ElementUtil import ElementUtil
from case.doinfo.getDONO1 import GetDONO1
from business.outward.GetBLNO import GetBLNO


class DODetermine(DODetermine):
    
    def doDeterm(self,driver):
        gb = GetBLNO()
        DONO = gb.test()
        gd = GetDONO1()
        gd.getDisDO(driver, DONO)
        gd.addCost(driver)

        eu = ElementUtil()
        #点击检索
        eu.click(driver, 15,'DO确定',*self.selElement)
        #选择数据
        eu.click(driver, 15,'DO确定',*self.selDateElement)
        #点击DO确定
        eu.click(driver, 15,'DO确定',*self.DODetermineElement)
        #点击确定
        eu.click(driver, 15,'DO确定',*self.determineElement)
    