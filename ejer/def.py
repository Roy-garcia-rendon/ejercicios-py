#🧪 Ejercicio guiado:
#Crea una función que reciba un nombre y lo salude.
def nombre():
    i = input("Ingresa tu nombre: ")
    i = i.capitalize()
    print("Hola", i.capitalize())
nombre()

#Crea una función que reciba 2 números y devuelva su suma.

def sum():
    i1= int(input("Ingresa primer número: "))
    i2 = int(input("Ingresa segundo número: "))
    print(i1 + i2)
sum()

#Crea una función que reciba una lista y devuelda la cantidada de elementos que contiene.
def conta(lista):
    return len(lista)

nombre = ["Perro", "Gato", "Cerdo", "Gallo"]
print("Elementos", conta(nombre))