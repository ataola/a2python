#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime

today = datetime.date.today().strftime('%Y-%m-%d')
today_time = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
print('today:', today)
print('today_time:', today_time)
