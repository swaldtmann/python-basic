#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:
"""
import os

# Ausgeben des aktuellen Arbeitsverzeichnisses
print(os.getcwd())
# Ändern des aktuellen Arbeitsverzeichnisses
os.chdir('/tmp')
# Ausführen des Kommandos mkdir in der Shell
os.system('mkdir Student13')
# Ausführen von ls in der Shell
os.system('ls')
