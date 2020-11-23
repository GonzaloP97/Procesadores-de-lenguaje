##
######################################################################################
Simbolos=['=','<>','<','<=','>=','>']
Palabras=['PROGRAMA','VAR','VECTOR','ENTERO','REAL'
              ,'BOOLEANO','INICIO','FIN','SI'
              ,'ENTONCES','SINO','MIENTRAS','HACER'
              ,'LEE','ESCRIBE','Y','O','NO'
              ,'CIERTO','FALSO']

# Clase generica que define un componente lexico 
class Componente:
  def __init__(self):
    self.cat= str(self.__class__.__name__)

 #este metodo mostrará por pantalla un componente lexico
  def __str__(self):
        #Declara un vector vacio
        s=[]
        #Recorre un diccionario de elementos
        for k,v in self.__dict__.items():
            #Si k es distinto al valor, entonces se le añade a s
            if k!= "cat": s.append("%s: %s" % (k,v))
        if s:
        #Se devuvle el valor de s
          return "%s (%s)" % (self.cat,", ".join(s))
        else:
          return self.cat

#definicion de las clases que representan cada uno de los componentes lexicos

#Algunas tendran camps adicionales para almacenar informacion importante (valor de un numero, etc)

#clases para los simbolos de puntuacion y operadores

class OpAsigna(Componente):
        
    def __init__(self,nl):
        self.valor = '='  
        self.linea = nl
    def __str__(self):
        return "Operador asignación establecido: %s  En la linea: %s" % (self.valor, self.linea)
        

# Clase que define la categoria OpAdd
class OpAdd(Componente):
    def __init__(self,nl):
        self.valor = '+'  
        self.linea = nl
    
    def __str__(self):
        return "Operador de suma establecido: %s  En la linea: %s" % (self.valor, self.linea) 
#debe almacenarse de que operador se trata

# Clase que define la categoria OpSub
class OpSub(Componente):
    def __init__(self,nl):
        self.valor = '-'  
        self.linea = nl
    def __str__(self):
        return "Operador de resta establecido: %s  En la linea: %s" % (self.valor, self.linea) 
#Debe alnmacenarse que operador es

# Clase que define la categoria OpMult
class OpMult(Componente):
    def __init__(self,nl):
        self.valor = '*'  
        self.linea = nl
    def __str__(self):
        return "Operador de multiplicación establecido: %s  En la linea: %s" % (self.valor, self.linea) 
#Debe alnmacenarse que operador es

# Clase que define la categoria OpDiv
class OpDiv(Componente):
    def __init__(self,nl):
        self.valor = '/'  
        self.linea = nl
    def __str__(self):
        return "Operador de modulo establecido: %s  En la linea: %s" % (self.valor, self.linea) 
#Debe alnmacenarse que operador es

class OpMod(Componente):
    def __init__(self,nl):
        self.valor = '%'  
        self.linea = nl
    def __str__(self):
        return "Operador de división establecido: %s  En la linea: %s" % (self.valor, self.linea) 
#Debe alnmacenarse que operador es

#clases para representar los numeros.
#Puede dividirse en 2 para representar los enteros y los reales de forma independiente
#Si se opta por una sola categoria debe alamcenarse el tipo de los datos ademas del valor
class Numero (Componente):
    
    def __init__(self,entera,decimal,nl):
        if(decimal == None):
            self.num =str(digitos(entera).digitos)
            self.linea = nl
        else:
            self.num=str(digitos(entera).digitos) + str(fraccion_opt(decimal).fraccion_opt)
            self.linea = nl
    def __str__(self):
        return "Numero establecido: %s  En la linea: %s" % (self.num, self.linea)
    
class digitos(Componente):
    def __init__(self,digito):
        self.digitos=digito
        
    def __str__(self):
        return "%s" % (self.digitos)
        
class fraccion_opt(Componente):
    def __init__(self,digito):
        if(digito == None):
            self.fraccion_opt =None
        else:    
            self.fraccion_opt = '.'+str(digitos(digito))
    
    def __str__(self):
        if(self.fraccion_opt()==None):
            return "No hay parte decimal"    
        return "0 %s" % (self.fraccion_opt)
        
#clases para representar los identificadores y palabras reservadas
class Identif (Componente):
    def __init__(self,v,nl):
#    Componente.__init__(self)
#    self.valor= v
#    self.linea=nl
     if(v not in Palabras):           
        if(v[0] in ascii_letters ):
            self.valor = v
            self.linea = nl
        else:
         print("Este valor no es válido como identificador")
         self.valor = None
         self.linea = nl
     else:
         print("Este valor no es válido como identificador")
         self.valor = None
         self.linea = nl
    def __str__(self):
        if self.valor== None:
            return "No es un identificador valido" 
        return "Identificador establecido: %s  En la linea: %s" % (self.valor, self.linea)

#Clase que representa las palabras reservadas.
#Sera una clase independiente de los identificadores para facilitar el analisis sintactico
class PR(Componente):


    def __init__(self,v,nl):
#  def __init__(self, v,nl):
#   Componente.__init__(self)
#   self.valor = v
#   self.linea=nl
        if(v in Palabras ):
            self.valor = v
            self.linea = nl
        else:
            print("Este valor no es válido como palabra reservada")
            self.valor = None
            self.linea = nl

    def __str__(self):
        if self.valor== None:
            return "No es una palabra reservada valida" 
        return "Palabra reservada establecida: %s  En la linea: %s" % (self.valor, self.linea)

# Clase que define la categoria OpRel
#Debe almacenarse que operador es concretamente

class OpRel (Componente):
    def __init__(self,v,nl):
        if(v in Simbolos ):
            self.valor = v
            self.linea = nl
        else:
            print("Este valor no es válido como operador relacional")
            self.valor = None
            self.linea = nl
        
    def __str__(self):
        if self.valor== None:
            return "No es operador relacional válido" 
        return "Operadr relacional establecido: %s  En la linea: %s" % (self.valor, self.linea)
    

class ComentarioLineal(Componente):
    def __init__(self,v,nl):
        self.valor = '%%'
        self.valor = self.valor+v
        self.linea = nl
    def __str__(self):
        return "Comentario lineal establecido: %s  En la linea: %s" % (self.valor, self.linea) 

class EspacioEnBlanco(Componente):
    def __init__(self,nl):
        self.valor = ' '  
        self.linea = nl
    def __str__(self):
        return "Espacio en blanco establecido: %s  En la linea: %s" % (self.valor, self.linea) 

class CaracterEspecial():
    def __init__(self,v,nl):
        if(v == '.'):
            a = Punto(nl)
            self.valor = a.valor
            self.linea = a.linea
        elif(v == ':'):
            a = DosPuntos(nl)
            self.valor = a.valor
            self.linea = a.linea
        elif(v == ';'):
            a = PuntoyComa(nl)
            self.valor = a.valor
            self.linea = a.linea
        elif(v == ','):
            a = Coma(nl)
            self.valor = a.valor
            self.linea = a.linea
        elif(v == '['):
            a = CorcheteA(nl)
            self.valor = a.valor
            self.linea = a.linea
        elif(v == ']'):
            a = CorcheteC(nl)
            self.valor = a.valor
            self.linea = a.linea
        elif(v == '('):
            a = ParentesisA(nl)
            self.valor = a.valor
            self.linea = a.linea
        elif(v == ')'):
            a = ParentesisC(nl)
            self.valor = a.valor
            self.linea = a.linea

    def __str__(self):
        return "Caracter especial establecido: %s  En la linea: %s" % (self.valor, self.linea) 


class Punto(Componente):
    def __init__(self,nl):
        self.valor = '.'  
        self.linea = nl
    def __str__(self):
        return "Punto establecido: %s  En la linea: %s" % (self.valor, self.linea) 

class DosPuntos(Componente):
    def __init__(self,nl):
        self.valor = ':'  
        self.linea = nl
    def __str__(self):
        return "Dos puntos establecido: %s  En la linea: %s" % (self.valor, self.linea) 
    
class PuntoyComa(Componente):
    def __init__(self,nl):
        self.valor = ';'  
        self.linea = nl
    def __str__(self):
        return "Punto y coma establecido: %s  En la linea: %s" % (self.valor, self.linea) 
    
class Coma(Componente):
    def __init__(self,nl):
        self.valor = ','  
        self.linea = nl
    def __str__(self):
        return "Coma establecido: %s  En la linea: %s" % (self.valor, self.linea) 

class CorcheteA(Componente):
    def __init__(self,nl):
        self.valor = '['  
        self.linea = nl
    def __str__(self):
        return "Corchete de apertura establecido: %s  En la linea: %s" % (self.valor, self.linea) 

class CorcheteC(Componente):
    def __init__(self,nl):
        self.valor = ']'  
        self.linea = nl
    def __str__(self):
        return "Corchete de cierre establecido: %s  En la linea: %s" % (self.valor, self.linea) 

class ParentesisA(Componente):
    def __init__(self,nl):
        self.valor = '('  
        self.linea = nl
    def __str__(self):
        return "Parentesis de apertura establecido: %s  En la linea: %s" % (self.valor, self.linea) 

class ParentesisC(Componente):
    def __init__(self,nl):
        self.valor = ')'  
        self.linea = nl
    def __str__(self):
        return "Parentesis de apertura cerrado: %s  En la linea: %s" % (self.valor, self.linea) 

    
