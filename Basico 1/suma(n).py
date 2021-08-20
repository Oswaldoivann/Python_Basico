# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 00:39:06 2020

@author: Oswaldo Ivann
"""

n = int(input("Ingrese el valor de la Suma: "))

def Suma(n):
    if n == 0:
        return 0
    else:
        return n + Suma(n - 1)
    
print(Suma(n))