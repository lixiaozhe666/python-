# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/06 10:44'
import requests
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331",
    "Referer":"https://www.lagou.com/jobs/list_Android?px=default&city=%E5%B9%BF%E5%B7%9E"
}
data = {
    'first':'true',
    'pn':'1',
    'kd':'Android'
}
response =requests.post("https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false",data=data,headers = header)
print(response.json())#输出字典格式json数据