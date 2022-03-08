"""
Para generar un mapa cloroplético necesitamos dos fuentes de datos:

La primera es un archivo que contenga datos en un formato llamado GeoJSON. El formato GeoJSON utiliza el formato JSON para representar características geográficas de una manera que pueda ser interpretada por una computadora. Un archivo GeoJSON puede incluir puntos en un mapa, regiones geográficas, anotaciones, nombres de regiones, etc. Este archivo nos sirve para poder colocar objetos sobre un mapa.

La segunda es nuestro dataset. Este dataset es como cualquier otro que hemos utilizando anteriormente. Lo único importante es que tenemos que asegurarnos de que haya una manera de relacionar nuestro dataset con nuestro archivo GeoJSON. Esto se hace de una manera similar a como funcionan los joins de SQL. Relacionando una columna de nuestro dataset con una llave de nuestro GeoJSON podemos entonces indicarle a nuestro programa cómo dibujar cosas sobre un mapa.

Una de las librerías que podemos utilizar para dibujar mapas se llama folium. Se utiliza de la siguiente manera:

"""



import pandas as pd
import folium

state_geo = f'../../Datasets/us_states.json'
state_unemployment = f'../../Datasets/us_unemployment-oct_2012.csv'
state_data = pd.read_csv(state_unemployment)

m = folium.Map(location=[48, -102], zoom_start=3, width='60%', height='60%')

folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate (%)'
).add_to(m)

folium.LayerControl().add_to(m)

m
