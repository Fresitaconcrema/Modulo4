"""
- Aprender a generar boxplots y violinplots para analizar distribuciones de valores numéricos agrupados usando una variable categórica.

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('white')

df = pd.read_csv('../../Datasets/athlete_olympic_events-clean.csv', index_col=0)

by_athlete = df.groupby(level=0)[['age', 'height', 'weight']].mean()
sex = df.groupby(level=0)['sex'].last()
merged = by_athlete.merge(sex, left_index=True, right_index=True)

#merged

"""
La tabla merged tiene 3 variables numéricas y 1 variable categórica. Ya hemos visto cómo podemos analizar 
la distribución de una variable numérica utilizando boxplots:
"""

sns.boxplot(df['weight'])

"""
Pero dado que tenemos una variable categórica (en este caso binaria, pues tiene solo dos valores posibles), 
podemos utilizar dos boxplots paralelos para analizar la distribución de esta misma variable numérica 
después de ser agrupada utilizando la variable categórica:
"""

plt.figure(figsize=(5, 10))
sns.boxplot(data=merged, x='sex', y='weight')

"""
También podemos explorar las distribuciones usando un violinplot. Un violinplot es muy parecido a un boxplot, 
pero la diferencia es que en vez de graficar frecuencias grafica estimados de densidad. 
¿Recuerdas las gráficas de densidad que utilizamos para hacer los histogramas más 'suaves' y 
poder comparar dos histogramas al mismo tiempo? Bueno, un violinplot es básicamente un boxplot mezclado con una gráfica de densidad.

En un violinplot es mucho más fácil ver ciertos detalles en la distribución de los datos que no es 
posible ver en los boxplots (ya que un boxplot no tiene mucha flexibilidad en cuanto a figuras se refiere). 
En cambio, en un violinplot es mucho más difícil ver los valores atípicos y dónde se encuentran ubicados.
"""

plt.figure(figsize=(5, 10))
sns.violinplot(data=merged, x='sex', y='weight')

"""
La 'pildorita' negra en medio del violinplot representa el Rango Intercuartílico y el punto blanco la mediana. 
Así puedes comparar más fácilmente lo que estamos viendo en esta gráfica con la gráfica anterior.
"""