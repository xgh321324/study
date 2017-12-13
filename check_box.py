#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('C://Users//Administrator//Desktop//test.html')
time.sleep(4)
#checkbox
browser.find_element_by_xpath('//input[@value="cv1"]').click()
browser.find_element_by_xpath('//input[@value="cv2"]').send_keys(Keys.SPACE)   #对这个狂发送空格键也能选中
time.sleep(5)

#radio
browser.find_element_by_xpath('//input[@value="rv1"]').click()
browser.find_element_by_xpath('//input[@value="rv2"]').send_keys(Keys.SPACE)  #对这个狂发送空格键也能选中
time.sleep(5)
#上例可以看出我们对这种checkbox和radio，可以通过直接点击或者发送空格的方式达到选中或者反选的目的

browser.close()
browser.quit()