from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging
import os,time,csv
from time import sleep
class Common(BaseView):
    personalcenter =(By.ID,'com.jiarui.jfps:id/frg_mine_setting_img')
    messageview=(By.ID,'com.jiarui.jfps:id/frg_mine_message_layout')
    personaldata=(By.ID,'com.jiarui.jfps:id/frg_mine_head_layout')
    nickname=(By.ID,'com.jiarui.jfps:id/frg_mine_nickname')
    mobile=(By.ID,'com.jiarui.jfps:id/frg_mine_mobile')
    mywallet=(By.ID,'com.jiarui.jfps:id/item_mine_nametv')
    all_order=(By.ID,'com.jiarui.jfps:id/frg_mine_all_order')
    order_name=(By.ID,'com.jiarui.jfps:id/item_mine_order_name_tv')
    my_service=(By.ID,'com.jiarui.jfps:id/frg_mine_service_rv')
    account=(By.ID,'com.jiarui.jfps:id/frg_login_pwd_edt_mobile')
    password=(By.ID,'com.jiarui.jfps:id/frg_login_pwd_edt_pwd')
    sumbit=(By.ID,'com.jiarui.jfps:id/frg_login_pwd_submit')
    bottom = (By.ID,'com.jiarui.jfps:id/act_main_tab_title')
    my_login =(By.ID,'com.jiarui.jfps:id/frg_mine_not_login')
    click_store = (By.XPATH, '//*[@class="android.support.v7.app.ActionBar$Tab" and @index="1"]')
    click_goods = (By.XPATH, '//*[@class="android.support.v7.app.ActionBar$Tab" and @index="0"]')
    product_img = (By.ID, 'com.jiarui.jfps:id/item_tv_new_product_img')
    setting_btn =(By.ID,'com.jiarui.jfps:id/frg_mine_setting_img')
    setting_out_btn = (By.ID,'com.jiarui.jfps:id/act_setting_out_login')
    setting_out_cancelbtn = (By.ID,'com.jiarui.jfps:id/dlg_prompt_cancel')
    setting_out_confirmbtn=(By.ID,'com.jiarui.jfps:id/dlg_prompt_confirm')
    home_citybtn = (By.ID,'com.jiarui.jfps:id/home_v2_title_bar_city_tv')
    city =(By.ID,'com.jiarui.jfps:id/city')
    sousuresult =(By.ID,'com.jiarui.jfps:id/common_recyclerView')
    def get_window_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x,y
    def swipeLeft(self):
        l = self.get_window_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[1] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def swipeRight(self):
        l = self.get_window_size()
        x1 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.5)
        x2 = int(l[1] * 0.9)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def swipeUp(self):
        l = self.get_window_size()
        # x1 = int(l[0] * 0.5)
        x1 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.2)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def swipeDown(self):
        l = self.get_window_size()
        # x1 = int(l[0] * 0.5)
        x1 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.2)
        y2 = int(l[1] * 0.8)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def getTime(self):
        self.now = time.strftime('%Y-%m-%d %H_%M_%S')
        return self.now
    def getScreenShot(self,module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__))+"/screenshots/%s_%s.png"%(module,time)
        self.driver.get_screenshot_as_file(image_file)

    def IndexPage(self):
        """首页——点击我的"""
        try:
            IndexPage = self.driver.find_elements(*self.bottom)
        except NoSuchElementException:
            pass
        else:
            IndexPage[0].click()
    def My(self):
        """首页——点击我的"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.bottom))
        try:
            My = self.driver.find_elements(*self.bottom)
        except NoSuchElementException:
            pass
        else:
            My[3].click()
    def ShoppingCart(self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        """首页--点击购物车"""
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.bottom))
        try:
            ShoppingCart = self.driver.find_elements(*self.bottom)
        except NoSuchElementException:
            pass
        else:
            ShoppingCart[2].click()
    def nearby(self):
        """首页——点击附近"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.bottom))
        try:
            shoppingcat = self.driver.find_elements(*self.bottom)
        except NoSuchElementException:
            pass
        else:
            shoppingcat[1].click()
    def Myclicklogin(self):
        """首页——未登录点击登录"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.my_login))
        try:
            notloginBtn = self.driver.find_element(*self.my_login)
        except NoSuchElementException:
            pass
        else:
            notloginBtn.click()
    def search_store(self):
        """首页搜索界面-点击门店"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.click_store))
        try:
            storeBtn = self.driver.find_element(*self.click_store)
        except NoSuchElementException:
            logging.info('no found storeBtn')
        else:
            storeBtn.click()
    def sousu_result(self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x: x.find_element(*self.sousuresult))
        try:
            sousu_result = self.driver.find_element(*self.sousuresult)
        except NoSuchElementException:
            logging.info('没有发现搜索结果')
        else:
            sousu_result.click()
    def search_goods(self):
        """首页搜索界面-点击商品"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.click_goods))
        try:
            goodsBtn = self.driver.find_element(*self.click_goods)
        except NoSuchElementException:
            logging.info('no found storeBtn')
        else:
            goodsBtn.click()
    def home_click_goods_img(self):
        act=self.driver.current_activity
        self.driver.wait_activity(act,10)
        for i in range(2):
            self.swipeUp()
            sleep(0.5)
        try:
            choose_product_img = self.driver.find_element(*self.product_img)
        except NoSuchElementException:
            logging.info('no found')
        else:
            choose_product_img.click()
    def get_csv_data(self,csv_file,line):
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader =csv.reader(file)
            for index,row in enumerate(reader,1):
                if index ==line:
                    return row
    def is_toast_exist(self,text,timeout=30,poll_frequency=0.5):
        try:
            toast_loc = ('xpath','.//*[contains(@text,"%s")]'%text)
            toast_element=WebDriverWait(self.driver,timeout,poll_frequency).until(EC.presence_of_element_located(toast_loc))
            print(toast_element.text)
            return True
        except:
            logging.info('没有定位toast元素')
            return False
    def setting(self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.setting_btn))
        try:
            seetingBtn = self.driver.find_element(*self.setting_btn)
        except NoSuchElementException:
            logging.info('没有发现设置按钮')
        else:
            seetingBtn.click()
    def setting_outlogin(self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.setting_out_btn))
        try:
            seetingoutBtn = self.driver.find_element(*self.setting_out_btn)
        except NoSuchElementException:
            logging.info('没有发现退出登录按钮')
        else:
            seetingoutBtn.click()
    def seeting_cancelBtn(self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.setting_out_cancelbtn))
        try:
            canceloutBtn = self.driver.find_element(*self.setting_out_cancelbtn)
        except NoSuchElementException:
            logging.info('没有发现取消按钮')
        else:
            canceloutBtn.click()
    def seeting_confrimBtn(self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x: x.find_element(*self.setting_out_confirmbtn))
        try:
            confrimBtn = self.driver.find_element(*self.setting_out_confirmbtn)
        except NoSuchElementException:
            logging.info('没有发现确认按钮')
        else:
            confrimBtn.click()
    def home_city_btn(self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.home_citybtn))
        try:
            homecityBtn = self.driver.find_element(*self.home_citybtn)
        except NoSuchElementException:
            logging.info('没有发现首页定位按钮')
        else:
            homecityBtn.click()
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.city))
        try:
            cityBtn =self.driver.find_elements(*self.city)
        except NoSuchElementException:
            logging.info("没有发现城市按钮")
        else:
            cityBtn[0].click()



if __name__ == '__main__':
    driver =appium_desired()
    com = Common(driver)
    com.home_city_btn()
    # com.My()
    # com.Myclicklogin()
    # # com.swipeLeft()
    # # com.swipeRight()
    # # for x in range(8):
    # #     com.swipeUp()
    # #     time.sleep(0.5)
    # # for y in range(8):
    # #     com.swipeDown()
    # #     time.sleep(0.5)
    # # com.swipeUp()
