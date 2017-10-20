from multiprocessing import Process
import os

def run_proc(name):
    """
    child process
    """
    print("child process running name=%s,pid=%s"%(name, os.getpid()))

if __name__ == '__main__':
    print('PProcessa %d.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('child precess')
    p.start()
    p.join()  # 防止未完成就退出
    print('child process done')
