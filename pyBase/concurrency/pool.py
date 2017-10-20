from multiprocessing import Pool
import os, time, random


def worker(msg):
    """
       worker 
    """
    t_start = time.time()
    print("%s starts processing, pid: %d"%(msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "done time used: %.2f"%(t_stop - t_start))

po = Pool(3)
for i in range(0, 10):
    po.apply_async(worker, (i, ))
    # po.apply(worker, (i, ))
        
print('----start----')
t_start = time.time()
po.close()
po.join()
t_stop = time.time()
print("----end----")
print("time sum: %.2f"%(t_stop - t_start))
