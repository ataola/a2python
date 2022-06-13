#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

pattern = r'(?<!\d)\d{6}(?!\d)'

print(re.match(pattern, '312000'))
