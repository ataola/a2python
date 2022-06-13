#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

test_str = 'the little cat cat is in the hat hat hat, we like it.'
res = re.sub(r"(\w+)(\s+\1)+", r"\1", test_str)
print(res)
