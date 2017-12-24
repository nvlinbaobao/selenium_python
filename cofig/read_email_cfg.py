#coding:utf-8
import ConfigParser
import os
#当前脚本的绝对路径
cur_path=os.path.dirname(os.path.realpath(__file__))
print cur_path

email_cfg_path=os.path.join(cur_path,'email_cfg.ini')
print email_cfg_path

#实例化这个导入的ConfigParser类
conf=ConfigParser.ConfigParser()
conf.read(email_cfg_path)

smtp_server=conf.get("email","smtp_server")
print smtp_server

sender=conf.get("email","sender")
print sender

psw=conf.get("email","psw")
print psw

receiver=conf.get("email","receiver")
print receiver
print type(receiver)

port=int(conf.get("email","port"))
print port
print type(port)