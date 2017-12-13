#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://pan.baidu.com/')
browser.find_element_by_link_text('帐号密码登录').click()
time.sleep(3)
browser.find_element_by_id('TANGRAM__PSP_4__userName').clear()
browser.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('不过如此1951')
time.sleep(4)
browser.find_element_by_id('TANGRAM__PSP_4__password').clear()
browser.find_element_by_id('TANGRAM__PSP_4__password').send_keys('xgh3213242016.')
time.sleep(4)
browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__submit"]').submit()
time.sleep(5)
now_user = browser.find_element_by_xpath('//*[@id="dynamicLayout_0"]/div/div/dl/dd[2]/span/span[2]').text    #.text是获取该位置的文本
if now_user == '不过如此1951':
    print('登录成功啦')
else:
    raise NameError('username Error')
#退出
target = browser.find_element_by_xpath('//*[@id="dynamicLayout_0"]/div/div/dl/dd[2]/span/i')
ActionChains(browser).move_to_element(target).perform()
time.sleep(3)
target2 = browser.find_element_by_xpath('//*[@id="dynamicLayout_0"]/div/div/dl/dd[2]/span/dl/dd/ul/li[4]/a')
time.sleep(4)
print('找到退出按钮了，开点击退出')
ActionChains(browser).move_to_element(target2).click()
print('点击退出')
print('退出成功，关闭浏览器')
browser.close()
browser.quit()
