"""
- Aprender a generar matrices de correlaciones y mapas de calor para cuantificar el coeficiente de
correlación de Pearson de múltiples variables al mismo tiempo.
2. Desarrollo:
Analicemos un poco el siguiente dataset:
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../../Datasets/diabetes-clean.csv', index_col=0)

"""
Este dataset tiene muchas variables numéricas que se prestan a la aplicación de nuestro coeficiente de correlación de Pearson.

Antes de aplicarlo, removeré la variable dependiente ('outcome'), dado que es una variable binaria no apta para este tipo de análisis.
"""

df_filtered = df.drop(columns=['outcome'])
df_filtered.corr()

"""
Tan fácil como esto. Como puedes observar, es un poco difícil discernir las distintas correlaciones de esta manera. 
Digamos que no 'saltan' a la vista.

Un par de cosas que podemos observar es que:

Hay una diagonal de 1s a la mitad de la matriz, donde cada variable se relaciona consigo misma.
Hay redundancia de datos debajo y arriba de la diagonal.
Usemos ahora un mapa de calor para visualizar esta matriz de una manera más fácil de interpretar:
"""

plt.figure(figsize=(8, 6))
ax = sns.heatmap(df_filtered.corr(), vmin=-1, vmax=1, annot=True, cmap="YlGnBu", linewidths=.5)

"""
Resulta mucho más sencillo visualizar las relaciones entre variables, ¿no es así?

¿Qué variables tienen correlaciones negativas? ¿Qué variables tienen correlaciones positivas? ¿Qué variables no tienen correlación?

Recuerda que estamos cuantificando la relación lineal entre dos variables. 
Esto significa que podría existir algún tipo de relación no lineal que no estamos visualizando con este mapa.
"""