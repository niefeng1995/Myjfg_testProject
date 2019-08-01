from selenium.webdriver.support.ui import WebDriverWait
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from businessView.login_jinfengou import Login_jinfenggou
from time import sleep
import logging
class HomeBuyGoods(Login_jinfenggou):
    coubonBtn = (By.ID, 'com.jiarui.jfps:id/item_rv_discount_coupon_btn')
    buyBtn = (By.ID,'com.jiarui.jfps:id/cd_buy_btn')
    joincatBtn = (By.ID,'com.jiarui.jfps:id/cd_addshoppingcar_btn')
    shoppingcatBtn = (By.ID,'com.jiarui.jfps:id/cd_shoppingcar_layout')
    collectionBtn = (By.ID,'com.jiarui.jfps:id/cd_collection_layout')
    shoppBtn = (By.ID,'com.jiarui.jfps:id/cd_shopp_layout')
    goodsnums=(By.ID,'com.jiarui.jfps:id/dsCar_number_tv')
    confirmBtn = (By.ID,'com.jiarui.jfps:id/dsCar_confirm_btn')
    goods_add_btn =(By.ID,'com.jiarui.jfps:id/item_rv_main_like_add_btn')
    store_confirm_Btn = (By.ID,'com.jiarui.jfps:id/shop_homepager_confirm_btn')
    store_shoppingcar_Btn = (By.ID,'com.jiarui.jfps:id/shop_homepager_shoppingcar_iv')
    def store_click(self,num):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element_by_id('com.jiarui.jfps:id/shop_homepager_goods_rv'))
        goods = ('//*[@resource-id="com.jiarui.jfps:id/shop_homepager_goods_rv"]/android.widget.LinearLayout[%s]'%num)
        try:
            click_goods = self.driver.find_element_by_xpath(goods)
        except NoSuchElementException:
            logging.info('没有发现门店首页商品')
        else:
            click_goods.click()
    def goods_category(self,num):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,5).until(lambda x:x.find_element_by_id('com.jiarui.jfps:id/shop_homepager_top_classification_rv'))
        goods_cate= ('//*[@resource-id="com.jiarui.jfps:id/shop_homepager_top_classification_rv"]/android.widget.CheckBox[%s]'%num)
        try:
            choose_good_cate = self.driver.find_element_by_xpath(goods_cate)
        except NoSuchElementException:
            logging.info('没有发现门店首页商品分类')
        else:
            choose_good_cate.click()
    def store_coupon(self,num):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.coubonBtn))
        try:
            coupon_btn =self.driver.find_elements(*self.coubonBtn)
        except NoSuchElementException:
            logging.info('没有发现领取优惠券按钮')
        else:
            coupon_btn['%s'%num].click()
    def store_add_goods_btn(self):
        """门店首页添加购物车"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.goods_add_btn))
        try:
            goodsBtn =self.driver.find_elements(*self.goods_add_btn)
        except NoSuchElementException:
            logging.info('没有发现门店首页添加购物车按钮')
        else:
            goodsBtn.click()
    def store_confirmBtn(self):
        """立即下单"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.store_confirm_Btn))
        try:
            confirmBtn =self.driver.find_elements(*self.store_confirm_Btn)
        except NoSuchElementException:
            logging.info('没有发现门店首页立即下单按钮')
        else:
            confirmBtn.click()
    def store_shoppingcatBtn(self):
        """门店首页查看购物车"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.store_shoppingcar_Btn))
        try:
            store_catBtn =self.driver.find_elements(*self.store_shoppingcar_Btn)
        except NoSuchElementException:
            logging.info('没有发现门店首页立即下单按钮')
        else:
            store_catBtn.click()
    def buy_now(self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.buyBtn))
        try:
            buynow = self.driver.find_element(*self.buyBtn)
        except NoSuchElementException:
            logging.info('没有发现立即购买按钮')
        else:
            buynow.click()
    def join_cart(self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.joincatBtn))
        try:
            join_cart = self.driver.find_element(*self.joincatBtn)
        except NoSuchElementException:
            logging.info('没有发现加入购物车按钮')
        else:
            join_cart.click()
    def shoppingcart(self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.shoppingcatBtn))
        try:
            shoppingcart = self.driver.find_element(*self.shoppingcatBtn)
        except NoSuchElementException:
            logging.info('没有发现购物车按钮')
        else:
            shoppingcart.click()
    def goods_collection(self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.collectionBtn))
        try:
            goods_collection = self.driver.find_element(*self.collectionBtn)
        except NoSuchElementException:
            logging.info('没有收藏按钮')
        else:
            goods_collection.click()

    def store_back(self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.shoppBtn))
        try:
            store_back = self.driver.find_element(*self.shoppBtn)
        except NoSuchElementException:
            logging.info('没有发现门店按钮')
        else:
            store_back.click()
    def buy_goods_num(self,num):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.goodsnums))
        try:
            goods_num = self.driver.find_element(*self.goodsnums)
        except NoSuchElementException:
            logging.info('没有发现购买数量输入框')
        else:
            goods_num.clear()
            goods_num.send_keys(num)
    def buy_goods_to_order (self):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.confirmBtn))
        try:
            confirmgoods = self.driver.find_element(*self.confirmBtn)
        except NoSuchElementException:
            logging.info('没有发现确定按钮')
        else:
            confirmgoods.click()

if __name__ == '__main__':
    driver = appium_desired()
    l = HomeBuyGoods(driver)
    l.home_click_goods_img()
    l.store_click(1)
    l.buy_now()
    l.buy_goods_num(5)
    l.buy_goods_to_order()
    print(l.is_toast_exist('请先登录'))
    l.login_jinfenggou(15979994517,123456)
    l.buy_goods_to_order()
    print(l.is_toast_exist('请选择配送时间'))