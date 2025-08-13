# Tuplas: Las tuplas son parecidas a las listas, pero con una gran diferencia: son inmutables (no se pueden modificar una vez creadas).

colores = ("rojo", "verde", "azul")
print(colores[0])  # Imprimir rojo

#🔹 Características:
#Se definen usando paréntesis ()
#Pueden contener datos de distintos tipos
#No se pueden agregar, eliminar o cambiar elementos después de crearse
#Se pueden recorrer con for
#Se pueden usar para almacenar datos fijos

#Ejemplos practicos

dias_semana = ("Luners", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
#mostrar todos los dias
for dia in dias_semana:
    print(dia)