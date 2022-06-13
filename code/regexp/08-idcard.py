#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

pattern = r'[1-9]\d{14}(\d\d[0-9Xx])?'

print(re.match(pattern, '330821199706132266'))