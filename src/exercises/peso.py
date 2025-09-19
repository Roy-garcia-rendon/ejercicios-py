peso = float(input("Ingresa tu peso:"))
altura = float(input("Ingresa tu altura:"))

imc = peso / (altura ** 2 )

print(f"El imc", round(imc, 2))