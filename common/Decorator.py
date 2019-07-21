import os
from time import strftime



def decorator(driver):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                file_path = os.path.dirname(os.getcwd()) + r"\screenShot\{}.png".format(strftime("%Y%m%d-%H:%M:%S"))
                driver.get_screenshot_as_file(file_path)
        return inner
    return wrapper