#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lz 
@file: demoSeleniumForm.py 
@time: 2018/05/13   13：41 
"""
from selenium import webdriver

driver_path = r"/home/lz/Document/python/pythonCourseDemo/chromedriver"
driver = webdriver.Chrome(driver_path)
# driver.get("https://www.baidu.com")

#form输入
# inputTag = driver.find_element_by_id("kw")
# inputTag.send_keys("python")
# inputTag.clear()#清除数据

# form点击
# button = driver.find_element_by_id("su")
# button.click()
#
# inputTag.clear()#清除数据

# form选择checkbox
# driver.get("https://www.douban.com/")
#
# checkBox =driver.find_element_by_id("form_remember")
# checkBox.click()

#form select标签
from selenium.webdriver.support.ui import Select
#要先用Select()包装成Select()对象，然后使用selectByValue,等方法实现操作