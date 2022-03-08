"""
a) Error estándar
Recordarás que la desviación estándar es una medida de dispersión de nuestros datos.
Bueno, pues el error estándar es la desviación estándar de nuestra serie de medidas estadísticas:
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('drive-download/diabetes-clean.csv', index_col=0)

df.head()

glucose = df['glucose']

means = []

for i in range(100_000):
    sample = glucose.sample(n=50, replace=True)
    means.append(sample.mean())

serie_means = pd.Series(means)

print(f'Error estandar: {serie_means.std()}')

"""
Recuerda que para poder interpretar correctamente la desviación estándar tienes que saber un poco acerca del rango y distribución de tus datos:
"""

print(f'Valor mínimo: {serie_means.min()}')
print(f'Valor máximo: {serie_means.max()}')
print(f'Rango: {serie_means.max() - serie_means.min()}')

"""
Vamos a preguntarnos:

¿Cómo podemos interpretar la desviación estándar? ¿Qué implica una mayor o menor desviación estándar?
¿Por qué necesitamos saber el rango de nuestros datos para interpretar correctamente la desviación estándar?
¿En este caso específico qué significa la desviación estándar que obtuvimos?
b) Intervalos de confianza
Los intervalos de confianza son una manera de cuantificar la incertidumbre que existe en nuestra medida estadística. Si pudiéramos regresar a nuesta fuente original a tomar más muestras, el intervalo de confianza sería el intervalo numérico en el cual podemos asegurar con cierto nivel de seguridad que caería nuestra nueva medición estadística.

Para obtener un intervalo de 95% de confianza, por ejemplo, tenemos que tomar nuestro histograma, removerle 2.5% de valores al principio y al final, y obtener los nuevos valores mínimo y máximo. De esta manera el 95% de los valores originales quedan dentro de este nuevo intervalo.

Podemos obtener nuestro intervalo de confianza utilizando cuantiles:


"""
limite_inferior = serie_means.quantile(0.025)
limite_superior = serie_means.quantile(0.975)

"""
Podemos escribir nuestro intervalo de confianza de dos maneras distintas:
"""
print(f'Intervalo de 95% confianza de la media: {limite_inferior} < {glucose.mean()} < {limite_superior}')


mean_of_intervals = ((glucose.mean() - limite_inferior) + (limite_superior - glucose.mean())) / 2

print(f'Intervalo de 95% confianza de la media: {glucose.mean()} +/- {mean_of_intervals}')

"""
Podemos visualizar estos límites también:
"""
sns.distplot(serie_means, kde=False, norm_hist=False)
plt.axvline(limite_inferior)
plt.axvline(limite_superior)


