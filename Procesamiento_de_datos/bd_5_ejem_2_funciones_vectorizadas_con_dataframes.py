import pandas as pd
import numpy as np

datos = {
    'precio': [34, 54, 223, 78, 56, 12, 34],
    'cantidad_en_stock': [3, 6, 10, 2, 5, 45, 2],
    'productos_vendidos': [3, 45, 23, 76, 24, 6, 2]
}

df = pd.DataFrame(datos, index = ["Pokemaster", "Cegatron", "Pikame Mucho", "Lazarillo de Tormes", "Stevie Wonder", "Needle", "El AyMeDuele"])



#Si aplicamos operaciones aritméticas a nuestro DataFrame
# la operación se aplicará elemento por elemento a nuestro DataFrame completo:

print(df* 100)

#También podemos aplicar funciones vectorizadas con el mismo resultado:

print(np.power(df, 2))
print('------')
print(np.sqrt(df))
print('------')
print(df.sum())
print('------')
print(df['precio'].sum())
print('------')
#Aunque podemos cambiar ese comportamiento usando axis=1 para hacerlo por fila:
print(df.sum(axis=1))
print('------')
#Todas las demás agregaciones funcionan también. El default (o axis=0) es hacerlo por columna, pero todas pueden funcionar por fila usando axis=1:

print(df.iloc[1].sum())
print('------')
print(df.loc['Pokemaster'].sum())






