from common.common_fun import Common
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
class Login_jinfenggou(Common):
    username_type = (By.ID, 'com.jiarui.jfps:id/frg_login_pwd_edt_mobile')
    password_type = (By.ID, 'com.jiarui.jfps:id/frg_login_pwd_edt_pwd')
    loginBtn = (By.ID, 'com.jiarui.jfps:id/frg_login_pwd_submit')
    def login_jinfenggou(self,username,password):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        # self.My()
        # self.Myclicklogin()
        self.driver.find_element(*self.username_type).send_keys(username)
        self.driver.find_element(*self.password_type).send_keys(password)
        self.driver.find_element(*self.loginBtn).click()
if __name__ == '__main__':
    driver = appium_desired()
    l = Login_jinfenggou(driver)
