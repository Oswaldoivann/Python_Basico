# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 22:52:35 2020

@author: Oswaldo Ivann
"""
'''

Es programa nos manda un lista con todos los numeros
que los divide el No. ingresado
'''
n = int(input("Ingrese el numero para saber quienes lo pueden dividir: "))

resultados = []

for k in range (1, n+1):
    if n % k == 0:
        resultados.append(k)
        
print(resultados)