from multiprocessing import Queue

q = Queue(3)
q.put('msg1')
q.put('msg2')
print('q is full: %s'%q.full())
q.put('msg3')
print('q is full: %s'%q.full())

# try:
#     q.put('msg4', True, 2) # 等待2s
# except:
#     print("error: q's size=%d"%q.qsize())

try:
    q.put_nowait('msg4')
except:
    print("error: q's size=%d"%q.qsize())

if not q.full():
    q.put_nowait('msg4')
else:
    print('q is full')

if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
