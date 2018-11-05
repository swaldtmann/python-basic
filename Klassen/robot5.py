#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:
"""

from robot import Roboter

class SteampunktRobot(Roboter):
    def __init__(self, name, baujahr, vorrat_feuerholz=0):
        Roboter.__init__(self, name, baujahr)
        self.vorrat_feuerholz = vorrat_feuerholz
        print("__init__ von SteampunktRobot wurde ausgeführt")

if __name__ == "__main__":
    x = SteampunktRobot("Spider", 2010, 43)
    print(x.get_name())
    print(x.get_baujahr())
    print(x.vorrat_feuerholz)
