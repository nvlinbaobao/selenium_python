from selenium import webdriver
from common.base import BasePage
from page.page_login import LoginPage,login_url
import unittest
from common.logger import Log
#数据分离
# test_01=["欧皇林宝","wangqing232732",False]
# test_02=["欧皇林宝","wangqing232732.",True]
#或者
#test_01={"user":u"欧皇林宝","psw":u"wangqing232732","except":False}
#test_02={"user":u"欧皇林宝","psw":u"wangqing232732.","except":True}
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
        #如果要log日志的话,就实例化
        #self.log=Log
    def tearDown(self):
        #每次清空登录的cookie,数据还原
        self.driver.delete_all_cookies()
    @classmethod
    def tearDownClass(cls):
        #关闭浏览器
        cls.driver.quit()

    def login_case(self,user,psw,excpect):
        '''登录的流程'''
        self.login_driver.input_username(user)
        self.login_driver.input_password(psw)
        self.login_driver.click_submit()
        result=self.login_driver.is_login_sucess()#获取结果
        expect_result=excpect#期望结果
        self.assertEqual(result,expect_result)#断言

    def test_login_01(self):
        '''登陆失败用例:输入正确的账户,错误的密码'''
        self.login_case("欧皇林宝","wangqing232732",False)
        #self.login_case(test_01)

        #self.login_case(**test_01) 用上面的字典传入的话需要加**

        # #第1步:输入 账号
        # self.login_driver.input_username(u"欧皇林宝")
        # #第2步:输入密码
        # self.login_driver.input_password(u"wangqing232732")
        # #第3步:点击登录按钮
        # self.login_driver.click_submit()
        # #第4步:实际结果
        # #result=self.login_driver.is_text_in_element(("id","lnk_current_user"),"女林")
        # result=self.login_driver.is_login_sucess()#调用的page_login中封装的方法
        # #第5步：期望结果
        # expect_result=False
        # #第6步：断言测试结果与期望结果一致
        # self.assertEqual(result,expect_result,msg="期望结果:%s与实际结果:%不符"%(expect_result,result))

    def test_login_02(self):
        '''登陆失败用例:输入正确的账户,正确的密码'''
        self.login_case("欧皇林宝","wangqing232732.",True)

        #self.login_case(test_02)

        #self.login_case(**test_02) 用上面的字典传入的话需要加**
        # #第1步:输入 账号
        # self.login_driver.input_username(u"欧皇林宝")
        # #第2步:输入密码
        # self.login_driver.input_password(u"wangqing232732.")
        # #第3步:点击登录按钮
        # self.login_driver.click_submit()
        # #第4步:实际结果
        # #result=self.login_driver.is_text_in_element(("id","lnk_current_user"),"女林")
        # result=self.login_driver.is_login_sucess()#调用的page_login中封装的方法
        # #第5步：期望结果
        # expect_result=True
        # #第6步：断言测试结果与期望结果一致
        # self.assertEqual(result,expect_result,msg="期望结果:%s与实际结果:%不符"%(expect_result,result))

if __name__=="__main__":
    unittest.main()