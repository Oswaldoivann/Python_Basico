# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:10:39 2020

@author: Oswaldo Ivann
"""
#Definimos la funcion que ordenara la lista de menor a mayor
def ordena(L):
#Declaramos una lista vacia en la que se reordenaran los valores    
    ordenado = []
#El bucle For recorrera la lista que sera ordenada
    for i in range(len(L)):
#Declaramos el mas pequeño con nuestro algoritmo mas_peque de la lista
        maspeque = mas_peque(L)
#Agregamos a la lista vacia el mas pequeño elimando los demas valores
        ordenado.append(L.pop(maspeque))
#Nos regresara la lista ordenada una vez termindado el Bucle For
    return ordenado