from selenium.webdriver.common.by import By
from time import sleep

class loading():

    def loading(self,driver,count):

            Loading = [By.XPATH, "//div[@class='v-dialog v-dialog--persistent']"]
            while count:
                loading = driver.find_element(Loading)
                status = loading.is_displayed()
                if status == False:
                    print('首页loading层消失')
                    break
                else:
                    count -= 1
                    print('loading层还没有消失，等待三秒')
                    sleep(3)
                    continue