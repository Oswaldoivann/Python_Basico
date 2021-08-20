# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 23:53:53 2020

@author: Oswaldo Ivann
"""

#Definimos nuestros variables que seran utilizadas en nuestra funcion miembro
def lista_vacia():
    return []
def car(lista):
    return lista[0]
def cdr(lista):
    return lista[1:]

#Definimos la funcion miembreo que buscara en una lista el item deseado

def miembro(lista, item):

#Por definicion anterior, si la lista es vacia entonces Falso
    if lista == lista_vacia:
        return False
    
#Por definicion anterior, si el primier elemento de la lista es el item entonces Verdad    
    if car(lista) == item:
        return True
    
#Si el Item ingresddo no existe dentro de la lista entonces Falso    
    if item not in lista:
        return False
    
#Aqui regresara a comparar el item del primer elemento de la cola hasta terminar la lista 
    else:
        return miembro(cdr(lista), item) 