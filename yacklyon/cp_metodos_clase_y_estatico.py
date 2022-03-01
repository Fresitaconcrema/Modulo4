class Pastel:
    def __init__(self, ingredientes, tamaño):
        self.ingredientes = ingredientes

    def __repr__(self):
        return f'pastel({self.ingredientes !r})'

    @classmethod
    def chocolate(cls):
        return cls(['harina', 'leche', 'chocolate'])

    @classmethod
    def vainilla(cls):
        return cls(['harina', 'leche', 'vainilla'])

print(Pastel.vainilla())

#metodoClase no tiene acceso a los valores de la instancia