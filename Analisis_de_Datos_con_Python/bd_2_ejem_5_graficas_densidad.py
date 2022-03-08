"""
Podemos obtener gráficas de densidad usando el método distplot de Seaborn,
sólo cambiando los argumentos que le pasamos:
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


sns.set(style='whitegrid')

laplace = np.random.laplace(loc=0.0, scale=1, size=10000)
sns.distplot(laplace, hist=False)
plt.show()

chisquare = np.random.chisquare(4, size=10000)
sns.distplot(chisquare, hist=False)
plt.show()

"""
Las gráficas de densidad son muy útiles para graficar varias distribuciones en la misma gráfica y poderlas comparar:
"""
sns.set(style='white')

normal_1 = np.random.normal(loc=-2, scale=3, size=10000)
normal_2 = np.random.normal(loc=4.5, scale=1, size=10000)
exponential = np.random.exponential(scale=1.0, size=10000) - 1

sns.distplot(normal_1, hist = False, kde_kws = {'shade': True})
sns.distplot(normal_2, hist = False, kde_kws = {'shade': True})
sns.distplot(exponential, hist = False, kde_kws = {'shade': True})
plt.show()

"""
Como puedes ver, usando gráficas de densidad obtenemos mucha claridad en la comparación. 
En este ejemplo agregamos la bandera kde_kws = {'shade': True} para obtener el color de relleno de cada distribución. 
En una sesión posterior aprenderemos cómo estilizar nuestras gráficas a profundidad.
"""





