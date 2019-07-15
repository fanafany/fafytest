#线程同步
"""
如果对多个线程共同修改某个数据，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步
使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire和release方法，
对于那些每次只允许一个线程的操作的数据，可以将其操作放到acquire和release方法之间。

注：有这样一种情况，一个列表里所有元素都是0，线程“set”从后向前把所有元素改成1，而线程“print”负责
从前往后读取列表并打印，那线程“set”开始改的时候，线程“print”便来打印列表了，输出就编程一半0一半1
这就是数据不同步，为了避免这种情况，引入锁的概念。
锁有两种状态：一种锁定一种未锁定。每当一个线程比如“set”要访问共享数据时，必须先获得锁定；如果已经有别的线程
比如“print”获得锁定了，那么就让线程“set”暂停，也就是同步阻塞；等到线程“print”访问完毕，释放锁以后，再让线程“set”继续
这样处理，打印列表要么全部输出0，要么全部输出1，不会再出现一半0或一半1
"""
import threading
import time

class myTread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开启线程："+ self.name)
        #获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        #释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print("%s:%s"%(threadName,time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

#创建新线程
thread1 = myTread(1,"t-1",1)
thread2 = myTread(2,"t-2",2)

#开启新线程
thread1.start()
thread2.start()

#添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

#等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")

