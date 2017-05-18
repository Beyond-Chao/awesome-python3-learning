# coding=utf-8

'url handlers'

import re, time, json, logging, hashlib, base64, asyncio

from coreweb import get, post

from models import User, Blog, Comment, next_id

@get('/')
async def index(request):

    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200),
        Blog(id='3', name='Python WebService', summary=summary, created_at=time.time() - 700)

    ]

    # users = await User.findAll()
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }

@get('/api/users')
async def api_get_users():
    users = await User.findAll()
    for u in users:
        u.passwd = '123456'
    return dict(users=users)