#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" author: """

umsaetze = [('John', 'Miller', 46, 18.67),
            ('Randy', 'Steiner', 48, 27.99),
            ('Tina', 'Baker', 53, 27.23),
            ('Andrea', 'Baker', 40, 31.75),
            ('Eve', 'Turner', 44, 18.99),
            ('Henry', 'James', 50, 23.56)]

print("Sortiert nach Verkaufserlöse:")
for i in sorted(umsaetze, key=lambda x: x[2] * x[3]):
    print(i)

print("\nSortiert nach Nachname und Vorname:")
for i in sorted(umsaetze, key=lambda x: x[1] + x[0]):
    print(i)
