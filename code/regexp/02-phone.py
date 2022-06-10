#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

test_str = "李雷的号码是13858176533，韩梅梅的手机号是15715860321"
pattern = r"1[3-9]\d{9}"

for phone in re.findall(pattern, test_str):
    print(phone)
