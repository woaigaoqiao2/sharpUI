'''
Created on 2019年6月20日

@author: chinasoft.jl.ma
'''

def init(driver):
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)