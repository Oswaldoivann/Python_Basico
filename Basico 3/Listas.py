# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:21:12 2020

@author: Oswaldo Ivann
"""

#Una lista de valores Alfanumericos deberan ser ingresado con comillas
Lista=['a', 'b', 'c', 'd', 'e']

#1 - Agragando un valor al final de la lista
Lista.append('z')

#2 - Agregando una lista a una lista
Lista.extend(['x', 'y', 'w'])

#3 - Incertar un elemento (h) por el indice indicado [0] de un lista
Lista.insert(0, 'h')

#4 - Remover y regresar el elemento al final de la lista
Lista.pop()

#5 - Remover y regresar el elemento que esta en la posicion 0 de una lista
Lista.pop(0)