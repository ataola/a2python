#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

test_str1 = '11abcd'
test_str2 = '1a2b3c'
pattern = r'^((?!\d\d)\w){6}$'

print(re.match(pattern, test_str1))
print(re.match(pattern, test_str2))
