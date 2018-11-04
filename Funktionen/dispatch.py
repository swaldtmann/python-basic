#!/usr/bin/env python
# -*- coding: utf-8 -*-

def a():
    print("Funktion: Go")

def b():
    print("Funktion: Stop")

dispatch = {'go': a, 'stop': b}  # Note lack of parens for funcs

dispatch[input()]() 

