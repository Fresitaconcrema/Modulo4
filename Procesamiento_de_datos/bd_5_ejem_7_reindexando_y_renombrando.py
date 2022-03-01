import pandas as pd

#Limpiemos nuestro dataset hasta que esté justo como lo dejamos en el Ejemplo pasado:
df = pd.read_csv('drive-download/melbourne_housing-raw.csv')

df_2 = df.drop(columns=['BuildingArea', 'YearBuilt'])

df_2['Regionname'] = df_2['Regionname'].fillna('Unknown')
df_dropped = df_2.dropna(axis=0, how='any')

df_dropped.reset_index()

#Nuestro índice ya está correcto, pero ahora tenemos un columna llamada
# index que contiene el índice original. Como no queremos guardar
# esos datos, agregamos la opción drop=True para eliminar el índice anterior:

df_dropped.reset_index(drop=True)

#Guardar cambios
df_dropped = df_dropped.reset_index(drop=True)

#inconsistencias en nombres

column_name_mapping = {
    'Suburb' : 'suburb',
    'Address' : 'address',
    'Rooms': 'rooms',
    'Type': 'type',
    'Price': 'price',
    'Method': 'method',
    'SellerG': 'seller_g',
    'Date': 'date',
    'Distance': 'distance',
    'Postcode': 'post_code',
    'Bedroom2': 'bedrooms',
    'Bathroom': 'bathroom',
    'Car': 'car',
    'Landsize': 'land_size',
    'CouncilArea': 'council_area',
    'Lattitude': 'latitude',
    'Longtitude': 'longitude',
    'Regionname': 'region_name',
    'Propertycount': 'property_count'
}

df_renamed = df_dropped.rename(columns=column_name_mapping)

print(df_renamed)



