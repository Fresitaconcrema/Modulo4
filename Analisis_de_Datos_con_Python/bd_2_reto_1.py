"""
- Aprender a graficar e interpretar boxplots utilizando Seaborn
- Aprender a lidiar con valores atípicos usando IQR-Score

a) Usando boxplots para analizar la distribución de nuestros datos
Vamos a hacer algunas gráficas de boxplot y describirlas en equipo.
Usa Seaborn para generar gráficas boxplot de los siguientes datasets y columnas:

Dataset: 'near_earth_objects-jan_feb_1995-clean.csv'
Columnas a graficar: 'estimated_diameter.meters.estimated_diameter_max' y
'relative_velocity.kilometers_per_second'

Dataset: 'new_york_times_bestsellers-clean.json'
Columnas a graficar: 'price.numberDouble'

Dataset: 'melbourne_housing-clean.csv'
Columnas a graficar: 'land_size'

Para conocer más detalles acerca de estos datasets, ve a Datasets/Readme.md y
visita los links de las fuentes de donde provienen. Es una gran idea hacer esto
para que entiendas el contexto alrededor de los análisis que vamos a estar realizando.

Realiza estas 4 visualizaciones y comenta con la experta y tus compañeros qué
conclusiones o hipótesis podemos hacer sobre nuestros datos.
Para profundizar en el análisis puedes obtener también el rango, la mediana, el valor mínimo
y máximo, el percentil 25 y el percentil 75. De esta manera tendrás valores concretos
con los que realizar tu análisis
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_1 = pd.read_csv('drive-download/near_earth_objects-jan_feb_1995-clean.csv', sep=',', index_col=0)
diameter_col = 'estimated_diameter.meters.estimated_diameter_max'
kms_per_second_col = 'relative_velocity.kilometers_per_second'

#df_2 = pd.read_csv('drive-download/new_york_times_bestsellers-clean.json')
#price_col = 'price.numberDouble'

df_3 = pd.read_csv('drive-download/melbourne_housing-clean.csv', sep=',', index_col=0)
size_col = 'land_size'

rango_diametro = df_1[diameter_col].max() - df_1[diameter_col].min()
print(f'Rango Diametro: {rango_diametro}')
print(f'Diametro Max: {df_1[diameter_col].max()}')
print(f'Diametro Min: {df_1[diameter_col].min()}')
print(f'Diametro Median: {df_1[diameter_col].median()}')
print(f'Diametro Quantile 25: {df_1[diameter_col].quantile(.25)}')
print(f'Diametro Quantile 75: {df_1[diameter_col].quantile(.75)}')

sns.set(style='whitegrid')
sns.boxplot(x=df_1[diameter_col])
plt.show()

sns.set(style='whitegrid')
sns.boxplot(x=df_3[size_col])
plt.show()

"""
b) Eliminando valores atípicos
A partir de las visualizaciones que realizaste en el punto anterior, 
decide en cuáles columnas tenemos valores atípicos que pueden estorbarnos en nuestro análisis. 
Elimina dichos valores atípicos usando el Score de Rango Intercuartílico. 
Puedes probar variando un poco la medida del Score (1.5 * IQR) para eliminar solamente los valores que tú consideras como extremos.

Para observar los cambios a detalle, obtén la mediana, la media y la desviación estándar 
de tus datos antes y después de eliminar los valores atípicos. 
Compara estos valores y explica qué es lo que está pasando.

Grafica de nuevo tus datos sin valores atípicos para compararlos con las gráficas anteriores.

Comenta con la experta y tus compañeros tus hallazgos.
"""

iqr = df_1[diameter_col].quantile(0.75) - df_1[diameter_col].quantile(0.25)
filtro_inferior = df_1[diameter_col] > df_1[diameter_col].quantile(0.25) - (iqr * 1.5)
filtro_superior = df_1[diameter_col] < df_1[diameter_col].quantile(0.75) + (iqr * 1.5)

df_filtrado_1 = df_1[filtro_inferior & filtro_superior]
sns.boxplot(df_filtrado_1[diameter_col])
plt.show()