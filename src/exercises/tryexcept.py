try:
    numero = int(input("Ingresa un númerio: "))
    print("El doble es: ", numero * 2)
except ValueError:
    print("Error: Debes ingresar un número valido")

#ejemplo con un archivo

try:
    with open("archivo_inexistente.txt", "r") as f:
        contenido = f.read()
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe ❌")


#varios errores

try:
    x = int("hola")
    y = 15/0
except ValueError:
    print("conversió invalida")
except ZeroDivisionError:
    print("No se puede dividir entre 0")