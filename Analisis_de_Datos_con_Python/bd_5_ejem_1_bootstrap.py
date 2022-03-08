"""
a) Muestreo aleatorio o randomizado
Una de las maneras en las que normalmente se evitan los sesgos a la hora de tomar muestras es a
través del muestreo aleatorio o randomizado. Esto significa crear una muestra a partir de una población
o de otra muestra eligiendo elementos del conjunto original aleatoriamente.
Cada elemento tiene las mismas posiblidades de ser elegido para la nueva muestra,
a menos que haya una buena razón para hacerlo distinto.

Con este procedimiento intentamos evitar el sesgo de selección.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('drive-download/diabetes-clean.csv', index_col=0)
df.head()

"""
Por ejemplo, vamos a tomar algunas muestras de la variable 'glucose'. 
Un muestreo aleatorio puede tomarse sin reposición, lo cual significa que cada vez que un elemento se toma de la 
muestra original, no se regresa a la muestra original. Con cada muestreo entonces nuestra muestra 
original se hace más pequeña, lo cual en realidad cambia las probabilidades de elegir las muestras restantes:
"""

df['glucose'].sample(n=20, replace=False)

"""
Tambíen podemos tomar elementos con reposición, donde regresamos cada elemento después de tomar la muestra. 
Esto quiere decir que en cada toma tenemos la misma probabilidad de elegir cualquiera de 
los elementos y además el remuestreo puede incluir elementos repetidos:
"""

df['glucose'].sample(frac=0.1, replace=True)

"""
b) Bootstrap
El Bootstrap nos sirve para generar lo que se llaman distribuciones muestrales de estadísticas. 
Esto es un histograma de una medida estadística cuantificada utilizando un gran número de 
remuestreos. ¿Para qué queremos hacer esto? Para calcular la incertidumbre de nuestra medida estadística. 
Dado que no podemos regresar a la fuente original, vamos a crear 'nuevas muestras' a partir de la que tenemos, 
con el fin de simular qué pasaría si regresáramos a la fuente original a tomar más muestras. 
El algoritmo es el siguiente:

Toma un elemento de tu conjunto de datos de manera aleatoria con reposición.
Repite el paso 1 n veces (entre más cerca esté n a la longitud total de tu muestra, más preciso tu cálculo).
Toma la medida estadística que te interese de tus valores remuestreados.
Repite los pasos 1 a 3 R veces (entre mayor sea R, más preciso tu cálculo).
Utiliza las medidas obtenidas para: 
a) Generar un histograma o boxplot 
b) Calcular el error estándar 
c) Calcular un intervalo de confianza
Nuestro cálculo va a resultar más exacto si n y R son lo más grandes posibles. 
Pero el boostrapping es un proceso que toma mucho tiempo y poder computacional, así que si nuestro dataset 
es muy grande habrá que disminuir estos valores hasta que el procedimiento completo tome una cantidad decente de tiempo.

Vamos a realizar estos pasos y llevar a cabo el inciso a del paso 5:
"""

glucose = df['glucose']

means = []

for i in range(100_000):
    sample = glucose.sample(n=50, replace=True)
    means.append(sample.mean())

serie_means = pd.Series(means)

sns.distplot(serie_means, kde=False, norm_hist=False)

"""
c) Teorema del límite central
Existe un teorema matemático llamado Teorema del Limíte Central que establece que las distribuciones muestrales de 
estadísticas van a tender hacia la normalidad. Ésta no es una regla absoluta, 
pero se cumple en muchos casos. En nuestro ejemplo podemos calcular qué tan cerca de la normalidad están 
nuestros promedios muestrales:
"""
serie_means.skew()
serie_means.kurtosis()


"""
Como puedes ver, en este caso se cumple con mucha precisión. Entre más pequeñas sean nuestras 
remuestras, normalmente la curtosis aumenta.

Vamos a preguntarnos:

¿Por qué creen que la curtosis aumente si nuestras remuestras son más pequeñas?
¿Por qué la teoría del límite central suele cumplirse?
¿Qué significa que la distribución muestral de una medida estadística no sea normal? ¿Cómo podemos interpretar ese fenómeno?
"""


