#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lz 
@file: demoSelenuimWait.py 
@time: 2018/05/13   17：07 
"""
from selenium import webdriver

from selenium import webdriver

#指定浏览器驱动位置
dirver_path = r'/home/lz/Document/python/pythonCourseDemo/chromedriver'
dirver =webdriver.Chrome(executable_path=dirver_path)
dirver.get("https://www.baidu.com")#url一定要写全，加上https或者http,否则报错

#隐式等待,等待10s后在去获取元素
# dirver.implicitly_wait(10)
# inputTag = dirver.find_element_by_id("k是是是w")

# 显示等待，如果找到这个元素就不等待，否则等待到限制时间
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

element = WebDriverWait(dirver,10).until(
    expected_conditions.presence_of_element_located((By.ID,'11111111111111'))#参数为元祖
)
