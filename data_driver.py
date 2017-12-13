#coding:utf-8
from selenium import webdriver
import os,time
with open('E:/pythonlianxi/study/data.txt') as f:
    values = f.readlines()
for x in values:
    browser = webdriver.Chrome()
    browser.maximize_window
    browser.get('http://www.baidu.com')
    browser.find_element_by_id('kw').send_keys(x)
    browser.find_element_by_id('su').click()
    time.sleep(4)
    browser.close()
    browser.quit()



