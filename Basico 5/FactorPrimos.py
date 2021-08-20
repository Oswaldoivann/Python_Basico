# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 23:53:53 2020

@author: Oswaldo Ivann
"""


def lista_vacia():
    return []
def car(lista):
    return lista[0]
def cdr(lista):
    return lista[1:]


def miembro(lista, item):
    if lista == lista_vacia:
        return False
    if lista[0] == item:
        return True
    else:
        return miembro(cdr(lista), item)