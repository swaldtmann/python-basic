#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:
"""

liste1 = []
for zeichen in 'Berlin':
    liste1.append(zeichen)
print(liste1)

liste2 = []
liste2 = [ zeichen for zeichen in 'Berlin' ]
print(liste2)