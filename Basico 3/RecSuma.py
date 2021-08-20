# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:26:53 2020

@author: Oswaldo Ivann
"""

lista = [1, 2, 3, 4, 5]
def recsuma(lista):
    if len(lista)==0:
        return 0
    else:
        return lista[-1]+recsuma(lista[:-1])
