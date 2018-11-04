#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    x = float(input("Zahl eingeben: "))
    inverse = 1.0 / x
except ValueError:
    print("Bitte Integer oder Fließkommazahl eingeben!")
except ZeroDivisionError:
    print("Unendlich")
finally:
    print("Es wurde eine ode auch keine Exception ausgeführt!")
