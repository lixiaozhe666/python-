# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/06 11:05'
import requests

proxy ={
    'http':'114.236.97.36:61234'
}
url = "http://ip.chinaz.com/getip.aspx"
response = requests.get(url,proxies=proxy)
print(response.text)
