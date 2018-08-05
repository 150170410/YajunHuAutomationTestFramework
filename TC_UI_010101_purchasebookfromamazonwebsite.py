# coding = utf-8

'''
created on 2018/7/14
@author: yajun.hu
project: xxxx

'''

from selenium import webdriver
import unittest, os, time

class Test(unittest.TestCase):

    url = "https://www.amazon.cn"
    keyword = "软件测试"
    bookname = "软件测试(原书第2版)"
    price = "￥ 29.50"
    carttext = "商品已加入购物车"

    def setUp(self):
        print("===setUp start===")
        self.driver = webdriver.Firefox()

    def test_purchase(self):
        print("===test start===")
        print("step1: 打开amazon 网站")
        self.driver.get(self.url)
        print("step2: 输入并搜索软件测试")
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys(self.keyword)
        self.driver.find_element_by_class_name("nav-input").click()
        #print("self.driver.title" + self.driver.title)
        print("step3: 点击选择软件测试（原书第2版）")
        self.driver.find_element_by_link_text(self.bookname).click()
        #self.assertTrue(self.driver.title)
        time.sleep(5)
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
        time.sleep(5)
        #print("self.driver.title" + self.driver.title)
        print("step4: 点击加入购物车")
        self.driver.find_element_by_id("add-to-cart-button").click()
        print("判断结果：商品已加入购物车并且价格为准确")
        self.assertTrue(self.driver.find_element_by_tag_name("body").text.find(self.carttext)!=-1)
        self.assertTrue(self.driver.find_element_by_tag_name("body").text.find(self.price)!=-1)
        
        

    def tearDown(self):
        print("===tearDown start===")
        self.driver.quit()


if __name__=="__main__":
    unittest.main()




