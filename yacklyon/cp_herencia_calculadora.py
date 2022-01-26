class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresar_dato(self):
        self.datos = [int(input('Ingresa datos ' + str(i + 1) + ' = ')) for i in range(self.n)]


class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

    def suma(self):
        a, b = self.datos
        s = a + b
        print('El resultado es: ', s)

    def resta(self):
        a, b = self.datos
        s = a - b
        print('El resultado es: ', s)


class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def cuadrada(self):
        import math

        a, = self.datos
        print('El resultado es :', math.sqrt(a))


ejemplo = op_basicas()
#print(ejemplo.ingresar_dato())
#print(ejemplo.suma())

print(isinstance(ejemplo, op_basicas))
print(issubclass(op_basicas, Calculadora))