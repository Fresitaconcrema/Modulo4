"""
- Aprender a generar tablas de contingencia usando el método `crosstab`
"""

import pandas as pd
df = pd.read_json('../../Datasets/zomato_reviews-clean.json')

"""
Podemos usar el método crosstab para generar tablas de contingencia usando dos de nuestras variables categóricas:

"""

pd.crosstab(df['price_range'], df['user_rating'])

"""
Podemos obtener una columna y una fila con los totales añadiendo la bandera margins y margins_name:
"""

pd.crosstab(df['price_range'], df['user_rating'], margins=True, margins_name='total')

"""
Como puedes observar, el índice está indicando la primera agrupación de nuestros datos (la columna 'price_range'), mientras que las columnas indican la segunda agrupación (la columna 'user_rating').
También podemos añadir una variable categórica más para generar múltiples niveles en las columnas:
"""


pd.crosstab(df['price_range'], [df['has_online_delivery'], df['user_rating']], margins=True, margins_name='total')

"""
Múltiples niveles en columnas
Es un buen momento para aprender a indexar múltiples niveles en columnas. Recordarás que los multiíndices en filas se indexan de la siguiente forma:

df.loc[(primer_indice, segundo_indice)]

Cuando tenemos múltiples niveles en las columnas, simplemente pasamos como primer valor nuestra indexación por filas, y después una tupla con la indexación por columnas:
"""

crosstab = pd.crosstab(df['price_range'], [df['has_online_delivery'], df['user_rating']])
crosstab.loc[:, (0)]
crosstab.loc[:, (1, 'Poor')]

"""
Aquí hemos obtenido la columna 'Poor' del grupo has_online_delivery == 1.
También otra cosa que podríamos hacer es usar el método stack. stack lo que hace es tomar una de nuestras columnas y convertirla en índice. Si le pedimos que haga el stack en el nivel 0, convertirá el nivel 'has_online_delivery' en índice:
"""

crosstab.stack(level=0)
stack_level_0 = crosstab.stack(level=0)
stack_level_0.loc[(2)]
stack_level_0.loc[(2, 1)]

"""
Si hacemos el stack por el nivel 1, obtenemos lo siguiente:
"""
crosstab.stack(level=1)

"""
¡Esto es otro nivel de manipulaciónd de DataFrames!
"""