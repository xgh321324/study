#coding:utf-8
from time import sleep,ctime
import threading
loops =[2,4]
def loop(nloop,nsec):
    print('start',nloop,'at:',ctime())
    sleep(nsec)
    print(nloop,'done at:',ctime())

def main():
    print('all is start at:',ctime())
    threads = []
    nloop = list(range(len(loops))) #nloop其实就是一个列表【0，1】
    #创建线程
    for i in nloop:
        t=threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)
    #开始线程
    for i in nloop:
        threads[i].start()
    #等待所有线程结束
    for i in nloop:
        threads[i].join()
    print('all is end at:',ctime())
if __name__=='__main__':
    main()

