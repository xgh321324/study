#coding:utf-8
from multiprocessing import Process   #Process P是大写

#multiprocessing 模块用来管理进程 而不是线程
def f(name):
    print('hello',name)
if __name__=='__main__':
    p = Process(target=f,args=('习近平',))    #multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})  args必须是一个tuple
    p.start()#开始                                 #target 表示调用对象，args 表示调用对象的位置参数元组。kwargs 表示调用对象的字典。Name 为别名。
                                                   # Group 实质上不使用。
    p.join() #