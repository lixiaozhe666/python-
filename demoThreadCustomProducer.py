# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/10 9:11'
import threading
import random
import time
gMoney = 0
gLock = threading.Lock()
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
            gLock.acquire()
            money = random.randint(100,500)
            if gMoney>=money:
                gMoney -=money
                print("%s 消费了%d元,剩余%d元"%(threading.current_thread(),money,gMoney))
            else:
                if Num>=nTotalNum:
                    gLock.release()
                    break
                print("%s 预计消费%d元,剩余%d元，余额不足" % (threading.current_thread(), money, gMoney))
            gLock.release()
            time.sleep(1)
        pass

class ProducerThread(threading.Thread):
    def run(self):
        global gMoney
        global Num
        global nTotalNum
        while True:
            gLock.acquire()
            if Num>=nTotalNum:
                gLock.release()#释放锁以后在break
                break
            money = random.randint(500,1000)
            gMoney +=money
            Num+=1
            print("%s 生产了%d元,剩余%d元"%(threading.current_thread(),money,gMoney))
            gLock.release()
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