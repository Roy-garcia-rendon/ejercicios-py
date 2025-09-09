#Un módulo es un archivo con funciones y clases que puedes importar en tus programas.
#Una librería es un conjunto de módulos listos para usar.


#Importar un módulo estándar
#Python trae muchos módulos integrados:
import math
print(math.sqrt(16)) #raíz cuadrada -> 4.0
print(math.pi) #valor de pi

#Importar funciones específicas
from math import  sqrt, pi
print(sqrt(25))
print(pi)

#Módulo random
#Para generar números aleatorios
import random
print(random.randint(1, 10)) #número entre 1 y 10
print(random.choice(["rojp", "verde", "azul"])) #elijir un color al azar

#crear tu propio modulo

def saludar(nombre):
    return f"Hola, {nombre}!"
#import mimodulo

#print(mimodulo.saludar("Rodrigo"))


import random
print(random.randint(1, 6))
