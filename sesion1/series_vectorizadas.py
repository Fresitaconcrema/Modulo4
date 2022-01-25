import pandas as pd

data = {'impares':[1, 3, 5, 7, 9]}

df = pd.DataFrame(data)


print(df.max(axis=0))