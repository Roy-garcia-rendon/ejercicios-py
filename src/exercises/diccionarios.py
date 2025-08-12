# 🧪 Ejercicio práctico:
# Crea un diccionario con tus datos personales (nombre, edad, correo)
# Modifica tu edad
# Agrega una clave nueva llamada "país"
#Imprime todo el diccionario con un for

yo = {
    "nombre" : "Rodrigo",
    "edad" : 18,
    "correo" : "rodrigoa.gr11@gmail.com"
}

yo["edad"] = 19
yo["pais"] = "Mexico"

for i in yo:
    print(i, ":", yo[i])