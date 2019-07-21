'''
Created on 2019年6月24日

@author: chinasoft.jl.ma
新规
'''
from pageElement.outward.NewBuilt import NewBuilt
from business.Login import Login
from util.ElementUtil import ElementUtil


class NewBuilt(NewBuilt):
    
    def newBuilt(self,driver):
        eu = ElementUtil()
        #登录
        login = Login()
        login.test_click_login_btn(driver)
        #点击做成
        eu.click(driver,15,'新规',*self.outWardElement)
        #点击新规
        eu.click(driver,15,'新规',*self.newBuiltElement)
        #输入B/L NO
        eu.send_keys(driver, 15, "mjl001",'新规',*self.BLNoEelement)
        #选择海外取引先
        eu.click(driver,15,'新规',*self.overseasSupElement)
        eu.click(driver,15,'新规',*self.selOverseasSupElement)
        #选择B/L发行日
        eu.click(driver,15,'新规',*self.BLDateElement)
        eu.click(driver,15,'新规',*self.selBLStartDateElement)
        #选择出发港
        eu.click(driver,15,'新规',*self.fromportElement)
        eu.click(driver,15,'新规',*self.selFromportElement)
        #选择到达港
        eu.click(driver,15,'新规',*self.toportElement)
        eu.click(driver,15,'新规',*self.selToportElement)
        #选择ETD
        eu.click(driver,15,'新规',*self.startDateElement)
        eu.click(driver,15,'新规',*self.selStartDateElement)
        #选择ETA
        eu.click(driver,15,'新规',*self.endDateElement)
        eu.click(driver,15,'新规',*self.selEndDateElement)
        #输入本船名
        eu.send_keys(driver, 15, "huchuan",'新规',*self.shipElement)
        #选择船社
        eu.click(driver,15,'新规',*self.shippingElement)
        eu.click(driver,15,'新规',*self.selShippingElement)
        #选择货物类型
        eu.click(driver,15,'新规',*self.carGoTypeElement)
        eu.click(driver,15,'新规',*self.selCarGoTypeElement)
        #选择报关者
        eu.click(driver,15,'新规',*self.customsElement)
        eu.click(driver,15,'新规',*self.selCustomsElement)
        #选择输送形态
        eu.click(driver,15,'新规',*self.transportElement)
        eu.click(driver,15,'新规',*self.selTransportElement)
        #选择建值
        eu.click(driver,15,'新规',*self.keyVElement)
        eu.click(driver,15,'新规',*self.selKyeVElement)
        #选择装法
        eu.click(driver,15,'新规',*self.loadingElement)
        eu.click(driver,15,'新规',*self.selLoadingElement)
        #选择货币
        eu.click(driver,15,'新规',*self.doriElement)
        eu.click(driver,15,'新规',*self.selDoriElement)
        #输入C/W
        eu.send_keys(driver, 15, 1,'新规',*self.cwElement)
        #输入G/W
        eu.send_keys(driver, 15, 1,'新规',*self.gwElement)
        #输入N/W
        eu.send_keys(driver, 15, 1,'新规',*self.nwElement)
        #点击保存
        eu.click(driver,15,'新规',*self.saveElement)
        #点击确定
        eu.click(driver,15,'新规',*self.doElement)

        
        
