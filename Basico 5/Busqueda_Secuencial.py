# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:38:26 2020

@author: Oswaldo Ivann
"""

#Definimos el nombre de nuestra funcion como busqueda secuencial

def busqueda_secuencial(lista,item):
    
#Definimos dos variables que nos indicaran la posicion y la condicion si el item es encontrado
    
    posicion = 0
    encontrado = False
    
#Definimos la condicion while para que se repita en toda nuestra lista 
    while posicion < len(lista) and not encontrado:
        
#En caso de que el item sea igual a la posicion cambiara a Verdadero y mandara el mensaje a pantalla      
        if lista [posicion] == item:
            encontrado == True
            return print ("El item", item, "si se encontro en la posicion", posicion, "de la lista")
        else:
            
#Con esta funcion incrementamos la posicion 1 mas cada que regrese a revisar el siguente item de nuestra lista
            posicion=posicion+1
            
#Cuando el Item nunca es encontrado regresa 2 mensaje en pantalla de rechazado            
    return print ("El item", item, "no se encontro en la lista")
