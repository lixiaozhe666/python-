#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lz 
@file: demoSelenuimCookie.py 
@time: 2018/05/13   16：50 
"""
from selenium import webdriver

#指定浏览器驱动位置
dirver_path = r'/home/lz/Document/python/pythonCourseDemo/chromedriver'
dirver =webdriver.Chrome(executable_path=dirver_path)
dirver.get("https://www.baidu.com")#url一定要写全，加上https或者http,否则报错

cookies = dirver.get_cookies()#得到关于百度的所有cookie
for cookie in cookies:
    print(cookie)

print("*"*30)
cookie = dirver.get_cookie("PSTM")#得到关于百度名称为PATM的cookie
print(cookie)
print("*"*30)

dirver.delete_cookie("PSTM")#删除名称为PSTM的cookie
print(dirver.get_cookie("PSTM"))
print("*"*30)

dirver.delete_all_cookies()#删除所有cookie
print(dirver.get_cookies())