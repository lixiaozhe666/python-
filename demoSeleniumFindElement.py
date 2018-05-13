#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lz 
@file: demoSeleniumFindElement.py 
@time: 2018/05/13   09：33 
"""
from  selenium import webdriver
from lxml import etree

driver_path = r"/home/lz/Document/python/pythonCourseDemo/chromedriver"
driver = webdriver.Chrome(driver_path)
driver.get("https://www.baidu.com")

# inputTag = driver.find_element_by_id("kw")
# inputTag.send_keys("python\n")#向指定元素写入数据,因为百度需要按下回车才能检索，所以加上\n

# inputTag = driver.find_element_by_class_name("s_ipt")
# inputTag.send_keys("python\n")

# inputTag = driver.find_element_by_name("wd")#input 的name属性值
# inputTag.send_keys("python\n")

# inputTag =driver.find_element_by_css_selector("#kw")
# inputTag.send_keys("python\n")

# inputTag = driver.find_element_by_xpath("//input[@id='kw']")
# inputTag.send_keys("python\n")

# find_element:不带s说明查找出的是第一个符合要求的元素
# find_elements:查找所有符合要求的元素，返回一个列表
# inputTag= driver.find_elements_by_xpath("//input[@id='kw']")[0]
# inputTag.send_keys("python\n")

#当只需要解析网页时，要使用python解析库，lxml或者BeautifulSoup去解析，因为效率高
html = etree.HTML(driver.page_source)
inputTag = html.xpath("//input[@id='kw']")[0]
#如果是需要点击网页的一个按钮或者输入数据，则需要使用selenium查找方法来完成查找



