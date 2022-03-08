import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../Datasets/athlete_olympic_events-clean.csv', index_col=0)

df.head()

"""
Por ejemplo, mira qué pasa cuando queremos visualizar la relación entre peso y altura utilizando todos los datos de nuestro dataset:
"""

df_grouped = df.groupby('name')[['height', 'weight']].max()

sns.set_style('white')

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()

sns.scatterplot(df_grouped['height'], df_grouped['weight'], ax=ax);

fig.suptitle('Relationship between height and weight in Olympic athletes', fontsize=15)

ax.spines["top"].set_color("None")
ax.spines["right"].set_color("None")

ax.set_xlim(110)
ax.set_ylim(0)

"""
Aunque podemos ver una forma más o menos distinguible, hay tantos puntos que es imposible discernir dónde hay más o menos densidad. Veamos ahora cómo se ven estos mismos datos pero con un binning hexagonal:
"""

sns.jointplot('height', 'weight', data=df_grouped, kind='hex', ratio=5, joint_kws={'gridsize': 50})


"""
Esta gráfica permite que visualicemos con mucho más detalle la distribución de nuestros datos. Observa también los histogramas que se encuentran en la parte superior y derecha de la gráfica. Estos histogramas nos ayudan a visualizar de qué manera participa cada variable en la densidad resultante.
"""