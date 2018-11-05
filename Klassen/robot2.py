#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:
"""


class Roboter:
    def __init__(self, name, baujahr):
        self.name = name
        self.baujahr = baujahr

    def SageHallo(self):
        print("Hallo, mein Name ist " + self.name)

if __name__ == "__main__":
    x = Roboter("Marvin", 1979)
    y = Roboter("Caliban", 1993)
    x.SageHallo()
    y.SageHallo()