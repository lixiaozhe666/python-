# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/06 9:31'
from urllib import request
from http.cookiejar import MozillaCookieJar


cookie =MozillaCookieJar("cookie.txt")
handel = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handel)

opener.open("http://httpbin.org/cookies/set?name=lizhe22")

cookie.save(ignore_discard=True)#保存
cookie.load(ignore_discard=True)#载入
for c in cookie:
    print(c)
