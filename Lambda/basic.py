#!/usr/bin/env python
# -*- coding: utf-8 -*-

for i in range(10):
    print((lambda x: x + 42)(i), end=' ')

print()

f42 = lambda x: x + 42
print(f42(4))
