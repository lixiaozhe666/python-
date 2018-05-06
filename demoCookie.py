# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/05 23:16'
from urllib import request

url ="http://www.renren.com/880792860/profile"
header ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331',
    'Cookie':'anonymid=jgtj84q4-txf6wv; depovince=HUB; _r01_=1; JSESSIONID=abcP30X8kXtzn-f8q4Wmw; ick_login=2fd80652-4a11-46c0-8390-620909c51cad; t=72bbd4f70c95d18f1459f9679acb27ad0; societyguester=72bbd4f70c95d18f1459f9679acb27ad0; id=965779570; xnsid=cf1e945b; jebecookies=e0a3ddd4-105d-47aa-8381-14d732843363|||||; ver=7.0; loginfrom=null; jebe_key=a928342b-f0b3-4a41-b26d-ed332bb8120b%7C7e4751b99e97b478a812137eab779aed%7C1525533471094%7C1%7C1525533472021; wp_fold=0'
}
req = request.Request(url,headers=header)
result = request.urlopen(req)

print(result.read().decode("utf-8"))#read()方法读取全部的文件内容，所以文件指针已经到最后了，再次read()时就为空

with open("renren.html",'w',encoding="utf-8") as file:
    file.write(result.read().decode("utf-8"))
