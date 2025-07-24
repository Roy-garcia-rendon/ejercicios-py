print("hola")
print(3+3)

nombre = input("ingresa un nombre:")
print("hola", nombre)

edad = int(input("edad: ")) #de str a int
altura = float("1.75") #de str a float
texto = str(100) #de in a str


#Cuenta cuántos elementos hay en una lista, cadena o cualquier estructura iterable.
frutas = ["manzana", "pera", "uva"]
print(len(frutas))

#Te dice de qué tipo es una variable.
nombre = "Rodrigo"
print(type(nombre))

#Ordena una lista sin modificar la original.
nombre = ["perro", "gato", "persona"]
nombres_ordenados = sorted(nombres)
print(nombres_ordenados)
#Si usas .sort(), modificas la lista original

#Genera una secuencia de números (ya lo vimos con bucles for).
for i in range(3):
    print(i)

#Operan sobre listas de números.
numeros = [5, 8, 2]
print(sum(numeros))  # 15
print(max(numeros))  # 8
print(min(numeros))  # 2
