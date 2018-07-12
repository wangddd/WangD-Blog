#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 1:26
# @Site    : 
# @File    : use_db.py
# @Software: PyCharm
__author__ = 'Wang Dong'

import orm
from orm import Model,IntegerField,StringField

import asyncio

user = 'root'
password='111111'
db='testdb'

class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()



async def test(loop, **kw):
    await orm.create_pool(loop=loop, user='root', password='111111', db='testdb')
    user = User(id=12, name='wangd5')
    await user.save()

# loop = asyncio.get_event_loop()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(test(loop))
loop.close()



