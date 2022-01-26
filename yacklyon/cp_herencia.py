class Pokemon:
    pass

    def __init__(self, name, type_pokemon):
        self.name = name
        self.type_pokemon = type_pokemon

    def description(self):
        return 'Its name is {} and it is a type of {}'.format(self.name, self.type_pokemon)


class Pikachu(Pokemon):
    def attack(self, attack_type):
        return '{} has {} as attack'.format(self.name, attack_type)


new_pokemon = Pikachu('Bobby', 'Electric')

print(new_pokemon.description())
print(new_pokemon.attack('Impact Thunder'))
