#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：a2python
@File    ：time-o.py
@Author  ：ataola
@Description ：O（1） < O（logn） < O（n） < O（nlogn） < O（n^2 ） < O（n^3 ）< O（2^n ） < O（n！） < O（n^n ）
"""

print('========O(1) Begin========')
print('Hello a2python')  # O(1)
print('========O(1) End==========')

n = 100

print('========O(n) Begin========')
for i in range(n):  # O(n)
    print(i)
print('========O(n) End==========')

print('========O(n^2) End==========')
for i in range(n):
    for j in range(n):
        print(i, j)
print('========O(n^2) End==========')

print('========O(n^3) End==========')
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
print('========O(n^3) End==========')
