'''
Created on 2019年5月22日

@author: chinasoft.xp.chen
'''

from random import choice
from time import sleep

from selenium.webdriver.common.keys import Keys

from pageElement.sendemail.SendMailEle import SendMailEle
from util.ElementUtil import ElementUtil


#from selenium.webdriver.common import keys
class SendOperate(SendMailEle):
    def __init__(self):
        self.en=ElementUtil()
       
    #通过B/L NO检索输入5个收件人和CC送信成功
    def sendMail1(self,driver,bl):
        en=self.en
        en.click(driver, 15,"testSendMail01",*self.Send_element)
        #输入B/L No
        en.send_keys(driver, 15,bl,"testSendMail01",*self.blno_element)
        #点击检索
        en.click(driver, 15,"testSendMail01",*self.Search_element)
        #点击B/l详情
        en.click(driver, 15,"testSendMail01",*self.bldetails_element)
        #点击纳入指示者1-CC
        sleep(2)
        clearlist = driver.find_elements(*self.clear_elements)
        for i in range(0, len(clearlist)):
            clearlist[i].click()
            sleep(0.5)
        en.send_keys(driver, 15,"NAOM","testSendMail01",*self.Deliveryone_element)
        en.click(driver, 15,"testSendMail01",*self.choice_receiver)
        en.send_keys(driver, 15,"廣本　","testSendMail01",*self.Deliverytwo_element)
        en.click(driver, 15,"testSendMail01",*self.choice_receiver)
        en.send_keys(driver, 15,"GU MINL","testSendMail01",*self.Deliverythree_element)
        en.click(driver, 15,"testSendMail01",*self.choice_receiver)
        en.send_keys(driver, 15,"Grace Zh","testSendMail01",*self.Deliveryfour_element)
        en.click(driver, 15,"testSendMail01",*self.choice_receiver)
        en.send_keys(driver, 15,"S.n.Ch","testSendMail01",*self.Deliveryfive_element)
        en.click(driver, 15,"testSendMail01",*self.choice_receiver)
        en.send_keys(driver, 15,"Danie","testSendMail01",*self.cc_element)
        en.click(driver, 15,"testSendMail01",*self.choice_receiver)
        #点击保存
        en.click(driver, 15,"testSendMail01",*self.preserve_alex)
        #点击勾选框
        sleep(4)
        en.click(driver, 15, "testSendMail01", *self.Option_element)
        # driver.find_element(*self.Option_element).send_keys(Keys.SPACE)
        sleep(1)
        #点击送信
        en.click(driver, 15,"testSendMail01",*self.Sendmail_element)
        #点击确定
        en.click(driver, 15,"testSendMail01",*self.sure_element)
        sleep(2)
        Success_element=en.getText(driver, 15,"testSendMail01",*self.actual_sendingstate)
        return Success_element
    
    
    #通过D/O NO检索输入5个收件人和CC送信成功
    def sendMail2(self,driver,bl):
        en=self.en
        en.click(driver, 15,"testSendMail02",*self.Send_element)
        #点击检索
        #输入do
        en.send_keys(driver, 15,bl,"testSendMail02",*self.dono_element)
        #点击检索
        en.click(driver, 15,"testSendMail02",*self.Search_element)
        sleep(1)
        #点击B/l详情
        js="window.scrollTo(400,1000)"
        driver.execute_script(js)
        en.click(driver, 15,"testSendMail02",*self.bldetails_element)
        #点击纳入指示者1-CC
        sleep(2)
        clearlist = driver.find_elements(*self.clear_elements)
        for i in range(0, len(clearlist)):
            clearlist[i].click()
            sleep(0.5)
        en.send_keys(driver, 15,"NAOM","testSendMail02",*self.Deliveryone_element)
        en.click(driver, 15,"testSendMail02",*self.choice_receiver)
        en.send_keys(driver, 15,"廣本　","testSendMail02",*self.Deliverytwo_element)
        en.click(driver, 15,"testSendMail02",*self.choice_receiver)
        en.send_keys(driver, 15,"GU MINL","testSendMail02",*self.Deliverythree_element)
        en.click(driver, 15,"testSendMail02",*self.choice_receiver)
        en.send_keys(driver, 15,"Grace Zh","testSendMail02",*self.Deliveryfour_element)
        en.click(driver, 15,"testSendMail02",*self.choice_receiver)
        en.send_keys(driver, 15,"S.n.Ch","testSendMail02",*self.Deliveryfive_element)
        en.click(driver, 15,"testSendMail02",*self.choice_receiver)
        en.send_keys(driver, 15,"Danie","testSendMail02",*self.cc_element)
        en.click(driver, 15,"testSendMail02",*self.choice_receiver)
        #点击保存
        en.click(driver, 15,"testSendMail02",*self.preserve_alex)
        #点击勾选框
        sleep(5)
        en.click(driver, 15, "testSendMail01", *self.Option_element)
        # driver.find_element(*self.Option_element).send_keys(Keys.SPACE)
        sleep(2)
        #点击送信
        en.click(driver, 15,"testSendMail02",*self.Sendmail_element)
        #点击确定
        en.click(driver, 15,"testSendMail02",*self.sure_element)
        sleep(3)
        Success_element=en.getText(driver, 15,"testSendMail02",*self.actual_sendingstate)
        return Success_element
    
   
    
    #通过D/O NO检索输入纳入指示者1和CC送信成功    
    def sendMail3(self,driver,do):
        en=self.en
        #输入do NO
        en.click(driver, 15,"testSendMail03",*self.Send_element)
        en.send_keys(driver, 15,do,"testSendMail03",*self.dono_element)
        #点击检索
        en.click(driver, 15,"testSendMail03",*self.Search_element)
        #点击B/l详情
        en.click(driver, 15,"testSendMail03",*self.bldetails_element)
        sleep(2)
        clearlist=driver.find_elements(*self.clear_elements)
        for i in range(0,len(clearlist)):
            clearlist[i].click()
            sleep(0.5)
        #点击纳入指示者1-CC
        en.send_keys(driver, 15,"NAOM","testSendMail03",*self.Deliveryone_element)
        en.click(driver, 15,"testSendMail03",*self.choice_receiver)
        en.send_keys(driver, 15,"Danie","testSendMail03",*self.cc_element)
        en.click(driver, 15,"testSendMail03",*self.choice_receiver)
        #点击保存
        en.click(driver, 15,"testSendMail03",*self.preserve_alex)
        #点击勾选框
        sleep(4)
        en.click(driver, 15, "testSendMail01", *self.Option_element)
        #en.click(driver, 15, *self.Option_element)
        # driver.find_element(*self.Option_element).send_keys(Keys.SPACE)
        sleep(2)
        #点击送信
        en.click(driver, 15,"testSendMail03",*self.Sendmail_element)
        #点击确定
        en.click(driver, 15,"testSendMail03",*self.sure_element)
        sleep(1)
        Success_element=en.getText(driver, 15,"testSendMail03",*self.actual_sendingstate)
        return Success_element
        
    
    #通过B/L NO检索输入纳入指示者5和CC送信成功
    def sendMail4(self,driver,bl):
        en=self.en
        en.click(driver, 15,"testSendMail04",*self.Send_element)
        #输入B/L NO
        en.send_keys(driver, 15,bl,"testSendMail04",*self.blno_element)
        #检索
        en.click(driver, 15,"testSendMail04",*self.Search_element)
        #点击B/l详情
        en.click(driver, 15,"testSendMail04",*self.bldetails_element)
        #点击纳入指示者5和CC
        sleep(2)
        clearlist=driver.find_elements(*self.clear_elements)
        for i in range(0,len(clearlist)):
            clearlist[i].click()
            sleep(0.5)
        en.send_keys(driver, 15,"S.n.Ch","testSendMail04",*self.Deliveryfive_element)
        en.click(driver, 15,"testSendMail04",*self.choice_receiver)
        en.send_keys(driver, 15,"Danie","testSendMail04",*self.cc_element)
        en.click(driver, 15,"testSendMail04",*self.choice_receiver)
        #点击保存
        en.click(driver, 15,"testSendMail04",*self.preserve_alex)
        #点击勾选框
        sleep(4)
        en.click(driver, 15, "testSendMail01", *self.Option_element)
        # driver.find_element(*self.Option_element).send_keys(Keys.SPACE)
        #点击送信
        sleep(1)
        en.click(driver, 15,"testSendMail04",*self.Sendmail_element)
        #点击确定
        en.click(driver, 15,"testSendMail04",*self.sure_element)
        sleep(1)
        Success_element=en.getText(driver, 15,"testSendMail04",*self.actual_sendingstate)
        return Success_element
        
    
    #通过B/L NO检索,输入1个收件人不输入CC送信成功
    def sendMail5(self,driver,bl):
        en=self.en
        en.click(driver, 15,"testSendMail05",*self.Send_element)
        #输入B/L NO
        en.send_keys(driver, 15,bl,"testSendMail05",*self.blno_element)
        #检索
        en.click(driver, 15,"testSendMail05",*self.Search_element)
        #点击B/l详情
        en.click(driver, 15,"testSendMail05",*self.bldetails_element)
        #输入纳入指示者
        sleep(2)
        clearlist=driver.find_elements(*self.clear_elements)
        for i in range(0,len(clearlist)):
            clearlist[i].click()
            sleep(0.5)
        en.send_keys(driver, 15,"S.n.Ch","testSendMail05",*self.Deliveryfive_element)
        en.click(driver, 15,"testSendMail05",*self.choice_receiver)
        #点击保存
        en.click(driver, 15,"testSendMail05",*self.preserve_alex)
        #点击勾选框
        sleep(4)
        en.click(driver, 15, "testSendMail01", *self.Option_element)
        # driver.find_element(*self.Option_element).send_keys(Keys.SPACE)
        sleep(1)
        #点击送信
        en.click(driver, 15,"testSendMail05",*self.Sendmail_element)
        #点击确定
        en.click(driver, 15,"testSendMail05",*self.sure_element)
        Success_element=en.getText(driver, 15,"testSendMail05",*self.actual_sendingstate)
        return Success_element
        
    
    #通过输入所有搜索框精确检索送信成功
    def sendMail6(self,driver,dono,blno):
        en=self.en
        #点击納入指示メール配信
        en.click(driver, 15,"testSendMail06",*self.Send_element)
        #输入bl
        en.send_keys(driver, 15,blno,"testSendMail06",*self.blno_element)
        #点击检索
        en.click(driver, 15,"testSendMail06",*self.Search_element)
        #点击BL详情
        en.click(driver, 15,"testSendMail06",*self.bldetails_element)
        sleep(2)
        en.send_keys(driver, 15,"Danie","testSendMail06",*self.cc_element)
        en.click(driver, 15,"testSendMail06",*self.choice_receiver)
        #点击保存
        en.click(driver, 15,"testSendMail06",*self.preserve_alex)
        #输入纳入指示者
        en.send_keys(driver, 15,"Daniel","testSendMail06",*self.Delivery)
        en.click(driver, 15,"testSendMail06",*self.choice_receiver)
        #输入D/O NO
        en.send_keys(driver, 15,dono,"testSendMail06",*self.dono_element)
        #输入B/L NO
        en.send_keys(driver, 15,blno,"testSendMail06",*self.blno_element)
        #点击检索
        en.click(driver, 15,"testSendMail06",*self.Search_element)
        #点击B/l详情
        en.click(driver, 15,"testSendMail06",*self.bldetails_element)
        sleep(2)
        #点击纳入指示者1-CC
        en.send_keys(driver, 15,"NAOM","testSendMail06",*self.Deliveryone_element)
        en.click(driver, 15,"testSendMail06",*self.choice_receiver)
        en.send_keys(driver, 15,"廣本　","testSendMail06",*self.Deliverytwo_element)
        en.click(driver, 15,"testSendMail06",*self.choice_receiver)
        en.send_keys(driver, 15,"GU MINL","testSendMail06",*self.Deliverythree_element)
        en.click(driver, 15,"testSendMail06",*self.choice_receiver)
        en.send_keys(driver, 15,"Grace Zh","testSendMail06",*self.Deliveryfour_element)
        en.click(driver, 15,"testSendMail06",*self.choice_receiver)
        en.send_keys(driver, 15,"S.n.Ch","testSendMail06",*self.Deliveryfive_element)
        en.click(driver, 15,"testSendMail06",*self.choice_receiver)
        en.send_keys(driver, 15,"Danie","testSendMail06",*self.cc_element)
        en.click(driver, 15,"testSendMail06",*self.choice_receiver)
        #点击保存
        en.click(driver, 15,"testSendMail06",*self.preserve_alex)
        #点击勾选框
        sleep(5)
        en.click(driver, 15, "testSendMail01", *self.Option_element)
        # driver.find_element(*self.Option_element).send_keys(Keys.SPACE)
        #点击送信
        en.click(driver, 15,"testSendMail06",*self.Sendmail_element)
        sleep(2)
        #点击确定
        en.click(driver, 15,"testSendMail06",*self.sure_element)
        Success_element=en.getText(driver, 15,"testSendMail06",*self.actual_sendingstate)
        return Success_element
    
    
    
    #不可以批量送信成功
    def sendMail7(self,driver,blno):
        en=self.en
        #点击納入指示メール配信
        en.click(driver, 15,"testSendMail07",*self.Send_element)
        #输入B/L NO
        en.send_keys(driver, 15,blno,"testSendMail07",*self.blno_element)
        #点击检索
        en.click(driver, 15,"testSendMail07",*self.Search_element)
        #点击B/l详情
        en.click(driver, 15,"testSendMail07",*self.bl_cxp006)
        sleep(3)
        clearlist=driver.find_elements(*self.clear_elements)
        for i in range(0,len(clearlist)):
            clearlist[i].click()
            sleep(0.5)
        en.send_keys(driver, 15,"NAOM","testSendMail07",*self.Deliveryone_element)
        en.click(driver, 15,"testSendMail07",*self.choice_receiver)
        en.send_keys(driver, 15,"Danie","testSendMail07",*self.cc_element)
        en.click(driver, 15,"testSendMail07",*self.choice_receiver)
        #点击保存
        en.click(driver, 15,"testSendMail07",*self.preserve_alex)
        #再次点击B/l详情
        sleep(2)
        en.click(driver, 15,"testSendMail07",*self.bl_cxp007)
        sleep(2)
        clear_list=driver.find_elements(*self.clear_elements)
        for i in range(0,len(clear_list)):
            clear_list[i].click()
            sleep(0.5)
        en.send_keys(driver, 15,"NAOM","testSendMail07",*self.Deliveryone_element)
        en.click(driver, 15,"testSendMail07",*self.choice_receiver)
        #点击保存
        en.click(driver, 15,"testSendMail07",*self.preserve_alex)
        #点击勾选框
        sleep(4)
        en.click(driver, 15,"testSendMail07",*self.option_cxp006)
        sleep(1)
        en.click(driver, 15,"testSendMail07",*self.option_cxp007)
        #点击送信
        en.click(driver, 15,"testSendMail07",*self.Sendmail_element)
        #点击确定
        en.click(driver, 15,"testSendMail07",*self.sure_element)
        #获取送信成功的文本
        Success_text1=en.getText(driver, 15,"testSendMail07",*self.sendresult_006)
        Success_text2=en.getText(driver, 15,"testSendMail07",*self.sendresult_007)
        return [Success_text1,Success_text2]
    
    #对已送信的可以进行送信解除
    def sendMail8(self,driver,blno):
        en=self.en
        #点击納入指示メール配信
        en.click(driver, 15,"testSendMail08",*self.Send_element)
        #输入B/L NO
        en.send_keys(driver, 15,blno,"testSendMail08",*self.blno_element)
        #点击检索
        en.click(driver, 15,"testSendMail08",*self.Search_element)
        en.click(driver, 15,"testSendMail08",*self.bldetails_element)
        sleep(2)
        clear_list=driver.find_elements(*self.clear_elements)
        for i in range(0,len(clear_list)):
            clear_list[i].click()
            sleep(0.5)
        en.send_keys(driver, 15,"NAOM","testSendMail08",*self.Deliveryone_element)
        en.click(driver, 15,"testSendMail08",*self.choice_receiver)
        #点击保存 
        en.click(driver, 15,"testSendMail08",*self.preserve_alex)
        sleep(4)
        #点击勾选
        en.click(driver, 15, "testSendMail01", *self.Option_element)
        # driver.find_element(*self.Option_element).send_keys(Keys.SPACE)
        sleep(1)
        #点击送信
        en.click(driver, 15,"testSendMail08",*self.Sendmail_element)
        #点击确定
        en.click(driver, 15,"testSendMail08",*self.sure_element)
        #点击勾选
        sleep(5)
        en.click(driver, 15, "testSendMail01", *self.Option_element)
        # driver.find_element(*self.Option_element).send_keys(Keys.SPACE)
        #点击送信解除
        en.click(driver, 15,"testSendMail08",*self.relieve_element)
        sleep(5)
        #点击确定
        en.click(driver, 15,"testSendMail08",*self.sure_element)
        Remove_text=en.getText(driver, 15,"testSendMail08",*self.tip3)
        return Remove_text
        
        
    #对已送信的可以批量解除送信
    def sendMail9(self,driver,blno):
        en=self.en
        #点击納入指示メール配信
        en.click(driver, 15,"testSendMail09",*self.Send_element)
        #输入B/L NO
        en.send_keys(driver, 15,blno,"testSendMail09",*self.blno_element)
        #点击检索
        en.click(driver, 15,"testSendMail09",*self.Search_element)
        #点击勾选所有的已送信
        sleep(3)
        sendEmail_list=driver.find_elements(*self.option_sendemail)
        for i in range(0,len(sendEmail_list)):
            sendEmail_list[i].click()
            sleep(0.5)
        #点击送信解除
        sleep(2)
        en.click(driver, 15,"testSendMail09",*self.relieve_element)
#         #点击确定
#         remove_text=en.getText(driver, 15,*self.remove_text)   
#         en.click(driver, 15,*self.sure_element)
#         return  remove_text


    #根据DO解除送信
    def sendMai25(self,driver,dono):
        en=self.en
        #点击納入指示メール配信
        en.click(driver, 15,"testSendMail25",*self.Send_element)
        #输入B/L NO
        en.send_keys(driver, 15,dono,"testSendMail25",*self.dono_element)
        #点击检索
        en.click(driver, 15,"testSendMail25",*self.Search_element)
        #点击勾选所有的已送信
        sleep(2)
        sendEmail_list=driver.find_elements(*self.option_sendemail)
        for i in range(0,len(sendEmail_list)):
            sendEmail_list[i].click()
            sleep(0.5)
        #点击送信解除
        en.click(driver, 15,"testSendMail25",*self.relieve_element)
#         #点击确定
#         remove_text=en.getText(driver, 15,*self.remove_text)   
#         en.click(driver, 15,*self.sure_element)
#         return  remove_text
    
    #通过b/l NO检索,不输入纳入指示者只输入CC送信失败
    def sendMail10(self,driver,bl):
        en=self.en
        #点击納入指示メール配信
        en.click(driver, 15,"testSendMail10",*self.Send_element)
        #输入B/L NO
        en.send_keys(driver, 15,bl,"testSendMail10",*self.blno_element)
        #点击检索
        en.click(driver, 15,"testSendMail10",*self.Search_element)
        #点击B/l详情
        en.click(driver, 15,"testSendMail10",*self.bldetails_element)
        sleep(2)
        clearlist=driver.find_elements(*self.clear_elements)
        for i in range (0,len(clearlist)):
            clearlist[i].click()
            sleep(0.5)
        #点击CC
        en.send_keys(driver, 15,"Danie","testSendMail10",*self.cc_element)
        en.click(driver, 15,"testSendMail10",*self.choice_receiver)
        #点击保存
        en.click(driver, 15,"testSendMail10",*self.preserve_alex)
        #点击勾选框
        sleep(5)
        en.click(driver, 15, "testSendMail01", *self.Option_element)
        # driver.find_element(*self.Option_element).send_keys(Keys.SPACE)
        sleep(1)
        #点击送信
        en.click(driver, 15,"testSendMail10",*self.Sendmail_element)
        sleep(1)
        tip2=en.getText(driver, 15,"testSendMail10",*self.tip2)
        #点击确定
        en.click(driver, 15,"testSendMail10",*self.sure_element)
        return tip2
        
    
    
    #通过B/L NO检索,不输入纳入指示者和CC送信失败
    def sendMail11(self,driver,bl):
        en=self.en
        en.click(driver, 15,"testSendMail11",*self.Send_element)
        #输入B/L NO
        en.send_keys(driver, 15,bl,"testSendMail11",*self.blno_element)
        #点击检索
        en.click(driver, 15,"testSendMail11",*self.Search_element)
        #点击B/l详情
        en.click(driver, 15,"testSendMail11",*self.bldetails_element)
        sleep(2)
        clearlist=driver.find_elements(*self.clear_elements)
        for i in range (0,len(clearlist)):
            clearlist[i].click()
            sleep(0.5)
        #点击保存
        en.click(driver, 15,"testSendMail11",*self.preserve_alex)
        #点击勾选框
        sleep(4)
        en.click(driver, 15, "testSendMail01", *self.Option_element)
        # driver.find_element(*self.Option_element).send_keys(Keys.SPACE)
        sleep(1)
        #点击送信
        en.click(driver, 15,"testSendMail11",*self.Sendmail_element)
        sleep(2)
        tip2=en.getText(driver, 15,"testSendMail11",*self.tip2)
        #点击确定
        en.click(driver, 15,"testSendMail11",*self.sure_element)
        return tip2
    
    #不输入条件检索成功
    def sendMail12(self,driver):
        #点击納入指示メール配信
        en=self.en
        en.click(driver, 15,"testSendMail12",*self.Send_element)
        #点击检索
        en.click(driver, 15,"testSendMail12",*self.Search_element)
        sleep(2)
        num=en.getText(driver, 15,"testSendMail12",*self.num_element)
        axtual_num=num[-3:]
        return axtual_num
    
    #通过納入指示者检索成功
    def sendMail13(self,driver):
        #点击納入指示メール配信
        en=self.en
        en.click(driver, 15,"testSendMail13",*self.Send_element)
        en.send_keys(driver, 15,"Daniel","testSendMail13",*self.Delivery)
        en.click(driver, 15,"testSendMail13",*self.choice_receiver)
        #点击检索
        en.click(driver, 15,"testSendMail13",*self.Search_element)
        sleep(1)
        num=en.getText(driver, 15,"testSendMail13",*self.num_element)
        axtual_num=num[-2:]
        return axtual_num
    
    #通过纳入指示者、D/O NO组合检索成功
    def sendMail14(self,driver,do):
        en=self.en 
        #点击納入指示メール配信
        en.click(driver, 15,"testSendMail14",*self.Send_element)
        #输入do
        en.send_keys(driver, 15,do,"testSendMail14",*self.dono_element)
        #点击检索
        en.click(driver, 15,"testSendMail14",*self.Search_element)
        #点击BL详情
        en.click(driver, 15,"testSendMail14",*self.bldetails_element)
        sleep(2)
        en.send_keys(driver, 15,"Daniel","testSendMail14",*self.cc_element)
        en.click(driver, 15,"testSendMail14",*self.choice_receiver)
        #点击保存
        en.click(driver, 15,"testSendMail14",*self.preserve_alex)
        #纳入指示者
        en.send_keys(driver, 15,"Danie", "testSendMail14",*self.Delivery)
        #输入纳入指示者
        en.click(driver, 15, "testSendMail14",*self.choice_receiver)
        #输入D/O NO
        en.send_keys(driver, 15,do,"testSendMail14",*self.dono_element)
        #点击检索
        en.click(driver, 15,"testSendMail14",*self.Search_element)
        do_num=en.getText(driver, 15,"testSendMail14",*self.do_num)
        return do_num
    
    #通过纳入指示者、B/L NO组合检索成功
    def sendMail15(self,driver,blno):
        en=self.en
        #点击納入指示メール配信
        en.click(driver, 15,"testSendMail15",*self.Send_element)
        # 纳入指示者
        en.send_keys(driver, 15, "Danie","testSendMail15", *self.Delivery)
        # 输入纳入指示者
        en.click(driver, 15,"testSendMail15",*self.choice_receiver)
        #输入B/L NO
        en.send_keys(driver, 15,blno,"testSendMail15",*self.blno_element)
        #点击检索
        en.click(driver, 15,"testSendMail15",*self.Search_element)
        bl_num=en.getText(driver, 15,"testSendMail15",*self.bl_num)
        return bl_num
        
    #通过纳入指示者、D/O NO、B/L NO组合检索成功   
    def sendMail16(self,driver,dono,blno):
        en=self.en
        #点击納入指示メール配信
        en.click(driver, 15,"testSendMail16",*self.Send_element)
        #输入bl
        en.send_keys(driver, 15,blno,"testSendMail16",*self.blno_element)
        #点击检索
        en.click(driver, 15,"testSendMail16",*self.Search_element)
        #点击BL详情
        en.click(driver, 15,"testSendMail16",*self.bldetails_element)
        sleep(2)
        en.send_keys(driver, 15,"Danie","testSendMail16",*self.cc_element)
        en.click(driver, 15,"testSendMail16",*self.choice_receiver)
        #点击保存
        en.click(driver, 15,"testSendMail16",*self.preserve_alex)
        # 纳入指示者
        en.send_keys(driver, 15, "Danie","testSendMail16", *self.Delivery)
        # 输入纳入指示者
        en.click(driver, 15, "testSendMail16",*self.choice_receiver)
        #DO
        en.send_keys(driver, 15,dono,"testSendMail16",*self.dono_element)
        #输入B/L NO
        en.send_keys(driver, 15,blno,"testSendMail16",*self.blno_element)
        #点击检索
        en.click(driver, 15,"testSendMail16",*self.Search_element)
        bl_num=en.getText(driver, 15,"testSendMail16",*self.bl_num)
        do_num=en.getText(driver, 15,"testSendMail16",*self.do_num)
        db_list=[do_num,bl_num]
        return db_list
    
    #通过错误的D/O NO检索没有结果
    def sendMail17(self,driver,dono):
        en=self.en
        #点击納入指示メール配信
        en.click(driver, 15,"testSendMail17",*self.Send_element)
        #DO
        en.send_keys(driver, 15,dono,"testSendMail17",*self.dono_element)
        #点击检索
        en.click(driver, 15,"testSendMail17",*self.Search_element)
        nodata=en.getText(driver, 15,"testSendMail17",*self.no_data)
        return nodata
    
    #通过错误的B/L NO检索，检索无结果
    def sendMail18(self,driver,blno):
        en=self.en
        #点击納入指示メール配信
        en.click(driver, 15,"testSendMail18",*self.Send_element)
        #DO
        en.send_keys(driver, 15,blno,"testSendMail18",*self.blno_element)
        #点击检索
        en.click(driver, 15,"testSendMail18",*self.Search_element)
        nodata=en.getText(driver, 15,"testSendMail18",*self.no_data)
        return nodata
    
   
 
##################################################################################
    #封装一个方法，勾选可以送信的数据
    def choiceSendEmail(self,driver):     
        driver.find_element(*self.Send_element).click()
        sleep(1)
        #点击检索
        driver.find_element(*self.Search_element).click()     
        element_list1 = driver.find_elements(*self.option_1)
        element_list2 = driver.find_elements(*self.option_2)
        element_list1.extend(element_list2)
        while element_list1==[]:
            js1 = "document.documentElement.scrollTop=10000"  
            driver.execute_script(js1)
            driver.find_element(*self.next_page_element).click()
            sleep(1)
            element_list1 = driver.find_elements(*self.option_1)
            element_list2 = driver.find_elements(*self.option_2)
            element_list1.extend(element_list2)            
        choice(element_list1).click()
        sleep(1)
        
             
    #封装一个方法，获取可以送信的B/L NO
    def getBl(self,driver,bl1):   
        en=self.en
        en.click(driver, 15,"getBl",*self.Send_element)
        #点击检索
        #输入BL
        en.send_keys(driver, 15,bl1,"getBl",*self.blno_element)
        en.click(driver, 15,"getBl",*self.Search_element)
        sleep(2)  
        element_list1 = driver.find_elements(*self.BL1)
        element_list2 = driver.find_elements(*self.BL2)
        while element_list1==[]:
#             js1 = "document.documentElement.scrollTop=10000"  
#             driver.execute_script(js1)
            en.click(driver, 15,*self.next_page_element)
            element_list1 = driver.find_elements(*self.BL1)
            element_list2 = driver.find_elements(*self.BL2)
            element_list1.extend(element_list2)            
        bl=choice(element_list1).text
        sleep(1)
        return bl

     
    def clearreceiver(self,clearlist):
        for i in range (0,len(clearlist)):
            clearlist[i].click()
            sleep(1)
        
        
        #封装一个方法，获取可以送信的D/O NO
    def getDo1(self,driver):     
        driver.find_element(*self.Send_element).click()
        sleep(2)
        #点击检索
        driver.find_element(*self.Search_element).click()   
        sleep(2)  
        element_list1 = driver.find_elements(*self.DO1)
        element_list2 = driver.find_elements(*self.DO2)
        element_list1.extend(element_list2)  
        while element_list1==[] :
            js1 = "document.documentElement.scrollTop=10000"  
            driver.execute_script(js1)
            driver.find_element(*self.next_page_element).click()
            sleep(2)
            element_list1 = driver.find_elements(*self.DO1)
            element_list2 = driver.find_elements(*self.DO2)
            element_list1.extend(element_list2)                      
        return element_list1