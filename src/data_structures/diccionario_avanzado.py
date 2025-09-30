# Los diccionarios en Python son estructuras que permiten guardar datos en pares clave:valor.
# Son ideales para representar cosas como un contacto (nombre: número), un producto (id: precio), etc.

persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Mexico"
}

# acceder a un valor
print(persona["nombre"])

# Agregar o modificar valores}
persona["edad"] = 64  # Modificar valor
persona["correo"] = "ana@gmail.com"  # Agregar valor

# aliminar valores
del persona["ciudad"]

# Recorrer un diccionario
for clave in persona:
    print(clave, ":", persona[clave])

# Contar cuantos elementos hay
len(persona)

# Verificar si una clave existe
"nombre" in persona

# Métodos útiles
# | Método         | Función                                  |
# | -------------- | ---------------------------------------- |
# | `keys()`       | Devuelve una lista con las claves        |
# | `values()`     | Devuelve una lista con los valores       |
# | `items()`      | Devuelve una lista de pares clave\:valor |
# | `get("clave")` | Devuelve el valor o `None` si no existe  |
