# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:08:01 2020

@author: Oswaldo Ivann
"""

def sumacuadrados(a,b):
    if a == b:
        return a*b
    else: 
        return a*a + sumacuadrados()