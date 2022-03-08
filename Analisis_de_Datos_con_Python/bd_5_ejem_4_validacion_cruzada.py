"""
- Aplicar la validación cruzada para evaluar un modelo predictivo

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('drive-download/diabetes-clean.csv', index_col=0)

df = df.drop(columns=['outcome'])

X = df[['glucose', 'skin_thickness']]
y = df['insulin']

"""
Validación Cruzada de K-Iteraciones
Hay muchas maneras de aplicar esta técnica. El algoritmo que vamos a aprender hoy se llama Validación Cruzada 
de K-Iteraciones. Consta de los siguientes pasos:

Tomamos nuestro dataset y lo revolvemos aleatoriamente.

Decidimos un número K que va a ser el número de subdivisiones en el que vamos a dividir a nuestro dataset.

Para el primer entrenamiento, dejamos fuera la primera sección. Entrenamos usando la secciones restantes, 
probamos el modelo entrenado con la primera sección y evaluamos su desempeño.

Volvemos a entrenar nuestro modelo, pero esta vez dejando fuera la segunda sección como dataset prueba. 
Entrenamos, probamos con la segunda sección y evaluamos el desempeño del modelo.

Repetimos el proceso K veces. En cada iteración dejamos la sección siguiente como dataset de prueba.

Tomamos todas las evaluaciones de los K entrenamientos (que en el caso de una Regresión Lineal Múltiple podrían ser 
coeficientes de determinación) y sacamos el promedio y la desviación estándar. 
Esto servirá como una medida del "valor típico" de desempeño y la incertidumbre que tiene nuestro modelo.
"""

from sklearn.model_selection import cross_validate
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
scores = cross_validate(lr, X, y, scoring='r2')

print(f'Score del modelo: {scores["test_score"].mean():.3f} +/- {scores["test_score"].std():.3f}')


