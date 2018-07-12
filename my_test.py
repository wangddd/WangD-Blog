#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 0:00
# @Site    : 
# @File    : my_test.py
# @Software: PyCharm
__author__ = 'Wang Dong'


import logging
logging.basicConfig(level=logging.INFO)


logging('found model: %s (table: %s)' % ('111', '222'))
logging.info('found model: %s (table: %s)' % ('111', '222'))