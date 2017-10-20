 #coding=utf-8
import threading
import time

class A(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                print('---A---1---')
                con.wait()
                print('---A---2---')
                con.release()
                time.sleep(1)

class B(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                input('输入任意字符:')
                con.notify()
                con.release()
                time.sleep(1)

con = threading.Condition()

if __name__ == '__main__':
    a = A()
    a.start()

    b = B()
    b.start()
    