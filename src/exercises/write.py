#📌 Ejercicio:
#Crea un archivo nombres.txt con varios nombres (puedes hacerlo desde Python con "w").
#Ábrelo en modo lectura y muestra cada nombre en pantalla, quitando los saltos de línea.
#Luego, abre el archivo en modo agregar ("a") y añade un nuevo nombre.

with open("nuevo.txt", "a") as archivo:
    archivo.write("Rodrigo\n")
    archivo.write("Keneth\n")
    archivo.write("Pedro\n")
    archivo.write("Juan\n")
    archivo.write("Ana\n")
    archivo.write("Katerine\n")



with open("nuevo.txt", "a") as archivo:
    archivo.write("Rodrigo\n")