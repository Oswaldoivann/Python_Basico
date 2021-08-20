# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 22:28:39 2020

@author: Oswaldo Ivann
"""
'''

No. Primos
Es primo (4) No
Es primo (5) Si
Es primo (n) si / no
'''
n = int(input("Ingrese el valor del #: "))

def primo(n):
    if n < 2:
        return False
    i = 2
    while i*i < n:
        if n % i == 0:
            return True
        i = i+1
        return True

print(primo(n))