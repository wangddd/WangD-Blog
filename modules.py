#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 12:46
# @Site    : 
# @File    : modules.py
# @Software: PyCharm
__author__ = 'Wang Dong'

import time, uuid

from orm import Model, StringField, BooleanField, TextField, FloatField

def next_id():
    return '%015d%s000' %(int(time.time() *1000), uuid.uuid4().hex)

123123