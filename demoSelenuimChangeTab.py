#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lz 
@file: demoSelenuimChangeTab.py 
@time: 2018/05/13   17：31 
"""

from selenium import webdriver

#指定浏览器驱动位置
dirver_path = r'/home/lz/Document/python/pythonCourseDemo/chromedriver'
dirver =webdriver.Chrome(executable_path=dirver_path)
dirver.get("https://www.baidu.com")#url一定要写全，加上https或者http,否则报错

dirver.execute_script("window.open('https://www.douban.com/')")#执行js脚本，打开一个新的tab页
print(dirver.current_url)#虽然页面显示的为豆瓣电影，但是dirver的当前url仍然为百度
dirver.switch_to_window(dirver.window_handles[1])#window_handles为打开网站句柄，从0开始，切换dirver的句柄
print(dirver.current_url)
