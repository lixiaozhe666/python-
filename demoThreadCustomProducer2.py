# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/10 10:02'
import threading
import random
import time
gMoney = 0
gCondtionLock = threading.Condition()#使用condition进行加锁解锁
nTotalNum = 10
Num = 0
#在爬虫的时候如果把url插入数据库，和从数据库读取的时候可以枷锁，
# 在网络上爬取的时候因为所用时间远大于读取数据库的时间，所以多线程可以提高效率
class CustomerThread(threading.Thread):
    def run(self):
        global gMoney
        global Num
        global nTotalNum
        while True:
            gCondtionLock.acquire()
            money = random.randint(100,500)
            while gMoney<money:
                if Num>=nTotalNum:
                    gCondtionLock.release()
                    return
                print("%s 预计消费 %d,还剩%d 余额不足" % (threading.current_thread(), money, gMoney))
                gCondtionLock.wait()#wait()释放锁后进行等待 直到notify_all()或者notify()发出通知，在获得锁

            gMoney -=money
            print("%s 消费 %d,还剩%d " % (threading.current_thread(), money, gMoney))
            gCondtionLock.release()
            time.sleep(1)
        pass

class ProducerThread(threading.Thread):
    def run(self):
        global gMoney
        global Num
        global nTotalNum
        while True:
            gCondtionLock.acquire()
            if Num>=nTotalNum:
                gCondtionLock.release()#释放锁以后在break
                break
            money = random.randint(500,1000)
            gMoney +=money
            Num+=1
            print("%s 生产了%d元,剩余%d元"%(threading.current_thread(),money,gMoney))
            gCondtionLock.notify_all()#给wait()的线程发通知，告诉他们有数据了
            gCondtionLock.release()
            time.sleep(1)
        pass

def main():
    for x in range(1,5):
        t = CustomerThread()
        t.start()
    for x in range(1,3):
        t = ProducerThread()
        t.start()

if __name__ == '__main__':
    main()