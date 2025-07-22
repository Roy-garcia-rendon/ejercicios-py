#ejercicio 3:
#1. Crea una lista con 5 nombres
#2. Imprime el segundo nombre
#3. Agrega otro nombre con append()
#4. Ordena alfabeticamente
#5. Recorre la lista con un bucle y saluda a cada persona

nombres = ["Rodrigo", "Bruno", "Ana", "Aner", "Aldegungo"]
# imprimir segundo nombre:         print(nombres[1])

#agregar otro nombre 

for nombre in nombres:
    nombres.append("Franco")
    nombres.sort()
    nombres = sorted(nombres)
    print("hola", nombre)

