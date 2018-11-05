#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:
"""


class Roboter:
    def __init__(self, name, baujahr):
        self._name = name
        self.__baujahr = baujahr
        print("__init__ von Roboter wurde ausgeführt")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_baujahr(self):
        return self.__baujahr

    def set_baujahr(self, baujahr):
        self.__baujahr = baujahr

if __name__ == "__main__":
    x = Roboter("Marvin", 1939)
    x.set_name("Bert")
    print(x.get_name())
    x.set_baujahr(1979)
    print(x.get_baujahr())
