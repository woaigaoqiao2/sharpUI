

from time import sleep

from pageElement.BlElement import BlElement


class BlOperate(BlElement):


    def bl(self,driver):
        driver.find_element(*self.BL_element).click()
        driver.find_element(*self.Search_element).click()
        driver.find_element(*self.Option_element).click()
        driver.find_element(*self.Inform_element).click()
        sleep(2)
        driver.find_element(*self.Sure_element).click()
        success_text=driver.find_element(*self.Success_element).text
        return success_text
