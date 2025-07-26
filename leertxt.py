with open("text.txt", "r") as archivo:
    contenido = archivo.readlines()
    #"nombres.txt" → es el nombre del archivo
    #"r" → significa “read” (leer)
    #.readlines() → guarda cada línea como un elemento de una lista
for contenidos in contenido:
    print("hola", contenidos)
    

    #🔴 Problema común: los saltos de línea (\n) al final de cada línea.
    #✅ Solución: .strip() para quitar espacios y saltos de línea:
    #              for nombre in nombres:
    #              print("Hola", nombre.strip())
#Puedes manejar errores con try...except
try:
    with open("text.txt", "r") as archivo:
         contenido = archivo.readlines()
except FileNotFoundError:
    print("El archivo no existe")
