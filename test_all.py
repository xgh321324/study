#coding:utf-8
import unittest
import baidu,youdao  #导入需要测试的测试用例
import HTMLTestRunner
import time

suite = unittest.TestSuite()  #实例化

#再将测试用例加入到测试容器中
suite.addTest(unittest.makeSuite(baidu.Baidu))  #baidu:模块名  Baidu：类的名称
suite.addTest(unittest.makeSuite(youdao.Youdao))

'''
#执行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)
'''
#要想在报告前加上该报告的时间要做如下操作：
now_time = time.strftime('%Y-%m-%d %H_%M_%S',time.localtime())   #格式化时间这里只有这样才不会报错   （时间的模板需要用下划线或横杠，加空格或冒号时编译器就会报错，这句话是网上说法）
filedir ="E:\\Test_Report\\"+now_time+' all_report.html'      #这里格式容易写错，要注意
with open(filedir,'wb') as fd:
    runner = HTMLTestRunner.HTMLTestRunner(stream=fd,title='百度和有道共三个用例的报告：',description='用例执行情况')
    runner.run(suite)
#下面我要生成报告啦html的报告


