#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" author: """

import random
n = 10

zu_findende_zahl = int(n * random.random()) + 1
print(zu_findende_zahl) # Debug Ausgabe

versuch = ''

while True:
    versuch = input("Neue Zahl: ")
    # print(versuch) # Debug Ausgabe
    if versuch == 'e':
        print("Programm vorzeitig beendet")
        break
    try:
        int_versuch = int(versuch)
    except:
        print("Falsche Eingabe! Nur Zahlen und der Buchstabe 'e' sind erlaubt!")
        continue
    if int_versuch < zu_findende_zahl:
        print("Ihre Zahl ist zu niedrig!")
    elif int_versuch > zu_findende_zahl:
        print("Ihre Zahl ist zu hoch!")
    elif int_versuch == zu_findende_zahl:
        print("Richtig geraten!")
        break
