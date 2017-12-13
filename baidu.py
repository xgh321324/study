#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re

class Baidu(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(29)
        self.base_url = 'https://www.baidu.com/?tn=93380420_hao_pg'
        self.verificationErrors =[]
        self.accept_next_alert = True
    #百度搜索功能的测试用例
    def testbaidu_serach(self):
        '''百度搜索'''
        browser = self.browser
        browser.get(self.base_url)
        browser.find_element_by_id('kw').send_keys('慢慢的我们都变成了自己讨厌的那种人')
        time.sleep(2)
        browser.find_element_by_id('su').click()
        time.sleep(5)
    #百度搜索设置的测试用例
    def testbaidu_set(self):
        '''百度设置'''
        browser = self.browser
        browser.get(self.base_url)
        browser.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
        browser.find_element_by_link_text('搜索设置').click()
        time.sleep(3)
        s = Select(browser.find_element_by_xpath('//*[@id="nr"]'))
        s.select_by_value('50')
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
        alert = browser.switch_to.alert
        print('弹框提示的内容是:%s' % alert.text )
        alert.accept()
    #释放
    def tearDown(self):
        self.browser.close()
        self.assertEqual([],self.verificationErrors)
if __name__ == '__main__':
    unittest.main()

#baidu.py 文件编写了两条用例
