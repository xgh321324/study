#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://sahitest.com/demo/selectTest.htm')
time.sleep(3)
s1 = Select(browser.find_element_by_id('s1Id'))    #先将Select类进行实例化
s1.select_by_index(1)   #用索引值--记住是从0开始
print('已经选择第二个选项')
time.sleep(3)
s1.select_by_value('o2')
time.sleep(3)         #用value属性
print('已经选择第三个选项')
s1.select_by_visible_text('o3')    #用标签中的文本
print('已经选择第四个选项')
time.sleep(5)
#下面查看所有的选项
for select in (s1.options):
    print(select.text)
print('===========================')
s4 = Select(browser.find_element_by_id('s4Id'))
s4.select_by_index(1)
time.sleep(3)
s4.select_by_value('o3val')
time.sleep(3)
s4.select_by_visible_text('    With spaces')
time.sleep(3)
for select in (s4.all_selected_options):
    print(select.text)
time.sleep(3)
s4.deselect_all()   #全不选
time.sleep(3)
browser.close()
browser.quit()

'''
总结

Select提供了三种选择方法：

select_by_index(index) ——通过选项的顺序，第一个为 0
select_by_value(value) ——通过value属性
select_by_visible_text(text) ——通过选项可见文本
同时，Select提供了四种方法取消选择：

deselect_by_index(index)
deselect_by_value(value)
deselect_by_visible_text(text)
deselect_all()
此外，Select提供了三个属性方法给我们必要的信息：

options ——提供所有的选项的列表，其中都是选项的WebElement元素
all_selected_options ——提供所有被选中的选项的列表，其中也均为选项的WebElement元素
first_selected_option ——提供第一个被选中的选项，也是下拉框的默认值
'''