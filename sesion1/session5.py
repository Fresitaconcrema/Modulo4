import pandas as pd
import numpy as np

data = {"lista_numeros": [1, 2, 3, 4, 5, 6, 7, 8, np.nan],
        "montos": [200, np.nan, 300, 500, 600, np.nan, np.nan, np.nan, np.nan]
        }

df = pd.DataFrame(data)
print(df)
df['montos'] = df['montos'].fillna(0)


#print(df.isna().sum(axis=1))
# print(df.dropna())
# print(df.dropna(how='all'))
# print(df.dropna(axis=1))
# print(df['montos'].fillna(0))

# df_potencia =np.power(df, 2)
#
# df_5 = df + 5
# df_total = df.sum()
# df_conteo = df.count()
#
# print(df)
# print(df_potencia)
# print(df_5)
# print(df_total)
# print(df_conteo)
# print('Máximo: ', df.max())
# print('Mínimo: ', df.min())

print(df.reset_index(drop=True).tail())

column_name_mapping = {"lista_numeros": 'Orden Numerico',
                       "montos": "Monto Ingreso"}

df_rename = df.rename(columns= column_name_mapping)
print(df_rename)