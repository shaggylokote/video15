coding: utf-8 -*-

Created on Tue Apr 26 17:20:45 2022

@author: nicosio

# Tenemos que importar la clase base abstracta y el decorador

# para el m'etodo abstracto

from abc import ABC, abstractmethod

#Creamo nuestra clase abstracta, desciende de ABC # Con esto no vamos a poder crear instancias de la clase # directamente, solo de aquellas de descienden de ella class Figura (ABC):

# Creamos un metodo abstracto para el area # No tiene codigo en su interior, es un metodo vacio

# las clases hijas se ven obligadas a implementarlo

#Hacemos uso del decorador abstractmethod

@abstractmethod def area(self): pass

# Ahora un metodo abstracto para el perimetro

@abstractmethod

def perimetro(self):

pass

# Ahora creamos una clase que desciende de Figura

class Cuadrado (Figura): def _init(self, lado):

self.lado lado

# Implementamos el primer metodo def area(self): return self.lado*self.lado

# Implementamos el segundo metodo def perimetro(self):

return self.lado*4

class Circulo (Figura):

# Creamos otra clase que desciende de Figura def init(self, radio): self.radio-radio

def area(self):

return 3.14159*self.radio*self.radio

def perimetro(self):

return 2*3.14159*self.radio

# Comprobamos que no se puede instanciar Figura

#f1=Figura()

#Instanciamos el cuadrado

C1=Cuadrado (5)

print('EL area es', c1.area())

print('El perimetro es', c1.perimetro())

# Instanciamos el circulo

c2=Circulo(5)

print('EL area es', c2. area()) print('El perimetro es', c2. perimetro())
