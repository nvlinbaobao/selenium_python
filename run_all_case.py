#------------文本报告---------
#coding:utf-8
#import unittest
# #1.用例的路径
# case_dir=r'D:\\Ui\\seven_session\\test_case'
#
# #2.加载所有的用例
# discover=unittest.defaultTestLoader.discover(start_dir=case_dir,
#                                             pattern='test*.py',
#                                             top_level_dir=None
#                                             )
# #3.批量执行多个用例
# runner=unittest.TextTestRunner()#生成文本报告
# runner.run(discover)
#######################################################################################
#----------HTML报告-----------
#coding:utf-8
import unittest
import time
from common import HTMLTestRunner_jpg
#HTMLTestRunner生成html的报告
#1.用例的路径
case_dir=r'D:\\Ui\\bokeyuan_web\\case'
#2.加载所有的用例
discover=unittest.defaultTestLoader.discover(start_dir=case_dir,
                                            pattern='test*.py',
                                            top_level_dir=None
                                            )
#按照一定格式获取当前时间
now=time.strftime("%Y-%m-%d %H_%M_%S")

#3.指定存放报告的路径
report_path="D:\\Ui\\seven_session\\report\\"+now+"result.html"

#4.通过open()方法以二进制写模式打开当前目录下的文件,如果没有,则自动创建
fp=open(report_path,"wb")
#5.定义测试报告
runner=unittest.HTMLTestRunner(stream=fp,#指定测试报告文件
                               title='测试报告的主题',#用来定义测试报告的标题
                               description='用例执行的情况')#用来定义测试报告的副标题
#6.运行测试用例
runner.run(discover)
#7.关闭报告文件
fp.close()
############################################################################
#发送QQ邮箱
# from cofig import read_email_cfg
# sender=read_email_cfg.sender
# print sender
# port=read_email_cfg.port
# print port