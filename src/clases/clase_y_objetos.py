class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre #atrivuto
        self.edad = edad #atrivuto

    def saludar(self): #metodo
        print(f"Hola, Soy {self.nombre} y tengo {self.edad} años")

#crear objeto
persona = persona("Rodrigo", 25)
persona.saludar()

#📌 __init__ es el constructor, se ejecuta al crear el objeto.
#📌 self representa al propio objeto.