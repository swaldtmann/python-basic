#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" author: """

print("(1) Umrechnung von Celsius nach Kelvin")
print("(2) Umrechnung von Celsius nach Fahrenheit")

wahl = input("Bitte wählen: ")

if wahl == "1":
    celsius = float(input("Temperatur in Celsius: "))
    if celsius >= -273.15:
        kelvin = celsius + 273.15
        print(celsius, "° = ", kelvin, "K", sep = "")
    else:
        print("Fehler: unmögliche Temperatur!")
elif wahl == "2":
    celsius = float(input("Temperatur in Celsius: "))
    if celsius >= -273.15:
        fahrenheit = 32.0 + 1.8*celsius
        print(celsius, "° = ", fahrenheit, "F", sep = "")    
    else:
        print("Fehler: unmögliche Temperatur!")   
else:
    print("Falsche Eingabe!")    
