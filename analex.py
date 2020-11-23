#!/usr/bin/env python

import componentes
import flujo
import string
import sys
import os
from sys import argv
from componentes import *
from string import ascii_letters

filename = "prueba.txt"
numeros = ['0','1','2','3','4','5','6','7','8','9']
Palabras=['PROGRAMA','VAR','VECTOR','ENTERO','REAL'
              ,'BOOLEANO','INICIO','FIN','SI'
              ,'ENTONCES','SINO','MIENTRAS','HACER'
              ,'LEE','ESCRIBE','Y','O','NO'
              ,'CIERTO','FALSO']
Simbolos=['=','<>','<','<=','>=','>']
CaracterEspeciales = [':',';',',',']','[','(',')']
class Analex:
#############################################################################
##  Conjunto de palabras reservadas para comprobar si un identificador es PR
#############################################################################
 PR = frozenset(["PROGRAMA", "VAR", "VECTOR","DE", "ENTERO", "REAL", "BOOLEANO", "INICIO", "FIN", "SI", "ENTONCES", "SINO", "MIENTRAS", "HACER", "LEE", "ESCRIBE", "Y", "O", "NO", "CIERTO","FALSO"])
 ############################################################################
 #
 #  Funcion: __init__
 #  Tarea:  Constructor de la clase
 #  Prametros:  flujo:  flujo de caracteres de entrada
 #  Devuelve: --
 #
 ############################################################################
 def __init__(self, flujo):
    self.flujo= flujo
    self.poserror= 0
    self.nlinea=1


 ############################################################################
 #
 #  Funcion: TrataNum
 #  Tarea:  Lee un numero del flujo
 #  Prametros:  flujo:  flujo de caracteres de entrada
 #              ch: primera caractera tratar
 #  Devuelve: El valor numerico de la cadena leida
 #
 ############################################################################
 def TrataNum(self,flujo, ch):
  entera=ch
  decimal=None
  BoolEntero = True 
  BoolDecimal = False
  ch = self.flujo.siguiente()
  while BoolEntero:
      if(ch in numeros):
          entera = entera + ch
          ch = self.flujo.siguiente()
      else:
          if(ch == '.'):
              BoolDecimal = True
              BoolEntero = False
              decimal = ''
          else:
              BoolDecimal = False
              BoolEntero = False
  while BoolDecimal:
   ch = self.flujo.siguiente()
   if(ch in numeros):
      decimal = decimal + ch
   else:
      BoolDecimal= False
  self.flujo.devuelve(ch)
  aux = Numero(entera,decimal,self.nlinea)          
  return aux
#Completar

 ############################################################################
 #
 #  Funcion: TrataIdent
 #  Tarea:  Lee identificadores
 #  Prametros:  flujo:  flujo de caracteres de entrada
 #              ch: Primer caracter a tratar
 #  Devuelve: Devuelve una cadena de caracteres que representa un identificador
 #
 ############################################################################
 def TrataIdent(self,flujo, ch):
  l = ch
  ch = flujo.siguiente()
  valido = True
  while valido:
      if ch == ' ' or ch == '.':
          valido= False
      else:
          if ch in numeros or ch in ascii_letters:
              l = l+ch
              ch = flujo.siguiente()
          else:
              valido= False
  
  self.flujo.devuelve(ch)
  if(l not in Palabras):
   aux = Identif(l,self.nlinea) 
   return aux
  else:
   return PR(l,self.nlinea)


  ############################################################################
  #
  #  Funcion: TrataIdent
  #  Tarea:  Lee identificadores
  #  Prametros:  flujo:  flujo de caracteres de entrada
  #              ch: Primer caracter a tratar
  #  Devuelve: Devuelve una cadena de caracteres que representa un identificador
  #
  ############################################################################
 def TrataComent(self, flujo):
     ch = flujo.siguiente() 
     if(ch =='%'):
         l = ''
         ch = flujo.siguiente()
         while ch  != '\n':
             l = l+ch
             ch = flujo.siguiente()
         return ComentarioLineal(l,self.nlinea) 
     else:
         return OpSub(self.nlinea)
                
 ############################################################################
 #
 #  Funcion: EliminaBlancos
 #  Tarea:  Descarta todos los caracteres blancos que hay en el flujo de entrada
 #  Prametros:  flujo:  flujo de caracteres de entrada
 #  Devuelve: --
 #
 ############################################################################
 def EliminaBlancos(self,flujo):
     pass
     #Completar

 ############################################################################
 #
 #  Funcion: Analiza
 #  Tarea:  Identifica los diferentes componentes lexicos
 #  Prametros:  --
 #  Devuelve: Devuelve un componente lexico
 #
 ############################################################################
 def Analiza(self):
  ch = self.flujo.siguiente()
  if ch == '=':
      return OpAsigna(self.nlinea)
  elif ch == '+':
      return OpAdd(self.nlinea)
  elif ch == '-':
      return OpSub(self.nlinea)
  elif ch == '*':
      return OpMult(self.nlinea)
  elif ch == '/':
      return OpDiv(self.nlinea)
  elif ch in Simbolos:
      return OpRel(ch,self.nlinea)
  elif ch in numeros:
      print('Tratando Numeros')
      return self.TrataNum(self.flujo,ch)
  elif ch in string.ascii_uppercase:
      print('Tratando Identificación')
      return self.TrataIdent(self.flujo,ch)
  elif ch == ' ':
      return self.Analiza()
  elif ch in CaracterEspeciales:
      return CaracterEspecial(ch, self.nlinea)
  elif ch == '.':
      return None
  elif ch == '%':
      return self.TrataComent(self.flujo)
  elif ch == '\n':
       self.nlinea=self.nlinea + 1
       return self.Analiza()
  else:
    print ('Caca')
    return self.Analiza()
    
############################################################################
#
#  Funcion: __main__
#  Tarea:  Programa principal de prueba del analizador lexico
#  Prametros:  --
#  Devuelve: --
#
############################################################################

if __name__=="__main__":
    #script, filename=argv
    txt=open(filename)
    print ("PROGRAMA FUENTE %r"  % filename)
    i=0
    fl = flujo.Flujo(txt)
    analex=Analex(fl)
    c = analex.Analiza()
    #while c.cat != "EOF":
        #print (c)
        #c = analex.Analiza()
    i = i + 1

