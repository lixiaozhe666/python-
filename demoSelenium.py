#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lz 
@file: demoSelenium.py 
@time: 2018/05/12   10：21 
"""
from selenium import webdriver
import time
#指定浏览器驱动位置
dirver_path = r'/home/lz/Document/python/pythonCourseDemo/chromedriver'
dirver =webdriver.Chrome(executable_path=dirver_path)
dirver.get("https://www.baidu.com")#url一定要写全，加上https或者http,否则报错

time.sleep(5)
dirver.close()#关闭当前选项卡

time.sleep(3)
dirver.quit()#退出整个浏览器