#a) Desviación estándar y distribución de los datos
#Como ya vimos, la desviación estándar es la medida que nos da la "desviación típica" (o esperada) de nuestros datos a comparación del promedio.
# Eso quiere decir que normalmente vamos a esperar que una gran parte de nuestros datos se encuentren a 1 desviación estándar de distancia del promedio. Entre más nos alejamos, menos muestras deberíamos de encontrar.

#Vamos a comprobar esto usando nuestro dataset de meteoritos que orbitan cerca de la Tierra. Tu Reto consiste en los siguientes pasos:

#Crea un DataFrame con el dataset 'near_earth_objects-jan_feb_1995-clean.csv'.
#Obtén la cantidad total de muestras en tu DataFrame.
#Obtén la desviación estándar de la columna 'estimated_diameter.meters.estimated_diameter_max'. Los siguientes pasos realízalos todos utilizando esta columna.
#Obtén el porcentaje de muestras que están a una distancia de 1 desviación estándar del promedio.
#Obtén el porcentaje de muestras que están a una distancia de 2 desviaciones estándares del promedio.
#Obtén el porcentaje de muestras que están a una distancia de 3 desviaciones estándares del promedio.
#Compara los porcentajes obtenidos y comenta con tus compañeros y la experta tus hallazgos. ¿Qué significa esto? ¿La definición de desviación estándar tiene sentido? ¿Qué puedo inferir acerca de la dispersión de mis datos a partir de los valores obtenidos?
#Nota: Para obtener los porcentajes de los subconjuntos primero necesitas filtrar el DataFrame original para que sólo permanezcan las muestras que cumplan con los requisitos.

#Nota: Este Reto está diseñado para tener una dificultad media. No te frustres si al principio parece demasiado difícil. Comienza poco a poco, resolviendo el problema en pedazos pequeños, y si no tienes la menor idea de cómo proceder recuerda que la experta está ahí para ayudarte.

import pandas as pd

df = pd.read_csv('drive-download/Remoto near_earth_objects-jan_feb_1995-clean.csv', sep=',')

n = df.shape[0]

std = df['estimated_diameter.meters.estimated_diameter_max'].std()
std = df['estimated_diameter.meters.estimated_diameter_max'].mean()

IR = mean + std
IL = mean - std

column = 'estimated_diameter.meters.estimated_diameter_max'

len(df[(df[column] < IR) & (df[column] > IL)])/n
IR = mean + 2 * std
IL = mean - 2 * std

len(df[(df[column] < IR) & (df[column] > IL)])/n

IR = mean + 3 * std\n
IL = mean - 3 * std"

import pandas as pd
df = pd.read_csv('../../Datasets/near_earth_objects-jan_feb_1995-clean.csv', index_col=0)
diameter_column = 'estimated_diameter.meters.estimated_diameter_max'
total_count = df.shape[0]
mean = df[diameter_column].mean()
std = df[diameter_column].std()
within_one_std_filter_bottom = df[diameter_column] >= (mean - std)
within_one_std_filter_top = df[diameter_column] <= (mean + std)
within_one_std = df[within_one_std_filter_bottom & within_one_std_filter_top]
percentage_of_data_within_one_std = within_one_std.shape[0] * 100 / total_count
within_two_std_filter_bottom = df[diameter_column] >= (mean - 2 * std)
within_two_std_filter_top = df[diameter_column] <= (mean + 2 * std)
within_two_std = df[within_two_std_filter_bottom & within_two_std_filter_top]
percentage_of_data_within_two_std = within_two_std.shape[0] * 100 / total_count
within_three_std_filter_bottom = df[diameter_column] >= (mean - 3 * std)
within_three_std_filter_top = df[diameter_column] <= (mean + 3 * std)
within_three_std = df[within_three_std_filter_bottom & within_three_std_filter_top]
percentage_of_data_within_three_std = within_three_std.shape[0] * 100 / total_count