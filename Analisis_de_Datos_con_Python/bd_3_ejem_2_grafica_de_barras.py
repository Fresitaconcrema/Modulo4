"""
- Aprender a realizar gráficas de barras con frecuencias y porcentajes


"""
import pandas as pd
import seaborn as sns
sns.set_style('white')

df = pd.read_json('../../Datasets/zomato_reviews-clean.json')

"""
En este dataset tenemos una variable llamada 'user_rating' que es categórica. 
Para saber si es categórica podemos primero revisar con el método unique para ver todos los 
valores únicos contenidos en esa columna:
"""
df['user_rating'].unique()
array(['Very Good', 'Excellent', 'Poor', 'Good', 'Average', 'Not rated'],
      dtype=object)

df['user_rating'].nunique()

"""
nunique nos da el número de categorías que tenemos.

Ahora, para poder graficar nuestra variable como gráfica de barras necesitamos los conteos 
de frecuencias de cada categoría (es decir, cuántas veces aparece cada categoría. 
Para eso pandas nos ofrece un método llamado value_counts:
"""
df['user_rating'].value_counts()

"""
El método nos regresa una Serie con los nombres de la categorías como índices y los conteos como valores. 
Esta tabla la podemos usar para generar nuestra gráfica:
"""

counts = df['user_rating'].value_counts()
ax = sns.barplot(counts.index, counts)
ax.set_title('Conteo de Ratings de restaurantes')
ax.set(ylabel='count')

"""
Ahora, si queremos que el eje y sean porcentajes en vez de conteos, podemos simplemente transformar 
nuestra Serie counts con una simple regla de 3:
"""

counts * 100 / counts.sum()
as_percentages = counts * 100 / counts.sum()

ax = sns.barplot(as_percentages.index, as_percentages)
ax.set_title('Conteo de Ratings de restaurantes(como porcentajes)')
ax.set(ylabel='porcentaje del total');

"""
Si quieres acomodar los nombres de tus tics en el eje x, puedes utilizar el siguiente código para cambiarles la rotación:
"""

ax = sns.barplot(as_percentages.index, as_percentages)
ax.set_title('Conteo de Ratings de restaurantes(como porcentajes)')
ax.set(ylabel='porcentaje del total')
ax.set_xticklabels(ax.get_xticklabels(), rotation=50);

"""
En este caso no había mucha necesidad de rotar los nombres, pero hay veces que rotar los nombres y/o cambiar 
el tamaño de la gráfica es la única manera de hacerlos comprensibles.

Hay veces que resulta más cómodo y comprensible acomodar nuestras barras de manera horizontal. 
Esto puede hacerse muy fácilmente agregando la bandera orient='h' y cambiando el orden de nuestros inputs:
"""

ax = sns.barplot(as_percentages, as_percentages.index, orient='h')
ax.set_title('Conteo de Ratings de restaurantes(como porcentajes)')
ax.set(xlabel='porcentaje del total');

"""
La Moda
La moda es el "valor típico" de nuestra variable categórica. Representa la categoría que más veces aparece 
en nuestro conjunto de datos.

Podemos extraer la moda de la tabla de value_counts o de la gráfica de barras, pero pandas también 
ofrece un método para obtenerla fácilmente:
"""

df['user_rating'].mode()