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
#看下当前文件数量
counts = browser.find_elements_by_class_name('EOGexf')
print('当前列表文件数量是%s' % len(counts))


#进入分享
browser.find_element_by_link_text('分享').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="body"]/div/div/div/div[1]/div[1]/div[2]/div/ul/li/p[1]').click()
print('点击分享文件给我的用户')
time.sleep(3)
browser.find_element_by_xpath('//*[@id="body"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/ul/li[10]/div[3]/div[1]/div[4]/a[1]').click()
print('点击文件中的保存小按钮')
time.sleep(3)
#browser.find_element_by_xpath('//*[@id="body"]/div/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/ul[2]/li[1]/a').click()
#print('选中文件')
#time.sleep(3)
#browser.find_element_by_xpath('//*[@id="body"]/div/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[2]/a[1]/span[2]').click()
#print('点击保存')
#点击确定，保存至
browser.find_element_by_id('_disk_id_31').click()
print('点击确定')
time.sleep(5)
browser.find_element_by_link_text('网盘').click()
time.sleep(5)
new_counts = browser.find_elements_by_class_name('EOGexf')
print('现在列表文件数量是%s' % len(new_counts))
if len(new_counts) == len(counts) + 1:
    print('说明这个文件保存成功')
else:
    raise ValueError('文件没有保存成功')
print('关闭浏览器')
browser.close()
browser.quit()
print('终于搞定啦')