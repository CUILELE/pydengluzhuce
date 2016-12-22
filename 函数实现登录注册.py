# /user/bin/env python
#  -*- coding:utf-8 -*-
# Author:CLL


def login(user,pw):

    f = open('db','r')
    for line in f:
        #表示一行一行读里面东西
        line_list = line.strip().line.split('|')
        if line_list[0] == user and line_list[1] == pw:
            return True
    return  False

def register(user,pw):
    f = open('db','a')
    tem ='\n'+ user+'|'+pw
    f.write(tem)
    f.close()

def main():
    t = input('1:登录；2:注册')
    if t == '1':
        user = input('输入用户名：')
        pw = input('输入密码：')
        tu = login(user,pw)
        if tu:
            print('成功登录')
        else:
            print('登录失败')

    elif t == '2':
        user = input('输入用户名：')
        pw = input('输入密码：')
        register(user,pw)
        print('注册完成')
main()