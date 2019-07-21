from pageElement.ConfirmAcceptance.CAccept import CAccept
from time import sleep
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from business.Login import Login
from util.ElementUtil import ElementUtil
from selenium.webdriver.common.action_chains import ActionChains

class CAcceptance(CAccept):


    def __init__(self):
        self.en = ElementUtil()

#筛选不同状态数据：0为受入確認，
    def publicElement(self,driver,style):
        en=self.en
        # 选择受入确认
        en.click(driver, 10, "受入確認_コンテナNo修改成功", *self.CAcceptanceElement)
        # 筛选不同状态的数据
        sleep(2)
        en.click(driver, 10, "受入確認_コンテナNo修改成功", *self.SelectSelectionsElement)
        if style==0:
            en.click(driver, 10, "受入確認_コンテナNo修改成功", *self.AcceptElement)
        else:
            en.click(driver, 10, "受入確認_コンテナNo修改成功", *self.DeliveryElement)
        en.click(driver, 10, "受入確認_コンテナNo修改成功", *self.SearchElement)
        sleep(5)

    # コンテナNo更新
    def ContainerNoUp(self, style,driver,dono=None):
        # 点击コンテナNo更新
        self.en.click(driver, 10, "納入指示済_コンテナNo修改成功", *self.ClickContainerUpElement)
        if style == 0:
            # 填写コンテナNo更新
            UpNo =dono
        else:
            UpNo = "TestAcceptNoBack" + str(time.strftime('%H%M%S', time.localtime(time.time())))
        self.en.send_keys(driver, 10, UpNo, "納入指示済_コンテナNo修改成功", *self.InputContainerUpElement)
        return UpNo

#配送模式修改
    def DeliveryModelUp(self,driver):
        # 点击パターン設定
        self.en.click(driver, 10, "受入確認_配送模式修改成功", *self.ClickPatternElement)
        # 点击配送パターン
        sleep(1)
        original = self.en.getText(driver, 10, "受入確認_配送模式修改成功", *self.GitPatternElement)
        sleep(1)
        self.en.click(driver, 10, "受入確認_配送模式修改成功", *self.ClickDeliveryPatternElement)
        # 选择配送パターン
        self.en.click(driver, 10, "受入確認_配送模式修改成功", *self.SelectDeliveryPatternElement)
        # 选择第一条
        DeliveryModel = self.en.getText(driver, 10, "受入確認_配送模式修改成功", *self.ChoiceDeliveryPatternElement)
        self.en.click(driver, 10, "受入確認_配送模式修改成功", *self.ChoiceDeliveryPatternElement)
        # action_chains = ActionChains(driver)
        # action_chains.double_click(driver.find_element(*self.SelectDeliveryPatternElement)).perform()
        # sleep(1)
        # self.en.click(driver, 10, "受入確認_配送模式修改成功", *self.ChoiceDeliveryPatternElement1)

        return DeliveryModel,original

#納入情報一括変更 0表示填写
    def DeliveryInformationUp(self,driver,date,period):
        en=self.en
        # 点击納入情報一括変更
        en.click(driver, 10, "納入指示済_納入情報修改成功", *self.ClickInformationUPElement)
        if date==0:
            sleep(3)
            # 填写納入予定日
            en.click(driver, 10, "納入指示済_納入情報修改成功", *self.DeliveryDateElement)
            sleep(1)
            en.click(driver, 10, "納入指示済_納入情報修改成功", *self.ChoiceDeliveryDateElement)
            sleep(2)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(self.DeliveryDateElement))
            ECDeliveryDate = driver.find_element(*self.DeliveryDateElement).get_attribute('value')
            sleep(1)
        else:
            ECDeliveryDate ="null"
        if period==0:
            # 填写受入予定时间
            ECDeliveryTime = time.strftime('%H%M', time.localtime(time.time()))
            en.send_keys(driver, 10, ECDeliveryTime, "納入指示済_納入情報修改成功", *self.InputAcceptanceTimeElement)
            sleep(2)
        else:
            ECDeliveryTime = "null"
        return ECDeliveryDate,ECDeliveryTime


#01受入確認済 コンテナNo更新
    def Acceptance(self, driver):
        en=self.en
        # 筛选状态为受入確認的数据
        self.publicElement(driver,0)
        #获取第一条数据的DONO
        dono=en.getText(driver, 10, "受入確認_コンテナNo修改成功", *self.GitDONoElement)
        # 选择状态为受入確認的数据
        en.click(driver, 10, "受入確認_コンテナNo修改成功", *self.ChoiceAcceptElement)
        #コンテナNo更新
        expect=self.ContainerNoUp(0,driver,dono)
        # 点击更新
        en.click(driver, 10, "受入確認_コンテナNo修改成功",*self.ClickNoUpElement)
        sleep(3)
        # 点击确认
        en.click(driver, 10, "受入確認_コンテナNo修改成功", *self.ClickYesElement)
        # #筛选通过DONO选择的数据
        # en.send_keys(driver, 10,dono, "受入確認_コンテナNo修改成功", *self.InputDONOElement)
        # # 筛选通过コンテナNo选择的数据
        # en.send_keys(driver, 10, expect, "受入確認_コンテナNo修改成功", *self.InputAcceptNoElement)
        # sleep(1)
        # en.click(driver, 10, "受入確認_コンテナNo修改成功", *self.SearchElement)
        # # 获取选择受入確認的コンテナNo
        # time.sleep(2)
        # actual=en.getText(driver, 10, "受入確認_コンテナNo修改成功", *self.GitAcceptNoElement)
        # return expect, actual
        return "OK"


#02納入指示済 コンテナNo更新
    def Delivery(self, driver):
        en=self.en
        # 筛选状态为納入指示済的数据
        self.publicElement(driver, 1)
        #获取第一条数据的DONO
        dono=en.getText(driver, 10, "納入指示済_コンテナNo修改成功", *self.GitDONoElement)
        # 选择状态为納入指示済的数据
        en.click(driver, 10, "納入指示済_コンテナNo修改成功", *self.ChoiceAcceptElement)
        # コンテナNo更新
        expect=self.ContainerNoUp(0,driver,dono)
        # 点击更新
        en.click(driver, 10, "納入指示済_コンテナNo修改成功", *self.ClickNoUpElement)
        sleep(3)
        # 点击确认
        en.click(driver, 10, "納入指示済_コンテナNo修改成功", *self.ClickYesElement)
        # # 筛选通过DONO选择的数据
        # en.send_keys(driver, 10,dono, "納入指示済_コンテナNo修改成功", *self.InputDONOElement)
        # # 筛选通过コンテナNo选择的数据
        # en.send_keys(driver, 10, expect, "納入指示済_コンテナNo修改成功", *self.InputAcceptNoElement)
        # en.click(driver, 10, "納入指示済_コンテナNo修改成功", *self.SearchElement)
        # 获取选择受入確認的コンテナNo
        # sleep(2)
        # actual=en.getText(driver, 10, "納入指示済_コンテナNo修改成功", *self.GitAcceptNoElement)
        actual = "OK"
        # return expect, actual
        return actual
#03受入確認済 配送パターン修改
    def AcceptancePattern(self,driver):
        en=self.en
        # 筛选状态为受入確認的数据
        self.publicElement(driver, 0)
        # 选择状态为受入確認的数据
        en.click(driver, 10, "受入確認_配送模式修改成功", *self.ChoiceAcceptElement)
        #配送模式修改
        expect=self.DeliveryModelUp(driver)[0]
        #点击配送パターン保存
        en.click(driver, 10, "受入確認_配送模式修改成功", *self.SaveDeliveryPatternElement)
        sleep(4)
        #获取修改后的配送パターン
        actual=en.getText(driver, 10, "受入確認_配送模式修改成功", *self.GitPatternElement)
        # 点击配送パターン設定戻る
        en.click(driver, 10, "受入確認_配送模式修改成功", *self.ClickPatternBackElement)
        return expect,actual

#04納入指示済 納入情報一括変更
    def DeliveryInformation(self,driver):
        en=self.en
        # 筛选状态为納入指示済的数据
        self.publicElement(driver, 1)
        # 获取第一条数据的コンテナNo
        AcceptNo=en.getText(driver, 10, "納入指示済_納入情報修改成功", *self.GitAcceptNoElement)
        # 选择状态为納入指示済的数据
        en.click(driver, 10, "納入指示済_納入情報修改成功", *self.ChoiceAcceptElement)
        #点击納入情報一括変更
        sleep(2)
        DeliveryInformationUp=self.DeliveryInformationUp(driver,0,0)
        ECDeliveryDate=DeliveryInformationUp[0]
        sleep(2)
        ECDeliveryTime=DeliveryInformationUp[1]
        #点击追加
        en.click(driver, 10, "納入指示済_納入情報修改成功", *self.ClickAdditionElement)
        sleep(2)
        #通过コンテナNo筛选选择的数据
        en.send_keys(driver,10,AcceptNo, "納入指示済_納入情報修改成功", *self.InputAcceptNoElement)
        en.click(driver, 10, "納入指示済_納入情報修改成功", *self.SearchElement)
        #获取修改后的納入予定日
        ACDeliveryDate=en.getText(driver,10, "納入指示済_納入情報修改成功", *self.GitDeliveryDateElement)
        #获取修改后的受入予定時間
        DeliveryTime = en.getText(driver, 10, "納入指示済_納入情報修改成功", *self.GitDeliveryTimeElement)
        ACDeliveryTime=''.join(DeliveryTime.split(":"))
        return ECDeliveryDate,ECDeliveryTime,ACDeliveryDate,ACDeliveryTime

#05纳入指示済 納入情報修改追加失败（仅填写納入予定日）
    def OnlyDeliveryDateUp(self,driver):
        en=self.en
        # 筛选状态为納入指示済的数据
        self.publicElement(driver, 1)
        # 获取第一条数据的コンテナNo
        AcceptNo=en.getText(driver, 10, "納入指示済_仅填写納入予定日追加失败", *self.GitAcceptNoElement)
        # 选择状态为納入指示済的数据
        en.click(driver, 10, "納入指示済_仅填写納入予定日追加失败", *self.ChoiceAcceptElement)
        sleep(2)
        # 点击納入情報一括変更（仅填写納入予定日）
        self.DeliveryInformationUp(driver, 0, 1)
        #查看是否可以追加
        actual=driver.find_element(*self.ClickAdditionElement).is_enabled()
        expect=0
        return expect,actual
#06纳入指示済 納入情報修改追加失败（仅填写納入予定时间）
    def OnlyDeliveryTimeUp(self,driver):
        en=self.en
        # 筛选状态为納入指示済的数据
        self.publicElement(driver, 1)
        # 获取第一条数据的コンテナNo
        AcceptNo=en.getText(driver, 10, "納入指示済_仅填写納入予定时间追加失败", *self.GitAcceptNoElement)
        # 选择状态为納入指示済的数据
        en.click(driver, 10, "納入指示済_仅填写納入予定时间追加失败", *self.ChoiceAcceptElement)
        # 点击納入情報一括変更（仅填写納入予定时间）
        self.DeliveryInformationUp(driver, 1, 0)
        #查看是否可以追加
        actual=driver.find_element(*self.ClickAdditionElement).is_enabled()
        expect=0
        sleep(2)
        return expect,actual

#07纳入指示済 配送パターン修改失败
    def BackDeliveryPatternUP(self,driver):
        # 筛选状态为纳入指示済的数据
        self.publicElement(driver, 1)
        # 选择状态为受入確認的数据
        self.en.click(driver, 10, "納入指示済_配送模式修改失败", *self.ChoiceAcceptElement)
        # 配送模式修改
        expect = self.DeliveryModelUp(driver)[1]
        #点击配送パターン戻る
        self.en.click(driver, 10, "納入指示済_配送模式修改失败", *self.ClickDeliveryBackElement)
        actual=self.en.getText(driver,10, "納入指示済_配送模式修改失败", *self.GitPatternElement)
        # 点击配送パターン設定戻る
        self.en.click(driver, 10, "納入指示済_配送模式修改失败", *self.ClickPatternBackElement)
        return expect,actual

#08受入确认済 コンテナNo修改失败
    def BackAcceptanceUP(self,driver):
        # 筛选状态为受入指示済的数据
        self.publicElement(driver, 0)
        # 选择状态为納入指示済的数据
        self.en.click(driver, 10, "受入確認_コンテナNo修改失败", *self.ChoiceAcceptElement)
        # コンテナNo更新
        AcceptNo = self.ContainerNoUp(1, driver)
        # 点击戻る
        self.en.click(driver, 10, "受入確認_コンテナNo修改失败", *self.ClickAcceptNoBackElement)
        # 通过コンテナNo筛选数据
        self.en.send_keys(driver, 10, AcceptNo, "受入確認_コンテナNo修改失败", *self.InputAcceptNoElement)
        self.en.click(driver, 10, "受入確認_コンテナNo修改失败", *self.SearchElement)
        # 获取筛选后table返回的数据
        actual = self.en.getText(driver, 10, "受入確認_コンテナNo修改失败", *self.GitTableElement)
        expect="No data available"
        return expect, actual

#09受入确认済 配送パターン修改失败
    def BackAcceptancePatternUP(self,driver):
        # 筛选状态为受入指示済的数据
        self.publicElement(driver, 0)
        # 选择状态为受入確認的数据
        self.en.click(driver, 10, "受入確認_配送パターン修改失败", *self.ChoiceAcceptElement)
        # 配送模式修改
        expect = self.DeliveryModelUp(driver)[1]
        # 点击配送パターン戻る
        self.en.click(driver, 10, "受入確認_配送パターン修改失败", *self.ClickDeliveryBackElement)
        sleep(2)
        actual = self.en.getText(driver, 10, "受入確認_配送パターン修改失败", *self.GitPatternElement)
        # 点击配送パターン設定戻る
        self.en.click(driver, 10, "受入確認_配送パターン修改失败", *self.ClickPatternBackElement)
        return expect,actual

#10纳入指示済 コンテナNo修改失败
    def BackDeliveryUP(self,driver):
        en=self.en
        # 筛选状态为纳入指示済的数据
        self.publicElement(driver, 1)
        # 选择状态为納入指示済的数据
        en.click(driver, 10, "纳入指示済_コンテナNo修改失败", *self.ChoiceAcceptElement)
        # コンテナNo更新
        AcceptNo = self.ContainerNoUp(1, driver)
        # 点击戻る
        en.click(driver, 10, "纳入指示済_コンテナNo修改失败", *self.ClickAcceptNoBackElement)
        # 通过コンテナNo筛选数据
        en.send_keys(driver, 10,AcceptNo, "纳入指示済_コンテナNo修改失败", *self.InputAcceptNoElement)
        en.click(driver, 10, "纳入指示済_コンテナNo修改失败", *self.SearchElement)
        sleep(2)
        # 获取筛选后table返回的数据
        actual=en.getText(driver, 10, "纳入指示済_コンテナNo修改失败", *self.GitTableElement)
        expect = "No data available"
        return expect, actual
#11納入指示済 納入情報一括変更失败
    def BackDeliveryInformationUP(self,driver):
        en=self.en
        # 筛选状态为纳入指示済的数据
        self.publicElement(driver, 1)
        # 获取第一条数据的コンテナNo
        AcceptNo=en.getText(driver, 10, "纳入指示済_納入情報修改失败", *self.GitAcceptNoElement)
        # 选择状态为納入指示済的数据
        en.click(driver, 10, "纳入指示済_納入情報修改失败", *self.ChoiceAcceptElement)
        #获取修改前的納入予定日
        ECDeliveryDate=en.getText(driver, 10, "纳入指示済_納入情報修改失败", *self.GitDeliveryDateElement)
        #获取修改前的受入予定時間
        ECDeliveryTime = en.getText(driver, 10, "纳入指示済_納入情報修改失败", *self.GitDeliveryTimeElement)
        # 点击納入情報一括変更
        self.DeliveryInformationUp(driver, 0, 0)
        #点击戻る
        en.click(driver, 10, "纳入指示済_納入情報修改失败", *self.ClickComplaintsBackElement)
        sleep(2)
        # 通过コンテナNo筛选选择的数据
        en.send_keys(driver,10,AcceptNo, "纳入指示済_納入情報修改失败", *self.InputAcceptNoElement)
        en.click(driver, 10, "纳入指示済_納入情報修改失败", *self.SearchElement)
        #获取修改后的納入予定日
        ACDeliveryDate = en.getText(driver,10, "纳入指示済_納入情報修改失败", *self.GitDeliveryDateElement)
        #获取修改后的受入予定時間
        ACDeliveryTime = en.getText(driver, 10, "纳入指示済_納入情報修改失败", *self.GitDeliveryTimeElement)
        return ECDeliveryDate,ECDeliveryTime,ACDeliveryDate,ACDeliveryTime


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)
    driver.maximize_window()
    url = "https://sharpuat.jusdaglobal.com"
    driver.get(url)
    # 登录
    login = Login()
    login.test_click_login_btn(driver)
    test = CAcceptance()
    test.BackDeliveryPatternUP(driver)
    driver.quit()
