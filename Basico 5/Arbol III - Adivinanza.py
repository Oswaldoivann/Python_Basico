#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Esta clase crea un arbol con sus nodos
class Tree:
    
    def __init__(self, root, izquierdo = None, derecho = None):
        self.root = root
        self.izquierdo = izquierdo
        self.derecho = derecho
        
    def __str__ (self):
        return str(self.root)


# In[2]:


# La funcion Yes,imprime un mensajes en pantalla (quest), y
#convierte lo ingresado en minusculas, y valida que la entrada sea igual a 'Y'

def yes(quest):
    ans = input(quest).lower()
    return (ans[0] == 'y')


#Se declara la función animal
def animal():
    
    #Se crea una raiz llamada Pajaro
    root = Tree('Pajaro')
    
    #Se crea una condicion para una pregunta
    while True:
        print()
        #Manda la siguente pregunta, y valida la entrada con (yes) 
        if not yes('¿Estas pensando en algun animal?'): break
            
        #Se asigna raiz root al arbol tree
        tree = root
        
        #Se condiciona mientras que
        while tree.izquierdo is not None:
            
            #Se declara (Prompt) como raiz para crear el arbol
            prompt = tree.root + '?'
            
            #Con (yes) crea las ramas del arbol 
            if yes (prompt):
                tree = tree.derecho
            #De lo contrario en la rama izquierda
            else:
                tree = tree.izquierdo
                
        #Se redefine la variable root ('Pajaro')     
        intento = tree.root
        
        #Se formula la pregunta con (Prompt) y se utiliza la variable (root)
        prompt = '¿Es un: ' + intento + '?'
        
        #Se llama la funcion (yes), si es == 'y' manda el mensaje 'Yo Gano!'
        if yes(prompt):
            print('Yo gano!')
            
            #Si Yes, nos regresa al bucle (while) abierto
            continue
            
            
        #se redefine (quest) asiganada a la variable prompt
        prompt = '¿Cual es el nombre del animal?'
        
        #Declara animal como entrada de (quest)
        animal = input(prompt)
        
        #Se imprime (quest) con identificadores {0} y {1}
        prompt = '¿Que pregunta deberia distinguir un {0} de un {1}?'
        
        #Se declara una variable para entrada, y quien sera la raiz del nuevo arbol
        question = input(prompt.format(animal, intento))
        tree.root = question
        
        #Imprime una pregunta en pantalla utilizando el identificador {0}
        prompt = '¿Si el animal fuera un {0}, la respuesta deberia ser?'
        
        #Se guardan los datos ingresados en los identificadores en las ramas del arbol
        if yes(prompt.format(animal)):
            tree.izquierdo = Tree(intento)
            tree.derecho = Tree(animal)
        else:
            tree.izquierdo = Tree(animal)
            tree.derecho = Tree(intento)


# In[ ]:


animal()

