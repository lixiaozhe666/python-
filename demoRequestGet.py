# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/06 10:22'
import requests
data = {
    "wd":"中国"
}
header ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331',
}
# 使用request库传参时不需要使用urlencode函数去编码成byte类型数据，库自动去编码。get方法参数是params=,post方法是data=
response = requests.get("http://www.baidu.com/s",params=data,headers = header)

# print(response.text)#.text输出str类型数据，可能自动匹配的解码方式不对，造成乱码
# print(response.content.decode("utf-8"))#response.content输出byte类型,硬盘与网络上传输的数据都是byte类型，可以自己定义解码方式
# print(response.url)
# print(response.status_code)
#
with open("baidu.html",'w',encoding='utf-8') as file:
    file.write(response.content.decode("utf-8"))

