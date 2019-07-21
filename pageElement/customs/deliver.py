'''
将编辑成功的数据送信的页面对象
'''

from selenium.webdriver.common.by import By

class Deliver(object):

    #首页S/A登錄
    SAElement = (By.XPATH,'//main[@class="v-content"]//div[text()="S/A登録"]')

    #新規
    newRulesElement = (By.XPATH,'//div[text()="新規"]')

    #B/L NO
    BLElement = (By.XPATH,'//input[@aria-label="B/L NO"]')

    #編集按钮
    editElement = (By.XPATH,'//div[text()="編集"]')

    #検索按钮
    searchElement = (By.XPATH,'//div[text()="検索"]')

    #打钩按钮
    checkElement = (By.XPATH,'//main[@class="v-content"]//div[@class="v-input--selection-controls__ripple"]')

    #確定送信
    ensureDeliverElement = (By.XPATH,'//div[text()="確定送信"]')

    #コンテナ情報が不完全です
    incomplteInfoElement = (By.XPATH,'//div[text()="コンテナ情報が不完全です"]')

    #

    #SA送信成功しました。
    SADeliverSucceedElement = (By.XPATH,'//div[text()="SA送信成功しました。"]')

