#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" author: """


def reverse(daten):
    for index in range(len(daten)-1, -1, -1):
        yield daten[index]


for zeichen in reverse('golf'):
    print(zeichen)
