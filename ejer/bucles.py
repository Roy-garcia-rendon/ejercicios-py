#1. Usa un bucle for para imprimir los numeros del 1 al 10
for i in range(1,11):
    print(i)

#2. Usa un bucle while para imprimir los numeros del 1 al 10
i = 10
while i >= 1:
    print(i)
    i -= 1

#3. Usa un for para recorrer una lista de 5 frutas y saluda a cada persona
frutas = ["manzanja", "mango", "pera", "durazno", "uva"]
for fruta in frutas:
    print("hola", fruta)

#4. Reto: Crea un while que pida nombres por teclado y los salude hasta que el usuario escriba "salir"
nombre = input("ingresa un nombre:")
while nombre != "salir":
    print("hola", nombre)
    nombre = input("ingresa un nombre:")
  