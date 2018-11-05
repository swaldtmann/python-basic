#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:
"""


class Roboter:
    def __init__(self, name, baujahr):
        self._name = name
        self.__baujahr = baujahr


if __name__ == "__main__":
    x = Roboter("Marvin", 1979)
    print(x._name)
    print(x.__baujahr)
