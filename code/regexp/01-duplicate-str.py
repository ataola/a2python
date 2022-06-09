#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

test_str = "the little cat cat in the hat hat."
# 'the little cat in the hat.'
print(re.sub(r'(\w+) \1', r'\1', test_str))
