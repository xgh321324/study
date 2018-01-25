#coding:utf-8from selenium import webdriverimport time,unittest'''#用下面的例子来看一下unitttest执行的顺序是怎样的class Oder(unittest.TestCase):    def setUp(self):        print('start..')    def test01(self):        print('执行测试用例1')    def test02(self):        print('执行测试用例02')    def test03(self):        print('执行测试用例3')    def tearDown(self):        print('end..')#由此可以看出unittest执行的顺序是每执行一个用例前和后都会执行一遍setup和teardown之中的内容#也就是测试的前置条件和后置条件，每条用例都会执行！'''class Blog(unittest.TestCase):    #前置条件    def setUp(self):        self.browser = webdriver.Chrome()        self.browser.maximize_window()        url = 'https://www.cnblogs.com/yoyoketang'        self.browser.get(url)        js1 = 'document.getElementById("blog_nav_admin").click();'        self.browser.execute_script(js1)        time.sleep(10)    #写一个公用的登录方法    def login(self,username,password):        #这里写了一个登录的方法,账号和密码参数化        self.browser.find_element_by_id('input1').send_keys(username)        self.browser.find_element_by_id('input2').send_keys(password)        self.browser.find_element_by_id('signin').click()        time.sleep(3)    #一个判断是否登录成功的方法    def is_success(self):        #判断是否获取到登录账户名称        try:            t = self.browser.find_element_by_xpath('//div[@id="blog_title"]/a').text            print(t)            return True        except Exception as e:            print(e)            return False    #测试用例1    def test01(self):        self.login('不过如此1951','xgh3213242016.')        R = self.is_success()        self.assertTrue(R)    #测试用例2    def test02(self):        self.login('不过如此1951','xgh3213242016.')        R = self.is_success()        self.assertTrue(R)    #资源回收    def tearDown(self):        self.browser.close()        self.browser.quit()if __name__ == '__main__':    unittest.main()