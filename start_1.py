#coding:utf-8
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://www.baidu.com')
browser.find_element_by_class_name('s_ipt').send_keys('selenium')
time.sleep(3)
browser.refresh()
browser.get('http://www.taobao.com')
time.sleep(3)
browser.back()
print('现在又回到百度啦')
browser.find_element_by_link_text('hao123').click()
time.sleep(4)
browser.forward()
print('现在又回到淘宝啦。。。')

time.sleep(3)
print('下面开始设置浏览器的窗口大小')
browser.set_window_size(560,440)
time.sleep(5)
browser.get_screenshot_as_file('123.png')  #如果不注明路径，那么久默认保存到运行的文件夹路劲下，testcases
#browser.get_screenshot_as_file('C:\\Users\\Administrator\\\Desktop\\证件照片\\123.png')
browser.close()
browser.quit()
#12-31日看到58页