# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:15:08 2020

@author: Oswaldo Ivann
"""
#Hacer un programa que sume desde una base hasta un limite

a = int(input("Ingrese el valor de base: "))
n = int(input("Ingrese el valor de limite: "))

def sumaab(a,n):
    if a == n:
        return n
    else:
        return a+sumaab(a+1, n)

    
print(sumaab(a,n))