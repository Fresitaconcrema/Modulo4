"""
Como ya dijimos, las tablas de frecuencias dividen nuestro conjunto en segmentos de igual tamaño que contiene un
número variable de muestras.

Para generar una tabla de frecuencias, lo primero que hay que hacer es decidir en cuántos
segmentos vamos a dividir nuestros datos.
"""
import pandas as pd


df = pd.read_csv('drive-download/melbourne_housing-clean.csv', index_col=0)

rango = df['price'].max() - df['price'].min()
print(rango)

"""
Tomando en cuenta nuestro rango, vamos a decidir dividir nuestro conjunto en 20 segmentos. 
Usemos ahora nuestro método cut para segmentar nuestros datos.
"""

rango_cut = pd.cut(df['price'], 20)

print(rango_cut)

"""
Ok... ¿Qué acaba de suceder? pd.cut toma el rango completo de nuestros datos, y luego crea 20 segmentos de 
igual tamaño. Después, revisa uno por uno nuestros datos, los ubica en uno de los segmentos y nos regresa una 
Serie donde tenemos cada índice clasificado en el segmento que lo toca.

Ahora, para dividir nuestro dataset por segmentos, podemos utilizar pd.groupby y pasarle la Serie que obtuvimos. 
Lo que hace groupby en este caso es leer la clasificación de cada índice y agruparlos de manera que todas 
las muestras que pertencen a la misma clasificación queden juntas.

Después de agruparlos, podemos usar un count para saber cuántas muestras hay en cada grupo:
"""

table_output = df['price'].groupby(rango_cut).count()
print(table_output)

"""
¡Y Listo! Tenemos una tabla donde los índices son los 20 rangos en los que se dividió nuestro dataset y los valores 
de la tabla son los conteos de cada agrupación. De esta manera quedan aún en más evidencia los valores atípicos, 
ya que podemos ver varios segmentos donde la cantidad de muestras es muy baja.

Ésta podría ser aún otra manera de eliminar valores atípicos, ya que podríamos, por ejemplo, decidir 
eliminar todos los datos que se encuentran en segmentos con menos de 50 muestras.
"""

