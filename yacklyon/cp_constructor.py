class Persona:
    pass
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def crear_nombre(self):
        return 'Su nombre y apellido son {} {}'.format(self.nombre, self.apellido)

    def crear_direccion(self, direccion):
        return 'Su direccion es: {}'.format(direccion)

ingeniero = Persona('Omar', 'Cruz')

print(ingeniero.crear_nombre())
print(ingeniero.crear_direccion('20 de Nov'))


class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

correo = Email()

print(correo.enviado)
correo.enviar_correo()
print(correo.enviado)