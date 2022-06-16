#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

# 粗糙版 \d{1,3}(\.\d{1,3}){3}

pattern = r'(?:0{0,2}\d|0?[1-9]\d|1\d\d|2[0-4]\d|25[0-5])(?:\.(?:0{0,2}\d|0?[1-9]\d|1\d\d|2[0-4]\d|25[0-5])){3}'

print(re.match(pattern, '192.168.1.1'))

# IPV6

# IPv6示例
# ABCD:EF01:2345:6789:ABCD:EF01:2345:6789
# 这种表示法中，每个X的前导0是可以省略的，例如：
# 2001:0DB8:0000:0023:0008:0800:200C:417A
# 上面的IPv6地址，可以表示成下面这样
# 2001:DB8:0:23:8:800:200C:417A
#
# 备注：这里不考虑0位压缩表示

# 前导匹配正则表达式：
# [0-9A-Fa-f]{4}(?:\:(?:[0-9A-Fa-f]{4})){7}

# 省略前导0正则表达式：
# (?:0|[1-9A-Fa-f][0-9A-Fa-f]{0,3})(?:\:(?:0|[1-9A-Fa-f][0-9A-Fa-f]{0,3})){7}