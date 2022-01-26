class Telefono:
    def __init__(self):
        pass

    def llamar (self):
        print('llamando...')

    def ocupado (self):
        print('ocupado...')

class Camara:
    def __init__(self):
        pass

    def foto(self):
        print('tomando..')

class Reproductor:
    def __init__(self):
        pass

    def video(self):
        print('reproduciendo video...')

    def musica(self):
        print('reproduciendo música...')


class Smartphone (Telefono, Camara, Reproductor):
    def __del__(self):
        print('Telefono apagado')

movil = Smartphone()

#Acciones que podemos aplicar
#print(dir(movil))

print(movil.musica())