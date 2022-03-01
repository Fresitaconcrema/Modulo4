from scipy import stats
import pandas as pd

#La media truncada es un estimado de locación más robusto que el promedio y la mediana. Esto significa que es menos sensible a valores atípicos. La media truncada se obtiene de la siguiente manera:

#Primero ordenamos nuestro conjunto de manera ascendente.
#Después decidimos qué porcentaje de nuestros datos vamos a truncar. Los valores más comunes suelen variar entre 5% y 25%.
#Divide el porcentaje acordado entre dos y elimina esa fracción de tus datos del inicio y del final de tu secuencia. Por ejemplo, si decides truncar un 5%, elimina el 2.5% de tus datos del inicio de tu secuencia y el otro 2.5% del final de tu secuencia.
#Obtén el promedio de los valores restantes.

df = pd.read_csv('../../Datasets/melbourne_housing-clean.csv', index_col=0)

stats.trim_mean(df['price'], 0.1)

df['price'].mean()

df['price'].median()