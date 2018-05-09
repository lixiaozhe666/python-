# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/09 10:24'

from bs4 import BeautifulSoup
text = '''
<li class="con_list_item default_list" data-index="1" data-positionid="4383913" data-salary="20k-25k" data-company="人人行(借贷宝)" data-positionname="Java工程师" data-companyid="61921" data-hrid="7134052" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4383913.html" target="_blank" data-index="1" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0102
                                                                                        " data-lg-tj-cid="4383913" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">Java工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>北京·朝阳区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">2天前发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">20k-25k</span>
                                    <!--<i></i>-->经验3-5年 / 不限
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/61921.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0102
                                                                                        " data-lg-tj-cid="61921" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">人人行(借贷宝)</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网,金融 / C轮
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/61921.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0102
                                                                                        " data-lg-tj-cid="61921" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/04/01/CgqKkVbFXXqAPo0fAAATqvTo2-I592.png" alt="人人行(借贷宝)" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                                                        <span>年底双薪</span>
                                                                                                                                                <span>节日礼物</span>
                                                                                                                                                <span>绩效奖金</span>
                                                                                                                                                <span>岗位晋升</span>
                                                                                                                        </div>
                        <div class="li_b_r">“弹性工作,高并发系统,团队大牛多,工作氛”</div>
                    </div>
                </li>
<li class="con_list_item default_list" data-index="2" data-positionid="4477797" data-salary="15k-25k" data-company="拉勾网" data-positionname="java开发工程师" data-companyid="147" data-hrid="2848224" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4477797.html" target="_blank" data-index="2" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0103
                                                                                        " data-lg-tj-cid="4477797" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">java开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>北京·海淀区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">3天前发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">15k-25k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/147.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0103
                                                                                        " data-lg-tj-cid="147" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">拉勾网</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                企业服务,招聘 / D轮及以上
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/147.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0103
                                                                                        " data-lg-tj-cid="147" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/76/40/Cgp3O1g1TNOAB2yxAAA9bQUyc4g814.png" alt="拉勾网" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>分布式</span>
                                                                    <span>架构</span>
                                                                                    </div>
                        <div class="li_b_r">“技术挑战,成长空间”</div>
                    </div>
                </li>
<li class="con_list_item default_list" data-index="3" data-positionid="3155873" data-salary="4k-8k" data-company="小肚皮App" data-positionname="实习JAVA/PHP开发" data-companyid="41030" data-hrid="795835" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/3155873.html" target="_blank" data-index="3" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0104
                                                                                        " data-lg-tj-cid="3155873" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">实习JAVA/PHP开发</h3>
                                                                                                                                                                        <span class="add">[<em>北京·大望路</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">10:13发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">4k-8k</span>
                                    <!--<i></i>-->经验应届毕业生 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/41030.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0104
                                                                                        " data-lg-tj-cid="41030" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">小肚皮App</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网 / A轮
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/41030.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0104
                                                                                        " data-lg-tj-cid="41030" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/65/83/CgpFT1mlFSWAJrrnAACWcSWNiu8425.png" alt="小肚皮App" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot" id ="test">
                        <div class="li_b_l">
                                                                                                <span>游戏</span>
                                                                    <span>后端开发</span>
                                                                                    </div>
                        <div class="li_b_r">“转正机会,逗逼氛围,美女如云,餐补”</div>
                    </div>
                </li>
'''

soup = BeautifulSoup(text,'lxml')#'lxml'解析器，按照lxml来解析html文档，如果html不规范无法解析可以使用'html5lib'解析器
                                 #'html5lib'解析器容错率最强
#1获得所有li标签
# lis = soup.find_all("li")
# for li in lis:
#     print(li)
#     print("*"*30)

# lis = soup.select("li")
# for li in lis:
#     print(li)
#     print("*"*30)

#2获得第2个li标签
# liTwo = soup.find_all("li",limit=2)[1]#limit控制查找出来元素的数量，find_all()返回一个数组
# print(liTwo)

# liTwo = soup.select("li")[1]
# print(liTwo)


#3获得第2个含第2个以后的li标签
# lis =soup.find_all("li")[1:]
# for li in lis:
#     print(li)
#     print("*"*30)

# lis =soup.select("li")[1:]
# for li in lis:
#     print(li)
#     print("*"*30)

#4获得所有class = industry的标签div元素
    #1.使用属性=值查找
    # divs = soup.find_all("div",class_="industry")
    # for div in divs:
    #     print(div)
    #     print("*"*30)

    #2使用attrs查找
    # divs  = soup.find_all("div",attrs={"class":"industry"})
    # for div in divs:
    #     print(div)
    #     print("*"*30)

# divs  = soup.select("div.industry")
# for div in divs:
#     print(div)
#     print("*"*30)

#5获得所有class中含有_list的元素li标签
# lis = htmlElement.xpath("//li[contains(@class,'_list')]")
# for li in lis:
#     print(etree.tostring(li,encoding="utf-8").decode("utf-8"))

#6.获得a标签的href的文本
# aList = soup.find_all("a")
# for a in aList:
#     print(a["href"])#或者a.attrs['href']
#     print("*"*30)

# aList = soup.select("a")
# for a in aList:
#     print(a["href"])#或者a.attrs['href']
#     print("*"*30)


#7.获得 class为list_item_bot ,id为test的div
# divs = soup.find_all("div",class_="list_item_bot",id="test")
# for div in divs:
#     print(div)

#8.获得所有文本信息
# lis = soup.find_all("li")
# lis  =soup.select("li")
# for li in lis:
#     infos = list(li.strings)#过滤掉所以非标签元素的文本
#     # print(infos)
#     infos2 = list(li.stripped_strings)#过滤掉所以非标签元素的文本，且不含控制字符和空格
#     # print(infos2)
#     infos2 = [x for x in infos2 if x!='[' and x !=']']
#     position = {
#         "title":infos2[0],
#         "address":infos2[1],
#         "pubtime":infos2[2],
#         "salary":infos2[3]
#     }
#     print( position)

#9.获得li下面的所有子孙div
# divs = soup.select("li div")
# for div in divs:
#     print(div)
#     print("*"*30)

#10 获得li下面直接子div
# divs = soup.select("li > div")
# for div in divs:
#     print(div)
#     print("*"*30)

#11 获得class 为industry的标签
# Elements = soup.select(".industry")
# for Element in Elements:
#     print(Element)
#     print("*"*30)

#12 获得所有id为test的标签
# Elements = soup.select("#test")
# for Element in Elements:
#     print(Element)
#     print("*"*30)












