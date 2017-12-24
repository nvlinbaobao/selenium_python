#coding:utf-8
from common.base import BasePage
#博客园首页
class PageHome(BasePage):#继承base中的BasePage类
    #定位博客园首页中的页面元素
    yuanzi_loc=("link text","园子")
    xinwen_loc=("link text","新闻")
    bowen_loc=("link text","博问")
    shancun_loc=("link text","闪存")
    xiaozu_loc=("link text","小组")
    shoucang_loc=("link text","收藏")

    def click_yuanzi(self):
        self.click(self.yuanzi_loc)

    def click_xinwen(self):
        self.click(self.xinwen_loc)

    def click_bowen(self):
        self.click(self.bowen_loc)

    def click_shancun(self):
        self.click(self.shancun_loc)

    def click_xiaozu(self):
        self.click(self.xiaozu_loc)

    def click_shoucang(self):
        self.click(self.shoucang_loc)

if __name__=="__main__":
    from selenium import webdriver
    driver=webdriver.Firefox()
    driver.get("http://www.cnblogs.com/linbao/p/")
    driver_home=PageHome(driver)#实例化
    driver_home.click_bokeyuan()#登录后的博客园首页