#coding:utf-8
import threading
from time import sleep,ctime
loops = [2,4]
class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        self.func = func
        self.name=name
        self.args=args
    def __call__(self):
        return (self.args,self.func,self.name)
    
def loop(nloop,nsec):
    print('start loop',nloop,'at:',ctime())
    sleep(nsec)
    print(nloop,'done at:',ctime())
def main():
    print('starting at:',ctime())
    threads = []
    nloop = list(range(len(loops)))
    for i in nloop:
        #调用Threadfunc实例化的对象，创建所有线程
        t = threading.Thread(target=ThreadFunc(loop,loops[i],loop.__name__))
        threads.append(t)
    #开始线程
    for i in nloop:
        threads[i].start()
    #等待线程结束
    for i in nloop:
        threads[i].join()
    print('all is end:',ctime())
if __name__=='__main__':
    main()
