#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 23:25
# @Site    : 
# @File    : orm.py.py
# @Software: PyCharm
__author__ = 'Wang Dong'

import logging, aiomysql
logging.basicConfig(level=logging.INFO)


async def create_pool(loop, **kw):
    logging('create database conntion pool')
    global __pool
    __pool = await aiomysql.create_pool(
        host = kw.get('host'),
        port = kw.get('port'),
        user =
    )









