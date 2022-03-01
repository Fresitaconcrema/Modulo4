import pandas as pd
import numpy as np

datos = {
    'precio': [34, 54, np.nan, np.nan, 56, 12, 34],
    'cantidad_en_stock': [3, 6, 14, np.nan, 5, 2, 10],
    'productos_vendidos': [3, 45, 23, np.nan, 24, 6, np.nan]
}


df = pd.DataFrame(datos, index=["Pokemaster", "Cegatron", "Pikame Mucho", "Lazarillo de Tormes", "Stevie Wonder", "Needle", "El AyMeDuele"])

df.isna()
print('-----')
df.isna().sum(axis = 0)

#Con axis=0 nos regresa el conteo por columnas. Con axis=1 nos regresa el conteo por filas:
print('-----')
df.isna().sum(axis = 1)

#Para limpiar las filas que tengan mínimo 1 valor NaN,
# se utiliza dropna(axis=0, how='any'):
print('-----')
df.dropna(axis=0, how='any')

#Con el axis=0 le estamos diciendo que queremos eliminar por filas. Con how='any' le decimos que queremos eliminar cualquier fila que tenga mínimo un NaN.
print('-----')
df = df.dropna(axis=0, how = 'all')

#Si quisiéramos eliminar sólo las filas donde todos los valores sean NaN, podemos usar axis='all':

df_dropped = df.dropna(axis=0, how = 'all')

#Limpiando NaNs por Columnas

df['descuento'] = np.nan

#Al igual que por filas, eliminar NaNs por columna también se puede hacer usando ´any´ y ´all´.
# La única diferencia es que ahora hay que usar axis=1 para que se haga la eliminación por columnas:

df.dropna(axis = 1, how = 'any')

df_dropped = df.dropna(axis=1, how='all')
#print(df_dropped)

df_no_nans = df.dropna(axis=1, how='all')
df_no_nans = df_no_nans.dropna(axis=0, how='all')

#print(df_no_nans)

#Ahora, digamos que podemos asumir que si hay un valor NaN en "productos_vendidos" es porque no ha sido vendido aún.
# En ese caso podemos rellenar ese NaN usando fillna:

df_no_nans['productos_vendidos'] = df_no_nans['productos_vendidos'].fillna(0)
print(df_no_nans)
print('\n')

#Para finalizar, "precio" sí es una variable muy importante, así que nos deshacemos de las filas que aún tengan NaNs:

print(df_no_nans.dropna(axis=0))



