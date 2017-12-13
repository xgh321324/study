#coding:utf-8
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()
try:
    browser.get('http://www.baidu.com')
    time.sleep(4)
    browser.find_element_by_id('kwsd').send_keys('人生何处不艰难！')
    browser.find_element_by_id('su').click()
except:
    browser.get_screenshot_as_file('C://Users//Administrator//Desktop//page_error.png')
    print('捕获错误截图')
finally:
    browser.close()
    browser.quit()
    print('关闭浏览器')
