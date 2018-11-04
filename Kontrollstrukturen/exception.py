#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = 10
for y in [3, 0, 1]:
    try:
        z = x / y
    except:
        z = None
    print("z: ", z)
