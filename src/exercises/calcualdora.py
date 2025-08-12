calcualr = input("Ingresa la operación (Suma,Resta,Multiplicación,División):")
calcualr = calcualr.capitalize()
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número:"))

if calcualr == "Suma":
    print(n1 + n2)
elif calcualr == "Resta":
    print(n1 - n2)
elif calcualr == "Multiplicación":
    print(n1*n2)
elif calcualr == "División":
    print(n1/n2)