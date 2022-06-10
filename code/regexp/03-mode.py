#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import regex

test_str = 'aaabb'
# 贪婪模式
print(re.findall(r'a*', test_str))
# 非贪婪模式
print(re.findall(r'a*?', test_str))

test_str2 = '"lilei is me", emmmmm, "hanmeimei is her"'
# 贪婪模式
print(re.findall(r'".*"', test_str2))
# 非贪婪模式
print(re.findall(r'".*?"', test_str2))

test_str3 = 'xyyz'
# 贪婪模式
print(regex.findall(r'xy{1,3}z', test_str3))

# 独占模式
print(regex.findall(r'xy{1,3}+z', 'xyyz'))

# 独占模式
print(regex.findall(r'xy{1,2}+yz', 'xyyz'))
