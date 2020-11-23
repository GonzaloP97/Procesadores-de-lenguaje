# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:22:54 2020

@author: gonza
"""
from componentes import *
from flujo import *
##Prueba flujo##
a = OpAsigna(14)
flujoExp = Flujo(open('prueba.txt', "r")) 
print(flujoExp.devuelve('='))
print (flujoExp.siguiente())
print(flujoExp.posleida())
print (flujoExp.siguiente())
print(flujoExp.posleida())
print (flujoExp.siguiente())
print(flujoExp.posleida())
a2 = flujoExp.siguiente()
print (a2)
print(flujoExp.posleida())
print( a2 == a.valor)
ch = '1'
numeros = ['0','1','2','3','4','5','6','7','8','9']
print (ch in numeros)
flujoExp.posleida()
