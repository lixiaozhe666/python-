# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/09 21:32'
import threading
import time

class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("%s is coding" % threading.current_thread())
            time.sleep(1)

class DrawThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("%s is drawing" % threading.current_thread())
            time.sleep(1)

def coding():
    for x in range(3):
        print("%s is coding"%threading.current_thread())
        time.sleep(1)

def drawing():
    for x in range(3):
        print("%s is drawing"%threading.current_thread())
        time.sleep(1)

def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    t3 = CodingThread()
    t4 = DrawThread()
    t1.start()
    t2.start()
    t3.start()
    t4.start()

if __name__ == '__main__':
    main()