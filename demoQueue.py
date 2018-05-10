# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/10 10:30'
import queue
import threading
import time

def put_Queue(q):
    index = 0
    while True:
        q.put(index)
        index+=1
        print("队列大小为%d"%q.qsize())
        time.sleep(1)
        if q.full():#如果满了就退出
            break
    pass

def get_Queue(q):
    while True:
        if q.full():#如果满了就退出
            break
        print(q.get())#q.get(block = False)当为false的时候就不阻塞直接获取，获取不到就报错，默认为阻塞即wait()
        time.sleep(2)
    pass

def main():
    q = queue.Queue(4)#4为最大队列长度

    t2 = threading.Thread(target=put_Queue,args=[q])#如果线程需要参数 则用args=[]方式来传
    t1 = threading.Thread(target=get_Queue, args=[q])

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()