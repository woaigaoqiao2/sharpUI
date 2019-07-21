
from time import sleep
# import unittest
from pageElement.SendMailEle import SendMailEle
# from util import log


class SendOperate(SendMailEle):
    def sendMail(self,driver):
#       logs = log.log_message()
        driver.find_element(*self.Send_element).click()
        driver.find_element(*self.Search_element).click()
        driver.find_element(*self.Option_element).click()
        driver.find_element(*self.Sendmail_element).click()
        sleep(2)
        driver.find_element(*self.Alert_sure).click()
        success_text=driver.find_element(*self.Success_element).text
        return success_text
        
#         try:
#             success_text=driver.find_element(*self.Success_element).text
#             self.assertIn('既に送信済み。',success_text)
#         except Exception as e:
#             logs.error_log('用例执行失败，原因：%s' % e)
        
        
        

        
        

    