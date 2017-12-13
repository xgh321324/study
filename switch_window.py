#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
browser = webdriver.Chrome()
browser.maximize_window() #最大化
browser.get('http://www.baidu.com') #访问百度
time.sleep(3)
print(browser.current_window_handle)  #输出当前句柄(百度)看看
first_handle = browser.current_window_handle
#下面新开一个窗口，通过js新开窗口，访问搜狗
js = 'window.open("http://www.sogou.com")'
time.sleep(2)
browser.execute_script(js)
#print(browser.current_window_handle) #输出当前句柄（搜狗）

#再新开一个窗口，用js新开，然后访问有道
js1 = 'window.open("http://www.youdao.com/")'
browser.execute_script(js1)
time.sleep(4)
#print(browser.current_window_handle) #输出当前句柄（有道）

#输出句柄集合
handles = browser.window_handles
print('所有的窗口句柄：%s' % handles)

print('现在切换到搜狗')
#现在切换到搜狗
browser.switch_to.window(handles[1])#这里要注意一下，之前的switch_to_window不用了
browser.find_element_by_id("translateContent").send_keys("selenium")  #有道翻译selenium
browser.find_element_by_css_selector("button").click() #搜索
browser.find_element_by_css_selector('[class="close js_close"]').click() #关闭弹窗
browser.get_screenshot_as_file('C://Users//Administrator//Desktop//youdao.png') #保存截图
time.sleep(3)
browser.close()

print('现在切换到有道')
#现在切换到有道
browser.switch_to.window(handles[2])
browser.find_element_by_id("query").send_keys("selenium") #搜狗索索
browser.find_element_by_id("stb").click() #点击搜索
time.sleep(3)
browser.get_screenshot_as_file('C://Users//Administrator//Desktop//sougou.png') #保存截图
time.sleep(2)
browser.close()

print('现在切换到baidu')
#切换到百度
browser.switch_to.window(handles[0])
browser.find_element_by_id("kw").send_keys("selenium")  #百度搜索selenium
browser.find_element_by_id("su").click()
time.sleep(3)
browser.get_screenshot_as_file('C://Users//Administrator//Desktop//baidu.png')
time.sleep(3)
browser.close()
print('结束！！！保存成功')
browser.quit()


