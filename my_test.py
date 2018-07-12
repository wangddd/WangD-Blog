#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 0:00
# @Site    : 
# @File    : my_test.py
# @Software: PyCharm
__author__ = 'Wang Dong'

import time, uuid



print('%015d' % int(time.time() *1000))
print('%s000' % uuid.uuid4().hex)