
try:
    with open("nombres.txt", "r") as archivo:
        nombres = archivo.readlines()

    for nombre in nombres:
        print(nombre.strip())

except FileNotFoundError:
    print("El archivo no existe")      




