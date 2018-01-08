#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://www.baidu.com')
time.sleep(3)
#browser.find_element_by_xpath('//form[@id="form"]/span/input').send_keys('屈小杰')  #其实这是利用爷爷级别的属性来定位
#browser.find_element_by_id('su').click()
browser.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
browser.find_element_by_link_text('搜索设置').click()
time.sleep(2)
win= browser.current_window_handle
browser.switch_to.window(win)
s= Select(browser.find_element_by_xpath('//*[@id="nr"]'))
s.select_by_visible_text('每页显示50条')
browser.find_element_by_link_text('保存设置').click()
time.sleep(2)
a = browser.switch_to.alert
a.accept()

print('保存成功')
print('测试结束')
browser.close()
browser.quit()
#kandao 64y页（未）明天去公司继续