#!/usr/bin/env python
# -*- coding: utf-8 -*-

count = 0
 
while count < 10:
    count += 1
    if count % 2 == 0:
           continue
    print(count, end=" ")
