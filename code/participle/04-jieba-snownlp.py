#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import jieba.posseg as psg
from snownlp import SnowNLP

text = "速度快，包装好，看着特别好，喝着肯定不错！价廉物美"
res = [(w.word, w.flag) for w in psg.cut(text)]
# 速度/快/，/包装/好/，/看着/特别/好/，/喝/着/肯定/不错/！/价廉物美

saved = ['a', 'l']
res_list = [x[0] for x in res if x[1] in saved]
print(res_list)
positive = 0
negtive = 0
for word in res_list:
    s2 = SnowNLP(word)
    if s2.sentiments > 0.7:
        positive += 1
    else:
        negtive += 1
    print(word, str(s2.sentiments))
print(f"正向评价数量:{positive}")
print(f"负向评价数量:{negtive}")
