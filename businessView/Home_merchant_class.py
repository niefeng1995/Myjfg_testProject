from selenium.webdriver.support.ui import WebDriverWait
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from businessView.login_jinfengou import Login_jinfenggou
import logging

class SelectHomeBusinessCategory(Login_jinfenggou):

    def selectbusinesscategory(self,num):
        text ='//android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]'%num
        try:
            select_home_business_cate = self.driver.find_element_by_xpath(text)
        except NoSuchElementException:
            logging.info('no found')
        else:
            select_home_business_cate.click()

    # def swipeRight(self):
    #     l = self.get_window_size()
    #     x1 = int(l[0] * 0.5)
    #     y1 = int(l[1] * 0.4)
    #     x2 = int(l[1] * 0.9)
    #     self.driver.swipe(x1, y1, x2, y1, 1000)

if __name__ == '__main__':
    driver = appium_desired()
    l = SelectHomeBusinessCategory(driver)
    l.selectbusinesscategory(10)