import configparser#引入python自带的读取配置文件的依赖
import os
'''
cf = configparser.ConfigParser()

#获取当前文件路径
nowpath = os.path.abspath('.')
print(nowpath)

#获取上一层
uppath = os.path.dirname(nowpath)
print(uppath)

#获取配置文件的路径
cfpath = uppath+'\\config\\config.ini'

#读取文件
cf.read(cfpath)
browsername = cf.get("browser","BrowserName")
print(browsername)
'''
#把上面的抽象成一个方法
'''
def getBrowserName(name):
    cf = configparser.ConfigParser()

    # 获取当前文件路径
    nowpath = os.path.abspath('.')
    print(nowpath)

    # 获取上一层
    uppath = os.path.dirname(nowpath)
    print(uppath)

    # 获取配置文件的路径
    cfpath = uppath + '\\config\\config.ini'

    # 读取文件
    cf.read(cfpath)
    browsername = cf.get("browser", name)
    return browsername

print(getBrowserName('BrowserName'))
'''

#如果需要还可以抽象成一个类
class getConfig:
    def getBrowserInfo(name):
        cf = configparser.ConfigParser()

        # 获取当前文件路径
        nowpath = os.path.abspath('.')
        print(nowpath)

        # 获取上一层
        uppath = os.path.dirname(nowpath)
        print(uppath)

        # 获取配置文件的路径
        cfpath = uppath + '\\config\\config.ini'

        # 读取文件
        cf.read(cfpath)
        info = cf.get("browser", name)
        return info
    def getLogInfo(name):
        cf = configparser.ConfigParser()

        # 获取当前文件路径
        nowpath = os.path.abspath('.')
        print(nowpath)

        # 获取上一层
        uppath = os.path.dirname(nowpath)
        print(uppath)

        # 获取配置文件的路径
        cfpath = uppath + '\\config\\config.ini'

        # 读取文件
        cf.read(cfpath)
        info = cf.get("log", name)
        return info


print(getConfig.getBrowserInfo('BrowserName'))
print(getConfig.getBrowserInfo('Url'))
print(getConfig.getLogInfo('Path'))

