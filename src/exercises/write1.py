with open("agenta.txt", "a") as archivo:
    texto = input("Ingresa un texto: ")
    archivo.write(texto + "\n")