#coding:utf-8
import time
'''
try:
    open('abc.txt')
except IOError as e:
    print('error:',e)

try:
    f = open('C://Users//Administrator//Desktop//poem.txt')
    while True:
        line = f.readlines()
        if len(line) == 0:
            break
        print(line,end='')
finally:
    f.close()
    print('close the file')

filename = input('please input your name:')
if filename == 'hello':
    raise NameError('please input correct name!')
'''

lename = input('what your name?:')
if lename == 'good':
    raise ValueError('your name is not legal')

