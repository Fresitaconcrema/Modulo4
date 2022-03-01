# propiedades

class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    def __getnombre(self):
        return self.__nombre

    def __getsalario(self):
        return self.__salario

    def __setnombre(self, nombre):
        self.__nombre = nombre

    def __setsalario(self, salario):
        self.__salario = salario

    def __delnombre(self):
        del self.__nombre

    def __delsalario(self):
        del self.__salario

    # empleado_uno = Empleado('victor', 2000)
    # print(empleado_uno.getnombre(), ',', empleado_uno.getsalario())
    # empleado_uno.setnombre('raul')
    # print(empleado_uno.getnombre(), ',', empleado_uno.getsalario())

    # para alguna validacion

    nombre = property(fget=__getnombre,
                      fset=__setnombre,
                      fdel=__delnombre,
                      doc="soy la propiedad del 'nombre'")

    salario = property(fget=__getsalario)


empleado_uno = Empleado('Victor', 3000)
empleado_uno.nombre = 'Sara'

print(empleado_uno.nombre, empleado_uno.salario)

help(empleado_uno)