#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Modul mit wichtigen Funktionen zur Fibonacci-Folge """

def fib(n):
    """ Die Fibonacci-Zahl für die n-te 
Generation wird iterativ berechnet """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fiblist(n):
    """ produziert die Liste der Fibbo-Zahlen 
        bis zur n-ten Generation """
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]]
    return fib
