#ocultamiento de datos para proteger la identidad del objeto

class Cliente:
    def __init__(self):
        self.__codigo = 4312

    def __cuenta(self):
        print('cuenta de procesamiento')

    def getcodigo(self):
        return self.__codigo


persona = Cliente()

#objeto._nombreclase__nombreatributo
print(persona._Cliente__codigo)

persona._Cliente__cuenta()