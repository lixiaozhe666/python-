#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lz 
@file: demoSelenuimActionChain.py 
@time: 2018/05/13   14：03 
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r"/home/lz/Document/python/pythonCourseDemo/chromedriver"
driver = webdriver.Chrome(driver_path)
driver.get("https://www.baidu.com")

inputTag = driver.find_element_by_id("kw")
button = driver.find_element_by_id("su")

action = ActionChains(driver)
action.move_to_element(inputTag)
action.send_keys_to_element(inputTag,"python")
action.move_to_element(button)
action.click(button)
action.perform()