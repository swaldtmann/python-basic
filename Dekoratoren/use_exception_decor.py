#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
URL: https://www.blog.pythonlibrary.org/2016/06/09/python-how-to-create-an-exception-logging-decorator/
"""

from exception_decor import exception
 
@exception
def zero_divide():
    1 / 0
 
if __name__ == '__main__':
    zero_divide()
