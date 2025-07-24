#ejercicio 5:
#1.  Pide al usuario que ingrese 3 números por input() y conviertelos a int.
#2. Guarda esos números en una lista.
#3. Muestra la lista ordenada con sorted().
# Cuántos números hay len()
#mayor max()
#menor min()
#suma total sum()

numeros = [int(input("Ingresa un números:")) for i in range(3)]
print(numeros)
print(sorted(numeros))
print(len(numeros))
print(max(numeros))
print(min(numeros))
print(sum(numeros))
