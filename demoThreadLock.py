# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/09 23:23'
import threading
import time
count = 0
glock =threading.Lock()
def add_count():
    global count

    for x in range(1000000):
        glock.acquire()
        count+=1
        # print(threading.current_thread())
        glock.release()

    print(count)

if __name__ == '__main__':
    t1 = threading.Thread(target=add_count)
    t2 = threading.Thread(target=add_count)#只要第二个输出的是2000000就可以，
                                           # 锁加在for 里面才是真正的并行，
                                           #锁在for外层还是先执行完t1在执行t2,还是串行

    t1.start()
    t2.start()
