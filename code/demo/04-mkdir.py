#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

file_path = './aaa/bbb/ccc'

if os.path.isdir(file_path):
    print(file_path)
else:
    os.makedirs(file_path)
    print('create directory success!')
