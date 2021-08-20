# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:40:05 2020

@author: Oswaldo Ivann
"""
#Definimos la funcion mas_peque quien realizara la busqueda
def mas_peque(L):
    
#Declaramos 1 variables: maspeque - Sera el primer valpr de nuestra lista
   maspeque = L[0]
   
#Declaramos la variable maspeque_indice - Indicara el indice del # mas pequeño
   maspeque_indice = 0
   
#El bucle For recorrera toda la lista comparando todos los valores
   for i in range(1, len(L)):
       
#La sentencia If hara la comparacion para determinar el # menor       
        if L[i] < maspeque:
            
#Aqui se guardara el indice que encontro como mas pequeño            
            maspeque = L[i]
            
#Para finalmente darnos el valor al terminar el Bucle For
            maspeque_indice = i
   return maspeque_indice