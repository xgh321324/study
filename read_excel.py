#coding:utf-8import xlrdfrom selenium import webdriverimport time,unittestdata = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\testdata.xlsx')  #打开表格table = data.sheet_by_name('Sheet1')  #获取哪个sheet的数据hang = table.nrows   #获取行的数量lie = table.ncols  #获取所有列的数量print('所有的列数是：%s' % lie)print('所有行的数量是：%s'% hang)col_values = table.col_values(0)  #获取第一列的值row_values = table.row_values(0) #获第一行的值print('第一行的值是：%s' % row_values)print('第一列的值是：%s' % col_values)