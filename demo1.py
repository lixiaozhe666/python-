# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/05 16:42'
from urllib import request,parse
data ={
    "first":'true',
    "pn":1,
    "kd":"Android"
}
header ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36",
    "Referer":"https://www.lagou.com/jobs/list_Android?px=default&city=%E5%B9%BF%E5%B7%9E"
}
req = request.Request("https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false",data = parse.urlencode(data).encode("utf-8"),headers = header,method="POST")
result = request.urlopen(req)
print(result.read().decode("utf-8"))