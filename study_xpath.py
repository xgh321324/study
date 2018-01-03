#coding:utf-8
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.maximize_window()
'''
#用xpath通过id定位
browser.find_element_by_xpath('//*[@id="kw"]').send_keys('南京天气')
browser.find_element_by_xpath('//*[@id="kw"]').click()
'''
#用xpath通过name属性定位
'''

browser.find_element_by_xpath('//*[@name="wd"]').send_keys('常州天气')
browser.find_element_by_xpath('//*[@id="kw"]').click()
'''


#用xpath通过class 属性定位
#browser.find_element_by_xpath('//*[@class="s_ipt"]').send_keys('泗洪')
#browser.find_element_by_xpath('//*[@id="kw"]').click()


#如果一个元素 id、name、class 属性都没有，这时候也可以通过其它属性定位
browser.find_element_by_xpath('//*[@autocomplete="off"]').send_keys(12345)
browser.find_element_by_xpath('//*[@id="kw"]').click()






time.sleep(3)
browser.close()
browser.quit()

#1-1日看到62页