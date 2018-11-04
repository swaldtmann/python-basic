#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" author: """


def fib(n):
    a, b, zaehler = 0, 1, 0
    while True:
        if (zaehler > n):
            return
        yield a
        a, b = b, a + b
        zaehler += 1


f = fib(15)

for x in f:
    print(x, " ", end="")

print()
