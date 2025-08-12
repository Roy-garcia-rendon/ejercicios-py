#📘 Tema 12: Funciones (def)
#Las funciones te permiten organizar y reutilizar tu código.
#🧱 ¿Qué es una función?
#Una función es un bloque de código que realiza una tarea y puede recibir datos y devolver resultados.

#sintaxis basica
def saludar():
    print("Hola mundo")
saludar()    

#con parametros

def saludar(nombre):
    print(f"Hola, {nombre}")
saludar("Ana")

#Función que devuelve valor (return)

def sumar(q, b):
    return q + b
resultado = sumar(3, 5)
print(resultado)