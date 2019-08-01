from selenium.webdriver.support.ui import WebDriverWait
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from businessView.shouye_search import HomePageSearch
from businessView.HomeBuyGoods import HomeBuyGoods
from time import sleep
import logging
class EditOrder(HomeBuyGoods):
    order_song = (By.ID,'com.jiarui.jfps:id/act_fill_order_song')
    order_self =(By.ID,'com.jiarui.jfps:id/act_fill_order_self')
    order_adders=(By.ID,'com.jiarui.jfps:id/act_fill_order_address')
    order_delivery_time=(By.ID,'com.jiarui.jfps:id/act_fill_order_delivery_time')
    order_pay_online=(By.ID,'com.jiarui.jfps:id/act_fill_order_pay_online')
    order_pay_offline=(By.ID,'com.jiarui.jfps:id/act_fill_order_pay_offline')
    order_counp=(By.ID,'com.jiarui.jfps:id/act_fill_order_counp')
    order_buyer_message=(By.ID,'com.jiarui.jfps:id/act_fill_order_buyer_message')
    order_pay_toall_record=(By.ID,'com.jiarui.jfps:id/act_fill_order_pay_toall_record')
    order_submit=(By.ID,'com.jiarui.jfps:id/act_fill_order_submit')
    order_delivery_time_sumbit=(By.ID,'com.jiarui.jfps:id/dialog_common_cancel')
    order_total_price=(By.ID,'com.jiarui.jfps:id/act_fill_order_total_price')
    order_freight=(By.ID,'com.jiarui.jfps:id/act_fill_order_freight')
    order_goods_price=(By.ID,'com.jiarui.jfps:id/act_fill_order_goods_price')
    discount_coupon_btn=(By.ID,'com.jiarui.jfps:id/item_rv_discount_coupon_btn')
    get_coupon_btn=(By.XPATH,'//*[@text="领取"]')
    use_coupon_btn=(By.XPATH,'//*[@text="使用"]')
    def ordersong(self):
        """商家配送"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.order_song))
        try:
            ordersong = self.driver.find_element(*self.order_song)
        except NoSuchElementException:
            logging.info('没有商家配送选项')
        else:
            ordersong.click()
    def orderinself(self):
        """门店自提"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.order_self))
        try:
            ordersong = self.driver.find_element(*self.order_self)
        except NoSuchElementException:
            logging.info('没有发现门店自提选项')
        else:
            ordersong.click()
    def orderadders(self):
        """配送地址"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.order_adders))
        try:
            orderadders = self.driver.find_element(*self.order_adders)
        except NoSuchElementException:
            logging.info('没有发现配送地址')
        else:
            orderadders.click()
    def orderonline(self):
        """线上支付"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.order_pay_online))
        try:
            orderonline = self.driver.find_element(*self.order_pay_online)
        except NoSuchElementException:
            logging.info('没有发现线上支付')
        else:
            orderonline.click()
    def orderoffline(self):
        """线下支付"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.order_pay_offline))
        try:
            orderoffline = self.driver.find_element(*self.order_pay_offline)
        except NoSuchElementException:
            logging.info('没有发现线下上支付')
        else:
            orderoffline.click()
    def ordercuoppon(self):
        """填写订单——优惠券"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,5).until(lambda x:x.find_element(*self.order_counp))
        try:
            ordercuoppon = self.driver.find_element(*self.order_counp)
        except NoSuchElementException:
            logging.info('没有发现使用优惠券')
        else:
            ordercuoppon.click()
    def ordermessage(self,message):
        """买家留言"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.order_buyer_message))
        try:
            ordermessage = self.driver.find_element(*self.order_buyer_message)
        except NoSuchElementException:
            logging.info('没有发现买家留言')
        else:
            ordermessage.clear()
            ordermessage.send_keys(message)
    def ordergoodsprice(self):
        """商品合计金额"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.order_goods_price))
        try:
            ordergoodsprice = self.driver.find_element(*self.order_goods_price).text
        except NoSuchElementException:
            logging.info('没有发现商品合计')
        else:
            print(ordergoodsprice)
    def orderfreprice(self):
        """配送费金额"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.order_freight))
        try:
            orderfreprice = self.driver.find_element(*self.order_freight).text
        except NoSuchElementException:
            logging.info('没有发现配送费金额')
        else:
            print(orderfreprice)
    def orderactprice(self):
        """订单金额"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.order_total_price))
        try:
            orderactprice = self.driver.find_element(*self.order_total_price).text
        except NoSuchElementException:
            logging.info('没有发现订单金额')
        else:
            print(orderactprice)
    def orderpayrecord(self):
        """应付金额"""
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.order_pay_toall_record))
        try:
            orderpayrecord = self.driver.find_element(*self.order_pay_toall_record).text
        except NoSuchElementException:
            logging.info('没有发现应付金额')
        else:
            print(orderpayrecord)
    def orderdeliverytime(self):
        """配送时间"""
        act = self.driver.current_activity
        self.driver.wait_activity(act,10)
        WebDriverWait(self.driver,10).until(lambda x:x.find_element(*self.order_delivery_time))
        try:
            ordeliverytime = self.driver.find_element(*self.order_delivery_time)
        except NoSuchElementException:
            logging.info('没有发现配送时间')
        else:
            ordeliverytime.click()

    def orderdeliverytimesumbit(self):
        """确认配送时间"""
        act = self.driver.current_activity
        self.driver.wait_activity(act,10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.order_delivery_time_sumbit))
        try:
            ordeliverytimesumbit = self.driver.find_element(*self.order_delivery_time_sumbit)
        except NoSuchElementException:
            logging.info('没有发现配送时间确认按钮')
        else:
            ordeliverytimesumbit.click()
    def ordersumbit(self):
        """提交订单"""
        act = self.driver.current_activity
        self.driver.wait_activity(act,10)
        WebDriverWait(self.driver,6).until(lambda x:x.find_element(*self.order_submit))
        try:
            ordersumbit = self.driver.find_element(*self.order_submit)
        except NoSuchElementException:
            logging.info('没有发现提交订单按钮')
        else:
            ordersumbit.click()
    def discountcouponBtn(self,num):
        act = self.driver.current_activity
        self.driver.wait_activity(act, 10)
        """可用优惠券"""
        try :
            discounponBtn = self.driver.find_elements(*self.discount_coupon_btn)
        except NoSuchElementException:
            logging.info("没有发现使用优惠券按钮")
        else:
            clicknum = int(num)
            discounponBtn[clicknum].click()
        if act !=self.driver.wait_activity('.ui.shoppingcart.activity.FillOrderActivity',2):
            discounponBtn[clicknum].click()
        else:
            pass





if __name__ == '__main__':
    driver =appium_desired()
    l = EditOrder(driver)
    l.home_city_btn()
    ser = HomePageSearch(driver).homepage_search('快乐城店超市')
    l.search_store()
    l.sousu_result()
    l.store_click(1)
    l.buy_now()
    l.buy_goods_num(5)
    l.buy_goods_to_order()
    print(l.is_toast_exist('请先登录'))
    l.login_jinfenggou(15979994517, 123456)
    l.buy_goods_to_order()
    print(l.is_toast_exist('请选择配送时间'))
    l.ordercuoppon()
    l.discountcouponBtn(5)