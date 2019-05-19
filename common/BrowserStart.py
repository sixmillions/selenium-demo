from common.ReadConfig import getConfig
from selenium import webdriver
import os
from common.ScreenCapture import screenShots
#启动浏览器
def browserName():
    browsername = getConfig.getBrowserInfo('BrowserName')
    url = getConfig.getBrowserInfo('Url')
    if browsername == 'firefox':
        driver = webdriver.Firefox()
        driver.get(url)
    if browsername == 'chrome':
        driver = webdriver.Chrome()
        driver.get(url)
    driver.maximize_window()
    screenShots(driver)
