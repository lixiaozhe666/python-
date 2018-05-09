# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/09 14:49'
import re
#1.匹配电话号码，第一位为1，第二位为34587，后面九位随意
# text ="11126470808"
# ret = re.match("1[34587]\d{9}",text)
# print(ret.group())

#2.匹配邮箱
# text = "lizhe276855526@qq.com"
# ret =re.match("\w+@\w+\.com",text)
# print(ret.group())
#以@163.com结尾的邮箱
# text = "lizhe276855526@163.com"
# ret =re.match("\w+@163\.com$",text)#$会找最后正常字符作为一个整体为匹配对象如：@163\.com，\w为特殊字符 有特别的意义
# print(ret.group())

#3.匹配URL
# text = "http://edu.51cto.com//center/course/lesson/index?id=1055_221944&type=wejob"
# ret = re.match("(http|https|ftp)://[^\s]+",text)
# print(ret.group())

#4.匹配0-100之间的数字
# text= "1"
# ret = re.match("[1-9]\d?$|100$",text)
# print(ret.group())

#5.原生字符串
# text = '\c'
# ret = re.match(r"\\c",text)#r'\\c' = '\\\\c'
# print(ret.group())

#6.分组
# 正则表达式中用()括起来的就是一个分组,可以通过group()来取特定位置的分组
# text = "apple's price  $30 , orange's price $20"
# ret = re.match(".*(\$\d+).*(\$\d+)",text)#.*(\$\d+).*(\$\d+) = (.*(\$\d+).*(\$\d+)),整个是个大分组ret.group(0)=ret.group()
# print(ret.group())
# print(ret.group(1))#输出第一个分组
# print(ret.group(2))#输出第一个分组
# print(ret.group(1,2))#输出第一个分组
# print(ret.groups())#输出所有分组，不包含group(0)

#7.findall()把所有满足添加的都选出来,返回一个列表,且列表元素为括号中的元素，如不加括号则返回全部满足正则表达式的str
text = "apple's price $30 , orange's price $20"
ret = re.findall("price (\$\d+)",text)
print(ret)

#8.sub()替换函数，返回替换后的字符串
# text = "apple's price  $30 , orange's price $20"
# ret = re.sub("\$\d+",'$0',text)
# print(ret)

#sub()使用案例，可以把标签替换为空字符串，获得文本信息
# html ='''
# <dd class="job_bt">
#         <h3 class="description">职位描述：</h3>
#         <div>
#         <p>岗位职责：</p>
# <p>1、 参与政府及企事业单位软件产品和软件项目的开发工作；</p>
# <p>2、 对所负责开发的模块进行功能测试、维护；</p>
# <p>3、 编写开发过程相关文档；</p>
# <p>4、 分析并解决软件开发过程中的问题；</p>
# <p>5、 客户现场实施部署并解决可能出现的问题。&nbsp;</p>
# <p><br></p>
# <p>任职要求：</p>
# <p>1）1年以上Java开发工作经验，具有一定规模的项目开发经验；</p>
# <p>2）熟练使用eclipse，IntelliJ IDEA等常用开发工具。</p>
# <p>3）熟悉NOSQL系列数据库并拥有一定开发经验。</p>
# <p>4）熟悉主流数据库，如ORACLE，MSSQL，MYSQL等。</p>
# <p>5）熟悉使用各类开源框架,如：Spring MVC、Spring boot Hibernate、mybatis等。</p>
# <p>6）熟练使用前端开发技术，如HTML，HTML5，JS、Ajax、基于DIV+CSS的页面布局等技术。</p>
# <p>7）熟悉主流应用服务器如Tomcat,Weblogic、TongWeb等J2EE服务器。</p>
# <p>8）熟悉Windows,Linux等平台环境下开发及部署。</p>
# <p>9）具有阅读相关技术需求文档能力；具有一定的软件设计及文档编写能力。</p>
# <p>10）有较好的沟通表达能力、学习能力和抗压能力，性格外向开朗，喜欢技术，有对技术难题的专研精神。</p>
#         </div>
#     </dd>
# '''
# ret = re.sub("<.+?>",'',html)
# print(ret)

#9.split()函数，根据正则表达式作为分割条件，返回列表
# text = 'hello world%ni hao'
# ret = re.split(' |%',text)#以空格与%作为分隔符，返回['hello', 'world', 'ni', 'hao']
# print(ret)

#10.compile()编译正则表达式，可以获得更高的执行效率，使用re.VERBOSE参数可以写注释
# text = "the price is 20.50 "
# r = re.compile(r'''
#                 \d+ #小数点前数字
#                 \.? #小数点
#                 \d* #小数点后数字
#                 ''',re.VERBOSE)
# ret = re.search(r,text)
# print(ret.group())