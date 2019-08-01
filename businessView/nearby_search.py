from selenium.webdriver.support.ui import WebDriverWait
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from businessView.login_jinfengou import Login_jinfenggou
import logging

class NearBySearch(Login_jinfenggou):
    nearbysearch = (By.ID,'com.jiarui.jfps:id/common_search_search')
    m_search=(By.ID,'com.jiarui.jfps:id/frg_nearby_merchant_classification')
    edit =(By.ID,'com.jiarui.jfps:id/search_edit_et')
    search_Btn = (By.ID,'com.jiarui.jfps:id/search_confirm_tv')
    def nearby_search(self,name):
        try:
            near_search =self.driver.find_element(*self.nearbysearch)
        except NoSuchElementException:
            logging.info('no foun near_search')
        else:
            near_search.click()
        try:
            near_search_edit = self.driver.find_element(*self.edit)
        except NoSuchElementException:
            logging.info('no found ')
        else:
            near_search_edit.send_keys(name)
        try:
            near_searchBtn = self.driver.find_element(*self.search_Btn)
        except NoSuchElementException:
            logging.info('no found ')
        else:
            near_searchBtn.click()
    def classification(self,num):
        WebDriverWait(self.driver,5).until(lambda x:x.find_element(*self.m_search))
        # check_box = 'className("android.widget.CheckBox").text("电脑办公")'
        # self.driver.find_element_by_android_uiautomator(check_box).click()
        try:
            mer_class = self.driver.find_element_by_xpath('//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]'%num)
        except NoSuchElementException:
            logging.info('not found merchant_class')
        else:
            mer_class.click()


if __name__ == '__main__':
    driver = appium_desired()
    l = NearBySearch(driver)
    l.login_jinfenggou(15979994517,123456)
    l.nearby()
    l.nearby_search('金丰果疏')
    l.search_store()