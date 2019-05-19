import time
import os
from selenium import webdriver

def screenShots(driver):
    picture = time.strftime('%Y%d%H%M',time.localtime(time.time()))#格式化时间用来命名截图名字

    pictureName = os.path.dirname(os.path.abspath('.')) + '\\picture\\' + picture + '.png'#拼接截图名字

    driver.get_screenshot_as_file(pictureName)#截屏
