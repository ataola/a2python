#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：a2python
@File    ：b1001.py
@Author  ：ataola
"""

if __name__ == '__main__':
    num = input()
    num = int(num)
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = num >> 1
        else:
            num = (3 * num + 1) >> 1
        count = count + 1
    print(count)
