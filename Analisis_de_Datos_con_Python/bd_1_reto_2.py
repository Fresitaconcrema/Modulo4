import pandas as pd

df_meteoritos = pd.read_csv('drive-download/Remoto near_earth_objects-jan_feb_1995-clean.csv', sep=',')

#print(df_meteoritos.head())

promedio_diametro = df_meteoritos['estimated_diameter.meters.estimated_diameter_max'].mean()
mediana_diametro = df_meteoritos['estimated_diameter.meters.estimated_diameter_max'].median()

print(promedio_diametro)
print(mediana_diametro)

