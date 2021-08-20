# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:40:27 2020

@author: Oswaldo Ivann
"""

def mcd(a,b):
    if b == 0:
        return a
    else:
        return (b,(a%b)) 