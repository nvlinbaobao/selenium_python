#coding:utf-8
from selenium import webdriver
from page.page_my_blog import *
from page.page_bokeyuan_home import *
import unittest
class Test_Blog_Yuanzi(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver_home=PageHome(self.driver)
        self.driver_bky=Pagemyblog(self)