#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:
"""
import os
import sys

basis_verzeichnis = '.'

if len(sys.argv) > 1:
    basis_verzeichnis = sys.argv[1]

for folder in os.listdir(basis_verzeichnis):
    print (folder)