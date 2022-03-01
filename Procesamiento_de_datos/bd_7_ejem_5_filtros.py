import pandas as pd

df = pd.read_csv('drive-download/new_york_times_bestsellers-dirty.csv', sep=',', index_col=0)

#Digamos que queremos todas los records donde
# el nombre del autor empiece con 'R'. Primero, usamos operadores de comparación (o en este caso, el método str.startswith) para obtener nuestro filtro:

output_1 = df['author'].str.startswith('R')

#Después, al pasar este filtro al operador de indexación del DataFrame, todas las filas a las que les corresponda un True se mantienen, mientras que las filas a las que les corresponde un False se dejan fuera del subconjunto resultante:
print(df[df['author'].str.startswith('R')].head())

#Podemos también guardar nuestros filtros en variables y después utilizarlos:

filtro_precio_mayor_a_20 = df['price.numberDouble'] > 20

#Podemos incluso aplicar dos o más filtros utilizando operadores lógicos. En este caso, nuestro operador and se representa con un & y el operador or se representa con |:

filtro_rank_numero_uno = df['rank.numberInt'] == '1'

df[filtro_precio_mayor_a_20 & filtro_rank_numero_uno].head()



