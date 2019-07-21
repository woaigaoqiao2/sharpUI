'''
Created on 2019年5月22日

@author: chinasoft.xp.chen
'''

from time import sleep
from util.ElementUtil import ElementUtil
from pageElement.bl.BlElement import BlElement


class BlOperate(BlElement):
    def __init__(self):
        self.en=ElementUtil()

    #通过B/L NO检索结果、核对全部集装箱信息送信成功
    def bl01(self,driver,blno):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl01",*self.BL_element)
        #输入B/L no
        en.send_keys(driver, 15,blno,"testBl01",*self.BLno_element)
        #点击检索
        en.click(driver, 15,"testBl01",*self.Search_element)
        #勾选数据
        en.click(driver, 15,"testBl01",*self.Option_element)
        #点击ActualInfo Input
        en.click(driver, 15,"testBl01",*self.ActualInfo_element)
        #输入C/W
        en.send_keys(driver, 15,'7',"testBl01",*self.CW)
        #输入GW
        en.send_keys(driver, 15,'5',"testBl01",*self.GW)
        #输入M3
        en.send_keys(driver, 15,'6',"testBl01",*self.M3)
        #点击保存
        en.click(driver, 15,"testBl01",*self.Preserve)
        #点击集装箱信息确定
        en.click(driver, 15,"testBl01",*self.sendok)
        #再次勾选
        en.click(driver, 15,"testBl01",*self.Option_element)
        #点击確認完了通知メール
        en.click(driver, 15,"testBl01",*self.Inform_element)
        #点击mail送信
        en.click(driver, 15,"testBl01",*self.mail)
        #点击OK确定
        en.click(driver, 15,"testBl01",*self.sendok)
        sleep(2)
        actual_text=en.getText(driver, 15,"testBl01",*self.actual_sendingstate)
        return actual_text
    
    #通过B/L NO检索结果、核对部分集装箱信息送信成功
    def bl02(self,driver,blno):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl02",*self.BL_element)
        #输入B/L no
        en.send_keys(driver, 15,blno,"testBl02",*self.BLno_element)
        #点击检索
        en.click(driver, 15,"testBl02",*self.Search_element)
        #勾选数据
        en.click(driver, 15,"testBl02",*self.Option_element)
        #点击ActualInfo Input
        en.click(driver, 15,"testBl02",*self.ActualInfo_element)
        #输入C/W
        en.send_keys(driver, 15,"78","testBl02",*self.CW)
        #输入M3
        en.send_keys(driver, 15,"80","testBl02",*self.M3)
        #点击保存
        en.click(driver, 15,"testBl02",*self.Preserve)
        #点击集装箱信息确定
        en.click(driver, 15,"testBl02",*self.sendok)
        #再次勾选
        en.click(driver, 15,"testBl02",*self.Option_element)
        #点击確認完了通知メール
        en.click(driver, 15,"testBl02",*self.Inform_element)
        # 点击mail送信
        en.click(driver, 15, "testBl02",*self.mail)
        # 点击OK确定
        en.click(driver, 15, "testBl02",*self.sendok)
        sleep(2)
        actual_text=en.getText(driver, 15,"testBl02",*self.actual_sendingstate)
        return actual_text
    
    #通过B/L NO检索结果、不核对集装箱信息送信成功
    def bl03(self,driver,blno):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl03",*self.BL_element)
        #输入B/L no
        en.send_keys(driver, 15,blno,"testBl03",*self.BLno_element)
        #点击检索
        en.click(driver, 15,"testBl03",*self.Search_element)
        #勾选
        en.click(driver, 15,"testBl03",*self.Option_element)
        #点击確認完了通知メール
        en.click(driver, 15,"testBl03",*self.Inform_element)
        # 点击mail送信
        en.click(driver, 15, "testBl03",*self.mail)
        # 点击OK确定
        en.click(driver, 15,"testBl03", *self.sendok)
        sleep(2)
        actual_text=en.getText(driver, 15,"testBl03",*self.actual_sendingstate)
        return actual_text

    #没有BL附件资料送信失败
    def bl04(self,driver,blno):
        #BL確認完了送信
        en=self.en
        en.click(driver, 15,"testBl04",*self.BL_element)
        #输入B/L no
        en.send_keys(driver, 15,blno,"testBl04",*self.BLno_element)
        #点击检索
        en.click(driver, 15,"testBl04",*self.Search_element)
        #勾选
        en.click(driver, 15,"testBl04",*self.Option_element)
        #点击確認完了通知メール
        en.click(driver, 15,"testBl04",*self.Inform_element)
        sleep(1)
        #获取提示需要添加B/L附件资料的文本 
        tip_text=en.getText(driver, 15,"testBl04",*self.tip)
        sleep(2)
        #点击确定
        en.click(driver, 15,"testBl04",*self.Bl_sure)
        return tip_text
    
    #通过D/O NO检索结果、核对全部集装箱信息送信成功
    def bl05(self,driver,dono):
        #BL確認完了送信
        en=self.en
        en.click(driver, 15,"testBl05",*self.BL_element)
        #输入D/O no
        en.send_keys(driver, 15,dono,"testBl05",*self.DOno_element)
        #点击检索
        en.click(driver, 15,"testBl05",*self.Search_element)
        #勾选数据
        en.click(driver, 15,"testBl05",*self.Option_element)
        #点击ActualInfo Input
        en.click(driver, 15,"testBl05",*self.ActualInfo_element)
        #输入C/W
        en.send_keys(driver, 15,'789',"testBl05",*self.CW)
        #输入GW
        en.send_keys(driver, 15,'5646',"testBl05",*self.GW)
        #输入M3
        en.send_keys(driver, 15,'89',"testBl05",*self.M3)
        #点击保存
        en.click(driver, 15,"testBl05",*self.Preserve)
        #点击集装箱信息确定
        en.click(driver, 15,"testBl05",*self.sendok)
        #再次勾选
        en.click(driver, 15,"testBl05",*self.Option_element)
        #点击確認完了通知メール
        en.click(driver, 15,"testBl05",*self.Inform_element)
        # 点击mail送信
        en.click(driver, 15,"testBl05", *self.mail)
        # 点击OK确定
        en.click(driver, 15, "testBl05",*self.sendok)
        sleep(2)
        actual_text=en.getText(driver, 15,"testBl05",*self.actual_sendingstate)
        return actual_text
    
    #通过D/O NO检索结果、核对部分集装箱信息送信成功
    def bl06(self,driver,dono):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl06",*self.BL_element)
        #输入D/O no
        en.send_keys(driver, 15,dono,"testBl06",*self.DOno_element)
        #点击检索
        en.click(driver, 15,"testBl06",*self.Search_element)
        #勾选数据
        en.click(driver, 15,"testBl06",*self.Option_element)
        #点击ActualInfo Input
        en.click(driver, 15,"testBl06",*self.ActualInfo_element)
        #输入C/W
        en.send_keys(driver, 15,'789',"testBl06",*self.CW)
        #输入M3
        en.send_keys(driver, 15,'962',"testBl06",*self.M3)
        #点击保存
        en.click(driver, 15,"testBl06",*self.Preserve)
        #点击集装箱信息确定
        en.click(driver, 15,"testBl06",*self.sendok)
        #再次勾选
        en.click(driver, 15,"testBl06",*self.Option_element)
        #点击確認完了通知メール
        en.click(driver, 15,"testBl06",*self.Inform_element)
        # 点击mail送信
        en.click(driver, 15, "testBl06",*self.mail)
        # 点击OK确定
        en.click(driver, 15, "testBl06",*self.sendok)
        sleep(2)
        actual_text=en.getText(driver, 15,"testBl06",*self.actual_sendingstate)
        return actual_text
    
    #通过D/O NO检索结果、不核对集装箱信息送信成功
    def bl07(self,driver,dono):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl07",*self.BL_element)
        #输入D/O no
        en.send_keys(driver, 15,dono,"testBl07",*self.DOno_element)
        #点击检索
        en.click(driver, 15,"testBl07",*self.Search_element)
        #勾选
        en.click(driver, 15,"testBl07",*self.Option_element)
        #点击確認完了通知メール
        en.click(driver, 15,"testBl07",*self.Inform_element)
        # 点击mail送信
        en.click(driver, 15,"testBl07", *self.mail)
        # 点击OK确定
        en.click(driver, 15,"testBl07", *self.sendok)
        sleep(2)
        actual_text=en.getText(driver, 15,"testBl07",*self.actual_sendingstate)
        return actual_text
    
    #不输入检索条件可以检索
    def bl08(self,driver):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl08",*self.BL_element)
        en.click(driver, 15,"testBl08",*self.Search_element)
        index=en.getText(driver, 15,"testBl08",*self.index_element)
        num=index[-3:]
        return num
    
    #通过海外取引先可以检索
    def bl09(self,driver):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl09",*self.BL_element)
        #点击海外取引先
        en.send_keys(driver, 15,"SHARP HONK KONG LIMITED","testBl09",*self.foreignguests_element)
        #选择海外领取先
        en.click(driver, 15,"testBl09",*self.Choice_forei)
        #点击检索
        en.click(driver, 15,"testBl09",*self.Search_element)
        index=en.getText(driver, 15,"testBl09",*self.index_element)
        num=index[-2:]
        return num
    
    #通过B/L DATE检索成功
    def bl10(self,driver):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl10",*self.BL_element)
        #点击B/L DATE
        en.click(driver, 15,"testBl10",*self.start_date)
        sleep(1)
        #选择日期
        en.click(driver, 15,"testBl10",*self.startdate_8)
        sleep(1)
        #点击~
        en.click(driver, 15,"testBl10",*self.end_date)
        #选择日期
        en.click(driver, 15,"testBl10",*self.enddate_8)
        #点击检索
        en.click(driver, 15,"testBl10",*self.Search_element)
        index=en.getText(driver, 15,"testBl10",*self.index_element)
        num=index[-2:]
        return num
    
    #通过運送形態为SEA检索成功
    def bl11(self,driver):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl11",*self.BL_element)
        #点击運送形態
        en.click(driver, 15,"testBl11",*self.Shochin_element)
        #选择SEA
        en.click(driver, 15,"testBl11",*self.SEA_element)
        #点击检索
        en.click(driver, 15,"testBl11",*self.Search_element)
        index=en.getText(driver, 15,"testBl11",*self.index_element)
        num=index[-3:]
        return num
    
    #通过運送形態为AIR检索成功
    def bl12(self,driver):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl12",*self.BL_element)
        #点击運送形態
        en.click(driver, 15,"testBl12",*self.Shochin_element)
        #选择AIR
        en.click(driver, 15,"testBl12",*self.AIR_element)
        #点击检索
        en.click(driver, 15,"testBl12",*self.Search_element)
        index=en.getText(driver, 15,"testBl12",*self.index_element)
        num=index[-3:]
        return num
    
    #通过送信状態为未送信检索成功
    def bl13(self,driver):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl13",*self.BL_element)
        #点击送信状態
        en.click(driver, 15,"testBl13",*self.Sendingstate_element)
        #选择未送信
        en.click(driver, 15,"testBl13",*self.notsend_element)
        #点击检索
        en.click(driver, 15,"testBl13",*self.Search_element)
        index=en.getText(driver, 15,"testBl13",*self.index_element)
        num=index[-2:]
        return num
    
    #通过送信状態为送信済み检索成功
    def bl14(self,driver):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl14",*self.BL_element)
        #点击送信状態
        en.click(driver, 15,"testBl14",*self.Sendingstate_element)
        #选择送信済み
        en.click(driver, 15,"testBl14",*self.Sendemail_element)
        #点击检索
        en.click(driver, 15,"testBl14",*self.Search_element)
        sleep(1)
        index=en.getText(driver, 15,"testBl14",*self.index_element)
        num=index[-3:]
        return num
    
    #通过选择SJL輸入担当：NAOMI检索成功
    def bl15(self,driver):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl15",*self.BL_element)
        #点击SJL輸入担当
        en.send_keys(driver, 15,"NAOMI","testBl15",*self.SJL_element)
        #选择
        en.click(driver, 15,"testBl15",*self.choice_sjl)
        #点击检索
        en.click(driver, 15,"testBl15",*self.Search_element)
        index=en.getText(driver, 15,"testBl15",*self.index_element)
        num=index[-2:]
        return num
    
    #通过D/O No和海外取引先组合检索成功
    def bl16(self,driver,dono):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl16",*self.BL_element)
        #输入D/O no
        en.send_keys(driver, 15,dono,"testBl16",*self.DOno_element)
        #点击检索
        en.click(driver, 15,"testBl16",*self.Search_element)
        #获取海外取引先
        foreignguests=en.getText(driver, 15,"testBl16",*self.actual_foreignguest)
        # 点击海外取引先
        en.send_keys(driver, 15, foreignguests, "testBl16",*self.foreignguests_element)
        # 点击
        en.click(driver, 15, "testBl16",*self.Choice_forei)
        # 输入D/O no
        en.send_keys(driver, 15, dono, "testBl16",*self.DOno_element)
        # 点击检索
        en.click(driver, 15,"testBl16", *self.Search_element)
        #获取检索结果D/O no的值
        actual_dono=en.getText(driver, 15,"testBl16",*self.actual_do)
        actual_forei=en.getText(driver, 15,"testBl16",*self.actual_foreignguest)
        return actual_dono,actual_forei,foreignguests
    
    #通过D/O No和B/L No组合检索成功
    def bl17(self,driver,dono,blno):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl17",*self.BL_element)
        #清除D/O no
        en.clear(driver, 15,"testBl17",*self.DOno_element)
        #输入D/O no
        en.send_keys(driver, 15,dono,"testBl17",*self.DOno_element)
        #清除B/L no
        en.clear(driver, 15,"testBl17",*self.BLno_element)
        #输入B/L no
        en.send_keys(driver, 15,blno,"testBl17",*self.BLno_element)
        #点击检索
        en.click(driver, 15,"testBl17",*self.Search_element)
        #获取检索结果D/O no的值
        sleep(2)
        actual_dono=en.getText(driver, 15,"testBl17",*self.actual_do)
        #获取检索结果B/L no的值
        actual_blno=en.getText(driver, 15,"testBl17",*self.actual_bl)
        return actual_dono,actual_blno
    
    #通过D/O No和B/L DATE组合检索成功
    def bl18(self,driver,dono):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl18",*self.BL_element)
        #输入D/O no
        en.send_keys(driver, 15,dono,"testBl18",*self.DOno_element)
        #点击B/L DATE
        sleep(1)
        en.click(driver, 15,"testBl18",*self.start_date)
        #选择开始日期
        en.click(driver, 15,"testBl18",*self.startdate_8)
        #获取检索的日期
        date=en.getText(driver, 15,"testBl18",*self.startdate_8)
        #点击~
        sleep(1)
        en.click(driver, 15,"testBl18",*self.end_date)
        #选择结束日期
        en.click(driver, 15,"testBl18",*self.enddate_8)
        sleep(1)
        #点击检索
        en.click(driver, 15,"testBl18",*self.Search_element)
        #获取搜索结果的D/O号码
        sleep(2)
        actual_do=en.getText(driver, 15,"testBl18",*self.actual_do)
        #获取搜索结果的日期
        sleep(1)
        actual_date=en.getText(driver, 15,"testBl18",*self.atcual_date)
        return actual_do,actual_date,date
    
    #通过D/O No和運送形態组合检索成功
    def bl19(self,driver,dono):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl19",*self.BL_element)
        #输入D/O no
        en.send_keys(driver, 15,dono,"testBl19",*self.DOno_element)
        #点击運送形態
        en.click(driver, 15,"testBl19",*self.Shochin_element)
        #选择SEA
        en.click(driver, 15,"testBl19",*self.SEA_element)
        #点击检索
        en.click(driver, 15,"testBl19",*self.Search_element)
        #获取搜索结果的D/O no
        actual_do=en.getText(driver, 15,"testBl19",*self.actual_do)
        #获取搜索结果的運送形態
        actual_shochin=en.getText(driver, 15,"testBl19",*self.actual_shochin)
        return actual_do,actual_shochin
    
    #通过D/O No和送信状態组合检索成功
    def bl20(self,driver,dono):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl20",*self.BL_element)
        #输入D/O no
        en.send_keys(driver, 15,dono,"testBl20",*self.DOno_element)
        #点击送信状態
        en.click(driver, 15,"testBl20",*self.Sendingstate_element)
        #选择送信済み
        en.click(driver, 15,"testBl20",*self.notsend_element)
        #点击检索
        en.click(driver, 15,"testBl20",*self.Search_element)
        #获取搜索结果的D/O no
        actual_do=en.getText(driver, 15,"testBl20",*self.actual_do)
        #获取搜索结果的運送形態
        actual_sendingstate=en.getText(driver, 15,"testBl20",*self.actual_sendingstate)
        return actual_do,actual_sendingstate
        
    #通过B/L No和海外取引先组合检索成功
    def bl21(self,driver,blno):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl21",*self.BL_element)
        #输入B/L no
        en.send_keys(driver, 15,blno,"testBl21",*self.BLno_element)
        #点击检索
        en.click(driver, 15,"testBl21",*self.Search_element)
        foreignguests=en.getText(driver, 15,"testBl21",*self.actual_foreignguest)
        # 点击海外取引先
        en.send_keys(driver, 15, foreignguests, "testBl21",*self.foreignguests_element)
        # 点击
        en.click(driver, 15, "testBl21",*self.Choice_forei)
        # 输入B/L no
        en.send_keys(driver, 15, blno,"testBl21", *self.BLno_element)
        # 点击检索
        en.click(driver, 15, "testBl21",*self.Search_element)
        #获取检索结果B/L no的值
        actual_blno=en.getText(driver, 15,"testBl21",*self.actual_bl)
        #获取海外取引先的值
        actual_foreignguest=en.getText(driver, 15,"testBl21",*self.actual_foreignguest)
        return actual_blno,actual_foreignguest,foreignguests
    
    
    #通过B/L No和B/L DATE组合检索成功
    def bl22(self,driver,blno):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl22",*self.BL_element)
        #输入B/L no
        en.send_keys(driver, 15,blno,"testBl22",*self.BLno_element)
        #点击B/L DATE
        en.click(driver, 15,"testBl22",*self.start_date)
        sleep(1)
        #选择开始日期
        en.click(driver, 15,"testBl22",*self.startdate_8)
        #获取检索的日期
        date=en.getText(driver, 15,"testBl22",*self.startdate_8)
        #点击~
        en.click(driver, 15,"testBl22",*self.end_date)
        #选择结束日期
        sleep(1)
        en.click(driver, 15,"testBl22",*self.enddate_8)
        #点击检索
        en.click(driver, 15,"testBl22",*self.Search_element)
        #获取搜索结果的B/L号
        actual_bl=en.getText(driver, 15,"testBl22",*self.actual_bl)
        #获取搜索结果的日期
        actual_date=en.getText(driver, 15,"testBl22",*self.atcual_date)
        return actual_bl,actual_date,date
        
    #通过B/L No和運送形態组合检索成功
    def bl23(self,driver,blno):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl23",*self.BL_element)
        #输入B/L no
        en.send_keys(driver, 15,blno,"testBl23",*self.BLno_element)
        #点击運送形態
        en.click(driver, 15,"testBl23",*self.Shochin_element)
        #选择SEA
        en.click(driver, 15,"testBl23",*self.SEA_element)
        #点击检索
        en.click(driver, 15,"testBl23",*self.Search_element)
        #获取搜索结果的B/L no
        actual_bl=en.getText(driver, 15,"testBl23",*self.actual_bl)
        #获取搜索结果的運送形態
        actual_shochin=en.getText(driver, 15,"testBl23",*self.actual_shochin)
        return actual_bl,actual_shochin
    
    #通过B/L No和送信状態组合检索成功
    def bl24(self,driver,blno):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl24",*self.BL_element)
        #输入B/L no
        en.send_keys(driver, 15,blno,"testBl24",*self.BLno_element)
        #点击送信状態
        en.click(driver, 15,"testBl24",*self.Sendingstate_element)
        #选择未送信
        en.click(driver, 15,"testBl24",*self.notsend_element)
        #点击检索
        en.click(driver, 15,"testBl24",*self.Search_element)
        #获取搜索结果的B/L no
        actual_bl=en.getText(driver, 15,"testBl24",*self.actual_bl)
        #获取送信状態
        actual_send=en.getText(driver, 15,"testBl24",*self.actual_sendingstate)
        return actual_bl,actual_send
    
    #通过输入所有条件检索成功
    def bl25(self,driver,dono,blno):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl25",*self.BL_element)
        # 输入D/O no
        en.send_keys(driver, 15, dono,"testBl25", *self.DOno_element)
        # 点击检索
        en.click(driver, 15, "testBl25",*self.Search_element)
        foreignguests=en.getText(driver, 15,"testBl25",*self.actual_foreignguest)
        #点击海外取引先
        en.send_keys(driver, 15,foreignguests,"testBl25",*self.foreignguests_element)
        en.click(driver, 15,"testBl25",*self.Choice_forei)
        #输入D/O no
        en.send_keys(driver, 15,dono,"testBl25",*self.DOno_element)
        #输入B/L no
        en.send_keys(driver, 15,blno,"testBl25",*self.BLno_element)
        #点击B/L DATE
        en.click(driver, 15,"testBl25",*self.start_date)
        #选择开始日期
        sleep(1)
        en.click(driver, 15,"testBl25",*self.startdate_8)
        #获取检索的日期
        date=en.getText(driver, 15,"testBl25",*self.startdate_8)
        #点击~
        en.click(driver, 15,"testBl25",*self.end_date)
        #选择结束日期
        sleep(1)
        en.click(driver, 15,"testBl25",*self.enddate_8)
        #点击運送形態
        en.click(driver, 15,"testBl25",*self.Shochin_element)
        #选择SEA
        en.click(driver, 15,"testBl25",*self.SEA_element)
        #点击送信状態
        en.click(driver, 15,"testBl25",*self.Sendingstate_element)
        #选择未送信
        en.click(driver, 15,"testBl25",*self.notsend_element)
        #点击SJL輸入担当
#         en.click(driver, 15,"testBl25",*self.SJL_element)
        #选择alex
#         en.click(driver, 15,"testBl25",*self.alex_element)
        #点击检索
        en.click(driver, 15,"testBl25",*self.Search_element)
        #获取海外取引先
        actual_foreignguest=en.getText(driver, 15,"testBl25",*self.actual_foreignguest)
        #获取搜索结果的D/O no
        actual_do=en.getText(driver, 15,"testBl25",*self.actual_do)
        #获取搜索结果的B/L no
        actual_bl=en.getText(driver, 15,"testBl25",*self.actual_bl)
        sleep(1)
        #获取B/L date
        actual_bldate=en.getText(driver, 15,"testBl25",*self.atcual_date)
        #获取運送形態
        actual_shochin=en.getText(driver, 15,"testBl25",*self.actual_shochin)
        #获取送信状態的结果
        actual_send=en.getText(driver, 15,"testBl25",*self.actual_sendingstate)
        return actual_foreignguest,actual_do,actual_bl,actual_bldate,actual_shochin,actual_send,date,foreignguests
    
    #通过错误的B/L NO检索无结果
    def bl26(self,driver,blno):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl26",*self.BL_element)
        #输入B/L no
        en.send_keys(driver, 15,blno,"testBl26",*self.BLno_element)
        #点击检索
        en.click(driver, 15,"testBl26",*self.Search_element)
        nodata=en.getText(driver, 15,"testBl26",*self.nodata)
        return nodata
    
    #通过错误的D/O NO检索无结果
    def bl27(self,driver,dono):
        en=self.en
        #BL確認完了送信
        en.click(driver, 15,"testBl27",*self.BL_element)
        #输入B/L no
        en.send_keys(driver, 15,dono,"testBl27",*self.DOno_element)
        #点击检索
        en.click(driver, 15,"testBl27",*self.Search_element)
        nodata=en.getText(driver, 15,"testBl27",*self.nodata)
        return nodata