import pandas as pd

df = pd.read_csv('drive-download/Remoto melbourne_housing-clean.csv', sep=',')

print(df.head())

print(df['price'].mean())
print(df['price'].sum() / len(df))

print(df['price'].median())


