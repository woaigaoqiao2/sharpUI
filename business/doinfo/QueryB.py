'''
Created on 2019年6月26日

@author: chinasoft.jl.ma
DO检索
'''
from business.Login import Login
from pageElement.doinfo.Query import Query
from util.ElementUtil import ElementUtil
from business.outward.GetBLNO import GetBLNO


class QueryB(Query):


    def getDoNo(self):

        gb = GetBLNO()
        DONO = gb.test()

        return DONO

    ##纳入场所检索
    def inPlaceQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '纳入场所检索', *self.DOElement)
        #选择纳入场所
        eu.click(driver, 15, '纳入场所检索', *self.inPlaceElement)
        eu.click(driver, 15, '纳入场所检索', *self.selInPlaceElement)
        #点击检索
        eu.click(driver, 15, '纳入场所检索', *self.searchElement)
        
    ##doNO检索
    def doNoQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'doNO检索', *self.DOElement)
        #输入DO no
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'doNO检索', *self.DONOElement)
        #点击检索
        eu.click(driver, 15, 'doNO检索', *self.searchElement)
        
    ##根据集装箱NO检索
    def containerNoQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '集装箱NO检索', *self.DOElement)
        #输入集装箱NO
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, '集装箱NO检索', *self.containerNOElement)
        #点击检索
        eu.click(driver, 15, '集装箱NO检索', *self.searchElement)
        
        
    ##根据输送形态检索
    def transportQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '输送形态检索', *self.DOElement)
        #选择输送形态
        eu.click(driver, 15, '输送形态检索', *self.transportElement)
        eu.click(driver, 15, '输送形态检索', *self.selTransportElement)
        #点击检索
        eu.click(driver, 15, '输送形态检索', *self.searchElement)
        
    ##根据海外取引先检索
    def overSeaQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '海外取引先检索', *self.DOElement)
        #选择海外取引先
        eu.click(driver, 15, '海外取引先检索', *self.overseasSupElement)
        eu.click(driver, 15, '海外取引先检索', *self.selOverseasSupElement)
        #点击检索
        eu.click(driver, 15, '海外取引先检索', *self.searchElement)
        
    ##根据到达港检索
    def toPortQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '到达港检索', *self.DOElement)
        #选择到达港
        eu.click(driver, 15, '到达港检索', *self.toportElement)
        eu.click(driver, 15, '到达港检索', *self.selToportElement)
        #点击检索
        eu.click(driver, 15, '到达港检索', *self.searchElement)
        
    ##根据ETD检索
    def startDateQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'ETD检索', *self.DOElement)
        #选择开始时间
        eu.click(driver, 15, 'ETD检索', *self.startDateElement)
        eu.click(driver, 15, 'ETD检索', *self.selStartDateElement)
        #点击检索
        eu.click(driver, 15, 'ETD检索', *self.searchElement)
        
    ##根据ETA检索
    def endDateQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'ETA检索', *self.DOElement)
        #选择结束时间
        eu.click(driver, 15, 'ETA检索', *self.endDateElement)
        eu.click(driver, 15, 'ETA检索', *self.selEndDateElement)
        #点击检索
        eu.click(driver, 15, 'ETA检索', *self.searchElement)
        
    ##根据B/L开始日期检索
    def blStartDateQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'B/L开始日期检索', *self.DOElement)
        #选择BL开始时间
        eu.click(driver, 15, 'B/L开始日期检索', *self.BLStartDateElement)
        eu.click(driver, 15, 'B/L开始日期检索', *self.selBLStartDateElement)
        #点击检索
        eu.click(driver, 15, 'B/L开始日期检索', *self.searchElement)
        
    ##根据B/L结束日期检索
    def blEndDateQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'B/L结束日期检索', *self.DOElement)
        #选择结束时间
        eu.click(driver, 15, 'B/L结束日期检索', *self.BLEndDateElement)
        eu.click(driver, 15, 'B/L结束日期检索', *self.SelBLEndDateElement)
        #点击检索
        eu.click(driver, 15, 'B/L结束日期检索', *self.searchElement)
        
    ##根据担当者ID检索
    def actorIDQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '担当者ID检索', *self.DOElement)
        #选择担当者ID、
        eu.click(driver, 15, '担当者ID检索', *self.actorIDElement)
        eu.click(driver, 15, '担当者ID检索', *self.selActorElement)
        #点击检索
        eu.click(driver, 15, '担当者ID检索', *self.searchElement)
        
    ##根据状态检索
    def statusQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '状态检索', *self.DOElement)
        #选择担当者ID
        eu.click(driver, 15, '状态检索', *self.statusElement)
        eu.click(driver, 15, '状态检索', *self.selStatusElement)
        #点击检索
        eu.click(driver, 15, '状态检索', *self.searchElement)
    
    ##doNO模糊检索
    def doNoLikeQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'doNO模糊检索', *self.DOElement)
        #输入DO no
        str = self.getDoNo()
        eu.send_keys(driver, 15, str[3:], 'doNO模糊检索', *self.DONOElement)
        #点击检索
        eu.click(driver, 15, 'doNO模糊检索', *self.searchElement)
        
    ##根据集装箱NO模糊检索
    def containerNoLikeQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '集装箱NO模糊检索', *self.DOElement)
        #输入集装箱NO
        str = self.getDoNo()
        eu.send_keys(driver, 15, str[3:], '集装箱NO模糊检索',  *self.DONOElement)
        #点击检索
        eu.click(driver, 15, '集装箱NO模糊检索', *self.searchElement)
        
    ##不存在的doNO检索
    def doNoFalseQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '不存在的doNO检索', *self.DOElement)
        #输入DO no
        eu.send_keys(driver, 15, 'xyz', '不存在的doNO检索', *self.DONOElement)
        #点击检索
        eu.click(driver, 15, '不存在的doNO检索', *self.searchElement)
        
    ##根据集装箱NO模糊检索
    def containerNoFalseQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '集装箱NO模糊检索', *self.DOElement)
        #输入集装箱NO
        eu.send_keys(driver, 15, 'xyz', '集装箱NO模糊检索', *self.DONOElement)
        #点击检索
        eu.click(driver, 15, '集装箱NO模糊检索', *self.searchElement)
        
    ##全量检索
    def fullQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '全量检索', *self.DOElement)
        #选择纳入场所
        eu.click(driver, 15, '全量检索', *self.inPlaceElement)
        eu.click(driver, 15, '全量检索', *self.selInPlaceElement)
        #输入DO no
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, '全量检索', *self.DONOElement)
        #输入集装箱NO
        eu.send_keys(driver, 15, str, '全量检索', *self.DONOElement)
        #选择输送形态
        eu.click(driver, 15, '全量检索', *self.transportElement)
        eu.click(driver, 15, '全量检索', *self.selTransportElement)
        #选择海外取引先
        eu.click(driver, 15, '全量检索', *self.overseasSupElement)
        eu.click(driver, 15, '全量检索', *self.selOverseasSupElement)
        #选择到达港
        eu.click(driver, 15, '全量检索', *self.toportElement)
        eu.click(driver, 15, '全量检索', *self.selToportElement)
        #选择开始时间
        eu.click(driver, 15, '全量检索', *self.startDateElement)
        eu.click(driver, 15, '全量检索', *self.selStartDateElement)
        #选择BL开始日期
        eu.click(driver, 15, '全量检索', *self.BLStartDateElement)
        eu.click(driver, 15, '全量检索', *self.selBLStartDateElement)
        #选择BL结束日期
        eu.click(driver, 15, '全量检索', *self.BLEndDateElement)
        eu.click(driver, 15, '全量检索', *self.SelBLEndDateElement)
        #选择担当者
        eu.click(driver, 15, '全量检索', *self.actorIDElement)
        eu.click(driver, 15, '全量检索', *self.selActorElement)
        #选择状态
        eu.click(driver, 15, '全量检索', *self.statusElement)
        eu.click(driver, 15, '全量检索', *self.selStatusElement)
        #点击检索
        eu.click(driver, 15, '全量检索', *self.searchElement)
        
    ##根据DO和集装箱NO检索
    def doNOAndContainerNoQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO和集装箱NO检索', *self.DOElement)
        #输入DONO和集装箱NO
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO和集装箱NO检索', *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DO和集装箱NO检索', *self.DONOElement)
        #点击检索
        eu.click(driver, 15, 'DO和集装箱NO检索', *self.searchElement)
    
    ##根据DO和运输形态检索
    def doNOAndTransportQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO和运输形态检索', *self.DOElement)
        #输入DONO和选择运输形态
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO和运输形态检索', *self.DONOElement)
        eu.click(driver, 15, 'DO和运输形态检索', *self.transportElement)
        eu.click(driver, 15, 'DO和运输形态检索', *self.selTransportElement)
        #点击检索
        eu.click(driver, 15, 'DO和运输形态检索', *self.searchElement)
        
    ##根据DO和到达港检索
    def doNOAndToportQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO和到达港检索', *self.DOElement)
        #输入DONO和到达港
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO和到达港检索', *self.DONOElement)
        eu.click(driver, 15, 'DO和到达港检索', *self.toportElement)
        eu.click(driver, 15, 'DO和到达港检索', *self.selToportElement)
        #点击检索
        eu.click(driver, 15, 'DO和到达港检索', *self.searchElement)
        
    ##根据DO和开始日期检索
    def doNOAndStartDateQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO和开始日期检索', *self.DOElement)
        #输入DONO和开始日期
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO和开始日期检索', *self.DONOElement)
        eu.click(driver, 15, 'DO和开始日期检索', *self.startDateElement)
        eu.click(driver, 15, 'DO和开始日期检索', *self.selStartDateElement)
        #点击检索
        eu.click(driver, 15, 'DO和开始日期检索', *self.searchElement)
        
    ##根据DO和结束日期检索
    def doNOAndEndDateQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO和结束日期检索', *self.DOElement)
        #输入DONO和开始日期
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO和结束日期检索', *self.DONOElement)
        eu.click(driver, 15, 'DO和结束日期检索', *self.endDateElement)
        eu.click(driver, 15, 'DO和结束日期检索', *self.selEndDateElement)
        #点击检索
        eu.click(driver, 15, 'DO和结束日期检索', *self.searchElement)
        
    ##根据DO和BL开始日期日期检索
    def doNOAndBLStartDateQuery(self, driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO和BL开始日期日期检索', *self.DOElement)
        #输入DONO和开始日期
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO和BL开始日期日期检索', *self.DONOElement)
        eu.click(driver, 15, 'DO和BL开始日期日期检索', *self.BLStartDateElement)
        eu.click(driver, 15, 'DO和BL开始日期日期检索', *self.selBLStartDateElement)
        #点击检索
        eu.click(driver, 15, 'DO和BL开始日期日期检索', *self.searchElement)
        
    ##根据DO和BL结束日期日期检索
    def doNOAndBLEndDateQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO和BL结束日期日期检索', *self.DOElement)
        #输入DONO和开始日期
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO和BL结束日期日期检索', *self.DONOElement)
        eu.click(driver, 15, 'DO和BL结束日期日期检索', *self.BLEndDateElement)
        eu.click(driver, 15, 'DO和BL结束日期日期检索', *self.SelBLEndDateElement)
        #点击检索
        eu.click(driver, 15, 'DO和BL结束日期日期检索', *self.searchElement)
        
    ##根据DO和开始日期检索
    def doNOAndStatusQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO和开始日期检索', *self.DOElement)
        #输入DONO和开始日期
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO和开始日期检索', *self.DONOElement)
        eu.click(driver, 15, 'DO和开始日期检索', *self.statusElement)
        eu.click(driver, 15, 'DO和开始日期检索', *self.selStatusElement)
        #点击检索
        eu.click(driver, 15, 'DO和开始日期检索', *self.searchElement)
        
    ##根据DO、集装箱NO和匀速形态
    def doNOAndContainerTransportQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO、集装箱NO和匀速形态', *self.DOElement)
        #输入DONO 集装箱NO和运输形态
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和匀速形态', *self.DONOElement)
        eu.send_keys(driver, 15, '19', 'DO、集装箱NO和匀速形态', *self.DONOElement)
        eu.click(driver, 15, 'DO、集装箱NO和匀速形态', *self.transportElement)
        eu.click(driver, 15, 'DO、集装箱NO和匀速形态', *self.selTransportElement)
        #点击检索
        eu.click(driver, 15, 'DO、集装箱NO和匀速形态', *self.searchElement)
        
    ##根据DO、集装箱NO和到达港
    def doNOAndContainerToportQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO、集装箱NO和到达港', *self.DOElement)
        #输入DONO 集装箱NO和运输形态
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和到达港',  *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和到达港', *self.DONOElement)
        eu.click(driver, 15, 'DO、集装箱NO和到达港', *self.toportElement)
        eu.click(driver, 15, 'DO、集装箱NO和到达港', *self.selToportElement)
        #点击检索
        eu.click(driver, 15, 'DO、集装箱NO和到达港', *self.searchElement)
    
    ##根据DO、集装箱NO和开始日期
    def doNOAndContainerStartDateQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO、集装箱NO和开始日期', *self.DOElement)
        #输入DONO 集装箱NO和运输形态
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和开始日期', *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和开始日期', *self.DONOElement)
        eu.click(driver, 15, 'DO、集装箱NO和开始日期', *self.startDateElement)
        eu.click(driver, 15, 'DO、集装箱NO和开始日期', *self.selStartDateElement)
        #点击检索
        eu.click(driver, 15, 'DO、集装箱NO和开始日期', *self.searchElement)
        
    ##根据DO、集装箱NO和结束日期
    def doNOAndContainerEndDateQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO、集装箱NO和结束日期', *self.DOElement)
        #输入DONO 集装箱NO和运输形态
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和结束日期', *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和结束日期', *self.DONOElement)
        
        eu.click(driver, 15, 'DO、集装箱NO和结束日期', *self.endDateElement)
        eu.click(driver, 15, 'DO、集装箱NO和结束日期', *self.selEndDateElement)
        #点击检索
        eu.click(driver, 15, 'DO、集装箱NO和结束日期', *self.searchElement)
        
    ##根据DO、集装箱NO和BL开始日期
    def doNOAndContainerBLStartDateQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO、集装箱NO和BL开始日期', *self.DOElement)
        #输入DONO 集装箱NO和运输形态
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和BL开始日期', *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和BL开始日期', *self.DONOElement)
        
        eu.click(driver, 15, 'DO、集装箱NO和BL开始日期', *self.BLStartDateElement)
        eu.click(driver, 15, 'DO、集装箱NO和BL开始日期', *self.selBLStartDateElement)
        #点击检索
        eu.click(driver, 15, 'DO、集装箱NO和BL开始日期', *self.searchElement)
        
    ##根据DO、集装箱NO和BL结束日期
    def doNOAndContainerBLEndDateQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO、集装箱NO和BL结束日期', *self.DOElement)
        #输入DONO 集装箱NO和运输形态
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和BL结束日期', *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和BL结束日期', *self.DONOElement)
        
        eu.click(driver, 15, 'DO、集装箱NO和BL结束日期', *self.BLEndDateElement)
        eu.click(driver, 15, 'DO、集装箱NO和BL结束日期', *self.SelBLEndDateElement)
        #点击检索
        eu.click(driver, 15, 'DO、集装箱NO和BL结束日期', *self.searchElement)
        
    ##根据DO、集装箱NO和状态
    def doNOAndContainerStatusQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DO、集装箱NO和状态', *self.DOElement)
        #输入DONO 集装箱NO和运输形态
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和状态', *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DO、集装箱NO和状态', *self.DONOElement)
        eu.click(driver, 15, 'DO、集装箱NO和状态', *self.statusElement)
        eu.click(driver, 15, 'DO、集装箱NO和状态', *self.selStatusElement)
        #点击检索
        eu.click(driver, 15, 'DO、集装箱NO和状态', *self.searchElement)
        
    ##根据开始日期和结束日期检索
    def startDateAndEndDateQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '开始日期和结束日期检索', *self.DOElement)
        #输入开始日期和结束日期
        eu.click(driver, 15, '开始日期和结束日期检索', *self.startDateElement)
        eu.click(driver, 15, '开始日期和结束日期检索', *self.selStartDateElement)
        
        eu.click(driver, 15, '开始日期和结束日期检索', *self.endDateElement)
        eu.click(driver, 15, '开始日期和结束日期检索', *self.selEndDateElement)
        #点击检索
        eu.click(driver, 15, '开始日期和结束日期检索', *self.searchElement)
        
    ##根据开始日期>结束日期检索
    def startDateGreaterEndDateQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, '开始日期>结束日期检索', *self.DOElement)
        #输入开始日期和结束日期
        eu.click(driver, 15, '开始日期>结束日期检索', *self.startDateElement)
        eu.click(driver, 15, '开始日期>结束日期检索', *self.selStartDateElement)
        
        eu.click(driver, 15, '开始日期>结束日期检索', *self.endDateElement)
        eu.click(driver, 15, '开始日期>结束日期检索', *self.selEndDate1Element)
        #点击检索
        eu.click(driver, 15, '开始日期>结束日期检索', *self.searchElement)
        
    ##根据DONO,集装箱NO和运输形态检索
    def doNOContainerNOAndtransportToportQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DONO,集装箱NO和运输形态检索', *self.DOElement)
        #输入DONO,集装箱NO和运输形态，到达港
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DONO,集装箱NO和运输形态检索', *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DONO,集装箱NO和运输形态检索', *self.containerNOElement)
        eu.click(driver, 15, 'DONO,集装箱NO和运输形态检索', *self.transportElement)
        eu.click(driver, 15, 'DONO,集装箱NO和运输形态检索', *self.selTransportElement)
        eu.click(driver, 15, 'DONO,集装箱NO和运输形态检索', *self.toportElement)
        eu.click(driver, 15, 'DONO,集装箱NO和运输形态检索', *self.selToportElement)
        #点击检索
        eu.click(driver, 15, 'DONO,集装箱NO和运输形态检索', *self.searchElement)
        
    ##根据DONO,集装箱NO和ETD检索
    def doNOContainerNOAndtransportETDQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DONO,集装箱NO和ETD检索', *self.DOElement)
        #输入DONO,集装箱NO和运输形态，到达港
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DONO,集装箱NO和ETD检索', *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DONO,集装箱NO和ETD检索', *self.containerNOElement)
        eu.click(driver, 15, 'DONO,集装箱NO和ETD检索', *self.transportElement)
        eu.click(driver, 15, 'DONO,集装箱NO和ETD检索', *self.selTransportElement)
        eu.click(driver, 15, 'DONO,集装箱NO和ETD检索', *self.startDateElement)
        eu.click(driver, 15, 'DONO,集装箱NO和ETD检索', *self.selStartDateElement)
        #点击检索
        eu.click(driver, 15, 'DONO,集装箱NO和ETD检索', *self.searchElement)
        
    ##根据DONO,集装箱NO和运输形态，到达港检索
    def doNOContainerNOAndtransportETAQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DONO,集装箱NO和运输形态，到达港检索', *self.DOElement)
        #输入DONO,集装箱NO和运输形态，到达港
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DONO,集装箱NO和运输形态，到达港检索', *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DONO,集装箱NO和运输形态，到达港检索', *self.containerNOElement)
        
        eu.click(driver, 15, 'DONO,集装箱NO和运输形态，到达港检索', *self.transportElement)
        eu.click(driver, 15, 'DONO,集装箱NO和运输形态，到达港检索', *self.selTransportElement)
        eu.click(driver, 15, 'DONO,集装箱NO和运输形态，到达港检索', *self.endDateElement)
        eu.click(driver, 15, 'DONO,集装箱NO和运输形态，到达港检索', *self.selEndDateElement)
        #点击检索
        eu.click(driver, 15, 'DONO,集装箱NO和运输形态，到达港检索', *self.searchElement)
        
    ##根据DONO,集装箱NO,运输形态和BL开始日期检索
    def doNOContainerNOAndtransportBLStartDateQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和BL开始日期检索', *self.DOElement)
        #输入DONO,集装箱NO和运输形态，到达港
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DONO,集装箱NO,运输形态和BL开始日期检索', *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DONO,集装箱NO,运输形态和BL开始日期检索', *self.containerNOElement)
        
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和BL开始日期检索', *self.transportElement)
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和BL开始日期检索', *self.selTransportElement)
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和BL开始日期检索', *self.BLStartDateElement)
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和BL开始日期检索', *self.selBLStartDateElement)
        #点击检索
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和BL开始日期检索', *self.searchElement)
        
    ##根据DONO,集装箱NO,运输形态和BL结束日期检索
    def doNOContainerNOAndtransportBLEDateQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和BL结束日期检索', *self.DOElement)
        #输入DONO,集装箱NO和运输形态，到达港
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DONO,集装箱NO,运输形态和BL结束日期检索', *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DONO,集装箱NO,运输形态和BL结束日期检索', *self.containerNOElement)
        
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和BL结束日期检索', *self.transportElement)
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和BL结束日期检索', *self.selTransportElement)
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和BL结束日期检索', *self.BLEndDateElement)
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和BL结束日期检索', *self.SelBLEndDateElement)
        #点击检索
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和BL结束日期检索', *self.searchElement)
        
    ##根据DONO,集装箱NO,运输形态和状态检索
    def doNOContainerNOAndtransportStatusQuery(self,driver):
        eu = ElementUtil()
        login = Login()
        login.test_click_login_btn(driver)
        #点击首页DO确定
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和状态检索', *self.DOElement)
        #输入DONO,集装箱NO和运输形态，到达港
        str = self.getDoNo()
        eu.send_keys(driver, 15, str, 'DONO,集装箱NO,运输形态和状态检索', *self.DONOElement)
        eu.send_keys(driver, 15, str, 'DONO,集装箱NO,运输形态和状态检索', *self.containerNOElement)
        
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和状态检索', *self.transportElement)
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和状态检索', *self.selTransportElement)
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和状态检索', *self.statusElement)
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和状态检索', *self.selStatusElement)
        #点击检索
        eu.click(driver, 15, 'DONO,集装箱NO,运输形态和状态检索', *self.searchElement)