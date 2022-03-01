import pandas as pd
import numpy as np
import os
import json

def solution (files):
    for i in files:
        maxprice =pd.read_csv(i)
        print(maxprice['price'].mean())


files = ['drive-download/new_york_times_bestsellers-dirty.csv'
        ]
#print(os.getcwd())
#solution(files)

f = open('drive-download/zomato_reviews-clean.json', 'r')

json_data = json.load(f)
f.close()
print(json_data)
print('--------')
df = pd.DataFrame(json_data)
print(df)


#Podemos saber la forma de nuestro DataFrame accediendo a la propiedad shape.
print(df.shape)

#Podemos ver un número determinado de filas comenzando desde el principio con head
print(df.head(5))

#Podemos ver también las filas del final con tail:
print(df.tail(5))

#Podemos ver los dtypes de todas nuestras columnas accediendo a esa propiedad:
print(df.dtypes)

#También podemos usar la función info del DataFrame para ver más información sobre las columnas. Por ejemplo, el número de valores no nulos que hay en cada una.
print(df.info())

#En caso de que tengamos tantas columnas que no podamos verlas todas en el preview de arriba, podemos acceder a una lista de columnas usando las propiedad columns:
print(df.columns)

