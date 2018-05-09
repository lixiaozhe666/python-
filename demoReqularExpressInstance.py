# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/09 17:16'
import requests
import re
def parse_page(url):
    header ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331'
    }
    response = requests.get(url,header)
    page = response.text
    titles = re.findall('<div class="cont">.*?<b>(.*?)</b>',page,re.DOTALL)#findall()函数找到（）里面的表达式
    dynasties = re.findall('<p class="source">.*?<a .*?>(.*?)</a>',page,re.DOTALL)
    authors = re.findall('<p class="source">.*?<a .*?<a .*?>(.*?)</a>',page,re.DOTALL)
    contents_pages = re.findall('<div class="contson".*?>(.*?)</div>',page,re.DOTALL)
    contents=[]
    poems = []
    for content_page in contents_pages:
        contents.append(re.sub("<.*?>","",content_page))

    for poem in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = poem
        temp = {
            "title":title,
            "dynasty":dynasty,
            "author":author,
            "content":content
        }
        poems.append(temp)
    print(poems)
    pass

def main():
    url = "https://www.gushiwen.org/default_2.aspx"
    parse_page(url)

if __name__ == '__main__':
    main()