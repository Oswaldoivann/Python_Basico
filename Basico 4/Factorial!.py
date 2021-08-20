# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 00:23:40 2020

@author: Oswaldo Ivann
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n=int(input("Numero del factorial: "))

print(factorial(n))

