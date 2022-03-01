import pandas as pd

datos = {
    "Nombre": ["Pepinillo Hernández", "Lúpulo de Dios", "Juan Juon", "Jimmy el Patatas", "Lorenzo Retaguardias"],
    "Cereal favorito": ["Korn Floks", "Verdurinis", "Zumbaritas", "Diabetukis, Papá", "Fibra Máxima 3000"],
    "Hora del desayuno": ["11:00", "07:30", "07:00", "08:30", "09:30"]
}

df = pd.DataFrame(datos)
print(df)

#add column
df["Fruta con la que acompaña el cereal"] = pd.Series(['Pera', 'Manzana', 'Plátano', 'Guayaba', 'Pizza'])

print(df)

df["Hora del desayuno"] = pd.Series(["10:30", "06:30", "06:00", "07:00", "08:00"])
print(df)

df.drop(columns=['Fruta con la que acompaña el cereal'])

print(df)

#Recuerda que estos métodos sólo regresan "vistas". Para que el cambio permanezca, tenemos que asignar el resultado de la operación a la variable df o a alguna otra variable:

