# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:56:38 2017

@author: Vitor Pereira
"""

#d=distancia
#p=profundiade

import turtle
def sierpinski(d,p):
    if p==0:
        for i in range(0,3):
            turtle.fd(d)
            turtle.left(120)
                 
    else:
        sierpinski(d/2,p-1)
        turtle.fd(d/2)
        sierpinski(d/2,p-1)
        turtle.bk(d/2)
        turtle.left(60)
        turtle.fd(d/2)
        turtle.right(60)
        sierpinski(d/2,p-1)
        turtle.left(60)
        turtle.bk(d/2)
        turtle.right(60)

d=int(input("informe o valor de d(distância) que determina o lado do triangulo grande(recomendado:200)"))
p=int(input("informe o valor p(profundidade) que determina o lado de cada triangulo pequeno(recomendado:4 ou 5)"))

sierpinski(d,p)
mostra_sierpinski = turtle.Screen()
