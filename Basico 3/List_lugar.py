# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:50:53 2020

@author: Oswaldo Ivann
"""

L = list(range(10))

def intercambiar_pos(L, n, r):
    temporal = L[n]
    L[n] = L[r]
    L[r] = temporal
    return L

intercambiar_pos(L, 0, 9)

print(intercambiar_pos())
