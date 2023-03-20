#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from multiprocessing import Pool


# 计算平方
def f(x):
    return x * x


def run():
    with Pool(8) as p:
        # 并行计算
        res = p.map(f, range(1, 101))
        print(f'计算平方的结果是:{res}')


if __name__ == '__main__':
    run()
