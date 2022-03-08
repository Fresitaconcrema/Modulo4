#Rango
#El rango es simplemente la diferencia entre el valor máximo de un conjunto y el valor mínimo
# de un conjunto. Por lo tanto, podemos obtenerla de esta manera:

import pandas as pd

df = pd.read_csv('drive-download/melbourne_housing-clean.csv', sep=',', index_col=0)

print(df.columns)
print(df.head())

rango = df['price'].max() - df['price'].min()

print(rango)


#Percentiles
#El percentil P es un valor que indica que por lo menos P% de los valores en el conjunto tienen este valor
# o un valor menor; mientras que (100-P)% de los valores tienen este valor o un valor mayor.
# Por ejemplo, para obtener el percentil 80 primero ordenamos nuestro conjunto de manera ascendente y después
# elegimos un valor de manera que el 80% de los valores en nuestro conjunto sean iguales o menores a ese valor.

#En pandas, los percentiles están implementados como cuantiles, que es lo mismo que los percentiles
# pero en versión fracciones. Es decir, el percentil 80 es lo mismo que el cuantil 0.8.

p_quantile_80 = df['price'].quantile(0.8)

print(p_quantile_80)

#En este caso, el 80% de los valores en nuestro conjunto de datos tienen un valor menor o igual a 1 440 000.

#Como podrás ya haber imaginado, el valor mínimo equivale al percentil 0 y el valor máximo equivale al percentil 100,
# mientras que la mediana es exactamente igual que el percentil 50.

#Sacando los percentiles podemos darnos una idea más o menos precisa de cómo están distribuidos nuestros datos.
#Por ejemplo:

print(f'Valor Mínimo: {df["price"].min()}')
print(f'Percentil 10: {df["price"].quantile(0.1)}')
print(f'Percentil 10: {df["price"].quantile(0.25)}')
print(f'Percentil 50: {df["price"].median()}')
print(f'Percentil 75: {df["price"].quantile(0.75)}')
print(f'Percentil 90: {df["price"].quantile(0.9)}')
print(f'Valor Máximo: {df["price"].max()}')

"""
Viendo estos números podemos inferir varias cosas:

Casi todos nuestros datos están concentrados en valores menores a 2 000 000.
Eso quiere decir que tenemos algunos valores atípicos demasiado grandes (si los comparamos con el resto de los valores)
La mediana nos estaba dando un número más cercano al verdadero "valor típico" que el promedio.
El promedio tenía un sesgo hacia arriba debido a los valores extremadamente grandes.
El rango entre el valor máximo y mínimo no nos da una medida representativa de qué valores pueden tomar nuestros datos.

Rango intercuartílico
Otra medida muy común es lo que llamamos el rango intercuartílico, 
que es la diferencia entre el percentil 75 y el percentil 25. 
Este número nos da una idea del rango que tienen los valores más cercanos al valor típico.

En nuestro ejemplo, nuestro rango intercuartílico sería:
"""
rango_inter = df['price'].quantile(.75) - df['price'].quantile(.25)

print(rango_inter)
