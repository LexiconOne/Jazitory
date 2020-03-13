# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:12:00 2020

@author: user
"""
a = 0
b = 1
c = b + a
print(a)
print(b)
while c < 1000:
    print(c)
    a = b
    b = c
    c = b + a