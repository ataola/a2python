#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

test_str = 'we found “the little cat” is in the hat, we like “the little cat”'

# 10 matches, 111 steps, 0.3ms
# pattern = r'(“.+?”|\w+)'

# 12 matches, 59 steps, 0.1ms
pattern = r'\w+|“[^”]+”'

for word in re.findall(pattern, test_str):
    print(word)
