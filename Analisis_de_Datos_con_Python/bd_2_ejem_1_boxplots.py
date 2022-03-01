import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('drive-download/Remoto melbourne_housing-clean.csv', sep=',')

sns.set(style='whitegrid')
a = sns.boxplot(x=df['price'])

#df['price'].loc[0]= -2000000 #valor atípico

plt.axvline(df['price'].mean(), c='g')

iqr = df['price'].quantile(0.75) - df['price'].quantile(0.25)
filtro_inferior = df['price'] > df['price'].quantile(0.25) - (iqr * 1.5)
filtro_superior = df['price'] < df['price'].quantile(0.75) + (iqr * 1.5)

df_filtrado = df[filtro_inferior & filtro_superior]

plt.show()



