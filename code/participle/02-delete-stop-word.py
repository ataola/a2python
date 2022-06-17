#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import jieba

text = "速度快，包装好，看着特别好，喝着肯定不错！价廉物美"
tmp = jieba.cut(text)
res = list(tmp)
print("/".join(res))
# 速度/快/，/包装/好/，/看着/特别/好/，/喝/着/肯定/不错/！/价廉物美

stop_words = ["，", "！"]
res_list = [x for x in res if x not in stop_words]
print(res_list)
# ['速度', '快', '包装', '好', '看着', '特别', '好', '喝', '着', '肯定', '不错', '价廉物美']
