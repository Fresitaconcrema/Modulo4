class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def tipo_animal(self):
        pass

class Leon(Animal):
    def tipo_animal(self):
        print('Es un animal salvaje')

class Perro(Animal):
    def tipo_animal(self):
        print('Es un animal domestico')

nuevo_animal = Leon('Simba')
nuevo_animal.tipo_animal()