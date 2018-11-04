#!/usr/bin/env python
# -*- coding: utf-8 -*-

def f(a,b,x,y):
  print(a,b,x,y)

t = (47,11)
d = {'x':'extract','y':'yes'}

f(*t, **d)

