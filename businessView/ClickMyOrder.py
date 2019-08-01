from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from businessView.login_jinfengou import Login_jinfenggou
from time import sleep
import logging
class ClickMyWallet(Login_jinfenggou):
    def clickmywallet(self,num):
        # self.login_jinfenggou(15979994517,123456)
        try:
            my_order  = self.driver.find_element_by_xpath('//*[@resource-id="com.jiarui.jfps:id/frg_mine_func_rv"]/android.widget.LinearLayout[%s]'%num)
        except NoSuchElementException:
            logging.info('no found')
        else:
            my_order.click()

if __name__ == '__main__':
    driver =appium_desired()
    l = ClickMyWallet(driver)
    l.My()
    l.clickmywallet(4)