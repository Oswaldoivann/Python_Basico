# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 00:00:29 2020

@author: Oswaldo Ivann
"""

a=2
b=5

def add(a,b):
    if a == 0:
        return  b
    else:
        return (a-1, b+1)

print(add(a,b))