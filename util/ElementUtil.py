"""
Created on 2019年6月24日

元素操作工具类
@author: chinasoft.l.yu

"""
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from util.logs import logs


class ElementUtil():

    """
    获取元素
    num ：执行次数
    *element：对应页面元素
    :param explain  描述
    """
    def getElement(self,driver,num,explain,*element):
        #   默认返回结果
        result = {
            "code" : 500,
            "msg" : ""
        }
        loadStatus = ""   #当前load加载状态
        while num > 0:
            num = num -1
            js = "return document.getElementsByClassName('v-progress-circular__info')" \
                 "[0].parentElement.parentElement.parentElement.parentElement.style.display"
            loadStatus = driver.execute_script(js)
            # print("---------当前load状态----------：",loadStatus,
            #       " 执行次数：",str(num)+" 当前元素："+element.__str__()," 描述："+explain)
            if loadStatus == "none":
                try:
                    el = driver.find_element(element[0],element[1])
                    if hasattr(el, "location"):
                        result['code'] = 200
                        result['msg'] = "成功"
                        result['element'] = el
                        break
                except Exception as e:
                    if num == 0:
                        msg = "用例描述：",explain," 执行find_element时不通过"
                        logs("ui").error_log(msg)
                        logs("ui").error_log(e)
                        assert "用例执行find_element时不通过" == "通过!"
                    else:
                        sleep(1)
            else:
                if num == 0:
                    msg = "用例描述：",explain,"当前load加载状态：",loadStatus
                    logs("ui").error_log(msg)
                    result['msg'] = "当前load加载状态:",loadStatus
                    assert "当前load层状态为："+loadStatus+"!" == "通过"
                else:
                    sleep(1)
        return result


    """
    执行click
    num ：执行次数
    *element：对应页面元素
    :param explain  描述
    """
    def click(self,driver,num,explain,*element):
        el = ElementUtil.getElement(self,driver,num,explain,*element)
        if el.get("code") != 200:
            msg = "用例描述："+explain+" 执行click方法时调用getElement不通过!"
            logs("ui").error_log(msg)
            logs("ui").error_log(el)
            assert "用例执行click方法时调用getElement不通过!" == "通过!"

        if 'element' in el.keys() and el['element'] != "":
            el = el.get("element")
            while num > 0:
                num = num -1
                try:
                    el.click()
                    break
                except Exception as e:
                    if num == 0:
                        msg = "用例描述：",explain," 执行click方法时不通过!"
                        logs("ui").error_log(msg)
                        logs("ui").error_log(e)
                        assert "用例执行click方法时不通过!" == "通过!"
                    else:
                        sleep(1)
        else:
            msg = "用例描述："+explain+" 执行click方法时调用element不通过!"
            logs("ui").error_log(msg)
            logs("ui").error_log(el)
            assert "用例执行click方法时调用element不通过!" == "通过!"

    """
    执行clear
    num ：执行次数
    *element：对应页面元素
    :param explain  描述
    """
    def clear(self,driver,num,explain,*element):
        el = ElementUtil.getElement(self,driver,num,explain,*element)
        if el.get("code") != 200:
            msg = "用例描述：",explain," 执行clear方法时调用getElement不通过!"
            logs("ui").error_log(msg)
            logs("ui").error_log(el)
            assert "执行clear方法时调用getElement不通过!" == "通过!"

        if 'element' in el.keys() and el['element'] != "":
            el = el.get("element")
            while num > 0:
                num = num -1
                try:
                    action = ActionChains(driver)
                    action.double_click(el).perform()
                    el.send_keys(Keys.CONTROL,'a')
                    el.send_keys(Keys.BACKSPACE)
                    break
                except Exception as e:
                    if num == 0:
                        msg = "用例描述："+explain+" 执行clear方法时不通过!"
                        logs("ui").error_log(msg)
                        logs("ui").error_log(e)
                        assert "用例执行clear方法时不通过!" == "通过!"
                    else:
                        sleep(1)
        else:
            msg = "用例描述："+explain+" 执行clear方法时调用element不通过!"
            logs("ui").error_log(msg)
            logs("ui").error_log(el)
            assert "用例执行clear方法时调用element不通过！" == "通过!"


    """
    输入值
    num ：执行次数
    values ：对应值
    *element：对应页面元素
    :param explain  描述
    """
    def send_keys(self, driver, num, values, explain, *element):
        el = ElementUtil.getElement(self, driver, num, explain, *element)
        if(el.get("code")!=200):
            msg = "用例描述：",explain," 执行is_enabled方法时调用getElement不通过!"
            logs("ui").error_log(msg)
            logs("ui").error_log(el)
            assert "执行is_enabled方法时调用getElement不通过!" == "通过!"

        if 'element' in el.keys() and el['element'] != "":
            el = el.get("element")
            while num > 0:
                num = num -1
                try:
                    action = ActionChains(driver)
                    action.double_click(el).perform()
                    el.send_keys(Keys.CONTROL,'a')
                    el.send_keys(Keys.BACKSPACE)
                    el.send_keys(values)
                    break
                except Exception as e:
                    if num==0:
                        msg = "用例描述：",explain," 执行send_keys方法时不通过!"
                        logs("ui").error_log(msg)
                        logs("ui").error_log(e)
                        assert "用例执行send_keys方法时不通过!" == "通过!"
                    else:
                        sleep(1)
        else:
            msg = "用例描述：",explain," 执行send_keys方法时调用element不通过!"
            logs("ui").error_log(msg)
            logs("ui").error_log(el)
            assert "用例执行send_keys方法时调用element不通过！" == "通过!"

    """
    判断按钮是否可点击
    num ：执行次数
    *element：对应页面元素
    :param explain  描述
    """
    def is_enabled(self,driver,num,explain,*element):
        r = None
        el = ElementUtil.getElement(self,driver,num,explain,*element)
        if(el.get("code")!=200):
            msg = "用例描述：",explain," 执行is_enabled方法时调用getElement不通过!"
            logs("ui").error_log(msg)
            logs("ui").error_log(el)
            assert "执行is_enabled方法时调用getElement不通过!" == "通过!"

        if 'element' in el.keys() and el['element'] != "":
            el = el.get("element")
            while num > 0:
                num = num -1
                try:
                    r = el.is_enabled()
                    break
                except Exception as e:
                    if num == 0 :
                        msg = "用例描述：",explain," 执行is_enabled方法时不通过!"
                        logs("ui").error_log(msg)
                        logs("ui").error_log(e)
                        assert "用例执行is_enabled方法时不通过!" == "通过!"
                    else:
                        sleep(1)
        else:
            msg = "用例描述：",explain," 执行is_enabled方法时调用element不通过!"
            logs("ui").error_log(msg)
            logs("ui").error_log(el)
            assert "用例执行is_enabled方法时调用element不通过！" == "通过!"
        return r


    """
    清空下拉文本框值
    num ：执行次数
    *element：对应页面元素
    :param explain  描述
    """
    def clearSelectInput(self,driver,num,explain,*element):
        el = ElementUtil.getElement(self,driver,num,explain,*element)
        if(el.get("code")!=200):
            msg = "用例描述：",explain," 执行clearSelectInput方法时调用getElement不通过!"
            logs("ui").error_log(msg)
            logs("ui").error_log(el)
            assert "执行clearSelectInput方法时调用getElement不通过!" == "通过!"

        if 'element' in el.keys() and el['element'] != "":
            el = el.get("element")
            while num > 0:
                num = num -1
                try:
                    ActionChains(driver).move_to_element(el).perform()
                    el.click()
                    break
                except Exception as e:
                    if num == 0:
                        msg = "用例描述：",explain," 执行clearSelectInput方法时不通过!"
                        logs("ui").error_log(msg)
                        logs("ui").error_log(e)
                        assert "用例执行clearSelectInput方法时不通过!" == "通过!"
                    else:
                        sleep(1)
        else:
            msg = "用例描述：",explain," 执行clearSelectInput方法时调用element不通过!"
            logs("ui").error_log(msg)
            logs("ui").error_log(el)
            assert "用例执行clearSelectInput方法时调用element不通过！" == "通过!"


    """
    执行Text
    num ：执行次数
    *element：对应页面元素
    :param explain  描述
    """
    def getText(self,driver,num,explain,*element):
        el = ElementUtil.getElement(self,driver,num,explain,*element)
        r = ""
        if el.get("code") != 200:
            msg = "用例描述：",explain," 执行getText方法时调用getElement不通过!"
            logs("ui").error_log(msg)
            logs("ui").error_log(el)
            assert "用例执行getText方法时调用getElement不通过!" == "通过!"
        if 'element' in el.keys() and el['element'] != "":
            el = el.get("element")
            while num > 0:
                num = num -1
                try:
                    r = el.text
                    break
                except Exception as e:
                    if num == 0:
                        msg = "用例描述：",explain," 执行getText方法时不通过!"
                        logs("ui").error_log(msg)
                        logs("ui").error_log(e)
                        assert "用例执行getText方法时不通过!" == "通过!"
                    else:
                        sleep(1)
        else:
            msg = "用例描述：",explain," 执行getText方法时调用element不通过!"
            logs("ui").error_log(msg)
            logs("ui").error_log(el)
            assert "用例执行getText方法时调用element不通过!" == "通过!"
        return r