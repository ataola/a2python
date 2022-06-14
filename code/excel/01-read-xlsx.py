#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import xlrd

file = './douban-250.xlsx'

data = xlrd.open_workbook(file)
table = data.sheets()[0]
for i in range(1, 251):
    print(table.row_values(rowx=i))
