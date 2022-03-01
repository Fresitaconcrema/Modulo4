import pandas as pd
import numpy as np

serie_1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#Recuerdas cómo utilizamos map para aplicar una función elemento
# por elemento a un arreglo. Podemos utilizar funciones vectorizadas
# para hacer esto mismo con Series y DataFrames de pandas.
# Esto resulta sumamente eficiente pues pandas
# está construido para funcionar de esta manera.
# Primero que nada, veamos cómo es posible aplicar
# operaciones aritméticas a Series de pandas y
# son aplicadas elemento por elemento. Por ejemplo:

print(serie_1 + 10)

print(np.power(serie_1, 2))

print(np.sqrt(serie_1))


#agregaciones

serie = pd.Series([1, 2, 3, 4, 5])

print('Sum:', serie.sum(), "\nMin:", serie.min(), "\nMax:",  serie.max(), "\nCount:",  serie.count(), "\nLen:",  len(serie))
