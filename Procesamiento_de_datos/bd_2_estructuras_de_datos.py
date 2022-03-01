from pprint import pprint
#las listas son colecciones ordenadas de elementos

nueva_lista = [1, 2, 33, 56]
nueva_lista.pop()
nueva_lista.pop(2)
nueva_lista.append(45)


#print(nueva_lista)


mi_diccionario = {'nombre' : 'Omar', 'apellido' : 'Cr', 'direccion' : 'Xola', 'dir_facturacion' : {'colonia' : 'Narvarte', 'CP' : '03020'}}

#agregar datos
mi_diccionario['numero'] = 55555

#print(mi_diccionario)

#modificar datos
mi_diccionario['nombre'] = 'Alonso'
#print(mi_diccionario)
mi_diccionario['dir_facturacion']['colonia'] = 'Loma Hermosa'
#print(mi_diccionario)

#Eliminar
mi_diccionario.pop('dir_facturacion')
#print(mi_diccionario)

lista_1 = [1, 4, 6, 2, 4]

print(f'primer elemento de la lista:{lista_1[0]}')
print(f'último elemento de la lista:{lista_1[-1]}')

uno = 1
dos = 2
tres = 3
cuatro = 4

lista_con_variables = [uno, dos, tres, cuatro]

print(lista_con_variables)

lista_1.append(7)
print(lista_1)


diccionario_4 = {
    "int": 123,
    "float": 23.56,
    "string": "Hola",
    "booleano": True,
    "lista": [1, 2, 3, 4],
    "diccionario": {
        1: "uno",
        2: "dos"
    }
}

print(diccionario_4['float'])

info_de_contacto = {
    "nombre": "Isabel",
    "tel": 5546352431,
    "dir": {
        "colonia": "Del Valle Centro",
        "calle": "Pilares",
        "num": 69,
        "cp": "03100"
    }
}

pprint(info_de_contacto)

info_de_contacto['dir']['alcaldia'] = 'Miguel Hidalgo'
pprint(info_de_contacto)

#modificar
info_de_contacto['dir']['alcaldia'] = 'Benito Juárez'
pprint(info_de_contacto)
print('-------')
info_de_contacto.pop('tel')
pprint(info_de_contacto)


def agregar_numero_a_lista_si_el_numero_es_par(lista, numero):
    if numero % 2 == 0:
        lista.append(numero)

    return lista


lista_de_ints = [2, 34, 26, 88, 4]

lista_de_ints = agregar_numero_a_lista_si_el_numero_es_par(lista_de_ints, 5)
lista_de_ints = agregar_numero_a_lista_si_el_numero_es_par(lista_de_ints, 66)

print(lista_de_ints)


def regresa_true_si_el_valor_esta_entre_50_y_60(valor):
    if valor > 50:
        if valor < 60:
            return True

    return False


resultado_1 = regresa_true_si_el_valor_esta_entre_50_y_60(58)
resultado_2 = regresa_true_si_el_valor_esta_entre_50_y_60(89)

if resultado_1 == True:
    print("El primer valor es mayor a 50 y menor a 60")

if resultado_2 == True:
    print("El segundo valor es mayor a 50 y menor a 60")


def si_los_valores_son_iguales_regresa_exito(valor_1, valor_2):
    if valor_1 == valor_2:
        return "Éxito"
    else:
        return "Error"


resultado = si_los_valores_son_iguales_regresa_exito(4, 4)

print(valor_1)