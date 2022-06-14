#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import xlrd
import xlwt


# 获取表格
def get_table(src_path):
    data = xlrd.open_workbook(src_path)
    table = data.sheets()[0]
    return table


# 写入文件
def write_2_file(filename, items):
    w_workbook = xlwt.Workbook(encoding='utf-8')
    w_sheet = w_workbook.add_sheet(filename)
    row, col = 0, 0
    for header_field in items[0]:
        w_sheet.write(row, col, header_field)
        col += 1
    row += 1
    col = 0
    for cell_value in items[1]:
        w_sheet.write(row, col, cell_value)
        col += 1
    w_workbook.save(f'./salary/{filename}.xlsx')


# 拆分excel文件
def split_excel(src_path):
    table = get_table(src_path)
    employee_num = table.nrows
    table_headers = table.row_values(rowx=0, start_colx=0, end_colx=None)
    for line in range(1, employee_num):
        content = table.row_values(rowx=line, start_colx=0, end_colx=None)
        tmp_list = [table_headers, content]
        write_2_file(filename=content[1], items=tmp_list)


if __name__ == '__main__':
    split_excel('./工资单.xlsx')
