import pandas as pd

df = pd.read_csv('drive-download/new_york_times_bestsellers-dirty.csv', sep=',', index_col=0)

#Por ejemplo, queremos ordenar nuestras entradas empezando por el libro de mayor precio hasta el libro de menor precio. Esto es un ordenamiento usando la columna 'price.numberDouble' de manera descendente. Esto se haría de la siguiente manera:

df.sort_values('price.numberDouble', ascending=False)

#Si convertimos 'published_date.numberLong' a datetime, podemos también ordenar desde la publicación más antigua hasta la publicación más reciente:

df['published_date.numberLong'] = pd.to_datetime(df['published_date.numberLong'], unit='ms')

df.sort_values('published_date.numberLong', ascending=True)

#Por ejemplo, podríamos primero filtrar para sólo tener los libros de la editorial que tiene más libros como 'best sellers' y después ordenarlos del que pasó más días en la lista de 'best sellers' al que pasó menos días en la lista:

df['publisher'].value_counts()

df_putnam = df[df['publisher'] == 'Putnam']

print(df_putnam)

df_putnam.sort_values('weeks_on_list.numberInt', ascending=False)









