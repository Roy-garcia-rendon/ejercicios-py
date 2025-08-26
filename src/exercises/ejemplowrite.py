while True:
    print("\n1. Sobrescribir archivo")
    print("2. Agregar al archivo")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        with open("notas.txt", "w") as archivo:
            nota = input("Escribe tu nota: ")
            archivo.write(nota + "\n")
        print("Archivo sobrescrito ✅")
    
    elif opcion == "2":
        with open("notas.txt", "a") as archivo:
            nota = input("Escribe tu nota: ")
            archivo.write(nota + "\n")
        print("Nota agregada ✅")
    
    elif opcion == "3":
        break
    else:
        print("Opción inválida ❌")
