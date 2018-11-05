#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:
"""


from datetime import date
now = date.today()
print(now)

print(now.strftime("%d.%m.%y ist der %d. Tag des %B"))
