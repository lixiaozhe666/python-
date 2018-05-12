#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lz 
@file: demotest.py 
@time: 2018/05/12   09：17 
"""
str="昨天应邀参加一个大型拍卖会，最终以10亿天价拍下这幅李11白大师所画的《龙凤呈祥》。10亿元虽然对于某些土豪来说不算什么，但是对于我们普通家庭来说这个是一个月的工资啊。也不知道值不值？请懂行姐夫们掌掌眼。"
if len(str)>=10:
    str = str[:10]

print(str)