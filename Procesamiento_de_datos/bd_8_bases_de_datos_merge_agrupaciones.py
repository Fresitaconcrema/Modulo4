#La base de datos con la que vamos a trabajar
# proviene del siguiente link: Movielens dataset.
# Vamos a utilizar el conjunto de
# datos llamado ml-1m. Este dataset contiene 3 tablas: "movies", "users" y "ratings".

from datetime import datetime
import mysql.connector

# tengo que crear un objeto cursor,
# que es el encargado de realizar las operaciones de consulta y modificación de la base de datos:
import pandas as pd

cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = ("Select * From Cat_Country")
cursor.execute(qry)
result = cursor.fetchall()
cursor.close()

print(type(result))
print(result[0])

paises = pd.DataFrame(result, columns=['id_country', 'code_alpha2', 'code_alpha3', 'country_name', 'region', 'population', 'insert_date', 'update_date'])
paises = paises.set_index('id_country', drop = True)

print(paises)
print('--------')
paises_agrupados = paises.groupby('code_alpha2')['code_alpha2'].count()
print(paises_agrupados)


