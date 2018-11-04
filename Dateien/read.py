#!/usr/bin/env python
# -*- coding: utf-8 -*-

fobj = open("lorem_ipsum.txt")
for line in fobj:
    # Ausgabe aller Zeilen, ohne Leerzeichen am Ende der Zeile
    print(line.rstrip())
fobj.close()
