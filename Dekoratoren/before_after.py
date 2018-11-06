#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:
"""

def before_after(f):  
    def decorator():  
        print('before')  
        f()  
        print('after')  
    return decorator  

# # DO NOT DO THIS! This is the bad old way from before we had @!  
# def hello_world():  
#     print('Hello, world!')  
# hello_world = before_after(hello_world)  

@before_after  
def hello_world():  
    print('Hello, world!')

hello_world()
