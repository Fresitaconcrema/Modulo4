import pandas as pd

df = pd.read_csv('drive-download/melbourne_housing-raw.csv', sep=',')

#19740 rows x 21 columns
print(df.shape)

#Hay demasiados NaNs en las columnas 'BuildingArea' y 'YearBuilt',
# así que vamos a deshacernos de esas columnas:
df_2 = df.drop(columns=['BuildingArea', 'YearBuilt'])
print(df.isna().sum())
print('\n')

#Llenemos los NaNs en Regionname con la palabra Unknown:
df_2['Regionname'] = df_2['Regionname'].fillna('Unknown')
print(df.isna().sum())

#Ahora eliminemos las filas que contengan al menos un NaN:

df_dropped = df_2.dropna(axis=0, how='any')
print('\n')
print(df_dropped.isna().sum())

print(df_dropped.shape)

df_dropped.to_csv('drive-download/melbourne_housing-no_nans.csv')