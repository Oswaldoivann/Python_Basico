# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:20:42 2020

@author: Oswaldo Ivann
"""
lista = [1, 2, -3, 4, 5]

def recnegativo(lista):
    if lista[-1] < 0:
        return True
    else:
        return recnegativo(lista[:-1])

print (recnegativo(lista))