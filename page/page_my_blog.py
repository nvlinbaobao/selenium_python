#coding:utf-8
from common.base import BasePage
#我的博客
class Pagemyblog(BasePage):
    #定位我的博客中的页面元素
    bokeyuan_loc=("id","blog_nav_sitehome")#博客园
    shouye_loc=("id","blog_nav_myhome")#首页
    xinsuibi_loc=("id","blog_nav_newpost")#新随笔
    lianxi_loc=("id","blog_nav_contact")#联系
    guanli_loc=("id","blog_nav_admin")#管理
    dingyue_loc=("id","blog_nav_rss")#订阅


    def click_bokeyuan(self):
        '''点博客园'''
        self.click(self.bokeyuan_loc)

    def click_shouye(self):
        '''点首页'''
        self.click(self.shouye_loc)

    def click_xinsuibi(self):
        '''点新随笔'''
        self.click(self.xinsuibi_loc)

    def click_lianxi(self):
        '''点联系'''
        self.click(self.lianxi_loc)

    def click_guanli(self):
        '''点管理'''
        self.click(self.guanli_loc)

    def click_dingyue(self):
        '''点订阅'''
        self.click(self.dingyue_loc)

if __name__=="__main__":
    from selenium import webdriver
    driver=webdriver.Firefox()
    driver.get("http://www.cnblogs.com/linbao/p/")
    driver_home=Pagemyblog(driver)#实例化
    driver_home.click_bokeyuan()#点击我的博客