import pandas as pd

#Muchas veces vamos a tener Series o DataFrames que queremos unir en una sola estructura. Para eso podemos usar pd.concat. Concatenando Series, podemos hacer lo siguiente:

series_1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
series_2 = pd.Series([5, 6, 7, 8], index=['e', 'f', 'g', 'h'])

output = pd.concat([series_1, series_2], axis=0)

#Podemos nombrar nuestras columnas para saber cuál era cuál:
# 1 Horizontalmente
output = pd.concat([series_1, series_2], axis=1, keys=['monto_1', 'monto_2'])

print(output)

series_3 = pd.Series([7, 8, 9, 10], index=['a', 'b', 'c', 'd'])

output_2 = pd.concat([series_1, series_3], axis=1, keys=['series_1', 'series_3'])

print('\n')
print(output_2, '\n')

#Si concatenamos verticalmente dos Series que comparten el índice, tenemos el problema de no poder diferenciar los índices:

output_3 = pd.concat([series_1, series_3], axis=0, keys=['serie_1', 'serie_2'])

print(output_3)

#Esto se llama un Multiíndice. Podemos acceder a un multiíndice en un solo nivel o en ambos:

print(output_3.loc['serie_1'])

print(output_3.loc[('serie_1', 'b')])

