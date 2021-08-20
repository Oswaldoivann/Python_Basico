# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 00:29:47 2020

@author: Oswaldo Ivann
"""

#Realizar una serie que suma n^3 

n = int(input("Ingresa el valor de n: "))

def SumaCubo(n):
    if n == 1:
        return 1
    else:
        return n*n*n + SumaCubo (n - 1)
    
print (SumaCubo(n))