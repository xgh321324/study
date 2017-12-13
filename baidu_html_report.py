#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re
import HTMLTestRunner  #引入htmltestrunner的包
class Baidu(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(29)
        self.base_url ='https://www.baidu.com/?tn=93380420_hao_pg'
        self.accept_next_alert = True
        self.verificationErrors = []
    def testbaidu_search(self):
        #百度搜索用例
        browser = self.browser
        browser.get(self.base_url)
        browser.find_element_by_id('kw').send_keys('美貌的皮囊千篇一律，有趣的灵魂万里挑一')
        browser.find_element_by_id('su').click()
        time.sleep(4)
        #百度设置的用例
    def testbaidu_set(self):
        browser = self.browser
        browser.get(self.base_url)
        browser.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
        browser.find_element_by_link_text('搜索设置').click()
        time.sleep(2)
        s = Select(browser.find_element_by_xpath('//*[@id="nr"]'))
        s.select_by_value('50')
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
        alert = browser.switch_to.alert
        print(alert.text)
        alert.accept()
    def tearDown(self):
        self.browser.close()
        self.assertEqual([],self.verificationErrors)

#下面开始测试啦
if __name__ == '__main__':
    testunit=unittest.TestSuite()
    #将测试用例加入到测试容器中
    testunit.addTest(Baidu('testbaidu_search'))
    testunit.addTest(Baidu('testbaidu_set'))
    #定义个报告存放路径，支持相对路径
    filename = 'E:\\report.html'

    #定义测试报告
    with open(filename,'wb') as fn:
        runner = HTMLTestRunner.HTMLTestRunner(stream= fn,title = u'百度测试报告',description=u'用例执行情况',)
        runner.run(testunit)

