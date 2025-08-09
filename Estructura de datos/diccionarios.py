#✅ 3. Diccionarios: Colección de pares clave:valor
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "México"
}
print(persona["nombre"])
persona["edad"] = 31
persona["correo"] = "juan@mail.com"
print(persona)

#📌 Métodos útiles:
#keys(), values(), items()
#get("clave"): #devuelve el valor o None si no existe
#del diccionario["clave"]: #elimina un elemento