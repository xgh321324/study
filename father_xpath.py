#coding:utf-8
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://www.baidu.com')
browser.find_element_by_xpath('//form[@id="form"]/span/input').send_keys('屈小杰')  #其实这是利用爷爷级别的属性来定位
browser.find_element_by_id('su').click()
print('测试结束')
browser.close()
browser.quit()
#kandao 64y页（未）明天去公司继续