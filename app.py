#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 22:53
# @Site    : 
# @File    : app.py
# @Software: PyCharm
__author__ = 'Wang Dong'

import logging;
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>This is Wangd-blog!</h1>', content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '99.1.1.1', 80)
    logging.info('server start at httpd 99.1.1.1 on port 80...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
