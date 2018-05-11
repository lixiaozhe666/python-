# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/10 11:13'
#多线程爬取表情包
#通过线程安全的quene来获取
#生产者为爬去每一页的每个表情的url
#消费者负责下载表情

import requests
import os
import re
import threading
import time
from lxml import etree
from urllib import request
from queue import Queue

class ProdecerUrl(threading.Thread):
    def __init__(self,page_urls,img_urls,*args,**kargs):
        super(ProdecerUrl,self).__init__(*args,**kargs)
        self.page_urls = page_urls
        self.img_urls = img_urls

    def run(self):
        while True:
            if self.page_urls.empty():
                break;
            url = self.page_urls.get()

            self.parse_page(url)

    def parse_page(self,url):
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
            self.img_urls.put((img_url,filename))
            # request.urlretrieve(img_url,'images/'+filename)#按照url下载数据到指定文件
            # print(filename)
            # # print(etree.tostring(img,encoding="utf-8"))
            # print('='*30)
class CustomUrl(threading.Thread):
    def __init__(self,page_urls,img_urls,*args,**kargs):
        super(CustomUrl,self).__init__(*args,**kargs)
        self.page_urls = page_urls
        self.img_urls = img_urls

    def run(self):
        while True:
            if self.img_urls.empty() and self.page_urls.empty():
                break
            img_url,filename = self.img_urls.get()

            request.urlretrieve(img_url,'images/'+filename)#按照url下载数据到指定文件
            print(filename)
            # # print(etree.tostring(img,encoding="utf-8"))
            print('='*30)

def main():
    page_urls = Queue(100)
    img_urls =Queue(1000)#如果生产者生产速度太快，不能因为队列长度太短造成等待
    for x in range(1,11):
        url = "http://www.doutula.com/photo/list/?page=%d"%x
        page_urls.put(url)

    for x in range(5):#如果线程数量和page_urls数量接近，容易造成消费者退出条件满足，因为生产者一人一个url page_urls就为空，img_urls还没有对象时就容易退出爬不到数据
        t = ProdecerUrl(page_urls,img_urls)
        t.start()

    for x in range(5):
        t = CustomUrl(page_urls, img_urls)
        t.start()



if __name__ == '__main__':
    main()