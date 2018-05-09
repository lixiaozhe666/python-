# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/09 20:37'
import csv
def WriteListCSV():
    header = ["name","age","height"]
    students=[
        ("张三",18,180),
        ("李四",19,190),
        ("王五",20,170)
    ]
    with open("student.csv",'w',encoding="utf-8",newline="") as fp:#默认newline = "\n"，如果不设置为空，则会在每行后加一个空行
        writer = csv.writer(fp)
        writer.writerow(header)
        writer.writerows(students)

def WriteDictCSV():
    header = ["name", "age", "height"]
    students =[
        {
            "name":"张三",
            "age":18,
            "height":180
        },
        {
            "name": "李四",
            "age": 18,
            "height": 180
        },
        {
            "name": "张三三",
            "age": 18,
            "height": 180
        }
    ]
    with open("student.csv",'w',encoding="utf-8",newline="") as fp:
        writer = csv.DictWriter(fp,header)
        writer.writeheader()#不写这一句则不会写入header
        writer.writerows(students)

def ReaderListCSV():
    with open("student.csv",'r',encoding="utf-8") as fp:
        readers = csv.reader(fp)
        next(readers)#可以去除第一行标题头  ['name', 'age', 'height']
        for reader in readers:
            print(reader)
            print(reader[0])#使用下标选取特定元素

def ReaderDictCSV():
    with open("student.csv",'r',encoding="utf-8") as fp:
        readers = csv.DictReader(fp)
        for reader in readers:
            print(reader)
            print(reader['name'])  # 使用字典键值选取特定元素

if __name__ == '__main__':
    # ReaderListCSV()
    ReaderDictCSV()