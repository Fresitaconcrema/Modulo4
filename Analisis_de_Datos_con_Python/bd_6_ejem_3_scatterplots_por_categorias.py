import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../Datasets/athlete_olympic_events-clean.csv', index_col=0)

df.head()

df_grouped = df.groupby('name')[['height', 'weight', 'sex', 'team', 'sport']].max()

china = df_grouped[df_grouped['team'] == 'China']

"""
He aquí una gráfica de dispersión para observar la relación entre las variables 'weight' y 'height' de los atletas chinos que han participado en Olimpiadas:
"""

sns.scatterplot(china['height'], china['weight']);

"""
Si queremos hacer una visualización comparativa entre los atletas hombres y mujeres de nuestro dataset de China, podemos entonces colorear nuestros puntos de acuerdo a la variable 'sex':
"""


sns.scatterplot(china['height'], china['weight'], hue=china['sex'])
sns.scatterplot(china['height'], china['weight'], hue=china['sex'], style=china['sex'])


"""
Esta gráfica nos hace ver con mucha claridad que sí hay una diferencia cuantificable entre los pesos y alturas de atletas masculinos y femeninos. También genera preguntas interesantes. Por ejemplo: ¿qué deporte realizan las atletas mujeres que tienen pesos cercanos al peso máximo?
"""

china[(china['sex'] == 'F') & (china['weight'] > 120)]


"""
¡Como era de esperarse, los pesos pesados entre las atletas mujeres de China hacen practican alterofilia y judo!
"""


