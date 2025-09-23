class estudiante(persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad) #hereda atributos
        self.curso = curso


    def mostrar(self):
        print(f"Estoy en el curso: {self.curso}")

alumno = estudiante("Rodrigo", 25, "python")
alumno.saludar()
alumno.mostrar_curso()
