try:
    with open("text.txt" ,"r") as archivo:
        lineas = archivo.readlines()
        nombres = [lineas.strip() for lineas  in lineas]
        nombres.sort()
        print("Nombres ordenados:")
        for nombre in  nombres:
            print(nombre)
except FileNotFoundError:
    print("El archivo no existe")            
