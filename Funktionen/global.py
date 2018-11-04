#!/usr/bin/env python
# -*- coding: utf-8 -*-

def f():
    global s
    print(s)
    s = "Hund"
    print(s) 
s = "Katze" 
f()
print(s)

