#coding:utf-8from selenium import webdriverimport time#xpath 看成是元素定位界的屠龙刀。武林至尊，宝刀 xpath，css 不出，#谁与争锋browser = webdriver.Chrome()browser.maximize_window()browser.get('http://www.baidu.com')time.sleep(2)#xpath的模糊匹配功能 重点掌握contains的格式以及用法#browser.find_element_by_xpath('//*[contains(text(),"hao123")]').click()   #就是说包含hao123这个文本内容的#time.sleep(3)#xpath也可以模糊匹配某个属性#browser.find_element_by_xpath("//*[contains(@id,'kw')]").send_keys('不悔入华夏，再生种花家')#time.sleep(5)#xpath还可以模糊匹配以什么属性开头#browser.find_element_by_xpath('//*[start-with(@id,"s_kw_")]').click()#xpath还支持最强大的正则表达式匹配browser.find_element_by_xpath("//*[matchs(text(),'hao123')]").click()   #这句不知道为啥，有问题定位不到time.sleep(3)browser.close()browser.quit()