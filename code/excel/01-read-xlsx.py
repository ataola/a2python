#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import xlrd

file = './douban-250.xlsx'

data = xlrd.open_workbook(file)
table = data.sheets()[0]
# value = table.cell_value(rowx=4, colx=4)
row = []
for i in range(1, 251):
    for j in range(0, 6):
        row.append(table.cell_value(i, j))
    print(row)
    row = []
