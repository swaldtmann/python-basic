#!/usr/bin/env python
# -*- coding: utf-8 -*-


def abc_generator():
    yield("a")
    yield("b")
    yield("c")


for el in abc_generator():
    print(el)
