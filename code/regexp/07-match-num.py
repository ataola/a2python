#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

# test case: 3，3.14，-3.3，+2.7

# 正数 负数 小数
pattern = r'[-+]?\d+(?:\.\d+)?'

print(re.match(pattern, '3.14'))
print(re.match(pattern, '3'))
print(re.match(pattern, '-3.3'))
print(re.match(pattern, '+2.7'))

# 非负整数，包含 0 和 正整数，可以表示成[1-9]\d*|0。
pattern_1 = r'[1-9]\d*|0'
print(re.match(pattern_1, '0'))
print(re.match(pattern_1, '1'))

# 非正整数，包含 0 和 负整数，可以表示成-[1-9]\d*|0。
pattern_2 = r'-[1-9]\d*|0'
print(re.match(pattern_2, '0'))
print(re.match(pattern_2, '-1'))

# 浮点数 -?\d+(?:\.\d+)?|\+?(?:\d+(?:\.\d+)?|\.\d+)
# 负数浮点数表示：-\d+(?:\.\d+)?。
# 正数浮点数表示：\+?(?:\d+(?:\.\d+)?|\.\d+)。
# 十六进制 [0-9A-Fa-f]+


