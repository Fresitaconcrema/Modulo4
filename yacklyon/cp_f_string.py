
# format %
curso = 'python'

print('Este curso es de % s'%curso)

nombre = 'Samuel'
edad = 34

print('Hola soy % s y tengo % s años.'%(nombre, edad))

#str.format()

print('Hola soy {} y tengo {} años.'.format(nombre, edad))

#f-string
print(f'Hola soy {nombre} y tengo {edad} años.')

class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __repr__(self):
        #representacion de una cadena, para poder arrojar un resultado tipo string
        return f"Hola que tal soy {self.nombre} {self.apellido} y tengo {self.edad} años"

nvo_estudiante = Estudiante('Omar', 'Cruz', 35)

print(f"{nvo_estudiante !r}")
