import _thread
import time

def rint_time(thname,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s:%s"%(thname,time.ctime(time.time())))

try:
    _thread.start_new_thread(rint_time,("thread-1",2,))
    _thread.start_new_thread(rint_time,("thread-2",4,))
    _thread.start_new_thread(rint_time,("thread-3",6,))
except:
    print("Error:无法启动线程")
while 1:
    pass