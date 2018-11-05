#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:
"""

class Roboter:
    def __init__(self, name, baujahr):
        self._name = name  # protected Attribut
        self.__baujahr = baujahr  # Dies ist ein private Attribut, das nicht von aussen gelesen werden kann.

    def get_baujahr(self):
        return self.__baujahr

    def set_baujahr(self, baujahr):
        self.__baujahr = baujahr


if __name__ == "__main__":
    x = Roboter("Marvin" , 1939 )
    print(x.get_baujahr())
    x.set_baujahr(1979)
    print(x.get_baujahr())
