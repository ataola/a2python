#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

# 粗糙版 \d{4}-\d{2}-\d{2}

# 日期
pattern = r'\d{4}-(?:1[0-2]|0?[1-9])-(?:[12]\d|3[01]|0?[1-9])'

# 24小时制
pattern_1 = r'(?:2[0-3]|1\d|0?\d):(?:[1-5]\d|0?\d):(?:[1-5]\d|0?\d)'

print(re.match(pattern, '2022-06-13'))

print(re.match(pattern_1, '12:12:12'))
