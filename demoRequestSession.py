# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/06 11:22'
import requests
login_url = "http://www.renren.com/PLogin.do"
header ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331'
}
data = {
    "email":"15111470603",
    "password":"21111111130"
}
session =requests.session()
session.post(login_url,headers=header,data = data)
main_url ="http://www.renren.com/880792860/profile"
response = session.get(main_url)
with open("renren2.html",'w',encoding="utf-8") as file:
    file.write(response.content.decode("utf-8"))