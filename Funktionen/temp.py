#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fahrenheit(T_in_celsius):
    """ gibt die Temperatur in  Grad Fahrenheit zurück"""
    return (T_in_celsius * 9 / 5) + 32

for t in (22.6, 25.8, 27.3, 29.8):
    print(t, ": ", fahrenheit(t))

