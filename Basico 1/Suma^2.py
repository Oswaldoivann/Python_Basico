# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 00:21:16 2020

@author: Oswaldo Ivann
"""

#Realizar una serie que suma n^2

n = int(input("Ingresa el valor de n: "))

def SumaCuadrado(n):
    if n == 1:
        return 1
    else:
        return n*n + SumaCuadrado (n - 1)
    
print (SumaCuadrado(n))
