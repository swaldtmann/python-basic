#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" author: """

# Wir definieren die Konstanten, die wir brauchen,
# um die Temperaturen umzurechnen.
ABSOLUTER_NP_C = -273.15  # absoluter Nullpunkt in Celsius

NULL_F = 32.0             # 0° C in Fahrenheit
FAKTOR_F_C = 9/5          # Umrechnungsfaktor zwischen Fahrenheit und Celsius

# Fehlermeldung für ungültige Eingabe
FEHLERMELDUNG_TEMP = "*** Fehler: unmögliche Temperatur! ***"


def get_float(msg="Bitte Zahl eingeben: "):
    while True:
        try:
            f = float(input(msg))
            return f
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")


def Celsius_Kelvin(t):
    if t >= ABSOLUTER_NP_C:
        return t - ABSOLUTER_NP_C
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)


def Celsius_Fahrenheit(t):
    if t >= ABSOLUTER_NP_C:
        return NULL_F + FAKTOR_F_C*t
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)


print()
print("*----------------------*")
print("* Temperatur Umwandler *")
print("*----------------------*")

wahl = -1
while wahl != 0:
    print()
    print("(1) Umrechnung von Celsius nach Kelvin")
    print("(2) Umrechnung von Celsius nach Fahrenheit")
    print()
    print("(0) Programm schliessen")
    print()
    print()
    wahl = int(input("Bitte wählen: "))
    print()
    if wahl == 1:
        t = get_float("Temperatur in Celsius: ")
        print(t, "° = ", Celsius_Kelvin(t), "K", sep="")
    elif wahl == 2:
        t = get_float("Temperatur in Celsius: ")
        print(t, "° = ", Celsius_Fahrenheit(t), "F", sep="")
    else:
        print("Programm wird vom Benutzer beendet.")
        break
