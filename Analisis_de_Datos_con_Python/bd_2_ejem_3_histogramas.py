"""
Vamos a generar un histograma segmentando nuestros datos en 20 segmentos (o bins).
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('drive-download/melbourne_housing-clean.csv', index_col=0)

sns.set(style='white')
sns.distplot(x=df['price'], kde=False, norm_hist=False, bins=20)
plt.show()

"""
La bandera kde=False evita que se grafique también la densidad de probabilidad (que veremos más adelante).
norm_hist=False sirve para que nuestro eje 'y' indique los conteos de nuestros segmentos.
bins=20 indica el número de segmentos.
Esta gráfica indica con mucha claridad hacia donde "tienden" nuestros datos, ¿no es así?

Podemos ver mucha más granularidad incluso si aumentamos el tamaño de nuestros bins:
"""

sns.set(style='ticks')
sns.distplot(df['price'], kde=False, norm_hist=False, bins=100)
plt.show()