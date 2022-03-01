import pandas as pd

#Las Series son secuencias ordenadas de unidimensionales que pueden contener diferentes tipos de valores. En esto se parecen a las listas. De hecho podemos crear Series usando listas

serie_1 = pd.Series([3, 7, 9, 8])
print(serie_1)

#Una gran diferencia que tienen con las listas es que cada elemento en una Serie tiene un índice asociado que no necesariamente es una secuencia de enteros como en las listas. En este aspecto, nuestras Series se parecen a los diccionarios:


serie_2 = pd.Series([4, 7, 9, 8], index=[10, 11, 12, 13])
print(serie_2)

serie_3 = pd.Series([5, 8, 7, 2], index=['a', 'b', 'c', 'd'])
print(serie_3)


datos = {
    "Juan": 45,
    "Pepe": 56,
    "Alfonsina": 12,
    "Jenny": 49,
    "Marco P.": 12
}

serie_4 = pd.Series(datos)

print(serie_4)

print(serie_1.loc[2])
print(serie_3.loc['c'])
print(serie_4.loc['Marco P.'])


#indexacion_de series
print('-----')
serie = pd.Series(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

print(serie)

print(serie.loc[[0, 1, 2]])

print(serie.loc[[5, 8, 2, 4]])
serie.loc[:4]
serie.loc[6:]
serie.loc[3:8]


serie_2 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(serie_2)


print(serie_2.loc['c':'f'])


#Dataframes
#Los DataFrames son entonces estructuras de datos bidimensionales. Tienen filas y columnas. Hay innumerables formas de crear DataFrames (si quieren ahondar en el tema, aquí hay una fuente muy completa). Vamos a aprender una de ellas: los diccionarios de listas.

datos = {
    'columna_1': ['valor_fila_0', 'valor_fila_1', 'valor_fila_2', 'valor_fila_3', 'valor_fila_4'],
    'columna_2': ['valor_fila_0', 'valor_fila_1', 'valor_fila_2', 'valor_fila_3', 'valor_fila_4'],
    'columna_3': ['valor_fila_0', 'valor_fila_1', 'valor_fila_2', 'valor_fila_3', 'valor_fila_4'],
    'columna_4': ['valor_fila_0', 'valor_fila_1', 'valor_fila_2', 'valor_fila_3', 'valor_fila_4']
}

df = pd.DataFrame(datos)

print(df)

#df = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'])

print(df['columna_1'])
print(df[['columna_1', 'columna_2', 'columna_3']])

#Importante: Usamos las palabras observar o ver porque indexar columnas no regresa una copia de esas columnas, sino solamente una "vista" de esas columnas, como si estuviéramos viéndolas a través de una ventana. Eso quiere decir que los cambios que realicemos a las "vista" se verán reflejados en el DataFrame original.
print('------------')
print(df.loc[1:2])
print('------------')
print(df.loc[1, 'columna_2'])

print(df.loc[[1, 3], ['columna_2', 'columna_1']])
