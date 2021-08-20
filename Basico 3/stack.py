#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def getStack():
    return []
    
    
def isEmpty (L):
    if L == []:
        return True
    else:
        return False
    
    
def top(L):
    if isEmpty (L):
        return None
    else: 
        return L[len(L)-1]
    
    
def push(L, item):
    L.append (item)
    
    
def pop (L):
    if isEmpty (L):
        return None
    else: 
        item = L[len(L)-1]
        del L[len(L)-1]
        return item

