#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

pattern = r'[1-9][0-9]{4,9}'

print(re.match(pattern, '1445749400'))
