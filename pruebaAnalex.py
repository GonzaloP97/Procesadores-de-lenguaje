# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:38:12 2020

@author: gonza
"""

from analex import *
from flujo import *

pruebaTratarNumero = open('pruebaTratarNumero.txt', "r")
pruebaTratarId1 = open('pruebaTratarId1.txt', "r")
pruebaTratarId2 = open('pruebaTratarId2.txt', "r")
pruebaTratarId3 = open('pruebaTratarId3.txt', "r")
pruebaTratarComentario = open('pruebaComentario.txt', "r")
prueba = open('prueba.txt', "r")

# =============================================================================
# #PruebaTratarNumero
# 
# flujoExp = Flujo(pruebaTratarNumero) 
# a = flujoExp.siguiente()
# analexExp = Analex(flujoExp)
# b = analexExp.TrataNum(flujoExp,a)
# print(b)
# 
# #PruebaTratarId
# 
# flujoExp = Flujo(pruebaTratarId1) 
# a = flujoExp.siguiente()
# analexExp = Analex(flujoExp)
# b = analexExp.TrataIdent(flujoExp,a)
# print(b)
# 
# flujoExp = Flujo(pruebaTratarId2) 
# a = flujoExp.siguiente()
# analexExp = Analex(flujoExp)
# b = analexExp.TrataIdent(flujoExp,a)
# print(b)
# 
# flujoExp = Flujo(pruebaTratarId3) 
# a = flujoExp.siguiente()
# analexExp = Analex(flujoExp)
# b = analexExp.TrataIdent(flujoExp,a)
# print(b)
# 
# #PruebaTrataComent
# flujoExp = Flujo(pruebaTratarComentario) 
# a = flujoExp.siguiente()
# analexExp = Analex(flujoExp)
# b = analexExp.TrataComent(flujoExp)
# print(b)
# =============================================================================

#PruebaAnaliza
flujoExp = Flujo(prueba) 
analexExp = Analex(flujoExp)
a = analexExp.Analiza()
while a != None:    
    print(a)
    a = analexExp.Analiza()
