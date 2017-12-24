#数据驱动DDT
#coding:utf-8
from selenium import webdriver
from common.base import BasePage
from page.page_login import LoginPage,login_url
from common.read_excel_ddt import ExcelUtil
import unittest
import ddt
case_data=[{"user":u"欧皇林宝","psw":u"xxxx","except":False},
           {"user":u"欧皇林宝","psw":u"xxxxxxx.","except":True}
           ]

@ddt.ddt
class Login_test(unittest.TestCase):
    '''登录页面的测试用例'''

    @classmethod
    def setUpClass(cls):
        #只打开一次浏览器
        cls.driver=webdriver.Firefox()
        #实例化page_login中的LoginPage类
        cls.login_driver=LoginPage(cls.driver)
        cls.driver.open(login_url)

    def setUp(self):
        #每次都从登录页开始
        self.driver.get(login_url)

    def tearDown(self):
        #每次清空登录的cookie,数据还原
        self.driver.delete_all_cookies()
    @classmethod
    def tearDownClass(cls):
        #关闭浏览器
        cls.driver.quit()

    def login_case(self,user,psw,exc):
        '''登录的流程'''
        self.login_driver.input_username(user)
        self.login_driver.input_password(psw)
        self.login_driver.click_submit()
        result=self.login_driver.is_login_sucess()#获取结果
        except_result=exc#期望结果
        self.assertEqual(result,except_result)#断言

    @ddt.data(*case_data)#多个数据 挨个去传
    def test_login_01(self,testdata):
        '''登陆失败用例:输入正确的账户,错误的密码'''
        print(case_data)
    def test_login_02(self):
        '''登陆失败用例:输入正确的账户,正确的密码'''
        print(case_data)
if __name__=="__main__":
    unittest.main(verbosity=2)

###############################################################################################################
#数据驱动ddt+excel数据读取
#coding:utf-8
from selenium import webdriver
from common.base import BasePage
from page.page_login import LoginPage,login_url
from common.read_excel_ddt import ExcelUtil
import unittest
import ddt

#用excle表格传入
filepath="data_excel.xlsx"
data=ExcelUtil(filepath)
datadict=data.dict_data()
print datadict

@ddt.ddt
class Login_test(unittest.TestCase):
    '''登录页面的测试用例'''

    @classmethod
    def setUpClass(cls):
        #只打开一次浏览器
        cls.driver=webdriver.Firefox()
        #实例化page_login中的LoginPage类
        cls.login_driver=LoginPage(cls.driver)
        cls.driver.open(login_url)

    def setUp(self):
        #每次都从登录页开始
        self.driver.get(login_url)

    def tearDown(self):
        #每次清空登录的cookie,数据还原
        self.driver.delete_all_cookies()
    @classmethod
    def tearDownClass(cls):
        #关闭浏览器
        cls.driver.quit()

    def login_case(self,user,psw,exc):
        '''登录的流程'''
        self.login_driver.input_username(user)
        self.login_driver.input_password(psw)
        self.login_driver.click_submit()
        result=self.login_driver.is_login_sucess()#获取结果
        #如果用excel的话 由于返回的是0,1所以需要用bool
        except_result=bool(exc)
        self.assertEqual(result,except_result)#断言

    @ddt.data(*datadict)#把excel中的数据挨个传入
    def test_login_01(self,data):
        '''登陆失败用例:输入正确的账户,错误的密码'''
        self.login_case(data["username"],data["psw"],data["expect"])

    @ddt.data(*datadict)#把excel中的数据挨个传入
    def test_login_02(self,data):
        '''登陆失败用例:输入正确的账户,正确的密码'''
        self.login_case(data["username"],data["psw"],data["expect"])

if __name__=="__main__":
    unittest.main()