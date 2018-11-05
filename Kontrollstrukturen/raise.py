#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: ", err)
except ValueError:
    print("Could not convert data to integer.")
    raise
except:
    print("Unexpected error!")
    raise
