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
import bs4
import re

url_header = 'https://www.manhuadui.com/manhua/douluodalu/' #douluodalu/979.html?p=1
headers = {'Referer': url_header, 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
url = url_header + '979.html?p=2'
r = requests.get(url, headers = headers)
if r.status_code == 200:
    print("URL get OK.")
else:
    print(r.status_code)
print(url)
with open('./1.html', 'wb') as f:
    f.write(r.content)
f.close()
img_url = re.findall(r'id="images".*?src="(.*?)"', r.text,re.S)
print(img_url)

# with open('./1.jpg','wb') as code:
#     code.write(r.content)# code.close()
#
# r = requests.get("http://www.xiaohuar.com/v/")
# print(r.status_code)
# print(r.content)
# print(r.text)
# urls = re.findall(r'class="items".*?href="(.*?)"', r.text, re.S)
# url = urls[5]
# result = requests.get(url)
# mp4_url = re.findall(r'id="media".*?src="(.*?)"', result.text, re.S)[0]
# video = requests.get(mp4_url)
# with open('./a.mp4', 'wb') as f:
#     f.write(video.content)

# url = "https://www.manhuadui.com/manhua/haizeiwang/68856.html"
# headers = {'Referer': url, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
# r = requests.get(url)
# img_urls = re.findall(r'id="images".*?src=".*?"', r.text, re.S)
# print(img_urls)
# img_url = img_urls[0]
# img = requests.get(img_url, headers = headers)
# with open('./1.jpg', 'wb') as pic:
#     pic.write(img.content)
# pic.close()



# 正则表达式例子
# l = "This is a line. And go on...\nThis is another lin~e."
# a = re.findall(r'This.*?\.', l, re.M)
# print(l)
# for aa in a:
#     print(aa)
