from selenium.webdriver.support.wait import WebDriverWait
from common.common_fun import Common
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from businessView.login_jinfengou import Login_jinfenggou
from selenium.webdriver.support import expected_conditions as EC
import logging
class HomePageSearch(Login_jinfenggou,Common):
    search=(By.ID,'com.jiarui.jfps:id/home_v2_title_bar_search_tv')
    search_edit =(By.ID,'com.jiarui.jfps:id/search_edit_et')
    search_button = (By.ID,'com.jiarui.jfps:id/search_confirm_tv')

    def homepage_search(self,name):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver, 6).until(lambda x: x.find_element(*self.search))
        try:
            search = self.driver.find_element(*self.search)
        except NoSuchElementException:
            logging.info('no search')
        else:
            search.click()
        WebDriverWait(self.driver,5).until(lambda x:x.find_element(*self.search_edit))
        self.driver.find_element(*self.search_edit).send_keys(name)
        self.driver.find_element(*self.search_button).click()
        try:
            self.is_toast_exist('定位失败')
        except NoSuchElementException:
            pass
        else:
            self.driver.find_element(*self.search_button).click()


if __name__ == '__main__':
    driver = appium_desired()
    l = HomePageSearch(driver)
    l.login_jinfenggou(15979994517, 123456)
    l.IndexPage()
    l.homepage_search('金丰果蔬')
    l.search_store()
