with open("nombres.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)


#📌 "r" = modo lectura.
#with cierra el archivo automáticamente cuando termina.

#leer linea por linea
with open("nombres.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())#strip() quita los espacios y saltos de linea

with open("nuevo.txt", "w") as archivo:
    archivo.write("Hola mundo")
    archivo.write("Segunda linea")
#📌 "w" = modo escritura (borra el contenido anterior).
#📌 "a" = modo agregar (añade contenido al final).