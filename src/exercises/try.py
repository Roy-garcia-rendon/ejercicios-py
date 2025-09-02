try:
    numero = int(input("ingresa un número: "))
    print("Tu número es:", numero)
except ValueError:
    print("no es un número")