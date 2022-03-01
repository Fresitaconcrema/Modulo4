import pandas as pd

data_1 = {
    'column_1': [1, 2, 3],
    'column_2': [4, 5, 6]
}

df_1 = pd.DataFrame(data_1, index=['a', 'b', 'c'])

data_2 = {
    'column_1': [7, 8, 9],
    'column_2': [10, 11, 12]
}

df_2 = pd.DataFrame(data_2, index=['d', 'e', 'f'])

print(pd.concat([df_1, df_2], axis=0))

#Horizontalmente:

print(pd.concat([df_1, df_2], axis=1))

print('\n')
#Si tienen el mismo índice, evitamos los NaNs:

data_3 = {
    'column_1': [13, 14, 15],
    'column_2': [16, 17, 18]
}

df_3 = pd.DataFrame(data_3, index=['a', 'b', 'c'])
print(pd.concat([df_1, df_3], axis=1))


#Si concatenamos verticalmente con el mismo índice, no podemos diferenciarlos:

data_4 = {
    'column_1': [7, 8, 9],
    'column_2': [10, 11, 12]
}

df_4 = pd.DataFrame(data_4, index=['a', 'b', 'c'])
print('\n')
print(pd.concat([df_1, df_4], axis=0))

#Podemos agregar multiíndices:

df_concat = pd.concat([df_1, df_4], axis=0, keys=['df_1', 'df_4'])
print(df_concat)

df_concat.loc['df_1']

df_concat.loc[('df_1', 'b')]

output_all = pd.concat([df_1, df_2, df_3, df_4], axis=1)

print(output_all)





