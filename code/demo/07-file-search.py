#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pathlib import Path

base_dir = '../demo'
keywords = '**/*address*'

# 遍历base_dir指向的目录下所有的文件
p = Path(base_dir)

# 当前目录下包含address的所有文件名称
files = p.glob(keywords)
# files的类型是迭代器
# 通过list()函数转换为列表输出
print(list(files))

# py结尾的文件
files2 = p.rglob('*.py')
print(list(files2))

# 遍历子目录和所有文件
files3 = p.glob('**/*')
print(list(files3))
