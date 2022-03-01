#metodo super para llamar un método especifíco

class Mamifero:
    def __init__(self, nombre):
        print(nombre, 'Es un animal de sangre caliente')

class Leon(Mamifero):
    def __init__(self):
        print('el león es un felino')
        super().__init__('simba')

nuevo_leon = Leon()