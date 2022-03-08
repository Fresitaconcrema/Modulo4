"""
- Aprender cómo dividir nuestro dataset en dos para entrenar nuestro modelo y probarlo utilizando diferentes datos.
- Aprender a entrenar un modelo de Regresión Linear Múltiple

a) Regresión Linear Múltiple
Vamos a combinar esta técnica con un modelo de Regresión Linear Múltiple.
La Regresión Linear Múltiple es básicamente lo mismo que la Regresión Linear Simple, con la diferencia de
que podemos utilizar más de una variable independiente y dependiente.
Es más difícil (y a veces en realidad imposible) visualizar la función lineal que obtenemos a través de una
Regresión Linear Múltiple, puesto que la línea que representa es una línea que se encuentra en ¡más de dos dimensiones!
Pero el concepto es el mismo: utilizamos una o más variables independientes para entrenar un modelo,
con el objetivo de encontrar una función lineal que pueda predecir a una o más variables dependientes.

Por suerte, el proceso de entrenamiento es en realidad el mismo, así que podemos concentrarnos en aprender
a dividir nuestro dataset en entrenamiento y prueba.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('drive-download/diabetes-clean.csv', index_col=0)

df.isna().sum()
df = df.drop(columns=['outcome'])

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True)

plt.show()

"""
Ahora vamos a utilizar este método de scikit learn para dividir nuestro dataset en dos. 
Voy a entrenar un modelo para intentar predecir los niveles de insulina en una persona utilizando las 
variables 'glucose' y 'skin_thickness', así que mi variable dependiente será 'glucose' y mis variables independientes 
serán las otras dos.
"""

from sklearn.model_selection import train_test_split
X = df[['glucose', 'skin_thickness']]
y = df['insulin']

X_training, X_test, y_training, y_test = train_test_split(X, y, test_size=0.3, shuffle=True)

"""
Nota el tamaño del dataset de prueba (30% del total) y que estamos revolviendo el dataset aleatoriamente 
antes de realizar la división
"""

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_training, y_training)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

lr.score(X_test, y_test)

"""
Como puedes ver, nuestro R2 es menor incluso que los coeficientes de correlación que 
tienen ambas variables independientes con la dependiente. 
Esto significa que nuestra precisión no es necesariamente 'acumulativa'.

Mira lo que sucede si entrenamos nuestro modelo sin hacer la división de entrenamiento y prueba:
"""
lr_2 = LinearRegression()
lr_2.fit(X, y)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

lr_2.score(X, y)

"""
Obtenemos un score ligeramente mejor. Aunque en este caso no resulta tan relevante porque de todas maneras 
el poder predictivo es prácticamente nulo, nos demuestra que el modelo puede a veces aprender a predecir 
correctamente los datos que conoce y generalizar muy mal a datos que no conoce.
"""
