import os

def isElementExist(driver,element):
    '''判断元素是否存在'''
    from selenium.common.exceptions import NoSuchElementException
    try:
        driver.find_element(*element)
        # print('%s 不存在！'%element)
    except NoSuchElementException as e:
        return False
    else:
        return True


def fileExists():
    '''读取文件'''
    current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    num_txt = os.path.join(os.path.dirname(current_path),'sharpUI','data','num.txt')
    num_txt = num_txt.replace('\\','/')
    return num_txt

if __name__ == '__main__':
    fileExists()