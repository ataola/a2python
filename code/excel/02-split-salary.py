#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import xlrd
import xlwt

"""
Problem: 对工资表按照个人进行拆分，然后批量保存为按照员工姓名命名新的独立表格
"""

# 定义读取和写入excel的目录
src_path = './工资单.xlsx'
dst_path = './salary'

# 打开读取的工资单excel表格
r_workbook = xlrd.open_workbook(src_path)
table = r_workbook.sheets()[0]

# 获取表头
table_header = table.row_values(rowx=0)
# print(table_header)

# 获取表格总行数
employee_num = table.nrows


# 写入文件的方法
def write_2_file(name, items):
    w_workbook = xlwt.Workbook(encoding='utf-8')
    w_sheet = w_workbook.add_sheet('个人工资')

    row = 0
    col = 0

    # 写入表头
    for cell_header in table_header:
        w_sheet.write(row, col, cell_header)
        col += 1

    row += 1

    # 写入数据
    col = 0
    for item in items:
        w_sheet.write(row, col, item)
        col += 1
    w_workbook.save(f'./salary/{name}.xlsx')


for line in range(1, employee_num):
    # 获取对应行数据内容
    content = table.row_values(rowx=line, start_colx=0, end_colx=None)
    write_2_file(name=content[1], items=content)
