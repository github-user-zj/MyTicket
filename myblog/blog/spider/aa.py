#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangjun'
__mtime__ = '2017/3/27'
   
"""
import json

data = [{'a':1,'b':2,'c':3, 'd' : 4, 'e' : 5 } ]
data02 = [{'a':1,'b':2,'c':3, 'd' : 4, 'e' : 5 } ]
data03 = data+data02

json = json.dumps(data03)
print type(json)
print json

ss = []

ss.append({"s":1})
print type(ss)
print ss

