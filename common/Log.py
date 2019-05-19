import logging
import os
import time
from common.ReadConfig import getConfig

#创建日志对象
logger = logging.getLogger('LogTestFun')#设置自己log对象
#设置日志调试等级
logger.setLevel(logging.INFO)

#设置log格式化
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s")

#在控制台输出log
consoleFile = logging.StreamHandler()#创建Handler
consoleFile.setLevel(logging.INFO)
consoleFile.setFormatter(formatter)
logger.addHandler(consoleFile)#写入控制台

#写入log文件
#设置日志路径和输出级别
#logFile = logging.FileHandler('D:\\temp\\test.log')#创建Handler
logFile = logging.FileHandler(getConfig.getLogInfo("Path"))#创建Handler
logFile.setLevel(logging.INFO)
logFile.setFormatter(formatter)#格式化
logger.addHandler(logFile)#写入文件

#测试一下
logger.info('hello,我是test')

