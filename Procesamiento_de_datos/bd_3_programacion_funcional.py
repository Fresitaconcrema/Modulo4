numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def multiplicar_por_10(numero):

    return numero * 2


nueva_multi = multiplicar_por_10(numeros)
nueva_multi_2 = list(map(multiplicar_por_10, numeros))

print(nueva_multi)
print(nueva_multi_2)


def convertir_en_string_mas_unidad(numero):
    return f'{numero} seg'


nuevo_output = list(map(convertir_en_string_mas_unidad, numeros))
print(nuevo_output)


def convertir_a_numeros_negativos(numero):
    return numero * -1


list(map(convertir_a_numeros_negativos, numeros))


def convertir_en_0_si_menor_a_5(numero):
    if numero < 5:
        return 0
    else:
        return numero


list(map(convertir_en_0_si_menor_a_5, numeros))


def convertir_en_true_si_mayor_a_6(numero):
    if numero > 6:
        return True
    else:
        return False


list(map(convertir_en_true_si_mayor_a_6, numeros))


#filter
numeros_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def numero_es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print('Filter')
print(list(filter(numero_es_par, numeros_2)))


def palabra_tiene_mas_de_5_caracteres(palabra):
    if len(palabra) > 5:
        return True


palabras = ["achicoria", "pasto", "sol", "loquillo", "moquillo", "sed", "pez", "jacaranda", "mil"]

list(filter(palabra_tiene_mas_de_5_caracteres, palabras))


def numero_es_negativo(numero):
    if numero < 0:
        return True


numeros = [3, 5, -1, -7, -8, 4, -78, 5, -46, 56, 98, 9, -1, -2, -4]

list(filter(numero_es_negativo, numeros))


def numero_es_divisible_entre_9(numero):
    if numero % 9 == 0:
        return True


numeros = [3, 7, 9, 34, 72, 90, 87, 34, 99, 56, 12, 18]

list(filter(numero_es_divisible_entre_9, numeros))


#AND
def numero_es_divisible_entre_3(numero):
    if numero % 3 == 0:
        return True
    else:
        return False


def numero_es_menor_que_10(numero):
    if numero < 10:
        return True
    else:
        return False

numero_es_divisible_entre_3(9) and numero_es_menor_que_10(9)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def numero_es_divisible_entre_3_y_menor_que_10(numero):
    return numero_es_divisible_entre_3(numero) and numero_es_menor_que_10(numero)

nuevo_output_2 = list(filter(numero_es_divisible_entre_3_y_menor_que_10, numeros))
print(nuevo_output_2)


#not
nuevo_output_3 = not(numero_es_divisible_entre_3(9))
print(nuevo_output_3)

#lambda

nuevo_output_4 = list(filter(lambda x: not numero_es_divisible_entre_3(x), numeros))
print(nuevo_output_4)

palabras = ["achicoria", "pasto", "sol", "loquillo", "moquillo", "sed", "pez", "jacaranda", "mil"]

list(filter(lambda x: len(x) > 5, palabras))



