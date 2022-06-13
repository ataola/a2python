#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

print(re.match(pattern, 'mahuateng@qq.com'))
