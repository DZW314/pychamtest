#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'DZW'
__mtime__ = '2019/6/26'
# code is far away from bugs with the god animal protecting
    I love animals. They are so funny. 
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃   *   ┃
            ┃ ┳┛ ┗┳ ┃
            ┃   ┻   ┃
            ┗━┓   ┏━┛
              ┃   ┗━━━┓
              ┃ Bless ┣┓
              ┃ NoBUG ┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""
import requests
url = 'https://res.333dm.com/images/comic/1/536/1539054282yC4_uWLvCogQ3-5v.jpg'
#header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
headers = {'Referer':'https://www.manhuadui.com/manhua/doupocangqiong/69098.html?p=1', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
r = requests.get(url, headers = headers)
#r.raise_for_status()

print('ok')
print(len(r.content))
with open('./1.jpg','wb') as code:
    code.write(r.content)
code.close()

# def download(img_url, img_name):
#     with closing(requests.get(img_url, stream=True)) as r:
