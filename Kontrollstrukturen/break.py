#!/usr/bin/env python
# -*- coding: utf-8 -*-

count = 0

while count < 10:
    count += 1
    if count == 5:
        break
    print("in der while schleife", count)

print("ausserhalb der while schleife")
