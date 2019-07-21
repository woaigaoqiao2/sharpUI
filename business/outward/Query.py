'''
Created on 15019年6月150日

@author: chinasoft.jl.ma
'''
from pageElement.outward.OutWardShipment import OutWardShipment
from business.Login import Login
from time import sleep
from util.ElementUtil import ElementUtil
from business.outward.GetBLNO import GetBLNO


class Query(OutWardShipment):
    gb = GetBLNO()
    BLNO = gb.test()
    likeBLNO =  BLNO[3:]
    
    ##无条件检索
    def nullQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'无条件检索',*self.outWardElement)
        #点击检索
        eu.click(driver, 15,'无条件检索',*self.searchElement)
        sleep(1)
        
        
    ##用BL no检索
    def blQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'用BL no检索',*self.outWardElement)
        #输入BL
        eu.send_keys(driver, 15, self.BLNO,'用BL no检索',*self.BLNoEelement)
        #点击检索
        eu.click(driver, 15,'用BL no检索',*self.searchElement)
        sleep(1)
        
    ##用BL no模糊检索
    def blLikeQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'用BL no检索',*self.outWardElement)
        #输入BL
        eu.send_keys(driver, 15, self.likeBLNO,'用BL no检索',*self.BLNoEelement)
        #点击检索
        eu.click(driver, 15,'用BL no检索',*self.searchElement)
        sleep(1)
        
    ##用不存在的BL no检索
    def falseBLQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'用BL no检索',*self.outWardElement)
        #输入BL
        eu.send_keys(driver, 15, 'xyz','用BL no检索',*self.BLNoEelement)
        #点击检索
        eu.click(driver, 15,'用BL no检索',*self.searchElement)
        sleep(1)
    
    ##用海外取引先检索   
    def overSeasQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'海外取引先检索',*self.outWardElement)
        #选择海外取引先
        eu.click(driver, 15,'海外取引先检索',*self.overseasSupElement)
        eu.click(driver, 15,'海外取引先检索',*self.selOverseasSupElement)
        #点击检索
        eu.click(driver, 15,'海外取引先检索',*self.searchElement)
        sleep(1)
        
    ##用B/L开始发行日检索
    def blDateQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'用B/L开始发行日检索',*self.outWardElement)
        #选择BL开始发行日
        eu.click(driver, 15,'用B/L开始发行日检索',*self.BLStartDateElement)
        eu.click(driver, 15,'用B/L开始发行日检索',*self.selBLStartDateElement)

        #点击检索
        eu.click(driver, 15,'用B/L开始发行日检索',*self.searchElement)
        sleep(1)
        
    ##用B/L结束发行日检索
    def blEndDateQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'用B/L结束发行日检索',*self.outWardElement)
        #选择BL结束发行日
        eu.click(driver, 15,'用B/L结束发行日检索',*self.BLEndDateElement)
        eu.click(driver, 15,'用B/L结束发行日检索',*self.SelBLEndDateElement)

        #点击检索
        eu.click(driver, 15,'用B/L结束发行日检索',*self.searchElement)
        sleep(1)
        
    ##用输送形态检索
    def transportQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'用输送形态检索',*self.outWardElement)
        #选择输送形态为SEA
        eu.click(driver, 15,'用输送形态检索',*self.transportElement)
        eu.click(driver, 15,'用输送形态检索',*self.selTransportElement)
        #点击检索
        eu.click(driver, 15,'用输送形态检索',*self.searchElement)
        sleep(1)
        
    ##用出发港检索
    def fromPortQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'用出发港检索',*self.outWardElement)
        #选择出发港
        eu.click(driver, 15,'用出发港检索',*self.fromportElement)
        eu.click(driver, 15,'用出发港检索',*self.selFromportElement)
        #点击检索
        eu.click(driver, 15,'用出发港检索',*self.searchElement)
        sleep(1)
        
    ##用到达港检索
    def toPortQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'到达港',*self.outWardElement)
        #选择到达港
        eu.click(driver, 15,'到达港',*self.toportElement)
        eu.click(driver, 15,'到达港',*self.selToportElement)
        #点击检索
        eu.click(driver, 15,'到达港',*self.searchElement)
        sleep(1)
        
    ##本船名检索
    def shipQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'本船名',*self.outWardElement)
        #输入本船名
        eu.send_keys(driver, 15, self.BLNO,'本船名',*self.shipElement)
        
        #点击检索
        eu.click(driver, 15,'本船名',*self.searchElement)
        sleep(1)
        
    ##本船名模糊检索
    def shipLikeQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'本船名',*self.outWardElement)
        #输入本船名
        eu.send_keys(driver, 15, self.likeBLNO,'本船名',*self.shipElement)
        
        #点击检索
        eu.click(driver, 15,'本船名',*self.searchElement)
        sleep(1)
    
    ##用不存在的本船名检索 
    def falseShipQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'用不存在的本船名检索',*self.outWardElement)
        #输入本船名
        eu.send_keys(driver, 15, 'xyz','用不存在的本船名检索',*self.shipElement)
        
        #点击检索
        eu.click(driver, 15,'用不存在的本船名检索',*self.searchElement)
        sleep(1)
        
    ##船社或航空社检索
    def shippingQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'船社',*self.outWardElement)
        #选择船社
        eu.click(driver, 15,'船社',*self.shippingElement)
        eu.click(driver, 15,'船社',*self.selShippingElement)
        
        #点击检索
        eu.click(driver, 15,'船社',*self.searchElement)
        sleep(1)
        
    ##用ETD检索
    def startDateQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'ETD',*self.outWardElement)
        #选择开始时间
        eu.click(driver, 15,'ETD',*self.startDateElement)
        eu.click(driver, 15,'ETD',*self.selStartDateElement)
        
        #点击检索
        eu.click(driver, 15,'ETD',*self.searchElement)
        sleep(1)
        
    ##用ETA检索
    def endDateQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'ETA',*self.outWardElement)
        #选择结束时间
        eu.click(driver, 15,'ETA',*self.endDateElement)
        eu.click(driver, 15,'ETA',*self.selEndDateElement)
        
        #点击检索
        eu.click(driver, 15,'ETA',*self.searchElement)
        sleep(1)
        
    ##用BL no和海外取引先检索
    def blAndSeaQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'BL no和海外',*self.outWardElement)
        #输入BL
        eu.send_keys(driver, 15, self.BLNO,'BL no和海外',*self.BLNoEelement)
        #选择海外取引先
        eu.click(driver, 15,'BL no和海外',*self.overseasSupElement)
        eu.click(driver, 15,'BL no和海外',*self.selOverseasSupElement)
        #点击检索
        eu.click(driver, 15,'BL no和海外',*self.searchElement)
        sleep(1)
        
    ##用BL no和运输形态检索
    def blAndTransportQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'BL no和运输',*self.outWardElement)
        #输入BL
        eu.send_keys(driver, 15, self.BLNO,'BL no和运输',*self.BLNoEelement)
        #选择输送形态为SEA
        eu.click(driver, 15,'BL no和运输',*self.transportElement)
        eu.click(driver, 15,'BL no和运输',*self.selTransportElement)
        #点击检索
        eu.click(driver, 15,'BL no和运输',*self.searchElement)
        sleep(1)
        
    ##用BL no和本船名检索
    def blAndShipQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'BL no和本船',*self.outWardElement)
        #输入BL
        eu.send_keys(driver, 15, self.BLNO,'BL no和本船',*self.BLNoEelement)
        #输入本船名
        eu.send_keys(driver, 15, self.BLNO,'BL no和本船',*self.shipElement)
        #点击检索
        eu.click(driver, 15,'BL no和本船',*self.searchElement)
        sleep(1)
        
    ##用ETD和ETA检索
    def ETDAndETAQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'ETD和ETA',*self.outWardElement)
        #选择开始时间
        eu.click(driver, 15,'ETD和ETA',*self.startDateElement)
        eu.click(driver, 15,'ETD和ETA',*self.selStartDateElement)
        #选择结束时间
        eu.click(driver, 15,'ETD和ETA',*self.endDateElement)
        eu.click(driver, 15,'ETD和ETA',*self.selEndDateElement)
        #点击检索
        eu.click(driver, 15,'ETD和ETA',*self.searchElement)
        sleep(1)
        
    ##用ETD>ETA检索
    def ETDGreaterETAQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'ETD>ETA',*self.outWardElement)
        #选择开始时间
        eu.click(driver, 15,'ETD>ETA',*self.startDateElement)
        eu.click(driver, 15,'ETD>ETA',*self.selStartDateElement)
        #选择结束时间
        eu.click(driver, 15,'ETD>ETA',*self.endDateElement)
        eu.click(driver, 15,'ETD>ETA',*self.selEndDate1Element)
        #点击检索
        eu.click(driver, 15,'ETD>ETA',*self.searchElement)
        sleep(1)
        
    ##用BL no和船社检索
    def blAndShippingQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'BL no和船社',*self.outWardElement)
        #输入BL
        eu.send_keys(driver, 15, self.BLNO,'BL no和船社',*self.BLNoEelement)
        #选择船社
        eu.click(driver, 15,'BL no和船社',*self.shippingElement)
        eu.click(driver, 15,'BL no和船社',*self.selShippingElement)
        #点击检索
        eu.click(driver, 15,'BL no和船社',*self.searchElement)
        sleep(1)
        
    ##全条件检索
    def fullQuery(self,driver):
        login = Login()
        login.test_click_login_btn(driver)
        eu = ElementUtil()
        #点击 フレイトI/V作成
        eu.click(driver, 15,'全条件',*self.outWardElement)
        #输入BL
        eu.send_keys(driver, 15, self.BLNO,'全条件',*self.BLNoEelement)
        #选择海外取引先
        eu.click(driver, 15,'全条件',*self.overseasSupElement)
        eu.click(driver, 15,'全条件',*self.selOverseasSupElement)
        #选择BL开始发行日
        eu.click(driver, 15,'全条件',*self.BLStartDateElement)
        eu.click(driver, 15,'全条件',*self.selBLStartDateElement)
        #选择BL结束发行日
        eu.click(driver, 15,'全条件',*self.BLEndDateElement)
        eu.click(driver, 15,'全条件',*self.SelBLEndDateElement)
        #选择输送形态为SEA
        eu.click(driver, 15,'全条件',*self.transportElement)
        eu.click(driver, 15,'全条件',*self.selTransportElement)
        #选择出发港
        eu.click(driver, 15,'全条件',*self.fromportElement)
        eu.click(driver, 15,'全条件',*self.selFromportElement)
        #选择到达港
        eu.click(driver, 15,'全条件',*self.toportElement)
        eu.click(driver, 15,'全条件',*self.selToportElement)
        #选择开始时间
        eu.click(driver, 15,'全条件',*self.startDateElement)
        eu.click(driver, 15,'全条件',*self.selStartDateElement)
        #选择结束时间
        eu.click(driver, 15,'全条件',*self.endDateElement)
        eu.click(driver, 15,'全条件',*self.selEndDateElement)
        #输入本船名
        eu.send_keys(driver, 15, self.BLNO,'全条件',*self.shipElement)
        #选择船社
        eu.click(driver, 15,'全条件',*self.shippingElement)
        eu.click(driver, 15,'全条件',*self.selShippingElement)
        #点击检索
        eu.click(driver, 15, '全条件', *self.searchElement)
        sleep(1)
        