# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 23:47:48 2020

@author: Oswaldo Ivann
"""
#Funcion de Potencia: a^b = a_1 * a_2 * ..... a_b

a = int(input("Ingresa el numero base: "))
b = int(input("¿Cual es la potencia?"))

def potencia(a, b):
    if b == 0:
        return 1
    if a == 0:
        return 0
    if b == 1:
        return a
    else:
        return a * potencia(a, b-1)
    
print(potencia(a, b))