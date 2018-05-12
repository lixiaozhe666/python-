#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lz 
@file: demoAsynbsbdj.py 
@time: 2018/05/12   07：45 
"""
#三个类都是io频繁的类型，所以可以定义为多线程，虽然每个类的线程对于提高效率没有什么卵用，
# 但是三个io操作频繁的线程之间相互切换可以避免因为等待io而造成的cpu浪费，从而提高效率
import threading
import requests
import re
import csv
from queue import Queue
from lxml import etree
from urllib import request

lock = threading.Lock()

class Producer(threading.Thread):
    def __init__(self,page_urls,image_urls,*args,**kwargs):
        super(Producer,self).__init__(*args,*kwargs)
        self.page_urls = page_urls
        self.image_urls = image_urls
    def run(self):
        while True:
            if self.page_urls.empty():
                break
            self.parse_page(self.page_urls.get())
        pass

    def parse_page(self,url):
        header = {
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 66.0.3359.117Safari / 537.36'
        }
        response = requests.get(url, headers=header)
        text = response.content.decode("utf-8")
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='j-r-list-c-img']//img")
        for img in imgs:
            # print(etree.tostring(img))
            img_url = img.get("data-original")
            img_title = img.get("title")
            self.image_urls.put((img_url,img_title))
    pass

class CustomRetrive(threading.Thread):#从网络下载
    def __init__(self,page_urls,image_urls,content_urls,*args,**kwargs):
        super(CustomRetrive,self).__init__(*args,*kwargs)
        self.page_urls = page_urls
        self.image_urls = image_urls
        self.content_urls =content_urls
    def run(self):
        while True:
            if self.page_urls.empty() and self.image_urls.empty():
                break
            img_url,img_title = self.image_urls.get()
            img_title = re.sub("\?？，,\.。！!","",img_title)

            if len(img_title)>=10:
                img_title = img_title[:10]
            request.urlretrieve(img_url, 'images/%s' % img_title)
            self.content_urls.put({'title':img_title,'url':img_url})
            print("%s 下载完成-----"%img_title)


    pass

class CustomWirteCSV(threading.Thread):#保存到csv文件
    def __init__(self,page_urls,image_urls,content_urls,*args,**kwargs):
        super(CustomWirteCSV,self).__init__(*args,*kwargs)
        self.page_urls = page_urls
        self.image_urls = image_urls
        self.content_urls =content_urls

    def run(self):
        while True:
            if self.page_urls.empty() and self.image_urls.empty() and self.content_urls.empty():
                break
            self.WriteDictCSV(self.content_urls.get())

    def WriteDictCSV(self,content):
        header = ["title","url"]
        lock.acquire()

        with open("bsbdj.csv", 'a', encoding="utf-8", newline="") as fp:
            writer = csv.DictWriter(fp, header)
            writer.writeheader()  # 不写这一句则不会写入header
            writer.writerows([content])#必须为列表，且裂变元素为字典
        lock.release()


if __name__ == '__main__':
    page_urls = Queue(10)
    image_urls = Queue(500)
    content_url = Queue(500)
    for x in range(1,11):
        url = "http://www.budejie.com/text/%d"%x
        page_urls.put(url)
    for x  in range(5):
        t= Producer(page_urls,image_urls)
        t.start()
    for x in range(5):
        t=CustomRetrive(page_urls,image_urls,content_url)
        t.start()
    for x in range(5):
        t=CustomWirteCSV(page_urls,image_urls,content_url)
        t.start()
    # parse_page("http://www.budejie.com/text/1")
    print("----------下载完成----------------")
