from selenium.webdriver.common.by import By


def login(driver):
    username = [By.XPATH,'//input[@aria-label="ログインID"]']
    password = [By.XPATH,'//input[@aria-label="パスワード"]']
    button = [By.XPATH,'//div[@id="app"]/div[5]/main/div/div[1]/div/div[3]/button']
    
    driver.find_element(*username).clear()
    driver.find_element(*username).send_keys('alex')
    driver.find_element(*password).clear()
    driver.find_element(*password).send_keys('alex')
    driver.find_element(*button)
