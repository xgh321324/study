#coding:utf-8from selenium import webdriverfrom selenium.webdriver.support.select import Selectimport time# 配置文件地址profile_directory = r'C:\Users\Administrator\AppData\Local\Temp\rust_mozprofile.eQE65jHikbWU'#字符串前面加 r，使用字符串原型# 加载配置配置profile = webdriver.FirefoxProfile(profile_directory)# 启动浏览器配置browser = webdriver.Firefox(profile)browser.get('file:///C:/Users/Administrator/Desktop/table.html')browser.maximize_window()time.sleep(4)#现在我要定位第二行seleniu自动化 用xpathbrowser.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[2]/td[1]').click()print('定位成功')#打印单元格中的内容t = browser.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[2]/td[1]')print('单元格中的内容是：%s' % t.text)#browser.close()#browser.quit()