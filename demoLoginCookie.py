# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/06 8:19'
from urllib import request,parse
from http.cookiejar import CookieJar

# 1.创建cookiejar对象
cookie = CookieJar()
handle = request.HTTPCookieProcessor(cookie)#handler处理器，向request或者response加入特定信息
opener = request.build_opener(handle)#opener,用于打开request的请求,相当于浏览器对象

# 2.输入账号密码访问登录地址返回cookie
login_url = "http://www.renren.com/PLogin.do"
header ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331'
}
data = {
    "email":"15926470603",
    "password":"LZ19940330330"
}
req = request.Request(login_url,headers=header,data=parse.urlencode(data).encode("utf-8"))
rep = opener.open(req)
print(rep.read().decode("utf-8"))
#3.访问主页
main_url ="http://www.renren.com/880792860/profile"
req = request.Request(main_url,headers=header)
rep  = opener.open(req)

with open("renren.html",'w',encoding="utf-8") as file:
    file.write(rep.read().decode("utf-8"))