try:
    with open("nombre.txt", "r") as archivo:
        lineas = archivo.readlines()
        nombres = [linea.strip() for linea in lineas]
    nombres_validos = []

    for nombre in nombres:
        # Verificamos que el nombre no tenga números ni símbolos
        if nombre.replace(" ", "").isalpha():
            # Verificamos si está bien capitalizado
            if nombre == nombre.title():
                nombres_validos.append(nombre)
    print("Nombres válidos:")
    for n in nombres_validos:
        print(n)
except FileNotFoundError:
    print("El archivo no existe")

       
