# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 00:06:29 2020

@author: Oswaldo Ivann
"""

a=5
b=5

def resta(a,b):
    if b == 0:
        return a
    else:
        resta(a-1, b-1)
        
print(resta(a,b))