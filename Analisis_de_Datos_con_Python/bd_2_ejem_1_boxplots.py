"""
Los boxplots son una manera de visualizar la distribución de nuestros datos usando percentiles.
Vamos a utilizar una librería de visualización de datos llamada Seaborn que hace muy sencilla la creación de boxplots.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('drive-download/melbourne_housing-clean.csv', sep=',', index_col=0)

sns.set(style='whitegrid')
sns.boxplot(x=df['price'])


#df['price'].loc[0]= -2000000 #valor atípico

"""
¿Qué significa todo esto?

La caja está delimitada por 2 valores: El percentil 25 y el percentil 75.
La línea vertical dentro de la caja indica el percentil 50 (o sea, la mediana).
Los "bigotes" intentan abarcar el resto de los datos a la izquierda y derecha de la caja, 
PERO no se extienden más allá de una distancia equivalente a 1.5 * Rango Intercuartílico. 
Como bien recordarás, el rango intercuartílico es la diferencia entre el percentil 75 y el percentil 25. 
Si multiplicamos 1.5 por ese Rango Intercuartílico obtenemos el tamaño máximo de los bigotes.

Los puntos individuales que están fuera de los bigotes son, obviamente, las muestras cuyo valor excede 
el tamaño máximo de los bigotes. No podemos tomar esto como una "Regla Absoluta", 
pero en general se considera que estos valores son los valores atípicos de nuestro conjunto.
Como puedes ver, esta gráfica nos da muchísima información muy útil.

Ahora sabemos que la mayoría de nuestros datos están concentrados en valores menores a 2 000 000 y que los precios 
muy altos son anomalías en nuestro conjunto.
Sabemos que, dentro del rango total de los datos, tenemos una distribución que tiende hacia los valores más pequeños.
También sabemos que nuestros datos en general están muy concentrados (o sea, poco dispersos), 
pero que hay una "colita" de datos hacia la derecha que se extiende bastante lejos.
Vamos a ver qué pasa si graficamos una línea vertical justo donde está el promedio de nuestros datos. 
Para esto vamos a usar matplotlib, otra librería de visualizaciones de datos que aprenderemos a detalle más adelante:
"""



plt.axvline(df['price'].mean(), c='y')

"""
Como puedes ver, a pesar de los valores atípicos tan extremos, tenemos tantos valores en el rango 
menor de nuestros datos que el promedio queda bastante cercano a la mediana.

Los valores atípicos pueden significar múltiples cosas:

A veces son errores de medición
A veces son errores humanos de transcripción
Podrían ser simplemente anomalías naturales causadas por fenómenos aleatorios
O podrían tener un significado más profundo: por ejemplo, la riqueza de alguien como Carlos Slim es una 
anomalía en este país, pero que es un indicador de desigualdad muy fuerte que nos da información útil 
acerca de la distribución de la riqueza
Decidir cómo lidiar con estos valores atípicos (si eliminarlos o dejarlos) depende totalmente del contexto.

Dado que nuestro análisis de este conjunto aún no es muy profundo, por el momento vamos a asumir la posición de 
eliminar estos datos, solamente para ver cómo se haría este proceso.
"""

"""
Rango Intercuartílico y valores atípicos
Podemos utilizar la medida que utiliza el boxplot para limitar el tamaño de los bigotes y filtrar 
todos los datos que excedan ese límite. A esta medida se le suele llamar el Score de Rango Intercuartílico (IQR-Score). 
De esa manera estamos filtrando los valores atípicos (al menos lo que se considera valores atípicos bajo este esquema).
"""

iqr = df['price'].quantile(0.75) - df['price'].quantile(0.25)
filtro_inferior = df['price'] > df['price'].quantile(0.25) - (iqr * 1.5)
filtro_superior = df['price'] < df['price'].quantile(0.75) + (iqr * 1.5)

df_filtrado = df[filtro_inferior & filtro_superior]
sns.boxplot(df_filtrado['price'])
plt.show()

"""
Como ves, el algoritmo de Seaborn debe de ser ligeramente distinto al nuestro, pero el resultado fue prácticamente 
lo que queríamos. Ahora tenemos un conjunto de datos sin valores atípicos.
"""





