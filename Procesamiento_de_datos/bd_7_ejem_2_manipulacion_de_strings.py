import pandas as pd


df = pd.read_csv('drive-download/new_york_times_bestsellers-dirty.csv', sep=',')

#Empecemos con la columna description que tiene un 'Descr:' al inicio de cada texto. Si queremos remover ese texto podemos usar el método replace de la propiedad str de esa Serie:

df['description'].str.replace('Descr:', '')
#Para que el cambio persista, tenemos que reasignarlo:

df['description'] = df['description'].str.replace('Descr:', '')

print(df.loc[0, 'description'])

#Como puedes ver, tenemos también espacios vacíos al principio y final de nuestras strings. Vamos a removerlos usando strip:
df['description'] = df['description'].str.strip()

df['title'].str.lower() #lowercase
df['title'] = df['title'].str.title()

#separar columna por espacio
df['author'].str.split(' ')

#Podemos convertirlo en dos columnas así:
print(df['author'].str.split(' ', expand=True))

#asignar

df[['author_first_name', 'author_last_name']] = df['author'].str.split(' ', expand=True)

print(df.head(5))

