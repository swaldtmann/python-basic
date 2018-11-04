#!/usr/bin/env python
# -*- coding: utf-8 -*-

def nimmt_alles(benoetigt, *args, **kwargs):
    # Benötigter Parameter
    print(benoetigt)
    # tuple von allen variablen Parametern
    print(args)

    # dictionary aller Schlüsselwortparameter
    print(kwargs)

nimmt_alles("muss", 12, "kann", a="Keyword")

