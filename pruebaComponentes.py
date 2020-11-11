# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 00:55:54 2020

@author: gonza
"""
from componentes import *
from string import ascii_letters
diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': [2,3,5]}

for k in diccionario:
    print (diccionario.get(k))

a = OpAsigna(14)
print(a)
b = OpAdd(16)
print(b)
c = OpMult(18)
print(c)
d1 = Numero(3,None,20)
print(d1)
d2 = Numero(3,14,22)
print(d2)
e1 = Identif('A325',24)
print (e1)
e2 = Identif('325',26)
print (e2)
f1 = PR('PROGRAMA',28)
print (f1)
f2 = PR('HOLA',30)
print (f2)
g1 = OpRel('<>',32)
print (g1)
g2 = OpRel('*',34)
print (g2)


aux= ascii_letters
    
