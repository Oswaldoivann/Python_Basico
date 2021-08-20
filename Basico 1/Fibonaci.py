# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 21:21:30 2020

@author: Oswaldo Ivann
"""

def fibo(n):
   if n == 0 or n== 1:
       return n
   else:
       return (fibo(n-2) + fibo(n-1 ))
   