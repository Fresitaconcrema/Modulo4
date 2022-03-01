import time

import requests
import pandas as pd

payload = {'api_key': '4aT2hmsBYkMwWrPwqMXqtXSNmhCCGQH4wm4EH5PQ'}
endpoint = 'https://api.nasa.gov/neo/rest/v1/neo/browse'

r = requests.get(endpoint, params=payload)

#print(r.json().keys())
print(r.json()['links'])
#print(r.json()['page'])
#print(r.json()['near_earth_objects'])


normalized = pd.json_normalize(r.json()['near_earth_objects'])

df = pd.DataFrame.from_dict(normalized)
#print(df.head())

dict_datos = {}

for i in range(0, 10):
    #Cuando automatizamos programas, tenemos que evitar que Excepciones ocurran, pues detendrían nuestro programa y arruinarían nuestra automatización. Podemos usar estructuras try except para evitar que esto suceda:
    try:
        time.sleep(5)

        #Ambos se los pasamos al método GET de requests para realizar
        # la petición a ese endpoint y enviar los parámetros como información extra que el API necesita para validar nuestra petición:

        r = requests.get(endpoint, params=payload)

        #Ahora, podemos leer lo siguiente de nuestro objeto de respuesta:
        if r.status_code == 200:
            json = r.json()

            data = json['near_earth_objects']
            dict_datos[i] = data

            new_link = json['links']['next']
            endpoint = new_link
    except:
        continue

for par in dict_datos:
    normalized = pd.json_normalize(dict_datos[par])
    df = pd.DataFrame.from_dict(normalized)
    dict_datos[par] = df

primer_df = dict_datos[0]
primer_df.head(5)



#for_loop

dict_1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

for key in dict_1:
    print(dict_1[key])
