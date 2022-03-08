"""
Las gráficas de dispersión, como ya viste en los ejemplos anteriores, nos ayudan a visualizar la relación entre dos variables numéricas. Veamos unos ejemplos:
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../Datasets/diabetes-clean.csv', index_col=0)

"""
Vimos que insulina y glucosa tenían una correlación positiva de 0.33. 
Esta correlación lineal es bastante débil en realidad. Así se ven ambas variables en una gráfica de dispersión:
"""

sns.scatterplot(df['insulin'], df['glucose'])
df['insulin'].corr(df['glucose'])
"""

Podemos ver algo curioso en esta gráfica: En el valor 0 de 'insulin', podemos observar que los valores 'glucose' encontrados abarcan todo el rango posible. Esto es algo extraño. A menos que uno de ustedes sea doctor y sepa que esto tiene sentido, creo que podríamos elaborar la hipótesis de que los valores 0 en 'insulin' representan una falta de datos o un error de medición y no un valor real. Esta hipótesis la podemos elaborar simplemente al observar que la gráfica tiene una anomalía en ese lugar. Veamos qué pasa si removemos los valores 0 en 'insulin':

"""
df_no_zeros = df[df['insulin'] > 0]
sns.scatterplot(df_no_zeros['insulin'], df_no_zeros['glucose'])
df_no_zeros['insulin'].corr(df_no_zeros['glucose'])

"""
Interesante, ¿no crees? Obviamente para realizar una hipótesis coherente necesitaríamos ser médicos (si alguien es médico aquí, por favor demuestre que hemos cometido un grave error), pero como puedes ver, tan sólo con visualizar la relación entre estos dos datos ya vimos algunas preguntas emerger.

Veamos qué hay entre las variables 'bmi' y 'glucose':
"""
sns.scatterplot(df['bmi'], df['glucose'])
df['bmi'].corr(df['glucose'])

"""
Otra vez tenemos este fenómeno extraño donde hay algunos valores en 0 que seguramente están ahí por error. También vamos a realizar una pequeña apuesta y eliminar algunos valores de 'bmi' que parecen ser atípicos. Veamos cómo cambia nuestra gráfica:
"""

bmi_greater_than_zero = (df['bmi'] > 0) & (df['bmi'] < 55)
glucose_greater_than_zero = df['glucose'] > 0
df_no_zeros_2 = df[bmi_greater_than_zero & glucose_greater_than_zero]
sns.scatterplot(df_no_zeros_2['bmi'], df_no_zeros_2['glucose'])
df_no_zeros_2['bmi'].corr(df_no_zeros_2['glucose'])

"""
En este caso nuestro coeficiente de correlación mejoró pero no mucho. Es notable que la relación entre estas dos variables es bastante débil (si es que existe).

Vamos a revisar 'insulin' y 'skin_thickness' que tuvieron un coeficiente de 0.44:
"""

sns.scatterplot(df['insulin'], df['skin_thickness'])
df['insulin'].corr(df['skin_thickness'])

"""
Ya sabemos que insulin tiene valores 0 que probablemente sean erróneos, así que usaremos nuestro DataFrame df_no_zeros para eliminarlos:
"""

sns.scatterplot(df_no_zeros['insulin'], df_no_zeros['skin_thickness'])
df_no_zeros['insulin'].corr(df_no_zeros['skin_thickness'])

"""
¡¿Qué ha pasado aquí?! Un coeficiente de 0.4367 disminuyó a 0.1848 cuando eliminamos algunos valores que creemos son erróneos. Esto es una gran demostración de cómo nunca podemos confiar en una sola medida para realizar nuestras hipótesis. Con este dataset la verdad es que estamos explorando un poco a ciegas porque se requiere de conocimientos muy especializados para entender qué está pasando en realidad, pero resulta interesante que aún sin saber exactamente qué significan las variables, de todas maneras podemos encontrar comportamientos que generan muchas preguntas.

Otra pregunta que me interesa plantearme es si acaso la relación entre estas dos variables podría mejorar si eliminamos los valores atípicos de 'insulin':
"""

sns.boxplot(df_no_zeros['insulin'])
iqr_insulin = df_no_zeros['insulin'].quantile(0.75) - df_no_zeros['insulin'].quantile(0.25)
filter_upper_outliers = df_no_zeros['insulin'] < (df_no_zeros['insulin'].quantile(0.75) + iqr_insulin * 1.5)
df_insulin_no_outliers = df_no_zeros[filter_upper_outliers]
sns.scatterplot(df_insulin_no_outliers['insulin'], df_insulin_no_outliers['skin_thickness'])
df_insulin_no_outliers['insulin'].corr(df_insulin_no_outliers['skin_thickness'])

"""
Después de este procedimiento quedo bastante convencido de que la correlación positiva que habíamos encontrado anteriormente no era real. Ojalá y esto haya sido una demostración del cuidado que debemos de tener al explorar nuestras variables y las relaciones entre ellas.
"""