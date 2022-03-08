"""
a) Percentiles para evaluar la dispersión de nuestros datos
Tienes debajo 4 series. Cada una de esas series contiene un conjunto de datos conformado por números enteros
en el intervalo de 1 a 10. Los datos en cada una de estas series tienen un tipo de dispersión distinta.
Los valores típicos cambian así como los valores atípicos. Las medianas también son diferentes.

Usando percentiles, obtén información acerca de cuál es el valor donde están concentrados nuestros datos y
cómo está configurada su dispersión. Entre más percentiles utilices, obtienes una descripción más detallada,
pero como el dataset es muy pequeño, no necesitas tanta granularidad.

Obtén los percentiles y comenta con la experta y tus compañeros qué cosas podemos inferir acerca de nuestros datos
utilizando estos valores.
"""

import pandas as pd

serie_1 = pd.Series([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10])
serie_2 = pd.Series([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
serie_3 = pd.Series([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10])
serie_4 = pd.Series([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10])

print(f'Mean: {serie_1.mean()} y mediana {serie_1.median()}')
print(f'Percentil 80: {serie_1.quantile(.80)}')

print(f'Mean: {serie_2.mean()} y mediana {serie_2.median()}')
print(f'Percentil 80: {serie_1.quantile(.75)}')

print(f'Mean: {serie_3.mean()} y mediana {serie_3.median()}')
print(f'Percentil 80: {serie_1.quantile(.25)}')

print(f'Mean: {serie_4.mean()} y mediana {serie_4.median()}')
print(f'Percentil 80: {serie_1.quantile(.10)}')


"""
b) Percentiles para evaluar nuestro dataset de meteoritos
Ahora vamos a aplicar los percentiles a nuestro dataset de objetos que han orbitado cerca de la Tierra. 
Queremos entender cómo están organizados nuestros datos.

En el Reto pasado, usamos la desviación estándar para obtener la "desviación esperada" de nuestros datos. 
Aprendimos que la mayoría de nuestros datos están a una distancia de 1 desviación estándar o menos del promedio. 
Entre más desviaciones estándares añadíamos, menos datos quedaban fuera de nuestros subconjuntos. 
Lo que no sabemos es dónde están concentrados nuestros datos.

Piensa en lo siguiente:

Si tenemos un dataset con rango de 1 a 10, y nuestra desviación estándar es 2.5, los datos pueden estar organizados 
de maneras muy distintas:

Podría ser que el promedio es 3 y que la mayoría de los datos están en el rango de 0.5 a 5.5. 
En este caso podría haber datos muy distintos al resto en el parte superior del rango total (los valores entre 5.5 y 10).

Podría ser que el promedio es 7 y que la mayoría de los datos están en el rango de 4.5 a 9.5. 
En este caso los datos atípicos estarían concentrados en la parte inferior del rango total.

Podría ser que el promedio es 5 y que la mayoría de los datos están concentrados en el rango de 2.5 a 7.5. 
En este caso, lo más normal es que los datos estén alrededor del valor que está justo a la mitad del rango total 
y es cada vez más raro encontrar datos muy pequeños o muy grandes.

Hay muchas otras posibilidades, pero lo importante es darse cuenta de que saber solamente la desviación estándar 
nos da aún una descripción muy ambigua de nuestros datos. 

Saber el promedio ya es un primer indicador de lo que está pasando en realidad. 
Pero saber además los percentiles nos puede dar una idea muchísimo más clara de cómo están acomodados nuestros datos.

Lee el dataset 'near_earth_objects-jan_feb_1995-clean.csv' y obtén percentiles de 
la columna 'estimated_diameter.meters.estimated_diameter_max'. 
Comenta con tus compañeros y con la experta tus hallazgos y tus hipótesis acerca de qué 
podemos aprender sobre la organización de nuestros datos usando los percentiles.
"""

df = pd.read_csv('drive-download/near_earth_objects-jan_feb_1995-clean.csv', index_col=0)
diameter_col = 'estimated_diameter.meters.estimated_diameter_max'

print("\n near_earth_objects-jan_feb_1995 \n")
#print(df[diameter_col].head())
print(f'Mean: {df[diameter_col].mean()} and Median: {df[diameter_col].median()}')
print(f'Min Value: {df[diameter_col].min()} and Max Value: {df[diameter_col].max()}')
print(f'Percentil 10: {df[diameter_col].quantile(.10)}')
print(f'Percentil 25: {df[diameter_col].quantile(.25)}')
print(f'Percentil 75: {df[diameter_col].quantile(.75)}')
print(f'Percentil 90: {df[diameter_col].quantile(.90)}')






