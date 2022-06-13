#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

test_str = '你叉叉， 穷哈哈，halibut骑着扫帚飞， sorry， sorry'
pattern = r'[\u4E00-\u9FFF]'
reg = re.compile(pattern)
print(re.findall(reg, test_str))
