nombres = ["Ana", "Aner", "Bruno"]

for nombre in nombre:
    print("hola", nombre)

contador = 0
while contador < 6: #contado hasta 5 empenzando desde 0
    print("Número", contador)
    contador += 1

    
for i in range(5): # 0,1,2,3,4 
    print(i)   

    #range(inicio, fin) ##range(1,6) = 1 a 5
    #range(inicio,fin,paso) ##range(0,10,2) = 0,2,4,6,8


#salir de un bucle con break
for i in range(10):
    if i == 5:
        break
    print(i)

#saltar una iteracion con continue
for i in range(10):
    if i == 5:
        continue
    print(i)  
