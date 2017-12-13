#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import unittest,time,re
class Youdao(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(29)
        self.base_url = 'http://www.youdao.com/'
        self.verificationErrors = []
        self.accept_next_alert = True
    #有道搜索的测试用例
    def testyoudao_search(self):
        '''有道搜索'''
        browser = self.browser
        browser.get(self.base_url)
        browser.find_element_by_xpath('//*[@id="translateContent"]').send_keys('这可能就是生活吧')
        browser.find_element_by_xpath('//*[@id="form"]/button').click()
        time.sleep(4)
    #释放
    def tearDown(self):
        self.browser.close()
        self.assertEqual([],self.verificationErrors)
#测试
if __name__ == '__main__':
    unittest.main()

#youdao.py 文件中编写一条用例

