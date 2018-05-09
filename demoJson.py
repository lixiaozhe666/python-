# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/09 20:05'
#json只能序列化内置对象，int,float等，自定义对象不能使用json序列化,json实质是一个字符串
#检查json格式可以去 json.cn
import json
students =[
    {
        "name":"张三",
        "age":18,
        "sex":"男"
    },
    {
        "name":"李四",
        "age":18,
        "sex":"男"
    }
]
json_str = json.dumps(students,ensure_ascii=False)#如果json里面有中文，则需要把ensure_ascii设置为false，转化为json对象
print(type(json_str))#str
print(json_str)
jsonO = json.loads(json_str)#json转python对象
print(jsonO)
with open('student.json','w',encoding="utf-8") as fp:#如果有中文写进文件，要设置文件编码方式
    json.dump(students,fp,ensure_ascii=False)#写入文件
with open('student.json','r',encoding='utf-8') as fp:
    jsonO = json.load(fp)#读文件
    print(jsonO)