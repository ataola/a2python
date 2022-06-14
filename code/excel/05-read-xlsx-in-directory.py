#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pathlib import Path, PurePath

src_path = './survey'

p = Path(src_path)
files = [x for x in p.iterdir() if PurePath(x).match('*.xlsx')]
# [WindowsPath('survey/李雷.xlsx'), WindowsPath('survey/调查问卷模版.xlsx'), WindowsPath('survey/韩梅梅.xlsx')]
print(files)
