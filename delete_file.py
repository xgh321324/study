#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://pan.baidu.com/')
browser.find_element_by_link_text('帐号密码登录').click()
time.sleep(2)
browser.find_element_by_id('TANGRAM__PSP_4__userName').clear()
browser.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('不过如此1951')
time.sleep(2)
browser.find_element_by_id('TANGRAM__PSP_4__password').clear()
browser.find_element_by_id('TANGRAM__PSP_4__password').send_keys('xgh3213242016.')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__submit"]').submit()
time.sleep(2)
now_user = browser.find_element_by_xpath('//*[@id="dynamicLayout_0"]/div/div/dl/dd[2]/span/span[2]').text    #.text是获取该位置的文本
if now_user == '不过如此1951':
    print('登录成功啦')
else:
    raise NameError('username Error')
#显示当前列表数量
time.sleep(3)
counts = browser.find_elements_by_class_name('EOGexf')
print('当前页列表数量是%s' % len(counts))
#browser.find_element_by_link_text('检验师').click()
right = browser.find_elements_by_xpath('//*[@id="layoutMain"]/div/div/div/div[2]/div/div/div[3]/div/div/dd[7]/div[2]/div[1]')
time.sleep(3)
ActionChains(browser).context_click(right).perform() #右键点击要删除的文件
time.sleep(3)
sreach_window=browser.current_window_handle #方法：获得当前最后的窗口 这个方法很重要，如果元素定位没问题还是提示找不到元素，那么很可能窗口变了

time.sleep(2)
browser.find_element_by_xpath('//*[@id="layoutMain"]/div/div[1]/div[2]/div[4]/div[4]/a[7]/span/span').click() #点击删除
time.sleep(3)
browser.find_element_by_xpath('//*[@id="confirm"]/div[3]/a[1]/span').click() #确定删除
time.sleep(4)
new_counts = browser.find_elements_by_class_name('EOGexf')
print('现在的列表数量是%s' % len(new_counts))
if len(counts)- len(new_counts) == 1:
    print('说明现在删除成了！！')
else:
    raise ValueError('删除失败')

#下面再添加一个文件
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

print('关闭浏览器')
browser.close()
browser.quit()
