#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

test_str = "李雷的号码是13858176533，韩梅梅的手机号是15715860321"
pattern = r"1[3-9]\d{9}"

for phone in re.findall(pattern, test_str):
    print(phone)

# 精确的写法，但是如果号码段更改，正则也需要更改 1(?:3\d|4[5-9]|5[0-35-9]|6[2567]|7[0-8]|8\d|9[1389])\d{8}
