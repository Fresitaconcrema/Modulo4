import pandas as pd
import mysql.connector

paquete_detail = pd.read_csv('paquete_detail.csv', sep=',') #14056, 7
register_detail = pd.read_csv('register_detail.csv', sep=',') #(15573, 5)

df_1 = pd.DataFrame(paquete_detail)
df_2 = pd.DataFrame(register_detail)

paquete_detail.shape
register_detail.shape

df_len_1 = df_1.max()
df_len_2 = df_2.max()

#for i in df_len_2:
#    print(len(i))

print(df_1['id_paquete'])

cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = ("Insert into paquete_detail(id_paquete, cedis, estado, hora_recolectado, hora_creacion, hora_entregado, hora_falla)"+
" Select T.tconst, CT.id_genre, now()"
)
#cursor.execute(qry)

for i in df_1:



cnx.commit()
cursor.close()
cnx.close()