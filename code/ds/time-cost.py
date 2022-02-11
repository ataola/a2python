#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：a2python 
@File    ：time-cost.py
@Author  ：ataola
'''

from timeit import Timer


def test_o1():
    print('Hello a2python')


def test_on():
    n = 1000000
    my_list = []
    for i in range(n):
        my_list = my_list + [i]


def test_on2():
    n = 1000000
    my_list = []
    for i in range(n):
        for j in range(n):
            tmp = [i] + [j]
            my_list = my_list + tmp


def test_on3():
    n = 1000000
    my_list = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp = [i] + [j] + [k]
                my_list = my_list + tmp


t_o1 = Timer("test_o1", "from __main__ import test_o1")
print("test_o1: ", t_o1.timeit(number=1000), "seconds")

t_on = Timer("test_on", "from __main__ import test_on")
print("test_on: ", t_on.timeit(number=1000), "seconds")

t_on2 = Timer("test_on2", "from __main__ import test_on2")
print("test_on2: ", t_on2.timeit(number=1000), "seconds")

t_on3 = Timer("test_on3", "from __main__ import test_on3")
print("test_on3: ", t_on3.timeit(number=1000), "seconds")