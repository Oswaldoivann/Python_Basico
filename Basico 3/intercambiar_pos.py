# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:07:33 2020

@author: Oswaldo Ivann
"""

def intercambiar_pos(lista, n, r):
    temporal = lista[n]
    lista[n] = lista[r]
    lista[r] = temporal
    return lista