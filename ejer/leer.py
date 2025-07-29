
try:
    with open("nombres.txt", "r") as archivo:
        lineas = archivo.readlines()
    nombres = [linea.strip() for linea in lineas]
    nombres.sort()
    print("Nombres ordenados:")
    for nombre in nombres:
        print(nombre)
except FileNotFoundError:
    print("El archivo no existe")      

