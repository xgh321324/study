#coding:utf-8from selenium import webdriverimport timebrowser = webdriver.Chrome()browser.maximize_window()browser.get('https://www.baidu.com/?tn=22073068_5_oem_dg')time.sleep(4)#通过js修改target属性js = 'document.getElementsByClassName("mnav")[0].target="";'  #分号用于一个js语句的结束，且这里的elements是复数browser.execute_script(js)time.sleep(3)#修改属性后然后点击t = browser.find_elements_by_xpath('//*[contains(@class,"mnav")]')t[0].click()print('点击新闻按钮，在原来窗口打开')browser.close()browser.quit()