import os


rpid = os.fork()
if rpid < 0:
    print("Fork failed")
elif rpid == 0:
    print("PID: %s PPID: %s"%(os.getpid(), os.getppid()))
else:
    print("PID: %s CID: %s"%(os.getpid(), rpid))
print("All comes here")
exit()
