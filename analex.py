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
  decimal=''
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
      if ch == '':
          valido= False
      else:
          if ch in numeros or ch in ascii_letters:
              l = l+ch
              ch = flujo.siguiente()
          else:
              valido= False
  if(l not in Palabras):
   self.flujo.devuelve(ch)
   aux = Identif(l,self.nlinea) 
   return aux
  else:
   return None

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
          return None
                
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
  print(ch)
  if ch in numeros:
      print('Tratando Numeros')
      return self.TrataNum(self.flujo,ch)
  elif ch in string.ascii_uppercase:
      print('Tratando Identificación')
      return self.TrataIdent(self.flujo,ch)
  elif ch == '':
      self.EliminaBlancos(self.flujo)
  elif ch in CaracterEspeciales:
      aux = CaracterEspecial(ch, self.nlinea)
      return aux
  elif ch == '.':
      return None
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

