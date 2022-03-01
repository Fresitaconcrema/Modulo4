# lista_1 = [1, 2, 3, 4]
#
# print(f'Primer elemento de la lista: {lista_1[0]}')
# print(f'Último elemento de la lista:{lista_1[3]}')
#
# print(lista_1[-2])
#
# uno = 1
# dos = 2
# tres = 3
# cuatro = 4
#
# lista_2 = [uno, dos, tres, cuatro]
#
# print(lista_1)
# print(lista_2)
#
# lista_1.append(5)
# print(f'lista_1 {lista_1}')
# lista_2.pop(1)
# print(f'lista_2 {lista_2}')

# diccionario_1 = {}
#
# diccionario_2 = {
#     'carne': 'pollo',
#     'bebida': 'jugo de toronja',
#     'verdura': 'espinacas',
#     'fruta': 'manzana'
# }
#
# diccionario_4 = {
#     "int": 123,
#     "float": 23.56,
#     "string": "Hola",
#     "booleano": True,
#     "lista": [1, 2, 3, 4],
#     "diccionario": {
#         1: "uno",
#         2: "dos"
#     }
# }
#
# print(diccionario_2['verdura'])

# from pprint import pprint
#
# info_de_contacto = {
#     'nombre': 'Isabel',
#     'tel': 5521879218,
#     'dir': {
#         'colonia': 'Del Valle Centro',
#         'calle': 'Pilares',
#         'num': 69,
#         'cp': '03100'
#     }
# }
#
# pprint(info_de_contacto)
#
# info_de_contacto['email'] = 'mailto@admin.com'
#
# pprint(info_de_contacto)
#
# info_de_contacto['dir'] = {
#     'colonia': 'Escandon',
#     'calle': 'Progreso',
#     'num': 189,
#     'cp': '11800'
# }
#
# pprint(info_de_contacto)
#
# info_de_contacto['dir']['num']  = 34
#
# pprint(info_de_contacto)
#
# info_de_contacto.pop('tel')
# pprint(info_de_contacto)


def multiplicar_numero_por_pi(numero):
    resultado = numero * 3.14

    return print(resultado)

multiplicar_numero_por_pi(15)

def multiplica_argumento_por_10(parametro):
    resultado = parametro * 10

    return print(resultado)

def agregar_numero_a_lista_si_el_numero_es_par(lista, numero):

    if numero % 2 == 0:
        lista.append(numero)

    return lista

lista_de_ints = [2, 34, 26, 88, 4]

lista_de_ints = agregar_numero_a_lista_si_el_numero_es_par(lista_de_ints, 40)

print(lista_de_ints)


def regresa_booleano (valor):

    if valor > 50:
        if valor < 60:
            return True

    return False

resultado_1 = regresa_booleano(58)
resultado_2 = regresa_booleano(89)

if resultado_1 == True:
    print('El primer valor es mayor a 50 y menor a 60')

if resultado_2 == False:
    print('El resultado es mayor a 50 y mayor a 60')
