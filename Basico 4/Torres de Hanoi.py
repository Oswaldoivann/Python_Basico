# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:45:00 2020

@author: Oswaldo Ivann
"""

def hanoid (n, del_palo, al_palo, aux_palo):
    if n >= 1:
        hanoid(n-1, del_palo, al_palo, aux_palo)
        mover_disco(del_palo, al_palo)
        hanoid(n-1, aux_palo, al_palo, del_palo)
        
def mover_disco(del_palo, al_palo):
  print("Mover del palo", del_palo, "al palo", al_palo)
   
print(hanoid + 1 , mover_disco + 1)
    
hanoid(1, "del_palo", "al_palo", "aux_palo")
