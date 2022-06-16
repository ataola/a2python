#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pathlib import Path, PurePath


def read_dir(file_path):
    p = Path(file_path)
    files = [file for file in p.iterdir()]
    print(files)


if __name__ == '__main__':
    read_dir('../')
