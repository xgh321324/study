#coding:utf-8
import _thread
from time import sleep,ctime
loops=[2,4]
def loop(nloop, nsec, lock):
    print ('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print ('loop', nloop, 'done at:', ctime())
#解锁
    lock.release()
def main():
    print( 'starting at:', ctime())
    locks =[]
    #以 loops 数组创建列表，并赋值给 nloops
    nloops = list(range(len(loops)))
    print('nloops:::',nloops)
    print()
    for i in nloops:
        lock = _thread.allocate_lock()
    #锁定
        lock.acquire()
#追加到 locks[]数组中
        locks.append(lock)
#执行多线程
    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked():
            pass
    print ('all end:', ctime())
if __name__ == '__main__':
    main()

'''
我们应该避免使用 thread 模块，原因是它不支持守护线程。当主线程退出时，所有的子线程不论它
们是否还在工作，都会被强行退出。有时我们并不期望这种行为，这时就引入了守护线程的概念。threading
模块则支持守护线程。
'''

