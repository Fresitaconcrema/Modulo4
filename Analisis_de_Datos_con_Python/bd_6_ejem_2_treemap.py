import plotly.express as px
import pandas as pd

"""
Existen dos maneras de generar treemaps. La primera solamente es una manera de visualizar una jerarquía. Usando plotly.express podemos visualizar jerarquías tipo estructura de árbol.

Por ejemplo, tenemos esta estructura:
"""

from IPython.display import Image
Image('../Imgs/sesion_6-7.png')

"""
Podemos crear un treemap para visualizarla de otra manera que resulte más clara:
"""

fig = px.treemap(
    names=['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'x', 'y', 'z'],
    parents=['', '', '', '', '', 'A', 'B', 'B', 'E', 'b', 'a', 'd']
)

fig.show()

"""
La segunda manera de utilizar un treemap consiste en modificar el tamaño de los rectángulos proporcionalmente al tamaño de una variable numérica. Por ejemplo:
"""

df = pd.read_csv('../../Datasets/athlete_olympic_events-clean.csv', index_col=0)

df.head()

df_grouped = df.groupby('name')[['sex', 'sport']].max()

df_grouped.head()

df_grouped['count'] = 1

fig = px.treemap(df_grouped, path=['sport', 'sex'], values='count')

fig.show()

df_grouped_2 = df.groupby('name')[['team', 'sport']].max()

df_grouped_2.head()

"""
Algo que es genial de plotly es que hace gráficas interactivas. Dale click a una de las 'hojas' para ver más detalles.
"""