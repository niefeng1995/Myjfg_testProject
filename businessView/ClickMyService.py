from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from businessView.login_jinfengou import Login_jinfenggou
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import logging
class ClickMyService(Login_jinfenggou):
    def clickmyservice(self,num):
        # self.login_jinfenggou(15979994517,123456)
        WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//*[@resource-id="com.jiarui.jfps:id/frg_mine_service_rv"]/android.widget.LinearLayout'))
        try:
            receivingaddressBtn  = self.driver.find_element_by_xpath('//*[@resource-id="com.jiarui.jfps:id/frg_mine_service_rv"]/android.widget.LinearLayout[%s]'%num)
        except NoSuchElementException:
            logging.info('no found')
        else:
            receivingaddressBtn.click()

if __name__ == '__main__':
    driver =appium_desired()
    l = ClickMyService(driver)
    l.My()
    l.login_jinfenggou(15979994517,123456)
    l.clickmyservice(1)