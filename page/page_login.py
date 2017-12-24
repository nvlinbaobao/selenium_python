#coding:utf-8
from common.base import BasePage

#放在外面公共用
login_url="https//passport.cnblogs.com/user/signin"

#博客园登录页
class LoginPage(BasePage):
    #定位博客园登录页的页面元素
    username_loc=("id","input1")#输入账号
    password_loc=("id","input2")#输入密码
    submit_loc=("id","signin")#提交
    remember_loc=("id","remember_me")#记住账户信息
    retrieve_loc=("link text","找回")
    reset_loc=("link text","重置")
    register_loc=("link text","立即注册")
    feedback_loc=("link text","反馈问题")
    text_loc=("id," "is_text_in_element")#登录成功后的用户名文本

    def input_username(self,username):
        '''输入账号框'''
        self.send_keys(self.username_loc,username)

    def input_password(self,password):
        '''输入密码框'''
        self.send_keys(self.password_loc,password)

    def click_submit(self):
        '''登录按钮'''
        self.click(self.submit_loc)

    def is_login_sucess(self):
        try:
            result=self.is_text_in_element(self.text_loc,"女林")
            return result
        except Exception as msg:
            return False