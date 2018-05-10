# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/10 11:13'
import requests
import os
import re
from lxml import etree
from urllib import request
def parse_page(url):
    header = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 66.0.3359.117Safari / 537.36'
    }
    response = requests.get(url,headers=header)
    text = response.text
    html =etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")#可以选择直接不等于
    for img in imgs:
        img_url = img.get("data-original")#get方法可以直接获取属性
        title = img.get("alt")
        suffix = os.path.splitext(img_url)[1]#获取后缀名
        filename = title +suffix
        filename = re.sub("\?？，,\.。！!","",filename)
        request.urlretrieve(img_url,'images/'+filename)#按照url下载数据到指定文件
        print(filename)
        # print(etree.tostring(img,encoding="utf-8"))
        print('='*30)

def main():
    for x in range(1,11):
        url = "http://www.doutula.com/photo/list/?page=%d"%x
        parse_page(url)
        break
        pass

if __name__ == '__main__':
    main()