nombre = ["perro", "gato", "persona"]
numeros =[10,12,23,3,2]

print(nombre[0])
print(numeros[4])

nombre[0] = "andromeda"
print(nombre)

nombre.append("elena")
print(nombre)

nombre.remove("gato")
print(nombre)

for nombre in nombre:
    print("hola", nombre)

nombre.soport() #ordena la lista original

nombre= sorted(nombre) #crea una nueva lista ordenada

len(nombre) #cuantos elementos tiene

"Beatriz" in nombre #verifica si un elemento esta en la lista