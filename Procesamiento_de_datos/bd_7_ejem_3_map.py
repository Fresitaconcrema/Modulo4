import pandas as pd

df = pd.read_csv('drive-download/new_york_times_bestsellers-dirty.csv', sep=',')

#Digamos que queremos transformar los datos de nuestra columna 'rank.numberInt' para que el 'rankink' esté dado por letras, no por números.
#Sabemos que hay un valor 'No Rank' en esa columna, así que nuestro diccionario de conversión podría verse así:

int_a_letra = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    '10': 'j',
    '11': 'k',
    '12': 'l',
    '13': 'm',
    '14': 'n',
    '15': 'o',
    '16': 'p',
    'No Rank': 'z'
}

print(df['rank.numberInt'].map(int_a_letra).head(20))

#También podemos usar una función para map. Por ejemplo esta función que realiza una correspondencia entre el precio de un libro y su representación en string:

def double_to_money(value):
    return f'${value} USD'

print(df['price.numberDouble'].map(double_to_money))

#Lo único que tienes que pensar al usar map es: "¿Este dato tiene una correspondencia con otro dato que pueda representar con un diccionario o una función?". Y listo.


