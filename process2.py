#coding:utf-8
from multiprocessing import Process
import os
def info(title):
    print(title)
    print('modulname:',__name__)
    if hasattr(os,'getppid'):
        print('parent process is:',os.getppid())
    print('process id :',os.getpid())
def f (name):
    info('function f')
    print('hello',name)
if __name__=='__main__':
    info('mainly line')
    p = Process(target=f,args=('xuxu',))
    p.start()
    p.join()

