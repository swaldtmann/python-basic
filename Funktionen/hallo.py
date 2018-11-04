#!/usr/bin/env python
# -*- coding: utf-8 -*-


def Hallo(name="Leute"):
    """ Begrüßer """
    print("Hallo " + name + "!")


Hallo("Peter")
Hallo()

print("Der docstring der Funktion Hallo: " + Hallo.__doc__)
