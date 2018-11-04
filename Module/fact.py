#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:
"""


def fact(n):
    """ Fakultät des Parameter n
    """
    return 1 if n == 1 else n * fact(n-1)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))
