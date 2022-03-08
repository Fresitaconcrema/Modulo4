"""
- Aprender a generar varias gráficas al mismo tiempo para hacer comparaciones.
Tomemos la primera tabla de contingencia del Ejemplo pasado para graficarla:
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

df = pd.read_json('../../Datasets/zomato_reviews-clean.json')

crosstab = pd.crosstab(df['price_range'], df['user_rating'])

"""
¿Recuerdas el objeto figure? Bueno, si figure es el objeto que contiene nuestras gráficas, los objetos axes son los encargados de dibujar cada una de las gráficas. figure contiene axes y nuestras gráficas se dibujan sobre los axes.

Usando el método subplots, podemos generar al mismo tiempo una nueva figura y múltiples axes que están contenidos en esa figura:
"""

fig, axes = plt.subplots(2, 2)

"""
Le pasamos a subplots la estructura de nuestra 'tabla' de gráficas. En este caso, le indicamos un entramado de 2 x 2 porque tenemos 4 valores en el primer nivel.

Grafiquemos:
"""

fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=True)

sns.barplot(crosstab.columns, crosstab.loc[1], ax=axes[0, 0])
sns.barplot(crosstab.columns, crosstab.loc[2], ax=axes[0, 1])
sns.barplot(crosstab.columns, crosstab.loc[3], ax=axes[1, 0])
sns.barplot(crosstab.columns, crosstab.loc[4], ax=axes[1, 1])

axes[0, 0].set(xlabel='', ylabel='', title='Rango de Precio: 1')
axes[0, 1].set(xlabel='', ylabel='', title='Rango de Precio: 2')
axes[1, 0].set(xlabel='', ylabel='', title='Rango de Precio: 3')
axes[1, 1].set(xlabel='', ylabel='', title='Rango de Precio: 4')

fig.suptitle('Ratings de restaurantes separados por rango de precio', fontsize=15)

"""
Cosas importantes a notar:

Agregamos las banderas sharex y sharey porque tenemos el mismo eje x para todas nuestras gráficas y porque queremos comparar las gráficas una contra otra. Si nuestro eje y no fuera igual para todas, sería más difícil comparar usando sólo la vista.
La variable axes contiene un arreglo de dos dimensiones con cada uno de nuestros ax (el contenedor de cada gráfica). Así como accedemos a cualquier arreglo de 2 dimensiones, acceder a un ax se lleva a cabo de esta manera: axes[0, 1].
Eliminamos los xlabels y los ylabels porque no son muy informativos y generan ruido visual. En cambio, cada gráfica necesita un título para saber a qué categoría del primer nivel pertenece.
Agregamos un título a la figure (en lugar de al ax) usando el método suptitle.
"""