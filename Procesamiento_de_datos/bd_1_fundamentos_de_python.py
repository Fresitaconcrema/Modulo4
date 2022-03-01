var_1 = 4
var_2 = 54
var_3 = 23
var_4 = 89
variable_3 = 10
variable_nueva_4 = 20

print(var_1 + var_2)
print(var_2 - var_4)
print(var_3 * var_1)
print(var_4 / var_2)
print(var_2 ** var_1)

print(type(var_1))

var_5 = 16.34
print(type(var_5))

var_string = 'Hola Mundo'

print(type(var_string))

var_bool = True
print(type(var_bool))

#interpolacion de strings

print(f'El valor de var_string es: {var_string}')

#operadores de comparacion

var_11 = 34
var_22 = 12
var_33 = 23.24
var_44 = 23.56
var_55 = "OK"
var_66 = "ERROR"
var_77 = True
var_88 = False

print(var_11 > var_22)
print(var_11 < var_22)
print(var_33 < var_44)
print(var_33 <= var_33)
print(var_11 >= var_44)
print(var_55 == var_66)
print(var_55 != var_66)
print(var_77 == var_88)
print(var_77 == var_77)


#estructuras de ctrl
if var_11 > var_22:
    print('Se ejecuto el bloque')

if var_11 < var_22:
    print('en progreso')
else:
    print(f'{var_11} no es más grande que {var_22}')