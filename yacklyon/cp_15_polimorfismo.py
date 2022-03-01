#polimorfismo con funciones

class Tomate:
    def tipo(self):
        print('vegetal')
    def color(self):
        print('rojo')

class Manzana:
    def tipo(self):
        print('fruta')
    def color(self):
        print('verde')

def funcion(objeto):
    objeto.tipo()
    objeto.color()

nuevo_tomate = Tomate()
funcion(nuevo_tomate)
nueva_manzana = Manzana()
funcion(nueva_manzana)


#polimorfismo con metodos
class Colombia:
    def capital(self):
        print('Bogota')
    def idioma(self):
        print('Español')

class Francia:
    def capital(self):
        print('Paris')
    def idioma(self):
        print('Francés')

colombiano = Colombia()
frances = Francia()

for pais in (colombiano, frances):
    pais.capital()
    pais.idioma()

#polimorfismo con herencia

class Aves:
    def volar(self):
        print('la mayoría de las aves pueden volar pero algunas no')

class Aguila(Aves):
    def volar(self):
        print('las Aguilas pueden volar')

class Gallina(Aves):
    def volar(self):
        print('las gallinas no pueden volar')

obj_ave = Aves()
obj_aguila = Aguila()
obj_gallina = Gallina()

obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()