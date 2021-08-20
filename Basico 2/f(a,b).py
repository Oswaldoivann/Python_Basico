# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 00:58:25 2020

@author: Oswaldo Ivann
"""

def Sumai(a,b):
    if a == b:
        return a
    else: 
        return b + Sumai(a, b-1)