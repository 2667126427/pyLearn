import threading
import time

def say_sorry():
    print("I am sorry dear, can I have a meal?")

if __name__ == '__main__':
    start = time.time()
    for i in range(50000):
        t = threading.Thread(target=say_sorry)
        t.start()
    end = time.time()
    t1 = end - start
    start = time.time()
    for i in range(50000):
        say_sorry()
    end = time.time()
    t2 = end - start
    print('t1: %.2f t2: %.2f'%(t1, t2))
