import pandas as pd

df = pd.read_csv('drive-download/new_york_times_bestsellers-dirty.csv', sep=',', index_col=0)

df.head()
#print(df.dtypes, '\n')

#Específicamente, tenemos dos columnas con fechas
# (bestsellers_date.numberLong y published_date.numberLong)
# que tienen tipos object e int64.
# También tenemos una columna rank.numberInt que no tiene el tipo de dato adecuado.

#Podemos usar el método astype para pasarle a nuestro
# DataFrame un diccionario de conversión.
# Por ejemplo, vamos a convertir nuestras dos columnas de fechas usando
# un diccionario de conversión.
# El tipo de dato que usamos para manejar fechas es el llamado datetime.
# Este tipo de dato nos permite manipular fechas
# y horarios muy eficientemente.


diccionario_de_conversion = {
    'bestsellers_date.numberLong': 'datetime64[ns]',
    'published_date.numberLong': 'datetime64[ns]'
}

temp = df.astype(diccionario_de_conversion)
temp.head()
#print(temp.dtypes)

#Como puedes ver, nuestras columnas han sido transformadas.
# Pero parece que hay un problema, puesto que hay muchísima
# diferencia de años entre la columna bestsellers_date y la columna
# published_date. Esto se debe a que published_date está en formato
# 'milisegundos desde La Época (la medianoche UTC del 1 de enero de 1970)'
# y pandas asume por default que estamos lidiando con nanosegundos.

#Para evitar este problema vamos a usar el método
# pd.to_datetime para convertir published_date:

temp_2 = pd.to_datetime(df['published_date.numberLong'], unit='ms')

print(temp['published_date.numberLong'])
print(temp_2)

#to_datetime nos permite especificar las unidades para que la conversión se realice con éxito.
#Vamos ahora qué pasa si queremos convertir rank.numberInt usando astype:
#No podemos hacerlo porque hay unos valores tipo string
# que no pueden ser convertidos a int.
# Para esto usamos el método to_numeric, que nos permite indicar que
# cuando un error sea encontrado, debe de ser sustituido por un NaN:

df['rank.numberInt'] = pd.to_numeric(df['rank.numberInt'], errors='coerce')
#Vamos a reasignar el resultado al DataFrame original:

#Ahora, para convertirlo a tipo int podemos eliminar los NaNs y luego usar astype:
df = df.dropna(axis=0).copy()
df['rank.numberInt'] = df['rank.numberInt'].astype(int)

print(df.shape)




