#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import jieba.posseg as psg

text = "速度快，包装好，看着特别好，喝着肯定不错！价廉物美"
res = [(w.word, w.flag) for w in psg.cut(text)]
# 保留形容词
saved = ['a', 'l']
res_list = [x for x in res if x[1] in saved]
print(res_list)
# [('快', 'a'), ('好', 'a'), ('好', 'a'), ('不错', 'a'), ('价廉物美', 'l')]
