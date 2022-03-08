%matplotlib inline
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../Datasets/athlete_olympic_events-clean.csv', index_col=0)

df.head()

"""
Por ejemplo, digamos que queremos graficar la frecuencia de los 4 deportes que analizamos anteriormente. Queremos ver cuántas veces aparece cada uno en nuestro dataset para compararlos.
"""
df_grouped = df.groupby('name')[['sex', 'sport']].max()

df_ball = df_grouped[df_grouped['sport'].isin(['Basketball', 'Volleyball', 'Football', 'Baseball'])]

value_counts_all = df_ball['sport'].value_counts()

value_counts_all


fig = plt.figure()
ax = fig.add_subplot()

sns.barplot(value_counts_all.index, value_counts_all, ax=ax, palette='Blues');

ax.set_ylabel('count')
ax.set_title('Conteo de frecuencia de 4 deportes Olímpicos', fontsize=13, pad=10)

"""
¡Listo! Pero qué pasa si ahora además queremos segmentar nuestros conteos utilizando la variable 'sex'. Esto nos servirá para saber cómo es que cada género contribuye al conteo total de atletas.
"""
df_grouped['count'] = 1

df_grouped.head()

df_ball_with_count = df_grouped[df_grouped['sport'].isin(['Basketball', 'Volleyball', 'Football', 'Baseball'])]
value_counts = df_ball_with_count.groupby(['sport', 'sex'])['count'].sum()

value_counts


value_counts = value_counts.unstack(1)

value_counts

value_counts = value_counts.fillna(0)

plt.style.use('seaborn')

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot()

plt1 = ax.bar(value_counts.index, value_counts['M'], label='M')
plt2 = ax.bar(value_counts.index, value_counts['F'], bottom=value_counts['M'])

ax.set_ylabel('count')
ax.set_title('Conteo de frecuencia de 4 deportes Olímpicos', fontsize=13, pad=15);
plt.legend((plt1[0], plt2[0]), ('Men', 'Women'));
ax.set_ylim(0, 4500)

"""
Con esta gráfica se vuelve muy evidente la disparidad que existe en casi todos estos deportes. Excepto por volleyball, donde la participación de hombres y mujeres es similar, en los demás deportes la participación es femenina es mucho menor o incluso nula.
"""

