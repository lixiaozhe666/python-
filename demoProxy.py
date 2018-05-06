# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/05 22:02'
from urllib import request
url ="http://ip.chinaz.com/getip.aspx"
#1.ProxyHandle生成代理handle
handle = request.ProxyHandler({'http':'183.159.80.115:18118'})#http必须小写，报错很可能是代理的原因
#2.使用handel构建opener
opener = request.build_opener(handle)
#3.使用opener发送一个请求
resp = opener.open(url)
print(resp.read().decode("utf-8"))

