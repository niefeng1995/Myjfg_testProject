from appium import webdriver
import yaml
import logging
import logging.config
import os
from time import sleep
CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
def appium_desired():
    with open('../config/kyb_caps.yaml','r',encoding='utf-8')as file:
        data = yaml.load(file)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['app'])
    caps = {}
    caps['platformName'] = data['platformName']
    caps['platformVersion'] = data['platformVersion']
    # caps['app'] = app_path
    caps['deviceName'] = data['deviceName']
    caps['appPackage'] = data['appPackage']
    caps['appActivity'] = data['appActivity']
    caps['noRest'] = data['noRest']
    caps['automationName'] = data['automationName']
    # caps['unicodeKeyboard']=data['unicodeKeyboard']
    caps['resetKeyboard']=data['resetKeyboard']
    logging.info('Start app ..')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', caps)
    driver.implicitly_wait(10)
    return driver
if __name__ == '__main__':
    appium_desired()
    r = appium_desired()


