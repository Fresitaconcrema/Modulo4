import pandas as pd

data_1 = {'monto_1': [1, 2, 3, 4]}
data_2 = {'monto_2': [5, 6, 7, 8]}
data_3 = {'monto_3': [5.1, 6.1, 7.1, 8.1, 9.1]}
data_4 = {'monto_4': [11, 22, 33, 44]}




df_1 = pd.DataFrame(data_1, index = [0, 1, 2, 3])
df_2 = pd.DataFrame(data_2, index = [0, 1, 2, 3])
df_3 = pd.DataFrame(data_3, index = [0, 1, 2, 3, 4])
df_4 = pd.DataFrame(data_4, index = [4, 5, 6, 7])


output_1 = pd.concat([df_1, df_2], axis= 1)
output_2 = df_1.join(df_3, how='outer')
output_3 = pd.concat([df_1, df_4], axis = 0)


print(output_1)
print(output_2)
print(output_3)