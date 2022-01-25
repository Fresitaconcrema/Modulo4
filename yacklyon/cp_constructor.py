class Persona:
    pass
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def crear_nombre(self):
        return 'Su nombre y apellido son {} {}'.format(self.nombre, self.apellido)

ingeniero = Persona('Omar', 'Cruz')

print(ingeniero.crear_nombre())