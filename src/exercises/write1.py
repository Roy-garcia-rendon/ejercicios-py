while True:
    print("\n1.Rehacer")
    print("2.agregar")
    print("3.Salir")
    opcion = int(input("Ingresa una opción: "))
    if opcion == 1:
        with open("notas.txt", "w") as archivo:
            nota = input("Ingresa tu nueva nota: ")
            archivo.write(nota + "\n")
        print("nota reecheca")
    elif opcion == 2:
        with open("notas.txt", "a") as archivo:
            nota = input("añade a la nota: ")
            archivo.write(nota + "\n")
        print("nota agregada")

    elif opcion == 3:
        print("salir")
        break
    else:
        print("opcion no valida")