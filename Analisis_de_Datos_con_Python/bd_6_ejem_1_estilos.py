%matplotlib inline
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../Datasets/melbourne_housing-clean.csv', index_col=0)

sns.distplot(df['price'], kde=False, norm_hist=False)

"""
Seaborn y matplotib incluyen algunos estilos predefinidos que podemos usar para cambiar el estilo visual de nuestras gráficas:
"""


sns.set_style('white')

sns.distplot(df['price'], kde=False, norm_hist=False)

sns.set_style('whitegrid')

sns.distplot(df['price'], kde=False, norm_hist=False)

sns.set_style('darkgrid')

sns.distplot(df['price'], kde=False, norm_hist=False)

plt.style.use('fivethirtyeight')

sns.distplot(df['price'], kde=False, norm_hist=False)

plt.style.use('ggplot')

sns.distplot(df['price'], kde=False, norm_hist=False)

plt.style.use('classic')

sns.distplot(df['price'], kde=False, norm_hist=False)

plt.style.use('default')

"""
También podemos usar estilos de manera 'temporal'. Esto quiere decir que el estilo sólo aplica a las gráficas que realicemos dentro de la sentencia with:
"""

with sns.axes_style('ticks'):
    sns.distplot(df['price'], kde=False, norm_hist=False)

with plt.style.context('seaborn-bright'):
    sns.distplot(df['price'], kde=False, norm_hist=False)

"""
Hay veces que tenemos que modificar nuestros estilos manualmente para obtener algo altamente personalizado, 
pero vale la pena echarle un ojo a los estilos predefinidos. 
A veces pueden ser justo lo que necesitas. Puedes encontrar listas completas de estilos aquí para Seaborn y aquí para Matpotlib.
"""