"""
- Aprender a interpretar el coeficiente de correlación de Pearson
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_style('white')

"""
El coeficiente de correlación de Pearson cuantifica la correlación entre dos variables numéricas. 
Dos variables tienen una correlación si tienen cierta dependencia la una de la otra. 
Este coeficiente sólo mide las relaciones lineales, es decir, que pueden ser representadas con una línea.

El rango de valores posibles es el intervalo entre -1 y 1.

Un valor de -1 significa que hay una correlación negativa perfecta. 
Esto quiere decir que el aumento de una variable resulta en la disminución de la otra; y viceversa. 
Podemos graficar la relación entre dos variables con una gráfica de dispersión, o scatterplot, 
donde cada punto representa la intersección entre un valor de la variable x y un valor de la variable y. 
Si unimos los puntos con una línea que representa la relación entre las dos variables, 
una correlación de -1 se vería de la siguiente manera:
"""
arr_1_1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr_1_2 = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

plt.scatter(arr_1_1, arr_1_2, c='m');
plt.plot(arr_1_1, arr_1_2, c='c');

"""
Un valor de 1 significa que hay una correlación positiva perfecta. 
Esto quiere decir que el aumento de una variable resulta en el aumento de la otra; y la disminución 
de una variable resulta en la disminución de la otra. Esta relación se vería de la siguiente manera:
"""

arr_2_1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr_2_2 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

plt.scatter(arr_2_1, arr_2_2, c='m');
plt.plot(arr_2_1, arr_2_2, c='c');

"""
En cambio, un valor de 0 implica que no existe ninguna correlación entre las variables. Son completamente independientes la una de la otra. Si cada muestra es un punto formado por un valor de la variable x y un valor de la variable y, podríamos visualizar esta falta de relación de esta manera:
"""

arr_3_1 = pd.Series([1, 7, 1, 22, 54, 2, 7, 26, 3, 13, 37, 87, 63, 15, 16, 74, 56, 95, 78, 61, 12, 43, 63, 84])
arr_3_2 = pd.Series([64, 43, 12, 4, 75, 46, 94, 46, 24, 5, 85, 67, 98, 15, 12, 53, 3, 85, 36, 24, 74, 57, 64, 13])

plt.scatter(arr_3_1, arr_3_2, c='m');

"""
Como puedes ver, no hay manera de agregar una línea recta que represente la relación entre las dos variables.
Podemos utilizar el método corr de pandas para calcular el coeficiente de correlación de Pearson:
"""

print(f'Correlación entre las primeras dos Series: {arr_1_1.corr(arr_1_2)}')
print(f'Correlación entre las segundas dos Series: {arr_2_1.corr(arr_2_2)}')
print(f'Correlación entre las terceras dos Series: {arr_3_1.corr(arr_3_2)}')


"""
Obviamente las relaciones entre variables en el mundo real nunca son tan evidentes y perfectas como éstas. El coeficiente de correlación de Pearson simplemente nos ayuda a distinguir la naturaleza de la correlación (si es negativa, positiva o inexistente) y la fuerza de la correlación (qué tan cerca o lejos está de -1 o 1). Este coeficiente no tiene dirección, es decir, si la variable a y la variable b tienen un coeficiente de 8, podemos interpretarlo como que un aumento en la variable a implica comunmente un aumento de la variable b, y también podemos decir que un aumento en la variable b implica comunmente un aumento en la variable a.

- La correlación no implica necesariamente causalidad.

Es decir, el hecho de que haya una correlación alta entre dos variables no significa que una de las variables cause a la otra. Incluso podría suceder que la correlación se deba al azar y en realidad las variables son totalmente independientes la una de la otra.

- El coeficiente de correlación es muy sensible a valores atípicos.

Si hay valores atípicos en nuestro conjunto de datos, esto puede cambiar drásticamente el valor de nuestro coeficiente. Es por eso que siempre es importante trabajar con nuestros valores atípicos antes de investigar la relación entre las variables.

Veamos en el siguiente Reto qué tan bueno eres para interpretar gráficas de relaciones entre variables.

"""