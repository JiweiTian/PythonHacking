# -*- coding: UTF-8 -*-

def login(username, password):
    '''Test if the login is correct.

    The username and password are string.'''
    if username=='seven'and password=='123':
        print("login suceess")
    else:
        print("login failed")

user=str(input('请输入用户名：'))
password=str(input('请输入密码：'))
login(user,password)

