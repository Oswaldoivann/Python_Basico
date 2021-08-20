# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:29:31 2020

@author: Oswaldo Ivann
"""
def intercambiar_pos(lista, n, r):
    temporal = lista[n]
    lista[n] = lista[r]
    lista[r] = temporal
    return lista


def bubbleSort(L):
    for i in range(len(L)):
        for i in range(len(L)-1, i, -1):
            if (L[i-1] > L[i]):
                intercambiar_pos(L, i-1, i)
        else:
             return L