#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lz 
@file: demoSeleniumProxy.py 
@time: 2018/05/13   17：48 
"""

from selenium import webdriver
import time
#指定浏览器驱动位置
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://124.42.7.103:80")
dirver_path = r'/home/lz/Document/python/pythonCourseDemo/chromedriver'
dirver =webdriver.Chrome(executable_path=dirver_path,options=options)
dirver.get("http://www.httpbin.org/ip")#url一定要写全，加上https或者http,否则报错
