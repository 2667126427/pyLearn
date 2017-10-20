#coding=utf-8
import threading
import time

num = 0
mutex = threading.Lock()

class MyThread(threading.Thread):
    def run(self):
        global num 
        mutexFlag = mutex.acquire(True) #True表示堵塞
        print('---线程(%s)的锁状态为%d---'%(self.name,mutexFlag))
        if mutexFlag:#判断上锁是否成功
            num = num+1
            time.sleep(1)
            msg = self.name+' set num to '+str(num)
            print(msg)
            mutex.release()

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    test()
    